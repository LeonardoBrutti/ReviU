# Reviù 🤌

## Descrizione del progetto
Reviù è un assistente personale basato su intelligenza artificiale progettato per analizzare recensioni di prodotti in ambito E-commerce. Il suo obiettivo principale è fornire un'analisi accurata dei sentimenti degli acquirenti, aiutando i proprietari di siti specializzati a comprendere le opinioni dei clienti.Tutti possono usare Reviù. È semplice, è veloce e può aiutarvi a capire i sentimenti delle persone a voi più care

# Configurazione ed uso
# Installazzione

Per poter usare Reviù 🤌 c'è bisogno di installare diverse librerie e l'interprete python : 

- Essendo stato testato solamente su [python 3.8](https://www.python.org/downloads/release/python-380/) consigliamo vivamente di installare questa versione poichè versioni precedenti o più aggiornate potrebbero non funzionare correttamente.

- Scaricare il repository tramite il seguente comando sul terminale oppure semplicemente utilizzando il tasto code e cliccare installa zip dopodichè estrarre il file
    ``` bash
    git clone https://github.com/LeonardoBrutti/ReviU.git
    ``` 
- Installare tutte le dipendenze contenute in `requirements.txt` tramite il comando 
    ``` bash
    pip install -r requirements.txt
    ```

- Installare spacy tramite il seguente comando
    ``` bash
    python -m spacy download en_core_web_sm
    ```

- Installare torch tramite il seguente comando
    ``` bash
    pip install torch==1.8.1+cu111 torchvision==0.9.1+cu111 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
    ```
# Utilizzo
Ora che sono state scaricate tutte le dipendenze neccessarie puoi recarti all'interno del progetto e avviare il file `app.py` tramite IDE o tramite terminale con 
``` bash
python app.py
``` 
una volta avviato il file python bisogno aspettare diversi secondi per il caricamento del modello, una volta che viene visualizzata la seguente scritta sul terminale è possibile avviare il sito .
```
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead. * Running on http://127.0.0.1:5000
Press CTRL+C to quit
* Restarting with stat
* Debugger is active!
* Debugger PIN: 144-891-974
```
Per avviare il sito bisogna andare nella directory `Reviù` e aprire il file `index.html` con un qualsiasi browser, dopodichè si aprirà una pagina di login con 2 possibili accessi, tramite admin admin e tramite utente utente, nel lato admin è possibile vedere l'arrivo delle recensioni e la predizione fatta da Reviù🤌 mentre nel lato utente è possibile scrivere la recensione per uno dei 4 prodotti disponibile nell'MVBL SHOP

# Tecnologie utilizzate
Il progetto Reviù è stato sviluppato utilizzando il linguaggio di programmazione Python (attualmente testato solo sulle macchine windows con python 3.8 versioni precendi o più aggiornate potrebbero non funzionare correttamente) e sfruttando principlamente le seguenti librerie:


- Pytorch, inclusi i moduli aggiuntivi come torchtext, torchaudio e torchvision.
- Pandas
- Spacy

Il modello di intelligenza artificiale si basa su una rete neurale ricorrente chiamata LSTM (Long Short-Term Memory), scelta per la sua efficacia nel gestire dati sequenziali come il linguaggio naturale.

# Dataset
Il dataset utilizzato per l'addestramento del modello è il "IMDB movie review dataset", contenente circa 50.000 recensioni di film in lingua inglese. Poiché non è stato possibile trovare un dataset equivalente in lingua italiana, si è optato per questo dataset inglese.

# Struttura del progetto 
Il progetto è suddiviso in diversi file e moduli:

- `LSTM_MODEL.py`: Contiene la definizione della classe LSTM, che stabilisce il comportamento del modello durante il training, inclusi l'embedding e la funzione forward.

- `training.py`: File per l'addestramento del modello, con funzioni per calcolare l'accuratezza e implementare la back propagation utilizzando algoritmi di ottimizzazione come SGD o Adam.

- `app.py`: Questo file gestisce il caricamento del modello addestrato e fornisce funzioni per predire la probabilità di sentimenti. Gestisce anche la comunicazione tra il sito web e l'applicazione Python utilizzando il framework Flask.

- `index.html`: Pagina di login del sito web, con due account disponibili: Admin e Utente.

- `admin.html` e `utente.html`: Pagine web fittizie hostato in locale per dimostrare il funzionamento di Reviù. Include una dashboard per gli admin per monitorare le recensioni e un'area per poter scrivere le recensioni .

# Approfondimenti

Se si è particolarmente interessati ai dettagli del progetto è possibile trovare una relazione tecnica [qui](https://github.com/LeonardoBrutti/ReviU/blob/main/Documentazione%20tecnica%20Revi%C3%B9%20.pdf)

# Crediti
La pagina di login come menzionato nella [documentazione tecnica](https://github.com/LeonardoBrutti/ReviU/blob/main/Documentazione%20tecnica%20Revi%C3%B9%20.pdf) è un template che è stato utilizzato come base e che poi è stato modificato. Il template è trovabile [qui](https://colorlib.com/wp/template/login-form-v1/). Inoltre il dataset è stato scaricato da [qui]().

# Ringraziamenti
Il team MVBL desidera ringraziare l'azienda SEEWEB per l'opportunità offerta e il Sig. Marco Cristofanilli per il suo supporto durante lo sviluppo del progetto.

# Contatti 

Un progetto a cura di [Viselli Marco](https://github.com/LeonardoBrutti) e  [Belli Leonardo](https://github.com/profumato4)
