const prompt = require("prompt-sync")();

const letrasDNI = "TRWAGMYFPDXBNJZSQVHLCKE";
let input = "";
const users = [];

do {
  input = prompt("Introduce user: ");

  if (input === "exit") {
    break;
  }
  const data = input.split(/\s+/);

  let dni = Number(data[3].substring(0, data[3].length - 1)) % 23;
  let letra = data[3].charAt(8);

  let repetido = false;

  for (const i in users) {
    if ((users[i][3] === data[3])) {
      repetido = true;
      break;
    }
  }

  if (letra !== letrasDNI.charAt(dni)) {
    console.log("Error DNI");
  } else if (repetido) {
    console.log("DNI ya existe");
  } else {
    users.push(data);
    console.log(users);
  }
} while (input !== "exit");
