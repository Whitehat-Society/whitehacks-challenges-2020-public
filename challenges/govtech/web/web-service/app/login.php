<!DOCTYPE html>
<html lang="en">

<?php include 'config.php'; ?>
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
    <div class="container">
        <div class="section">
            <div class="row">
                <br>
                <br>
            </div>
            <div class="row">
                <div class="col s3">
                </div>
                <div class="col s6">
                    <div class="card-panel">
                        <div class="row">
                            <div class="col s12">
                                <form action="process-login.php" method="post">
                                <div class="row center-align">
                                    <img class="responsive-img" src="img/sectech-logo.png">
                                    <h5>Authentication Page</h5>
                                </div>
                                <?php 
                                    if(isset($_GET['message'])) {
                                        echo '<div class="row center-align"><span class="flow-text red-text">' . $_GET['message'] . '</span></div>';
                                    }
                                ?>
                                <div class="row">
                                    <div class="input-field col s12">
                                        <input id="user" type="text" name="user">
                                        <label for="user" class="h3" style="font-size: 20px !important;">User</label>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="input-field col s12">
                                        <input id="password" type="password" name="password">
                                        <label for="password" style="font-size: 20px !important;">Password</label>
                                    </div>
                                </div>
                                <div class="row center-align">
                                    <button class="btn-large waves-effect waves-light" type="submit" name="action">Authenticate
                                        <i class="material-icons right">send</i>
                                    </button>
                                </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col s3">
                </div>
            </div>
        </div>
        <br>
        <br>
    </div>
</body>
<script type="text/javascript">
	$("#user").focus();
</script>
</html>