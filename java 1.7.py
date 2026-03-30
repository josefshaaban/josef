<!DOCTYPE html>
<html>
<body>

<script>
  const rolls = parseInt(prompt("How many dice rolls?"));
  let sum = 0;

  for (let i = 0; i < rolls; i++) {
    const dice = Math.floor(Math.random() * 6) + 1;
    sum += dice;
  }

  console.log("Sum:", sum);
  document.write("Sum of dice rolls: " + sum);
</script>

</body>
</html>