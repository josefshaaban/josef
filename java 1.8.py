<!DOCTYPE html>
<html>
<body>

<script>
  const start = parseInt(prompt("Enter start year:"));
  const end = parseInt(prompt("Enter end year:"));

  document.write("<ul>");

  for (let year = start; year <= end; year++) {
    if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
      document.write("<li>" + year + "</li>");
    }
  }

  document.write("</ul>");
</script>

</body>
</html>