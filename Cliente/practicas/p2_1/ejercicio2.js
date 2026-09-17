var prompt = require('prompt-sync')();

let frutas= []

for (let i = 0; i < 3; i++) {
    frutas[i] = prompt("Introduce el nombre de una fruta:")
    
}
console.log(`Tu macedonia contiene ${frutas[0]}, ${frutas[1]} y ${frutas[2]}`);
