import torch
import torch.nn.functional as F
import time
from LSTM_MODEL import model, train_loader, valid_loader

##TRAINING##

# NUMER0 DI EPOCHE USATE PER IL MODELLO, DAI VALORI FINALI(VISUALIZZABILI IN RISULTATI.TXT) ###
# È RISULTATO ESSERE OVERKILL, UN VALORE DI 15 È PIù CHE OTTIMALE###

NUM_EPOCHS = 30
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
optimizer = torch.optim.Adam(model.parameters(), lr=0.005)
#PERCORSO DI SALVATAGGIO DEL MODELLOMODELLO


PERCORSO_FINALE = "modelli_salvati/modello.pth"


#Funzione per il calcolo dell'accuratezza###
def compute_accuracy(model, data_loader, device):

    with torch.no_grad():

        correct_pred, num_examples = 0, 0

        for i, (features, targets) in enumerate(data_loader):

            features = features.to(device)
            targets = targets.float().to(device)

            logits = model(features)
            _, predicted_labels = torch.max(logits, 1)

            num_examples += targets.size(0)
            correct_pred += (predicted_labels == targets).sum()
    return correct_pred.float()/num_examples * 100


start_time = time.time()

for epoch in range(NUM_EPOCHS):
    model.train()
    for batch_idx, batch_data in enumerate(train_loader):

        text = batch_data.TEXT_COLUMN_NAME.to(DEVICE)
        labels = batch_data.LABEL_COLUMN_NAME.to(DEVICE)

        ### FORWARD E BACK PROPAGATION###

        logits = model(text)
        loss = F.cross_entropy(logits, labels)
        optimizer.zero_grad()

        loss.backward()


        ### AGGIORNAMENTO PARAMETRI DEL Modello####


        optimizer.step()


        ### AGGIORNAMENTI A SCHERMO###


        if not batch_idx % 50:
            print(f'Epoch: {epoch + 1:03d}/{NUM_EPOCHS:03d} | '
                  f'Batch {batch_idx:03d}/{len(train_loader):03d} | '
                  f'Loss: {loss:.4f}')


    with torch.set_grad_enabled(False):
        print(f'ACCURATEZZA TRAINING: '
              f'{compute_accuracy(model, train_loader, DEVICE):.2f}%'
              f'\nACCURATEZZA VALID: '
              f'{compute_accuracy(model, valid_loader, DEVICE):.2f}%')

    print(f'TEMPO PASSATO: {(time.time() - start_time) / 60:.2f} min')


# Salva il modello alla fine dell'addestramento###
torch.save(model, PERCORSO_FINALE)
print("Modello salvato.")