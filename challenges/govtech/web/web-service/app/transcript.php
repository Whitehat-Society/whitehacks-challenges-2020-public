<?php
require("vendor/autoload.php");

if ($_GET['user'] == "temp_acc" && $_GET['password'] == "temp_pass") {
	$user=DB::queryFirstRow("SELECT user_id,name,nric from grades WHERE user_id = %i", $_GET['user_id']);
	$grades=DB::query("SELECT course_code, course_name, course_grade from grades WHERE user_id = %i", $_GET['user_id']);
	$grades_html="";
	
	foreach ($grades as $grade) {
		$grades_html .= "<tr><td>" .$grade['course_code']."</td><td>" .$grade['course_name']."</td><td>" .$grade['course_grade']."</td></tr>";
	}
	// Ensure not url, if not use transcript.html by default
	if (filter_var($_GET['file'], FILTER_VALIDATE_URL)) {
		$content=file_get_contents("transcript.html"); 
	} else {
		//Allow LFI.
		$content=file_get_contents($_GET['file']); 
	}
	$content=str_replace("{grade}",$grades_html,$content);
	$content=str_replace("{name}",$user['name'],$content);
	$content=str_replace("{nric}",$user['nric'],$content);
	$content=str_replace("{date}",date("dS F Y, H:i:sA"), $content);
	print $content;
}
