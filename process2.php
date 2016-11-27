<?php
$text = file_get_contents('values');
echo json_encode(["status" => "success", "text" => json_decode($text)]);
file_put_contents('values', '');

exit();
?>