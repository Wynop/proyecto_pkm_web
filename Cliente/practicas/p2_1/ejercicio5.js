var prompt = require('prompt-sync')();

console.log('Calculador area rectángulo');

let input = prompt('Introduce la base(m):');
let input2 = prompt('Introduce la altura(m):');

console.log(`El área mide ${input * input2} m2`);
