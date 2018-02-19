<?php
$json = file_get_contents('./file2.json');
$json_data = json_decode($json, true);

echo $json_data["recherche"]["titre"];
var_dump($json_data);