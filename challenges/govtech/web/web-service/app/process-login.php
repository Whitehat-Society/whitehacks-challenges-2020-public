<?php
session_start();
if(isset($_POST['user']) && isset($_POST['password']))
{

    // Hard code the user account
    if ($_POST['user'] == "temp_acc" &&$_POST['password'] == "temp_pass") {
        $user_cookie=array(
            "user"=>$_POST['user'],
            "admin"=>false
        );
        setcookie("sectech", base64_encode(serialize($user_cookie)), time() + (86400 * 30), "/");
        $_SESSION["user"] = $user_cookie;

        
        setcookie("user_id", "c4ca4238a0b923820dcc509a6f75849b");
	   
        header('Location: grades.php');

    } else {
        header('Location: login.php?message=Incorrect credentials');
	}
}