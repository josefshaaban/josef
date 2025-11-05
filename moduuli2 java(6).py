function rollDice() {
  return Math.floor(Math.random() * 6) + 1;
}

document.body.innerHTML += "<h3>Nopanheitot:</h3><ul>";

let result = 0;
while (result !== 6) {
  result = rollDice();
  document.body.innerHTML += `<li>${result}</li>`;
}
document.body.innerHTML += "</ul>";
