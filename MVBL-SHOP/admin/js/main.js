const lastThreeReviews = [];

function recensioneGiaPresente(testo) {
    // Controlla se una recensione con lo stesso testo è già presente nell'array
    return lastThreeReviews.some(review => review.messaggio === testo);
}

function ottieniRisposta(url) {
    fetch(url)
        .then(response => response.json())
        .then(data => {
            const messageTable = document.getElementById('messageTable');
            const tbody = messageTable.getElementsByTagName('tbody')[0];

            // Se una recensione con lo stesso testo è già presente, non aggiungere la nuova recensione
            if (data.predizione !== undefined && !recensioneGiaPresente(data.messaggio)) {
                // Aggiungi la nuova recensione all'inizio dell'array
                lastThreeReviews.unshift(data);

                // Mantieni solo le ultime tre recensioni
                if (lastThreeReviews.length > 3) {
                    lastThreeReviews.pop(); // Rimuovi la recensione più vecchia
                }
            }

            // Rimuovi i messaggi precedenti dalla tabella
            tbody.innerHTML = '';

            // Aggiorna la tabella con le ultime tre recensioni
            lastThreeReviews.forEach(review => {
                const newRow = tbody.insertRow();
                const cell1 = newRow.insertCell(0);
                const cell2 = newRow.insertCell(1);
                const cell3 = newRow.insertCell(2);

                cell1.innerText = review.messaggio;
                cell2.innerText = "Recensione " + (parseFloat(review.predizione) > 0.50 ? "positiva" : "negativa");
                cell3.innerText = review.predizione;

                // Imposta il colore del testo in base alla predizione
                if (parseFloat(review.predizione) > 0.50) {
                    cell1.classList.add('reviewContent');
                    cell2.classList.add('positiveReview');
                    cell3.classList.add('positiveReview');
                } else {
                    cell1.classList.add('reviewContent');
                    cell2.classList.add('negativeReview');
                    cell3.classList.add('negativeReview');
                }
            });


        })
        .catch(error => console.error('Errore:', error));
}

