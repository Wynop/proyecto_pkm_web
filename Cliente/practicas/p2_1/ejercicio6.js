var prompt = require('prompt-sync')();

console.log('Calcula el precio final');

let input = prompt('Introduce el valor(€): ')
let input2 = prompt('Introduce el porcentaje de descuento: ')

console.log(`Son ${input - (input * (input2/100))} €`);
