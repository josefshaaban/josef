let nums = [];
while (true) {
  let n = Number(prompt("Anna numero (0 lopettaa):"));
  if (n === 0) break;
  nums.push(n);
}

nums.sort((a, b) => b - a);
console.log("Numerot suurimmasta pienimpään:");
console.log(nums);
