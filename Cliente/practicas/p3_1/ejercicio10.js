const prompt = require("prompt-sync")();

const tablero = [];
let pum = false;
let aciertos = 0;

const inTablero = (input) => {
  if (input[0] > 9 || input[0] < 0 || input[1] > 9 || input[1] < 0) {
    console.log("Error de juego");
    process.exit();
  } else {
    return true;
  }
};

const aledanos = (data) => {
  let cerca = false;
  for (let i = -1; i <= 1; i++) {
    for (let j = -1; j <= 1; j++) {
      const fila = data[0] + i;
      const columna = data[1] + j;
      if (fila >= 0 && fila <= 9 && columna >= 0 && columna <= 9) {
        if (tablero[fila][columna] === 1) {
          cerca = true;
        }
      }
    }
  }

  if (cerca) {
    console.log("Caliente, caliente");
  } else {
    console.log("Frío, frío");
  }
};

for (let i = 0; i < 10; i++) {
  tablero.push([]);
  for (let j = 0; j < 10; j++) {
    tablero[i].push(0);
  }
}

const mina = prompt("Donde quiere que se situe la mina: ")
  .split(",")
  .map(Number);

if (inTablero(mina)) {
  tablero[mina[0]][mina[1]] = 1;
}

do {
  const input = prompt("Donde quiere buscar: ").split(",").map(Number);

  inTablero(input);

  let consulta = tablero[input[0]][input[1]];
  pum = false;

  switch (consulta) {
    case 1:
      pum = true;
      console.log("Game over");
      break;
    case 2:
      break;
    default:
      aciertos++;

      if (aciertos > 98) {
        console.log("Has ganado, enhorabuena!");
        pum = true;
      } else {
        aledanos(input);
        tablero[input[0]][input[1]] = 2;
      }
      break;
  }
} while (!pum);
