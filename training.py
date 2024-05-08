import torch
import torch.nn.functional as F
import time
from LSTM_MODEL import model, train_loader, valid_loader, test_loader

##Training##

# NUMER0 DI EPOCHE USATO PER IL Modello, DAI VALORI FINALI(VISUALIZZABILI IN Risultati.TXT) RISULTATO OVERKILL
NUM_EPOCHS = 30
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
optimizer = torch.optim.Adam(model.parameters(), lr=0.005)
#PERCORSO DI SALVATAGGIO DEL Modello
PERCORSO_FINALE = "modelli_salvati/modello.pth"

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

        ### FORWARD E BACK PROPAGATION

        logits = model(text)
        loss = F.cross_entropy(logits, labels)
        optimizer.zero_grad()

        loss.backward()


        ### AGGIORNAMENTO PARAMETRI DEL Modello


        optimizer.step()


        ### AGGIORNAMENTI A SCHERMO


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



torch.save(model, PERCORSO_FINALE) # Salva il modello alla fine dell'addestramento


print("Modello salvato.")
print(f'TEMPO TOTALE TRAINING: {(time.time() - start_time) / 60:.2f} min')
print(f'ACCURATEZZA TEST: {compute_accuracy(model, test_loader, DEVICE):.2f}%')