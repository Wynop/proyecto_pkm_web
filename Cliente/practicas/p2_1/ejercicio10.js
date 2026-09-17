var prompt = require('prompt-sync')();

console.log('Medidor de textos');

let input = prompt('Introduce un texto: ')

let count = input.trim().split(" ").length;

console.log(`El texto tiene ${count} palabras.`);





