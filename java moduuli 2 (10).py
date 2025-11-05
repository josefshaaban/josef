let candidatesCount = Number(prompt("Kuinka monta ehdokasta?"));
let candidates = [];

for (let i = 0; i < candidatesCount; i++) {
  let name = prompt(`Ehdokkaan ${i + 1} nimi:`);
  candidates.push({ name: name, votes: 0 });
}

let voters = Number(prompt("Kuinka monta äänestäjää?"));

for (let i = 0; i < voters; i++) {
  let vote = prompt(`Äänestäjä ${i + 1}, kenelle äänesi? (jätä tyhjäksi tyhjä ääni)`);
  let found = candidates.find(c => c.name === vote);
  if (found) {
    found.votes++;
  }
}

candidates.sort((a, b) => b.votes - a.votes);

console.log(`Voittaja on ${candidates[0].name} ${candidates[0].votes} äänellä.`);
console.log("Tulokset:");
for (let c of candidates) {
  console.log(`${c.name}: ${c.votes} ääntä`);
}
