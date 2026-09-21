const prompt = require('prompt-sync')();

const p1 = Number(prompt("Velocidad coche 1: "))
const p2 = Number(prompt("Velocidad coche 2: "))

console.log(p1 === p2 ? "ERROR" : `El coche más rápido es el coche ${p1 > p2 ? "1" : "2"}`);

