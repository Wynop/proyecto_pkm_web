var prompt = require('prompt-sync')();

console.log('Conversión horas->segundos');

let input = prompt('Introduce las horas:')

console.log(`Son ${input * 3600}`);
