const prompt = require('prompt-sync')();

const contraseña = "1234"
const usuario = "admin"

let inputUser = prompt("Introduzca el usuario: ")
let inputPass = prompt("Introduzca la contraseña: ")

console.log((usuario === inputUser && contraseña === inputPass) ? "Usuario autorizado" : "Usuario sin acceso");
