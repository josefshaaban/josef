<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>JavaScript tehtävät</title>
</head>
<body>

<h1>JavaScript tehtävät</h1>

<script>
// 1. Tulosta konsoliin
console.log("I'm printing to console!");

// 2. Kysy nimi ja tulosta HTML:ään
let nimi = prompt("Anna nimesi:");
document.write("<h2>Hello, " + nimi + "!</h2>");

// 3. Kysy kolme kokonaislukua ja laske summa, tulo ja keskiarvo
let a = parseInt(prompt("Anna ensimmäinen kokonaisluku:"));
let b = parseInt(prompt("Anna toinen kokonaisluku:"));
let c = parseInt(prompt("Anna kolmas kokonaisluku:"));

let summa = a + b + c;
let tulo = a * b * c;
let keskiarvo = summa / 3;

document.write("<h3>Summa: " + summa + "</h3>");
document.write("<h3>Tulo: " + tulo + "</h3>");
document.write("<h3>Keskiarvo: " + keskiarvo + "</h3>");

// 4. Lajitteluhattu
let oppilas = prompt("Anna oppilaan nimi:");
let arvo = Math.floor(Math.random() * 4) + 1;
let tupa = "";

if (arvo == 1) {
  tupa = "Rohkelikko";
} else if (arvo == 2) {
  tupa = "Luihuinen";
} else if (arvo == 3) {
  tupa = "Hufflepuff";
} else {
  tupa = "Korpinkynsi";
}

document.write("<p>" + oppilas + ", olet " + tupa + ".</p>");

// 5. Karkausvuosi
let vuosi = parseInt(prompt("Anna vuosi:"));
if ((vuosi % 4 == 0 && vuosi % 100 != 0) || vuosi % 400 == 0) {
  document.write("<p>" + vuosi + " on karkausvuosi.</p>");
} else {
  document.write("<p>" + vuosi + " ei ole karkausvuosi.</p>");
}

// 6. Neliöjuuri
let kysy = confirm("Pitäisikö minun laskea neliöjuuri?");
if (kysy == true) {
  let luku = Number(prompt("Anna numero:"));
  if (luku < 0) {
    document.write("<p>Negatiivisen luvun neliöjuurta ei ole määritelty.</p>");
  } else {
    document.write("<p>Luvun " + luku + " neliöjuuri on " + Math.sqrt(luku) + "</p>");
  }
} else {
  document.write("<p>Neliöjuurta ei lasketa.</p>");
}

// 7. Nopanheitto
let n = parseInt(prompt("Kuinka monta noppaa heitetään?"));
let noppaSumma = 0;

for (let i = 0; i < n; i++) {
  let silma = Math.floor(Math.random() * 6) + 1;
  noppaSumma += silma;
}
document.write("<p>Noppien summa on " + noppaSumma + "</p>");

// 8. Karkausvuodet aikavälillä
let alku = parseInt(prompt("Anna alkuvuosi:"));
let loppu = parseInt(prompt("Anna loppuvuosi:"));

document.write("<ul>");
for (let v = alku; v <= loppu; v++) {
  if ((v % 4 == 0 && v % 100 != 0) || v % 400 == 0) {
    document.write("<li>" + v + "</li>");
  }
}
document.write("</ul>");

// 9. Alkuluku
let n2 = parseInt(prompt("Anna kokonaisluku:"));
let onAlku = true;

if (n2 < 2) {
  onAlku = false;
} else {
  for (let i = 2; i <= Math.sqrt(n2); i++) {
    if (n2 % i == 0) {
      onAlku = false;
      break;
    }
  }
}

if (onAlku) {
  document.write("<p>" + n2 + " on alkuluku.</p>");
} else {
  document.write("<p>" + n2 + " ei ole alkuluku.</p>");
}

// 10. Noppasumman todennäköisyys
let dice = parseInt(prompt("Kuinka monta noppaa?"));
let haluttu = parseInt(prompt("Mikä silmälukujen summa kiinnostaa?"));
let kokeet = 10000;
let osumat = 0;

for (let i = 0; i < kokeet; i++) {
  let s = 0;
  for (let j = 0; j < dice; j++) {
    s += Math.floor(Math.random() * 6) + 1;
  }
  if (s == haluttu) {
    osumat++;
  }
}

let todennakoisyys = (osumat / kokeet) * 100;
document.write("<p>Probability to get sum " + haluttu + " with " + dice + " dice is " + todennakoisyys.toFixed(2) + "%</p>");

</script>

</body>
</html>
