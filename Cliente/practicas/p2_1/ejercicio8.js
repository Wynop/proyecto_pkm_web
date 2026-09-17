var prompt = require('prompt-sync')();

let input = prompt('Dividendo:');
let input2 = prompt('Divisor');

console.log(input % input2 == 0);