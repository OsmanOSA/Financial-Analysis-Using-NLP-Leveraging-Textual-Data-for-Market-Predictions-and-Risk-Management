function predictSentiment() {
    const text = document.getElementById('inputText').value;
  
    fetch('http://localhost:8000/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById('prediction').innerText = `Prédiction : ${data.predicted_label}`;
      document.getElementById('confidence').innerText = `Score de confiance : ${data.confidence_score}`;
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }
  