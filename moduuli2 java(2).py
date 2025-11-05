let count = Number(prompt("Kuinka monta osallistujaa?"));
let names = [];

for (let i = 0; i < count; i++) {
  let name = prompt(`Anna osallistujan ${i + 1} nimi:`);
  names.push(name);
}

names.sort();

document.body.innerHTML += "<h3>Osallistujat:</h3><ol>";
for (let n of names) {
  document.body.innerHTML += `<li>${n}</li>`;
}
document.body.innerHTML += "</ol>";
