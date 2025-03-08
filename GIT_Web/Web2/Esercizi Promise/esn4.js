function callback1(){
    console.log("sono nella callback1");
}

function callback2(){
    console.log("sono nella callback2");
}

var test = new Promise(function(resolve, reject){
    setTimeout(function() {
        callback1();
        
        for (let i = 0; i < 3; i++) {
            setTimeout(function(){
                callback2();
            }, 1000)
        }
    }, 2000)

})


test.then((ris) => {
    console.log(ris);
})