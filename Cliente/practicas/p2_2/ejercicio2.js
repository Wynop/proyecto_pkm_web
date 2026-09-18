const prompt = require('prompt-sync')();

const entra = (contenedor, contenido) => {
    let res = true;
    for (let i = 0; i < contenedor.length; i++) {
        res = res && (contenedor[i] >= contenido[i]);
    }
    return res;
}


let contenedor = []
let contenido =  []

for (let i = 0; i < 3; i++) {
    contenedor[i] = Number(prompt(`Introduce el tamaño del contenedor(m): `))
    
}
for (let i = 0; i < 3; i++) {
    contenido[i] = Number(prompt(`Introduce el tamaño del contenido(m): `))
    
}

console.log(entra(contenedor, contenido) ? "entra" : "no entra");

