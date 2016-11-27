<?php
set_time_limit(0);

if(isset($_POST['stop']) && $_POST['stop']) {
	unlink('company');
	echo "updated sess";
	exit();
}

if(isset($_POST['company']) && $_POST['company']) {
	$company = $_POST['company'];
	$time = strtotime("now");
	if(file_exists('company')) {
		unlink('company');
	}
	$file = fopen('company', 'w');
	fwrite($file, $time);

	while($time && $time + 100 > strtotime("now")) {
		$file = fopen('values', 'w');
		$values = [["x" => 12, "y" => 33]];
		fwrite($file, json_encode($values));
		fclose($file);
		sleep(10);
		if(file_exists('company')){
			$file = fopen('company', 'r');
			$time = fgets($file);
		} else {
			$time = 0;
		}
	}
}
?>