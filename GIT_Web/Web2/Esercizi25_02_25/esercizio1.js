
let numero = 5;  // Cambia il numero da 1 a 10
let Esercizio1 = document.getElementById('tabellina');

// Ciclo for per la tabellina
Esercizio1.innerHTML += "<h2>Usando il ciclo for:</h2>";
for (let i = 1; i <= 10; i++) {
    Esercizio1.innerHTML += `${numero} x ${i} = ${numero * i}<br>`;
}

// Ciclo while per la tabellina
Esercizio1.innerHTML += "<h2>Usando il ciclo while:</h2>";
let i = 1;
while (i <= 10) {
    Esercizio1.innerHTML += `${numero} x ${i} = ${numero * i}<br>`;
    i++;
}