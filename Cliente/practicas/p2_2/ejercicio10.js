const prompt = require('prompt-sync')()

let valor = 1150

console.log("¿Estás a punto de comprar el Smartphone Galaxy Z Flip 8 por 1150 euros, quieres configurar algún extra?");

prompt("Más memoria?(Si/No)") === 'Si' ? valor += 100 : ''
prompt("Mejor cámara?(Si/No)") === 'Si' ? valor += 50 : ''
prompt("Funda protectora?(Si/No)") === 'Si' ? valor += 30 : ''

console.log(valor);
