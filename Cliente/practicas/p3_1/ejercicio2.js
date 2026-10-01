const prompt = require("prompt-sync")();

const array = [];

for (let i = 0; i < 10; i++) {
  array[i] = prompt("Introduce «true» o «false»: ") === "true";
}

for (const i in array) {
  if (array[i] === true) {
    console.log(i);
  }
}
