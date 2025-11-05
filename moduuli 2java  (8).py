function concat(arr) {
  let result = "";
  for (let i = 0; i < arr.length; i++) {
    result += arr[i];
  }
  return result;
}

let names2 = ["Johnny", "DeeDee", "Joey", "Marky"];
let combined = concat(names2);
document.body.innerHTML += `<p>${combined}</p>`;
