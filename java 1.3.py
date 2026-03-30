<!DOCTYPE html>
<html>
<head>
  <title>Sum, Product, Average</title>
</head>
<body>

<script>
  // Ask for three integers
  const a = parseInt(prompt("Enter first integer:"));
  const b = parseInt(prompt("Enter second integer:"));
  const c = parseInt(prompt("Enter third integer:"));

  // Calculate results
  const sum = a + b + c;
  const product = a * b * c;
  const average = sum / 3;

  // Print to HTML document
  document.write("Sum: " + sum + "<br>");
  document.write("Product: " + product + "<br>");
  document.write("Average: " + average);
</script>

</body>
</html>