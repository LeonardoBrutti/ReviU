from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
import spacy
from LSTM_MODEL import TESTO
app = Flask(__name__)
CORS(app)

# Definisci il percorso del modello e caricalo
model_path = "modelli_salvati/modello.pth"
loaded_model = torch.load(model_path)
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
loaded_model.to(DEVICE)
loaded_model.eval()

nlp = spacy.blank("en")

# Funzione per predire la probabilità
def predici_probabilità(sentence):
    tokenized = [tok.text for tok in nlp.tokenizer(sentence)]
    indexed = [TESTO.vocab.stoi[t] for t in tokenized]
    tensor = torch.LongTensor(indexed).to(DEVICE)
    tensor = tensor.unsqueeze(1)
    prediction = torch.nn.functional.softmax(loaded_model(tensor), dim=1)
    return prediction[0][0].item()


# Lista per memorizzare le recensioni
recensioni = []


# Route per gestire la richiesta POST di invio della recensione
@app.route('/invia_recensione', methods=['POST'])
def invia_recensione():
    if request.method == 'POST':
        data = request.json
        message = data.get('message', '')
        recensioni.append(message)  # Aggiungi la recensione alla lista
        print("Recensione ricevuta:", message)  # Stampa il messaggio ricevuto nella console del server Flask
        return "Recensione ricevuta con successo!"

# Route per ottenere la risposta del modello
@app.route('/ottieni_risposta', methods=['GET'])
def ottieni_risposta():
    if recensioni:  # Verifica se ci sono recensioni nella lista
        recensione = recensioni[-1]  # Prendi l'ultima recensione inserita
        predizione = predici_probabilità(recensione)  # Ottieni la predizione del modello
        return jsonify({"messaggio": recensione, "predizione": predizione})
    else:
        return jsonify({"messaggio": "Nessuna recensione disponibile"})
if __name__ == '__main__':
    app.run(debug=True)