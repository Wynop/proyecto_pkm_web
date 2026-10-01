const prompt = require("prompt-sync")();

const array = [[], [], []];

for (const e of array) {
  for (let i = 0; i < 3; i++) {
    e[i] = Number(prompt("Insiere un número entero: "));
  }
}
for (let i = 0; i < 3; i++) {
  console.log(array[i][i]);
}
