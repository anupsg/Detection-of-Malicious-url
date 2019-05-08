<?php
if( $_REQUEST["eng"] )
{
   $name = $_REQUEST['eng'];
   /*$myfile = fopen("/var/www/html/URL/d.txt", "w") or die("Unable to open file!");
   fwrite($myfile, $name);
   fclose($myfile);*/
   $mystring = exec("python /prathikshabalakrishna⁩/my-project⁩/⁨Prathi-URL-project/lstmtest2.py $name",$output);
   /*$mystring = exec("python /var/www/html/DGA/test.py",$output);*/
   header('Content-type: application/json');
   echo json_encode($mystring);

}
?>

