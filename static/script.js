function showOption(option) {
    document.getElementById("homepage").style.display = "none";

    if (option === "fitness") {
        document.getElementById("fitnessFormContainer").style.display = "block";
    } else if (option === "image") {
        document.getElementById("imageUploadContainer").style.display = "block";
    }
}

function goBack() {
    document.getElementById("homepage").style.display = "block";
    document.getElementById("fitnessFormContainer").style.display = "none";
    document.getElementById("imageUploadContainer").style.display = "none";
}

// Handle image upload
document.getElementById("imageForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const formData = new FormData();
    formData.append("image", document.getElementById("imageInput").files[0]);

    try {
        const response = await fetch("/upload", {
            method: "POST",
            body: formData
        });

        const result = await response.json();
        document.getElementById("imageOutput").innerText = result.message || "Upload failed.";
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("imageOutput").innerText = "Error uploading image.";
    }
});
