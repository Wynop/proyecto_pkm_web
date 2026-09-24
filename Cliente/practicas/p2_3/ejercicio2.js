const prompt = require("prompt-sync")();

const input = Number(prompt("Insiere un tiempo: "));

if (Number.isNaN(input) || input <= 0) {
  console.log("Error de formato");
} else {
  let s = input % 60;
  if (30 >= s && s !== 0) {
    console.log("verde");
  } else if (35 >= s && s > 30) {
    console.log("amarillo");
  } else if (s > 35 || s === 0) {
    console.log("rojo");
  }
}
