<?php
$lien = $_POST['lien'];

$command = "python scrapy.py " . $lien;
$output = shell_exec($command);
echo "<pre>$output<pre>";