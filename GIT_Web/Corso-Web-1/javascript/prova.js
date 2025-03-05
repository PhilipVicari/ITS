//console.log("ciao")
/*function capitalizeFirstLetter(string)
{
    return string.charAt(0).toUpperCase() + string.slice(1)
}

const prompt = require("prompt-sync")()
var str = prompt("Enter a string: ")
console.log("Hai inserito prima " + str)
str = capitalizeFirstLetter(str)
console.log("Hai inserito dopo " + str)
*/

function check(sNum)
{
    for ( i = 0; i < sNum.length; i++) 
        
    {
    if ((sNum.charAt(i) < '0') || (sNum.charAt(i)>'9'))
        return false
    }
    return true
}

function parseIntMy(sNum)
{
    bEsito = check(sNum)
    if(bEsito==true)
        return parseInt(sNum)
    var sNum1 = "0"
    for(i=0; i<3; i++)
        {
        sNum1 = prompt("Attenzione, numero errato, riprova")
        bEsito = check(sNum1)
        if(bEsito==true)
            return parseInt(sNum1)
        }

    return null 
}

const prompt = require('prompt-sync')();
var sPrimoNum = prompt("Inserisci primo numero ");
var iNum = parseIntMy(sPrimoNum);
if(iNum != null)
    console.log("Hai inserito" + iNum);
else
    console.log("Non sei riuscito ad inserire un numero");
var sSecondoNum = prompt("Inserisci il secondo numero ")
check(sSecondoNum)
var iSecondNum = parseInt(sSecondoNum)

var sSomma = iPrimoNum + iSecondNum

console.log("La somma vale " + sSomma)