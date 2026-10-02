const prompt = require("prompt-sync")();

const input = [];
const conteo = [[], []];
let output = "";

for (let i = 0; input.length < 10; i++) {
  input[i] = prompt("Introduce un elemento: ");
}

do {
  let value = input.pop();
  let times = 1;
  conteo[0].push(value);

  while (input.includes(value)) {
    times++;
    let i = input.indexOf(value);
    input.splice(i, 1);
  }
  conteo[1].push(times);
} while (input.length !== 0);

const maxTimes = Math.max(...conteo[1]);
const posMax = conteo[1].indexOf(maxTimes);

output = conteo[0][posMax];

console.log(conteo[1].indexOf(maxTimes, posMax + 1 ) !== -1 ? "error" : output);

