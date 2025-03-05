/*esercizio 1*/
var A;
var B;
A = 3;
B = "buongiorno a tutti";
console.log("Il tipo della var A e' " + typeof(A) + "\n");
console.log("Il tipo della var B e' " + typeof (B) + "\n");

/*esercizio 2*/

var a
a = "C"
console.log(typeof(a))
a = 3
console.log(typeof(a))

/*esercizio ex.*/

var iPosizione;
var sMiaStringa;
sMiaStringa = "paperino"
iPosizione = sMiaStringa.indexOf("z");
if((iPosizione == -1) || (iPosizione > 3))
						console.log("La z non c'e' nei primi 4 caratteri")
else
	console.log("La z c'e' nei primi 4 caratteri");


/*esercizio 3*/
var iPosizione;
var sMiaStringa;
sMiaStringa = "farfalla"
iPosizione = sMiaStringa.indexOf("f");
if((iPosizione >= 0))
	console.log("La f c'e'")
else
	console.log("La f non c'e' ");

/*esercizio 4*/

function TerminaconLettera(sStringa, sTermine)
{   
    len= sStringa.lenght
    len_termine= sTermine.lenght
    if (len_termine> len)
        return 0
    iPosizione= sStringa.indexOf(sTermine, len - len_termine)
    if (iPosizione >= 0)
        return 1
    else
        return 0

}

ese= TerminaconLettera("Ciao", "u")
console.log(ese)
process.exit(0)