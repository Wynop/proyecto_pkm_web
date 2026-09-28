const prompt = require("prompt-sync")();

const number = Number(prompt("Insiere un número entero: "));
let primo = true;

if (Number.isNaN(number) || !Number.isInteger(number)) {
  console.log("Error de formato");
} else {
    if (number < 2){
        primo = false
    } else {
        for (let i = 2; i < number; i++) {
            if (number % i === 0) {
                primo = false
                break
            }
        }
    }
}
console.log(primo);

