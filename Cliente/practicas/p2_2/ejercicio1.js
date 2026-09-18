const prompt = require('prompt-sync')();

let arboles = [];
for (let i = 0; i < 3; i++) {
    arboles[i] = prompt("Ingresa la atura de un árbol: ") > 10;
}

console.log(arboles[0] || arboles[1] || arboles[2]);

