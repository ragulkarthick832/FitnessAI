from flask import Flask, render_template, request, jsonify
from openai import AzureOpenAI

# Fetch API credentials (Consider using environment variables for security)
api_key = 'EIEKaF9jQN9A1RaprnLGZ5nNKqptnXtolZxtpm2S7lJgHtKxbrxTJQQJ99BCACHYHv6XJ3w3AAAAACOGXYXb'
api_version = '2024-02-15-preview'
azure_endpoint = 'https://cben-m8jtydeu-eastus2.openai.azure.com/'
azure_deployment = 'gpt-4'

# Initialize Flask app
app = Flask(__name__)

# Initialize OpenAI client
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
    try:
        data = request.json
        if not all(key in data for key in ["age", "sex", "height", "weight", "exercises", "equipment", "diet"]):
            return jsonify({"error": "Missing required parameters"}), 400

        fitness_summary = (
            f"I am a {data['age']}-year-old {data['sex']}, with a height of {data['height']} cm and weight of {data['weight']} kg. "
            f"I do {data['exercises']} using {data['equipment']}. My diet includes {data['diet']}."
        )

        response = client.chat.completions.create(
            model=azure_deployment,
            messages=[{"role": "user", "content": fitness_summary}]
        )

        return jsonify({"response": response.choices[0].message.content})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
