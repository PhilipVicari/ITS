var job = () => {
    return new Promise(function(resolve, reject){
        setTimeout(() => {
            resolve("Hello World")
        }, 2000)
    })
}

job().then( (ris) =>{
    console.log(ris);
}).catch((err)=>{
    console.log(err);
})