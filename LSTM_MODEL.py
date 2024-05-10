import torch
import torchtext
import random


RANDOM_SEED = 123
torch.manual_seed(RANDOM_SEED)

GRANDEZZA_VOCABOLARIO = 20000
BATCH_SIZE = 128
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
EMBEDDING_DIM = 128
HIDDEN_DIM = 256
NUM_CLASSES = 2   # si potrebbe usare 1 per classificazione binaria



TESTO = torchtext.legacy.data.Field(
    tokenize='spacy', # il tokenizer di default taglia a ogni spazio
    tokenizer_language='en_core_web_sm'
)


            ### LABEL ####

LABEL = torchtext.legacy.data.LabelField(dtype=torch.long)



fields = [('TEXT_COLUMN_NAME', TESTO), ('LABEL_COLUMN_NAME', LABEL)]


    ### Dataset, IMDB REWIEWS Dataset###


dataset = torchtext.legacy.data.TabularDataset(
    path='movie_data.csv', format='csv',
    skip_header=True, fields=fields)

    ###DIVISIONE DEI DATI IN TRAIN ,TEST E VALID###


train_data, test_data = dataset.split(
    split_ratio=[0.8, 0.2],
    random_state=random.seed(RANDOM_SEED))



train_data, valid_data = train_data.split(
    split_ratio=[0.85, 0.15],
    random_state=random.seed(RANDOM_SEED))



            ####VOCABOLARIO DI PAROLE UNICHE####
TESTO.build_vocab(train_data, max_size=GRANDEZZA_VOCABOLARIO)
LABEL.build_vocab(train_data)




train_loader, valid_loader, test_loader = \
    torchtext.legacy.data.BucketIterator.splits(
        (train_data, valid_data, test_data),
         batch_size=BATCH_SIZE,
         sort_within_batch=False,
         sort_key=lambda x: len(x.TEXT_COLUMN_NAME),
         device=DEVICE
    )

            ####CLASSE CHE SPECIFICA DATI E FUNZIONI DEL MODELLO####
class LSTM(torch.nn.Module):

    def __init__(self, input_dim, embedding_dim, hidden_dim, output_dim):
        super().__init__()

        self.embedding = torch.nn.Embedding(input_dim, embedding_dim)
        self.rnn = torch.nn.LSTM(embedding_dim,
                                 hidden_dim)

        self.fc = torch.nn.Linear(hidden_dim, output_dim)

    def forward(self, text):

        embedded = self.embedding(text)

        output, (hidden, cell) = self.rnn(embedded)


        hidden.squeeze_(0)

        output = self.fc(hidden)  #fc = fully connected
        return output


torch.manual_seed(RANDOM_SEED)
model = LSTM(input_dim=len(TESTO.vocab),
            embedding_dim=EMBEDDING_DIM,
            hidden_dim=HIDDEN_DIM,
            output_dim=NUM_CLASSES
)

model = model.to(DEVICE)






