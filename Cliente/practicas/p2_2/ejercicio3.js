const prompt = require('prompt-sync')();

let res = [];
res[0] = prompt("Se ha registrado?(Si/No)")
res[1] = prompt("Ha pagado la entrada?(Si/No)")
res[2] = prompt("Tiene una identificación valida?(Si/No)")

console.log((res[0] == "Si" && res[1] == "Si"  && res[20] == "Si") ? "Torno abierto" : "Torno cerrado");
