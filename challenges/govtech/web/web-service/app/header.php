<?php
include 'config.php';
if (!isset($_SESSION["user"])) {
    header('Location: login.php');
    exit;
}
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0" />
    <link rel="shortcut icon" href="img/sectech-favicon.png" />
    <title>SecTech University</title>

    <!-- CSS  -->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
	<link rel="stylesheet" href="css/materialize.css">
    <link href="css/style.css" type="text/css" rel="stylesheet" media="screen,projection" />
	<link href="css/custom.css" rel="stylesheet">

    <!--  Scripts-->
    <script src="js/jquery-2.1.1.min.js"></script>
    <script src="js/materialize.min.js"></script>
    <script src="js/init.js"></script>
</head>

<body>
    <nav role="navigation">
        <div class="nav-wrapper container">
            <a id="logo-container" href="#" class="brand-logo">SecTech</a>
            <ul class="right hide-on-med-and-down">
                <li><a href="grades.php">List Student Grades</a></li>
                <li><a href="past_records.php">Past Student Records</a></li>
                <li><a href="rankings.php?ranking-url=http://localhost/university-rankings.html">Rankings</a></li>
                <li><a href="admin.php">Admin</a></li>
                <li><a href="profile.php">Profile</a></li>
                <li><a href="logout.php">Logout</a></li>
            </ul>

            <ul id="nav-mobile" class="sidenav">
                <li><a href="grades.php">List Student Grades</a></li>
                <li><a href="past_records.php">Past Student Records</a></li>
                <li><a href="rankings.php?ranking-url=http://localhost/university-rankings.html">Rankings</a></li>
                <li><a href="admin.php">Admin</a></li>
                <li><a href="profile.php">Profile</a></li>
                <li><a href="logout.php">Logout</a></li>
            </ul>
            <a href="#" data-target="nav-mobile" class="sidenav-trigger"><i class="material-icons">menu</i></a>
        </div>
    </nav>