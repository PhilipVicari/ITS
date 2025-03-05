let a = 2;
let b = 3;
let c = 4;
let d = 5;
let e = 6;

let somma = a+b+c+d+e;
let media = somma / 5;




document.getElementById("risultato 1").innerHTML = somma;
document.getElementById("risultato 2").innerHTML = media;

let box = document.createElement("h1");
box.setAttribute("id", "risultato 1");
document.appendChild(box);

let box2 = document.createElement("h1");
box.setAttribute("id", "risultato 2");
document.appendChild(box2);
