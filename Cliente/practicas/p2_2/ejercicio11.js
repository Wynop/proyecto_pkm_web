const prompt = require('prompt-sync')();

const preguntas = ['La tierra es plana?', 'El agua suele hervir a 100ºC?', "El agua hidrata más que desidrata?"]
const res = []
const ans = []

let win = true

for (let i = 0; i < 3; i++) {
    res[i] = prompt(preguntas[i] + ' ')
}

for (let i = 0; i < 3; i++) {
    ans[i] = prompt(preguntas[i] + ' ')
}

for (let i = 0; i < 3; i++) {
    !win ? '' : win = res[i] == ans[i]
}

let noes = ans[0] == "No" && ans[1] == "No" && ans[2] == "No"
let sies = ans[0] == "Si" && ans[1] == "Si" && ans[2] == "Si"

console.log(
    !win
        ? "Vaya… has fallado" : (
        sies
            ? "Sí, sí, enhorabuena, has ganado"
            : noes
                ? "No, no, pero enhorabuena, has ganado"
                : "Enhorabuena, has ganado"
    )

);

