const prompt = require("prompt-sync")();

const base = 100

let precio = 0

const nacional = prompt('Tipo de vuelo: ')
const edad = Number(prompt('Edad: '))
const vuelo = Number(prompt('Dia vuelo: '))
const reserva = Number(prompt('Dia reserva: '))

if (Number.isNaN(edad) || !Number.isInteger(edad) || Number.isNaN(vuelo) || !Number.isInteger(vuelo) || Number.isNaN(reserva) || !Number.isInteger(reserva)) {
  console.log("Error de formato");
} else {
    if (nacional === 'nacional') {
        precio = base;
    } else if (nacional === 'internacional'){
        precio = base * 1.20;
    }
    if (edad < 0 ) {
        precio = 0
    } else if (edad < 12) {
        precio = precio * 0.95
    } else if (edad > 65) {
        precio = precio * 0.9
    }
    if(vuelo > 30 || reserva > 30 || reserva > vuelo || vuelo === 0 || reserva === 0 ){
        precio = 0
    }

    console.log(precio);
    

}