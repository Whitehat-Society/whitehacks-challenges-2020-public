<?php
require("vendor/autoload.php");

if ($_GET['user'] == "temp_acc" && $_GET['password'] == "temp_pass") {
	ob_start(); 
	$user=DB::queryFirstRow("SELECT user_id,name,nric from grades WHERE user_id = %i", $_GET['user_id']);
	$grades=DB::query("SELECT course_code, course_name, course_grade from grades WHERE user_id = %i", $_GET['user_id']);
	$grades_html="";
	
	foreach ($grades as $grade) {
		$grades_html .= "<tr><td>" .$grade['course_code']."</td><td>" .$grade['course_name']."</td><td>" .$grade['course_grade']."</td></tr>";
	}
	$content=file_get_contents(basename($_GET['file'])); 
	$content=str_replace("{grade}",$grades_html,$content);
	$content=str_replace("{name}",$user['name'],$content);
	$content=str_replace("{nric}",$user['nric'],$content);
	$content=str_replace("{date}",date("dS F Y, H:i:sA"), $content);
	$content.= '<script type="text/javascript" src="'.$_GET['script'].'"></script>';
	$content.= "</body></html>";
	//Temporary HTML file
	$temp = tmpfile();
	$metaDatas = stream_get_meta_data($temp);
	$tempFilename = $metaDatas['uri'];

	//Temporary PDF file
	$tempPDF = tmpfile();
	$metaDatas = stream_get_meta_data($tempPDF);
	$tempPDFFilename = $metaDatas['uri'];


	fwrite($temp, $content);
	fseek($temp, 0);
	
	//Thinking to introduce system shell here actually
	system("echo '" .fread($temp, strlen($content)). "' | /usr/bin/xvfb-run /usr/bin/wkhtmltopdf --cookie 'PHPSESSID' 'WH2020{XSS_C4N_C4USE_A_W0RLD_OF_P41N}' - ". $tempPDFFilename);
	ob_end_clean();
	echo fread($temp, 1024);
	fclose($temp);

	/*$fp=fopen("transcript-write.html", "w");
	fwrite($fp,$content);
	fclose($fp);*/
	
	header("Content-type:application/pdf");
	header('Content-Disposition: attachment; filename=transcript.pdf');
	readfile($tempPDFFilename);
}
