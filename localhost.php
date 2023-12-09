//This portion of the code helps to locally launch the website

<?php
// Connect to the database
$servername = "localhost";
$username = "your_username";
$password = "your_password";
$dbname = "your_database";

$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Add a product to the database
if (isset($_POST["product"])) {
    $min_price = $_POST["min_price"];
    $max_price = $_POST["max_price"];
    $auction_duration = $_POST["auction_duration"];

    $sql = "INSERT INTO products (min, max_price, auction_duration) VALUES ($min_price, $max_price, $auction_duration)";
    if ($conn->query($sql) === TRUE) {
        echo "Product added successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

// Add a bid to the database
if (isset($_POST["bid"])) {
    $product_id = $_POST["product_id"];
    $user_id = $_POST["user_id"];
    $bid_amount = $_POST["bid_amount"];

    $sql = "INSERT INTO bids (product_id, user_id, bid_amount) VALUES ($product_id, $user_id, $bid_amount)";
    if ($conn->query($sql) === TRUE) {
        echo "Bid submitted successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

// Close the database connection
$conn->close();
?>
