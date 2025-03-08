var promise = job1();

promise.then( (data1) => {
    console.log('data1', data1);
    return 'Hello World';
}).then((data2) => {
    console.log('data2', data2);
    return job2();
}).then((data3) => {
    console.log('data3', data3);
});

function job1(){
    return new Promise(function(resolve, reject){
        setTimeout(function(){
            resolve('result of job1');
        }, 1000);
    });
}

function job2(){
    return new Promise(function(resolve, reject){
        setTimeout(function(){
            resolve('result of job2');
        }, 1000);
    });
}

