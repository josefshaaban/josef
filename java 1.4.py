<!DOCTYPE html>
<html>
<head>
  <title>Sorting Hat</title>
</head>
<body>

<script>
  // Ask for student's name
  const name = prompt("Enter your name:");

  // Draw a random number between 1 and 4
  const randomNumber = Math.floor(Math.random() * 4) + 1;

  let house;

  // Assign house using if...else
  if (randomNumber === 1) {
    house = "Gryffindor";
  } else if (randomNumber === 2) {
    house = "Slytherin";
  } else if (randomNumber === 3) {
    house = "Hufflepuff";
  } else {
    house = "Ravenclaw";
  }

  // Print result to HTML document
  document.write(name + ", you are " + house + ".");
</script>

</body>
</html>