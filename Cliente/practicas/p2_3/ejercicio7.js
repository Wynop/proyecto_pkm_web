let output = "";
let i = 1;
const retorno = () => {
  if (output.length < 10) {
    i++;
  } else {
    i--;
  }
};

for (i = 1; i !== 0; retorno()) {
  output += (i % 10);
  console.log(output);
}
