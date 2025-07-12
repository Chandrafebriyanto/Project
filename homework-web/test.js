function intro (name, callback){
    console.log("hallo my name is " + name)
    callback(name)
}

function greeting (name){
    console.log("hallo " + name)
}

intro("agus", greeting)