<!DOCTYPE html>
<html>
<body>

<script>
  const diceCount = parseInt(prompt("Enter number of dice:"));
  const targetSum = parseInt(prompt("Enter desired sum:"));

  const simulations = 10000;
  let success = 0;

  for (let i = 0; i < simulations; i++) {
    let sum = 0;

    for (let j = 0; j < diceCount; j++) {
      sum += Math.floor(Math.random() * 6) + 1;
    }

    if (sum === targetSum) {
      success++;
    }
  }

  const probability = (success / simulations) * 100;

  document.write(
    "Probability to get sum " + targetSum +
    " with " + diceCount + " dice is " +
    probability.toFixed(2) + "%."
  );
</script>

</body>
</html>