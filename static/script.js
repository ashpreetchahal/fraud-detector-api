document.getElementById("fraudForm").addEventListener("submit", async function(event) {
  event.preventDefault();

  const form = event.target;
  const user_id = form.user_id.value.trim();
  const amount = parseFloat(form.amount.value);
  const timestamp = form.timestamp.value;
  const location = form.location.value.trim().toUpperCase();

  const resultDiv = document.getElementById("result");
  resultDiv.textContent = "Checking...";

  try {
    const response = await fetch("http://127.0.0.1:8000/detect-fraud", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ user_id, amount, timestamp, location })
    });

    if (!response.ok) {
      throw new Error(`Server responded with status ${response.status}`);
    }

    const data = await response.json();

    if (data.is_fraud) {
      resultDiv.textContent = "⚠️ Transaction flagged as FRAUDULENT.";
      resultDiv.classList.remove("text-gray-800");
      resultDiv.classList.add("text-red-600", "font-bold");
    } else {
      resultDiv.textContent = "✅ Transaction is clean.";
      resultDiv.classList.remove("text-red-600", "font-bold");
      resultDiv.classList.add("text-green-600", "font-semibold");
    }
  } catch (error) {
    resultDiv.textContent = "Error checking transaction. Please try again.";
    resultDiv.classList.remove("text-green-600", "text-red-600", "font-bold", "font-semibold");
    resultDiv.classList.add("text-yellow-600");
    console.error(error);
  }
});