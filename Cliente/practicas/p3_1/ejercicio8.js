let output = [1];
let i = 2;
const retorno = () => {
  if (output.length < 10) {
    i++;
  } else {
    i--;
  }
};

for (i = 2; output.length > 0; retorno()) {
  console.log(JSON.stringify(output));
  if (i > 0) {
    output.push(i % 10);
  } else {
    output.shift();
  }
}
