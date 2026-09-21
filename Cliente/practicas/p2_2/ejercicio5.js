const prompt = require('prompt-sync')();

const p1 = (prompt("Tiene frenos funcionales?(Si/No)") === "Si" ? true : false)
const p2 = (prompt("Tiene las ruedas infladas?(Si/No)") === "Si" ? true : false)
const p3 = (prompt("Ha tenido un accidente?(Si/No)") === "Si" ? true : false)

console.log((p1 && p2 && !p3) ? "A la carrera" : "Mantenimiento necesario");
