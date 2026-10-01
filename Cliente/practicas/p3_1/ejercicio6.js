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

for(let i = input.length; i >= 0; i--){
    if (quitar[i]) {input.splice(i,1)}
}

console.log(input);

//3/7 pero creo que va bien me salto desquitar el array con datos
