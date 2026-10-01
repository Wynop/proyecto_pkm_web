const prompt = require("prompt-sync")();

const input = [];
let output = 0;

for (let i = 0; i < 10; i++) {
  input[i] = prompt("Introduce un elemento: ");
}

do {
  let comparar = input.pop();
  if (input.includes(comparar)) {
    output += 2;
    let i = input.indexOf(comparar);
    input.splice(i, 1);
    while (input.includes(comparar)) {
      output++;
      i = input.indexOf(comparar);
      input.splice(i, 1);
    }
  }
} while (input.length !== 0);

console.log(output);
