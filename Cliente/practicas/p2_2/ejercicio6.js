const prompt = require('prompt-sync')();

const p1 = (prompt("Tiene pase anual?(Si/No)") === "Si" ? true : false)
const p2 = (prompt("Compró una entrada?(Si/No)") === "Si" ? true : false)

console.log((p1 || p2)? "Puedes entrar al parque" :"No puedes entrar al parque" );
