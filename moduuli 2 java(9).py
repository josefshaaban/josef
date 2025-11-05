function even(arr) {
  let evens = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0) {
      evens.push(arr[i]);
    }
  }
  return evens;
}

let numbers2 = [2, 7, 4, 9, 10];
let evenNums = even(numbers2);

console.log("Alkuperäinen taulukko:", numbers2);
console.log("Parilliset:", evenNums);
