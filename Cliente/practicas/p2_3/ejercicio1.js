const prompt = require("prompt-sync")();

const number = Number(prompt("Insiere una calificación del 0 al 100: "));

if (Number.isNaN(number) || !Number.isInteger(number)) {
  console.log('Error de formato');
  
} else {
    if (100 >= number && number >= 90) {
    console.log("A");
  } else if (89 >= number && number >= 80) {
    console.log("B");
  } else if (79 >= number && number >= 70) {
    console.log("C");
  } else if (69 >= number && number >= 60) {
    console.log("D");
  } else if (59 >= number && number >= 0) {
    console.log("F");
    if (number < 50) {
      console.log("supenso");
    }
  } else {
    console.log("ERROR");
  }
}
