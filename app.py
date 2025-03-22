import os
from flask import Flask, render_template, request, jsonify
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch API credentials from .env
api_key = os.getenv("AZURE_OPENAI_API_KEY")
api_version = os.getenv("AZURE_API_VERSION")
azure_endpoint = os.getenv("AZURE_ENDPOINT")
azure_deployment = os.getenv("AZURE_DEPLOYMENT_NAME")

# Initialize Flask app
app = Flask(__name__)

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=api_key,
    api_version=api_version,
    azure_endpoint=azure_endpoint
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    fitness_summary = f"I am a {data['age']}-year-old {data['sex']}, with a height of {data['height']} cm and weight of {data['weight']} kg."
    
    response = client.chat.completions.create(
        model=azure_deployment,
        messages=[{"role": "user", "content": fitness_summary}]
    )

    return jsonify({"response": response.choices[0].message.content})

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"message": "No file uploaded"}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    # Placeholder for image processing logic
    return jsonify({"message": "Image received successfully!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
