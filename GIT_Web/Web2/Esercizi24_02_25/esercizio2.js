let anno = 2025;

let annoNascita = 2004;

let eta = anno - annoNascita;

let raggiungimento = 100 - eta;

console.log("L'eta della persona è: " + eta);
console.log(' Per raggiungere i 100 mancano ancora ${raggiungimento} ');

document.getElementById("Esercizio 2_R1").innerHTML = eta;
document.getElementById("Esercizio 2_R2").innerHTML = raggiungimento;

let box = document.createElement("h1");
box.setAttribute("id", "Esercizio 2_R1");
document.appendChild(box);

let box2 = document.createElement("h1");
box.setAttribute("id", "Esercizio 2_R2");
document.appendChild(box2);
