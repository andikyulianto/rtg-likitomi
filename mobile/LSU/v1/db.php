<?php
define("HOST", "localhost", TRUE);
define("PORT", 3306, TRUE);
define("USER", "root", TRUE);
define("PASS", "", TRUE);
define("DB", "likitomiv7", TRUE);
define("CHARSET","SET NAMES TIS620",TRUE);
//define("REMOTEHOST", "http://im.ait.ac.th/aptana/likitomi/index.php/", TRUE);

//define("REMOTEURL", "http://203.159.1.4/aptana/likitomi/index.php/stock/getClampLiftFilter/", TRUE);
//define("LOCATEURL", "/clamplift/locatebytext.php", TRUE);

function mydb_connect()
{
	$conn = mysql_connect(HOST, USER, PASS) or die ("Error Connecting Local Database");
	mysql_select_db(DB);
	mysql_query(CHARSET);
	return $conn;
}

function remotedb_connect()
{
	$conn = mysql_connect(HOST, USER, PASS) or die ("Error Connecting Remote Database");
	mysql_select_db(DB,$conn);
	mysql_query(CHARSET);
	return $conn;
}
?>