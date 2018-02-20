<!DOCTYPE html>
<?php
   $last_ctime = 0;
   $good_file = "";
   if ($handle = opendir('./json_file')) {
     while (false !== ($entry = readdir($handle))) {
       if ($entry != "..") {
         if ($entry != ".") {
           if ((filectime("./json_file/" . $entry)) > $last_ctime) {
	     $good_file = $entry;
	     $last_ctime = filectime("./json_file/" . $entry);
           }
         }
       }
     }
     closedir($handle);
   }
   $j_file = "./json_file/" . $good_file;
   $json = file_get_contents($j_file);
   $json_data = json_decode($json, true);
?>
<html>
  <header>
    <meta charset="utf-8">
    <title>Dashboard</title>
  </header>
  <body>
    <?php
       $var = 1;
       while ($var <= 10) {
    ?>
    <div style='border:1px solid black'>
      <h1><?php echo $json_data[$var]['titre']; ?></h1>
      <p>Numero : <?php echo $json_data[$var]['numero']; ?></p>
      <p>Prix : <?php echo $json_data[$var]['prix']; ?></p>
      <p>Description : <?php echo $json_data[$var]['desc']; ?></p>
      <img src='<?php echo $json_data[$var]['images']['image1']; ?>' style='height: 56px;'/>
      <img src='<?php echo $json_data[$var]['images']['image2']; ?>' style='height: 56px;'/>
      <img src='<?php echo $json_data[$var]['images']['image3']; ?>' style='height: 56px;'/>
    </div>
    <?php
       $var++;
       }
    ?>
  </body>
  <footer>
    Arnaud_h
  </footer>
</html>
