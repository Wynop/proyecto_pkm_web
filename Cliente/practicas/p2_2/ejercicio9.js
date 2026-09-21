const prompt = require('prompt-sync')();

const p1 = prompt("Peso cajas: ")
let igual = false

const comparar = (input, n) => {
    igual ? `` : igual = (peso === input ? true : false)
    input > peso ? (peso = input, pesada = n) : ''
    count++
}

let peso = -1
let pesada = -1
let count = 1

p1.split(" ").forEach(e => {
    e.length > 0 ? comparar(Number(e),count) : ""
});

console.log(igual ? "ERROR" : `La caja más pesada es la ${pesada}`);

