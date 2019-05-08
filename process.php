<?php
if( $_REQUEST["eng"] )
{
   $name = $_REQUEST['eng'];
   /*$myfile = fopen("/var/www/html/URL/d.txt", "w") or die("Unable to open file!");
   fwrite($myfile, $name);
   fclose($myfile);*/
   $mystring = exec("python /Users/prathikshabalakrishna/Desktop/test/Prathi-URL-project-edited/lstmtest_1.py $name",$output);
  // $mystring = exec("python /var/www/html/DGA/test.py",$output);*/
   
    //$mystring = exec("python /Users/prathikshabalakrishna/Desktop/test/name.py",$output);
    //$mystring = "HEllo";
    header('Content-type: application/json');
    echo json_encode($mystring);

}
?>

