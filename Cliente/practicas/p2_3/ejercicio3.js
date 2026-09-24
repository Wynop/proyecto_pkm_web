const prompt = require("prompt-sync")();

const mes = prompt("Insiere un mes: ");
const dia = Number(prompt("Insiere un dia: "));

const validDate = (m, d) => {
  if (d <= 0) {
    return false;
  }

  switch (m) {
    case "enero":
    case "marzo":
    case "mayo":
    case "julio":
    case "agosto":
    case "octubre":
    case "diciembre":
      if (d <= 31) {
        return true;
      } else {
        return false;
      }

    case "abril":
    case "junio":
    case "septiembre":
    case "noviembre":
      if (d <= 30) {
        return true;
      } else {
        return false;
      }
    case "febrero":
      if (d <= 29) {
        return true;
      } else {
        return false;
      }
    default:
      return false;
  }
};

if (Number.isNaN(dia) || !Number.isInteger(dia)) {
  console.log("Error de formato");
} else if (!validDate(mes, dia)) {
  console.log("Día inexistente");
} else {
  console.log(
    (mes === "enero" && dia === 1) ||
      (mes === "marzo" && dia === 29) ||
      (mes === "octubre" && dia === 12) ||
      (mes === "noviembre" && dia === 1) ||
      (mes === "diciembre" && dia === 6) ||
      (mes === "diciembre" && dia === 25)
      ? "Fiesta"
      : "Día normal",
  );
}
