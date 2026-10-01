const letras = ["a", "a", "i", "a", "e", "i", "a"];

const output = [];
let i = 0;

do {
  i = Number(letras.indexOf("a", i)) + 1;
  if (i !== 0) {

    output.push(i);
  }
} while (i !== 0);

console.log(output);

