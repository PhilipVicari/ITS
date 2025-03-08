var job = (data) => {
    return new Promise(function(resolve, reject){
        if (isNaN(data)) {
            setTimeout(() => {
                reject("errore")
            })
        } else {
            if (data % 2 === 0) {
                setTimeout(() => {
                    resolve("pari")
                })
            }else{
                setTimeout(() => {
                    resolve("dispari")
                })
            }
        }
    })
}


job().then((ris) => {
    console.log(ris);
    
}).catch((err) => {
    console.log(err);
    
});