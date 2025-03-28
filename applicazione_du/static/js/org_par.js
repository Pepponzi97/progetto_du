/* Organizza Partita */

// Funzione per gestire la selezione dei giocatori
function toggleSelection(event) {
    const playerDiv = event.currentTarget;
    playerDiv.classList.toggle('selected');
    const checkbox = playerDiv.querySelector('input[type="checkbox"]');
    checkbox.checked = !checkbox.checked;

    updateSelectedPlayersList();
}

// Funzione per filtrare i giocatori in base alla barra di ricerca
function filterPlayers() {
    const searchInput = document.getElementById('searchBar').value.toLowerCase(); // Ottiene il valore della barra di ricerca e lo converte in minuscolo
    const players = document.querySelectorAll('.giocatore'); // Seleziona tutti i riquadri dei giocatori
    
    players.forEach(player => { // Itera su ogni giocatore
        const playerName = player.querySelector('.player-name').textContent.toLowerCase(); // Ottiene il nome del giocatore e lo converte in minuscolo
        if (playerName.includes(searchInput)) { // Verifica se il nome del giocatore contiene il valore della barra di ricerca
            player.classList.remove('hidden'); // Rimuove la classe 'hidden' per mostrare il riquadro del giocatore
        } else {
            player.classList.add('hidden'); // Aggiunge la classe 'hidden' per nascondere il riquadro del giocatore
        }
    });
}

// Funzione per aggiornare la lista dei giocatori selezionati
function updateSelectedPlayersList() {
    const selectedPlayersList = document.getElementById('selectedPlayersList');
    selectedPlayersList.innerHTML = ''; // Pulisce la lista

    const selectedPlayers = document.querySelectorAll('.giocatore.selected');
    selectedPlayers.forEach((player, index) => {
        const playerName = player.querySelector('.player-name').textContent;
        
        const row = document.createElement('tr');

        const playerNumberCell = document.createElement('td');
        playerNumberCell.className = 'player-number';
        playerNumberCell.textContent = index + 1;

        const playerNameCell = document.createElement('td');
        playerNameCell.textContent = playerName;

        const removeButtonCell = document.createElement('td');
        const removeButton = document.createElement('span');
        removeButton.textContent = 'X';
        removeButton.className = 'remove-button';
        removeButton.onclick = function() {
            player.classList.remove('selected');
            updateSelectedPlayersList();
        };

        removeButtonCell.appendChild(removeButton);

        row.appendChild(playerNumberCell);
        row.appendChild(playerNameCell);
        row.appendChild(removeButtonCell);

        selectedPlayersList.appendChild(row);
    });
}

// Barra overall giocatori
document.addEventListener('DOMContentLoaded', function () {
    const players = document.querySelectorAll('.giocatore');
    players.forEach(player => {
        const overall = player.dataset.overall;
        const progressBar = player.querySelector('.progress-bar');
        const normalizedOverall = (overall - 70) * (100 / 18); // Normalizza il valore tra 70 e 88 su una scala da 0 a 100
        progressBar.style.width = normalizedOverall + '%';

        if (overall <= 70) {
            progressBar.classList.add('low');
        } else if (overall <= 76) {
            progressBar.classList.add('midlow');
        } else if (overall <= 79) {
            progressBar.classList.add('mid');
        } else if (overall <= 84) {
            progressBar.classList.add('midhigh');
        } else {
            progressBar.classList.add('high');
        }
        
    });
});
