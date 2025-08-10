const form = document.getElementById("fraudForm");
const resultDiv = document.getElementById("result");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const data = {
    user_id: form.user_id.value,
    amount: parseFloat(form.amount.value),
    timestamp: form.timestamp.value,
    location: form.location.value.toUpperCase(),
  };

  try {
    const response = await fetch("/detect-fraud", {  // <-- IMPORTANT: use "/detect-fraud"
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    const result = await response.json();
    resultDiv.textContent = result.message;
    if (result.is_fraud) {
      resultDiv.style.color = "red";
    } else {
      resultDiv.style.color = "green";
    }
  } catch (error) {
    resultDiv.textContent = "Error checking transaction. Please try again.";
    resultDiv.style.color = "red";
  }
});