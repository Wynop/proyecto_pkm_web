var prompt = require('prompt-sync')();

console.log("Train Timetable:");

let distancias = []

for (let i = 0; i < 3; i++) {
    distancias[i] = Number(prompt(`Valor distancia ${i + 1} (km): `));
    
}
let velocidad = Number(prompt('Velocidad del tren(km/h): '));


console.log(`Si el tren viaja a ${velocidad} km/h,
    tardaría en llegar ${distancias[0] / velocidad * 60} minutos a la primera estación,
    ${((distancias[0]) + distancias[1]) / velocidad * 60} minutos a la segunda estación y 
    ${(distancias[0] + distancias[1] + distancias[2]) / velocidad * 60} en completar el recorrido completo.`);
