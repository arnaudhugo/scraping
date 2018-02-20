<?php
$json = file_get_contents('./2018-02-20_13-36.json');
$json_data = json_decode($json, true);

//echo $json_data["recherche"]["titre"];
var_dump($json_data);