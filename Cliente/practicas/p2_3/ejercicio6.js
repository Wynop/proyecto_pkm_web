const prompt = require("prompt-sync")();

const A = Number(prompt("Insiere un número: "));
const B = Number(prompt("Insiere un número: "));
const option = prompt("Seleciona una tipo de operación: ");

if (Number.isNaN(A) || Number.isNaN(B)) {
  console.log("Error de formato");
} else {
    switch (option) {
        case 'suma':
            console.log( A + B);
            break;
        case 'resta':
            console.log(A - B);
            break;
        case 'multiplicacion':
            console.log(A * B);
            break;
        case 'division':
            console.log(B === 0 ? 'ERROR' : A / B);
            break;
        default:
            console.log('Operación no permitida');
            break;
    }
}
