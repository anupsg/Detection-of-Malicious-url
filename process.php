<?php
if( $_REQUEST["eng"] )
{
   $name = $_REQUEST['eng'];
   /*$myfile = fopen("/home/spark/vinay/code/newfile.txt", "w") or die("Unable to open file!");
   fwrite($myfile, $name);
   fclose($myfile);*/
   $mystring = exec("python /home/spark/vinay/code1/lstm-dgcorrecttest.py",$output);
   /*$mystring = exec("python /var/www/html/DGA/test.py",$output);*/
   header('Content-type: application/json');
   echo json_encode($mystring);

}
?>

