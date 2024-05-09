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
recensioni_bicicletta = []
recensioni_pannello = []
recensioni_gpu = []
recensioni_elio = []

class Comandi:
    def invia_recensione_bici(self, message):
        recensioni_bicicletta.append(message)
        print("Recensione bicicletta ricevuta:", message)

    def invia_recensione_pannelli(self, message):
        recensioni_pannello.append(message)
        print("Recensione pannello ricevuta:", message)

    def invia_recensione_GPU(self, message):
        recensioni_gpu.append(message)
        print("Recensione gpu ricevuta:", message)

    def invia_recensione_elioKit(self, message):
        recensioni_elio.append(message)
        print("Recensione elio ricevuta:", message)



    def ottieni_risposta_bici(self):
        if recensioni_bicicletta:
            recensione = recensioni_bicicletta[-1]
            predizione = predici_probabilità(recensione)
            predizione = round(predizione, 4)
            return jsonify({"messaggio": recensione, "predizione": predizione})
        else:
            return jsonify({"messaggio": "Nessuna recensione disponibile"})

    def ottieni_risposta_pannelli(self):
        if recensioni_pannello:
            recensione = recensioni_pannello[-1]
            predizione = predici_probabilità(recensione)
            predizione = round(predizione, 4)
            return jsonify({"messaggio": recensione, "predizione": predizione})
        else:
            return jsonify({"messaggio": "Nessuna recensione disponibile"})

    def ottieni_risposta_GPU(self):
        if recensioni_gpu:
            recensione = recensioni_gpu[-1]
            predizione = predici_probabilità(recensione)
            predizione = round(predizione, 4)
            return jsonify({"messaggio": recensione, "predizione": predizione})
        else:
            return jsonify({"messaggio": "Nessuna recensione disponibile"})

    def ottieni_risposta_elioKit(self):
        if recensioni_elio:
            recensione = recensioni_elio[-1]
            predizione = predici_probabilità(recensione)
            predizione = round(predizione, 4)
            return jsonify({"messaggio": recensione, "predizione": predizione})
        else:
            return jsonify({"messaggio": "Nessuna recensione disponibile"})

comandi = Comandi()

@app.route('/invia_recensione_bicicletta', methods=['POST'])
def invia_recensione_bicicletta():
    if request.method == 'POST':
        data = request.json
        message = data.get('message', '')
        comandi.invia_recensione_bici(message)
        return "Recensione bicicletta ricevuta con successo!"

@app.route('/invia_recensione_pannello', methods=['POST'])
def invia_recensione_pannello():
    if request.method == 'POST':
        data = request.json
        message = data.get('message', '')
        comandi.invia_recensione_pannelli(message)
        return "Recensione pannello ricevuta con successo!"

@app.route('/invia_recensione_gpu', methods=['POST'])
def invia_recensione_gpu():
    if request.method == 'POST':
        data = request.json
        message = data.get('message', '')
        comandi.invia_recensione_GPU(message)
        return "Recensione gpu ricevuta con successo!"

@app.route('/invia_recensione_elio', methods=['POST'])
def invia_recensione_elio():
    if request.method == 'POST':
        data = request.json
        message = data.get('message', '')
        comandi.invia_recensione_elioKit(message)
        return "Recensione elio ricevuta con successo!"

@app.route('/ottieni_risposta_bicicletta', methods=['GET'])
def ottieni_risposta_bicicletta():
    return comandi.ottieni_risposta_bici()

@app.route('/ottieni_risposta_pannello', methods=['GET'])
def ottieni_risposta_pannello():
    return comandi.ottieni_risposta_pannelli()

@app.route('/ottieni_risposta_gpu', methods=['GET'])
def ottieni_risposta_gpu():
    return comandi.ottieni_risposta_GPU()

@app.route('/ottieni_risposta_elio', methods=['GET'])
def ottieni_risposta_elio():
    return comandi.ottieni_risposta_elioKit()

if __name__ == '__main__':
    app.run(debug=True)