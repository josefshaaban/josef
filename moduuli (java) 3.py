let dogs = [];
for (let i = 0; i < 6; i++) {
  let dog = prompt(`Anna koiran ${i + 1} nimi:`);
  dogs.push(dog);
}

dogs.sort().reverse();

document.body.innerHTML += "<h3>Koirat:</h3><ul>";
for (let d of dogs) {
  document.body.innerHTML += `<li>${d}</li>`;
}
document.body.innerHTML += "</ul>";
