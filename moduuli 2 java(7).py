function rollDice(sides) {
  return Math.floor(Math.random() * sides) + 1;
}

let sides = Number(prompt("Anna nopan sivujen määrä:"));
document.body.innerHTML += `<h3>${sides}-sivuinen noppa:</h3><ul>`;

let result2 = 0;
while (result2 !== sides) {
  result2 = rollDice(sides);
  document.body.innerHTML += `<li>${result2}</li>`;
}
document.body.innerHTML += "</ul>";
