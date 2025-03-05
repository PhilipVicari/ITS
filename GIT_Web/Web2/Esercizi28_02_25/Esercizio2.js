var risultato;
var esercizio_5_2 = (n) =>{
    if (num >= 1 && num <= 7) {
        risultato = true;
    } else {
        risultato = false;
    }
    return risultato;
}

var esercizio_5_2 = (n) =>{
    if (risultato = true){
        switch(risultato){
            case 1:
                console.log("Lunedi");
                break
            case 2:
                console.log("Martedi");
                break
            case 3:
                console.log("Mercoledi");
                break
            case 4:
                console.log("Giovedi");
                break
            case 5:
                console.log("Venerdi");
                break
            case 6:
                console.log("Sabato");
                break
            case 7:
                console.log("Domenica");
                break
        }
    }else{
        return "Non posso indovinare il giorno"
    }
}