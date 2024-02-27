<html>
<head><TITLE>For Loop</TITLE>
<style>
table {
border-collapse: collapse;
width: 65%;
}

th, td {
text-align: center;
padding: 12px;
}

tr:nth-child(even){background-color: #7fff00}

th {
background-color: #A52A2A;
color: Brown;
}
</style>
</head>
<body>
<?php
$car = array("BMW", "Chevy", "Ford","Acura");
$Cost = array("10000", "8000", "3000","9000");
$Owner = array("Gary", "Trent", "Mary","Sam");
echo '<input type="image" src="img.jpg" alt="Submit">';
echo '<table><tr><tr><th>Sr.No</th><th>car</th><th>Cost</th><th>Owner</th></tr>';
for($i=0;$i<count($car);$i++)
{

switch ($i) {
case 0:
echo "<tr><td>1</td><td>" . $car[$i] . "</td><td>" . $Cost[$i] . "</td><td>" . $Owner[$i] . "</td></tr>";
break;
case 1:
echo "<tr><td>2</td><td>" . $car[$i] . "</td><td>" . $Cost[$i] . "</td><td>" . $Owner[$i] . "</td></tr>";
break;
case 2:
echo "<tr><td>3</td><td>" . $car[$i] . "</td><td>" . $Cost[$i] . "</td><td>" . $Owner[$i] . "</td></tr>";
break;
case 3:
echo "<tr><td>3</td><td>" . $car[$i] . "</td><td>" . $Cost[$i] . "</td><td>" . $Owner[$i] . "</td></tr>";
break;
}
}
?>

</body>
</html>