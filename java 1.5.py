<!DOCTYPE html>
<html>
<head>
  <title>Leap Year Checker</title>
</head>
<body>

<script>
  // Ask user for a year
  const year = parseInt(prompt("Enter a year:"));

  let result;

  // Leap year logic
  if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
    result = year + " is a leap year.";
  } else {
    result = year + " is not a leap year.";
  }

  // Print result to HTML document
  document.write(result);
</script>

</body>
</html>