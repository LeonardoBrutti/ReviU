function buttonPress(url){
    document.getElementById('reviewForm').addEventListener('submit', function(event) {
        event.preventDefault();
        var message = document.getElementById('message').value;
        inviaDatiAlBackend(message, url);
        document.getElementById('message').value = '';
        document.getElementById('successMessage').style.display = 'block'; // Mostra il messaggio di successo
        setTimeout(function() {
            document.getElementById('successMessage').style.display = 'none'; // Nasconde il messaggio di successo dopo 3 secondi
        }, 3000);
    });
}

function inviaDatiAlBackend(message, url) {
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({message: message})
    })
    .then(response => response.text())
    .then(data => {
        console.log('Risposta dal server Flask:', data); // Visualizza la risposta del server Flask nella console del browser
    })
    .catch(error => console.error('Errore:', error));
}
