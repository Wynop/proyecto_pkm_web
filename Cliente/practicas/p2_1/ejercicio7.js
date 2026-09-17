var prompt = require('prompt-sync')();

console.log('Tiempo transcurrido');

let input = prompt('Introduce la distancia a desplazarse(km): ')

console.log(`Son ${input /4} horas caminando`);
console.log(`Son ${input /60} horas conduciendo`);
console.log(`Son ${input /100} horas en tren`);