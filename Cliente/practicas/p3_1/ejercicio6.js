const prompt = require("prompt-sync")();

const input = [];
const quitar = []

for (let i = 0; input.length < 10; i++) {
  input[i] = prompt("Introduce un elemento: ");
}

for (let i = 0; i < 10; i++) {
    
    if (input.indexOf(input[i], i+1) !== -1) {
        quitar[i] = true
    }else{
        quitar[i] = false
    }
}

for(let i = input.length - 1; i >= 0; i--){
    if (quitar[i]) {input.splice(i,1)}
}

console.log(input);