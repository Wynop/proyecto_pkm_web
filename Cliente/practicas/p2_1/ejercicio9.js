var prompt = require('prompt-sync')();

console.log('Conversión de segundos a hh/mm/ss');

let input = prompt('Introduce los segundos: ')

let segundos = input % 60;
let minutos = Math.floor(input / 60);
let horas = Math.floor(minutos / 60);
minutos = minutos % 60;



console.log(`Son ${horas} horas, ${minutos} minutos y ${segundos} segundos.`);