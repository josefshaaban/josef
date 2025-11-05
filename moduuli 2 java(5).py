let given = [];

while (true) {
  let n = Number(prompt("Anna numero:"));
  if (given.includes(n)) {
    alert("Numero on jo annettu!");
    break;
  }
  given.push(n);
}

given.sort((a, b) => a - b);
console.log("Annetut numerot (nouseva järjestys):", given);
