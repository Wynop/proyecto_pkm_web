const prompt = require("prompt-sync")();

const number = Number(prompt("Insiere un número entero: "));
const option = Number(prompt("Seleciona una operación:(1-3)[Binario-Octal-Hexadecimal]"));

const BINARIO = ["0", "1"];
const OCTAL = ["0", "1", "2", "3", "4", "5", "6", "7"];
const DECIMAL = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
const HEXADECIMAL = [
  "0",
  "1",
  "2",
  "3",
  "4",
  "5",
  "6",
  "7",
  "8",
  "9",
  "A",
  "B",
  "C",
  "D",
  "E",
  "F",
];

const transform = (input, base, values) => {
  let output = "";
  let middle = [];

  while (input >= base) {
    let value = input % base;
    middle.unshift(value);
    input = (input - value) / base;
  }
  middle.unshift(input);
  middle.forEach((e) => {
    output = output + values[e];
  });
  return output;
};

if (
  Number.isNaN(number) ||
  !Number.isInteger(number) ||
  Number.isNaN(option) ||
  !Number.isInteger(option)
) {
  console.log("Error de formato");
} else {
  let output = "";
  if (number < 0) {
    output = "-";
    number = number * -1;
  }
  switch (option) {
    case 1:
      console.log(output + transform(number, 2, BINARIO));
      break;
    case 2:
      console.log(output + transform(number, 8, OCTAL));
      break;
    case 3:
      console.log(output + transform(number, 16, HEXADECIMAL));
      break;
    default:
      console.log("Operación no permitida");

      break;
  }
}
