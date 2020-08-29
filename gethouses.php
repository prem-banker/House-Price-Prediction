
<html>
<title>W3.CSS Template</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
<style>
body,h1,h2,h3,h4,h5,h6 {font-family: "Raleway", sans-serif}

body, html {
  height: 100%;
  line-height: 1.8;
}

/* Full height image header */
.bgimg-1 {
  background-position: center;
  background-size: cover;
  background-image: url("/home/mili/Desktop/SSIP/house.jpg");
  min-height: 100%;
}

.w3-bar .w3-button {
  padding: 16px;
}
</style>
<body class='' style="background-color: #b4b8b8;">

<!-- Navbar (sit on top) -->
<div class="w3-top">
  <div class="w3-bar w3-white w3-card" id="myNavbar">
    <a href="#home" class="w3-bar-item w3-button w3-wide">PRICE FINDER</a>
    <!-- Right-sided navbar links -->
    <div class="w3-right w3-hide-small">
      <a href="#home" class="w3-bar-item w3-button">HOME</a>
      <a href="#pricepredictor" class="w3-bar-item w3-button"><i class="fa fa-user"></i> PRICE PREDICTOR</a>
      <a href="#priceaggregator" class="w3-bar-item w3-button"><i class="fa fa-th"></i> PRICE AGGREGATOR</a>
      <a href="#areas" class="w3-bar-item w3-button"><i class="fa fa-usd"></i> AREAS</a>
    </div>
    <!-- Hide right-floated links on small screens and replace them with a menu icon -->

    <a href="javascript:void(0)" class="w3-bar-item w3-button w3-right w3-hide-large w3-hide-medium" onclick="w3_open()">
      <i class="fa fa-bars"></i>
    </a>
  </div>
</div>

<!-- Sidebar on small screens when clicking the menu icon -->
<nav class="w3-sidebar w3-bar-block w3-black w3-card w3-animate-left w3-hide-medium w3-hide-large" style="display:none" id="mySidebar">
  <a href="javascript:void(0)" onclick="w3_close()" class="w3-bar-item w3-button w3-large w3-padding-16">Close ×</a>
  <a href="#home" onclick="w3_close()" class="w3-bar-item w3-button">HOME</a>
  <a href="#pricepredictor" onclick="w3_close()" class="w3-bar-item w3-button">PRICE PREDICTOR</a>
  <a href="#priceaggregator" onclick="w3_close()" class="w3-bar-item w3-button">PRICEAGGREGATOR</a>
  <a href="#areas" onclick="w3_close()" class="w3-bar-item w3-button">AREAS</a>
</nav>

</body>
</html>











<?php
$housetype = $_POST["radio"];
//echo($housetype);
//echo "<br>";
$bedrooms = $_POST['BHK'];
//echo "<br>";
//echo($bedrooms);
echo "<br>";
$area = $_POST['area'];

$price = $_POST['price'];

//echo($area);
echo "<br>";
echo "<br>";

echo "<br>";
echo "<br>";



$sql = "SELECT * from aggregate_data WHERE Type = '$housetype' and BHK = $bedrooms and Area = '$area' and Price  <= $price";
//$sql = "SELECT * from aggregate_data WHERE Type = 'Apartment' and BHK = 3 and Area = 'Maninagar'";

$conn = new mysqli("localhost","root","","housedata");
$result = $conn->query($sql);

 while($row=$result->fetch_assoc()){
?>

<div class='row' style="padding-top: 100px;  background: white; width: 90%; margin-left: 5%; margin-right: 5%;">
	<div class='col-lg-3 col-md-3 col-sm-3'></div>
	<div class='col-lg-3 col-md-3 col-sm-3'>
		
		<img src="buildingdummy.jpg"  style='text-align: center; padding-top: 10px;'>
		<br>
		<br>
		<a href="#" ><button class='btn btn-dark' style='width: auto; margin-left: 20%; margin-right: 20%;'>Visit Now</button></a>
	</div>

	<div class='col-lg-3 col-md-3 col-sm-3'>
		<br>
		<h6 style='text-align: center;'> Type : <span style='font-weight: bold'><?php echo ($row["Type"])?> </span> </h6>
		<h6 style='text-align: center;'> location : <span style='font-weight: bold'> <?php echo($row["Area"])?> </span> </h6>
		
		<h6  style='text-align: center;'>BHK : <span style='font-weight: bold'><?php echo ($row["BHK"])?> </span> </h6>
		
		<h6 style='text-align: center;'> Size : <span style='font-weight: bold'> <?php echo ($row["Sqft"])?> sqft.</span> </h6>
	
		<h6 style='text-align: center;'> Price : <span style='font-weight: bold'> ₹ <?php echo ($row["Price"])?> </span> </h6>
		<br>
		<h6 style='text-align: center;'> Website : <a style='font-weight: bold' href='https://www.makaan.com/ahmedabad/gala-infrastructure-eternia-in-thaltej-8508183/3bhk-3t-1385-sqft-apartment'> Weblink</a> </h6>
		<br>
		<div style='text-align: center;'> This <span><?php echo ($row["Type"])?></span> is located in the <span><?php echo($row["Area"])?></span> region of Ahmedabad. It is <span><?php echo ($row["Age"])?></span> years old and it is <span><?php echo ($row["Furniture"])?></span>.</div>
	</div>

	<div class='col-lg-3 col-md-3 col-sm-3'></div>

	


</div>


<?php } ?>

