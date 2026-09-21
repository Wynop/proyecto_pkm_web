const prompt = require('prompt-sync')();

let res = []
let count = 0

for (let i = 0; i < 3; i++) {
    input = Number(prompt("Puntuación competición" + i + ":(0-10)"))
    res[i] = input;
    input >= 8 ? count++ : ""
}


console.log(count >= 2 && (res[0] >= 5 && res[1] >= 5 && res[2] >= 5))
