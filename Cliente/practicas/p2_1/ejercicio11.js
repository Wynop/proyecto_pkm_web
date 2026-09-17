var prompt = require('prompt-sync')();

console.log("Concatenación de 3 números:");


let output = ""

for (let i = 0; i < 3; i++) {
    output = output + prompt("Introduce un numero: ")
}

console.log(output);
