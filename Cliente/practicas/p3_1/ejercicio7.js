const prompt = require("prompt-sync")();

const input = prompt("Introduce users: ");

let users = input.split(" ");


for (let i = users.length - 1; i >= 0; i--) {
  if (!/^@.+$/.test(users[i])) {
    users.splice(i, 1);
  }
}

switch (users.length) {
  case 1:
    console.log(users[0] + ' está online');
    break;
  case 2:
    console.log(`${users[1]} y ${users[0]} están online`);
    break;
  default:
    console.log(`${users[users.length -1]}, ${users[users.length -2]} y ${users.length -2} persona(s) más están online`);
    break;
}
