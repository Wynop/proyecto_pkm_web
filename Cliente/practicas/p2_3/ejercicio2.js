const prompt = require("prompt-sync")();

const input = Number(prompt("Insiere un tiempo: "));

if (Number.isNaN(input) || input < 0) {
  console.log("Error de formato");
} else {
  let s = input % 60;
  if (30 > s ) {
    console.log("verde");
  } else if (34 > s && s >= 30) {
    console.log("amarillo");
  } else if (s > 34 ) {
    console.log("rojo");
  }
}
