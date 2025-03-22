document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("fitnessForm").addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent form reload

        let formData = {};
        new FormData(this).forEach((value, key) => (formData[key] = value));

        fetch("/generate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(formData),
        })
        .then(response => response.json())
        .then(data => {
            if (data.response) {
                document.getElementById("output").innerHTML = `<strong>Recommendation:</strong> ${data.response}`;
            } else {
                document.getElementById("output").innerHTML = `<strong>Error:</strong> ${data.error}`;
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });
});
