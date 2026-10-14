const prompt = require("prompt-sync")();

const bbdd = [];

let again = true;

const mostrarTareas = () => {
  for (const key in bbdd) {
    const e = bbdd[key];
    console.log(`${Number(key) + 1} ${e[0]} ${e[2]}`);
  }
};

const agregar = () => {
  const titl = prompt("Ingrese el título: ");
  const desc = prompt("Ingresela descripción: ");

  if (titl.length === 0 || desc.length === 0) {
    bbdd.push(["error", "error", false]);
    return;
  }
  for (const key in bbdd) {
    const e = bbdd[key][0];
    if (e === titl) {
      console.log("Error. Título duplicado");
      return;
    }
  }
  bbdd.push([titl, desc, false]);
  return;
};

const eliminar = () => {
  if (bbdd.length === 0) {
    console.log("No hay tareas para eliminar");
    return;
  }
  if (bbdd.length === 0) {
    console.log("No hay tareas para eliminar");
    return;
  } else {
    mostrarTareas();
  }

  const input = Number(prompt("Que tarea quiere eliminar: "));
  if (input <= 0 || input > bbdd.length) {
    console.log("Error de rango");
    return;
  }
  console.log(`Tarea ${bbdd[input - 1][0]} eliminada`);
  bbdd.splice(input - 1, 1);
  return;
};

const marcar = () => {
  if (bbdd.length === 0) {
    console.log("No hay tareas para marcar como completadas");
    return;
  } else {
    mostrarTareas();
  }
  const input = Number(prompt("Que tarea ha completado: "));
  if (input <= 0 || input > bbdd.length) {
    console.log("Tarea inexistente");
    return;
  }
  if (bbdd[input - 1][2] === true) {
    console.log(`Tarea ${bbdd[input - 1][0]} ya completada`);
    return;
  }
  bbdd[input - 1][2] = true;
};

const completadas = () => {
  const temp = [];
  for (const key in bbdd) {
    const e = bbdd[key];
    if (e[2] === true) {
      temp.push(e);
    }
  }
  if (temp.length === 0) {
    console.log("No existen tareas completadas");
  } else {
    for (const key in temp) {
      const e = temp[key];
      console.log(e);
    }
  }
};

do {
  console.log("1-Agregar tarea");
  console.log("2-Eliminar tarea");
  console.log("3-Marcar tarea como compeltada");
  console.log("4-Tareas completadas");
  console.log("5-Salir del programa");
  const input = prompt("Elige una opción (1-5): ");

  switch (input) {
    case "1":
      agregar();
      break;
    case "2":
      eliminar();
      break;
    case "3":
      marcar();
      break;
    case "4":
      completadas();
      break;
    case "5":
      console.log("Hasta pronto");
      again = false;
      break;

    default:
      console.log("error");
      break;
  }
} while (again);
