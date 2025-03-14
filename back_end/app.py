from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_path = './back_end/Fine-tuned-model_Bert-base-uncased-110M-sentiment_analysis'

# Chargez le modèle 
model = AutoModelForSequenceClassification.from_pretrained(model_path, num_labels=3)
# Chargez le tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Créer FastAPI app
app = FastAPI()


# Créer une classe pour définir les données d'entrée
class RequestInputText(BaseModel):
    text: str = Field(..., min_length=1, example="I love this product!")


# Créer une fonction pour la prédiction
@app.post("/predict")
def predict(resquest: RequestInputText):

    text = resquest.text

    id2label = {0: "Negative", 1: "Positive", 2:"Neutral"}

    if not text:  # Vérification que le texte n'est pas vide
        raise HTTPException(status_code=400, detail="Text input cannot be empty.")

    input_data = tokenizer(text, return_tensors="pt", truncation=True, max_length=512).to(model.device)

    # Faire la prédiction 
    predictions = model(**input_data)

    # Récupérer la classe avec la plus plus haute probabilité 
    predicted_class = predictions.logits.argmax().item()
    # Afficher le label associer à la classe
    predicted_label = id2label[predicted_class]

    # Récupérer les logits et les convertir en probabilités avec la fonction softmax
    logits = predictions.logits
    probabilities = torch.nn.functional.softmax(logits, dim=-1)

    # Récupérer le score de confiance (probabilité de la classe prédite)
    confidence_score = probabilities[0][predicted_class].item()

    return  { "Classe Prédite": predicted_label, "Probabilité": confidence_score}

# Endpoint pour vérifier si l'API fonctionne
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de sentiment analysis!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)





