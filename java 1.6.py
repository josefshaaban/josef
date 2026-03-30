<!DOCTYPE html>
<html>
<head>
  <title>Square Root Calculator</title>
</head>
<body>

<script>
  // Ask for confirmation
  const shouldCalculate = confirm("Should I calculate the square root?");

  if (shouldCalculate) {
    // Ask for a number
    const number = parseFloat(prompt("Enter a number:"));

    if (number < 0) {
      document.write("The square root of a negative number is not defined.");
    } else {
      const squareRoot = Math.sqrt(number);
      document.write("The square root of " + number + " is " + squareRoot + ".");
    }
  } else {
    document.write("The square root is not calculated.");
  }
</script>

</body>
</html>