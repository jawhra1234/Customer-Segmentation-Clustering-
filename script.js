async function predictCluster(event) {
    event.preventDefault();  // Prevent page reload on form submit

    const income = parseFloat(document.getElementById("income").value);
    const spendingScore = parseFloat(document.getElementById("score").value);

    const responseElement = document.getElementById("result");

    try {
        const response = await fetch("http://127.0.0.1:5000/predict_cluster", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                income: income,
                spending_score: spendingScore
            })
        });

        if (!response.ok) {
            throw new Error("Server error");
        }

        const data = await response.json();
        responseElement.innerText = `Predicted Cluster: ${data.predicted_cluster}`;
    } catch (error) {
        responseElement.innerText = "Error: Could not contact server.";
    }
}

document.getElementById("predictionForm").addEventListener("submit", predictCluster);
