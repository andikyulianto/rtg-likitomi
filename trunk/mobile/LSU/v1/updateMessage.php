<?php
$mo = $_GET[mo];
$eID = $_GET[eID];
$eTask = $_GET[eTask];
$amount = $_GET[amount];

include("db.php");
remotedb_connect();

$conn1 = remotedb_connect ();
$sql1 ="select product_code from planning where mo='".$mo."'";
$rs1 = mysql_query($sql1,$conn1);
while($row1 = mysql_fetch_array($rs1))
{
	$pCode = $row1[0];
        $oldAmount = $row1[1];
}

$conn2 = remotedb_connect ();
$sql2 = "select firstname from employee where eID='".$eID."'";
$rs2 = mysql_query($sql2,$conn2);
while($row2 = mysql_fetch_array($rs2))
{
	$name = $row2[0];
}

$conn3 = remotedb_connect ();
$sql3 ="select amount from status where mo='".$mo."'";
$rs3 = mysql_query($sql3,$conn3);
while($row3 = mysql_fetch_array($rs3))
{
        $oldAmount = $row3[0];
}

$conn = remotedb_connect ();
//retrive list of SO
if($eTask == 'CR')
{
$sql ="INSERT INTO status (mo,product_code,CR)
VALUES ('".$mo."','".$pCode."',".$amount.")
";
}
if($eTask == 'CV')
{
$remove_CR = 0-$amount;
$sql ="INSERT INTO status (mo,product_code,CR,CV)
VALUES ('".$mo."','".$pCode."',".$remove_CR.",".$amount.")";
echo $sql;
}
if($eTask == 'PT')
{
$remove_CV = 0-$amount;
$sql ="INSERT INTO status (mo,product_code,CV,PT)
VALUES ('".$mo."','".$pCode."',".$remove_CR.",".$amount.")";
}
if($eTask == 'WH')
{
$remove_PT = 0-$amount;
$sql ="INSERT INTO status (mo,product_code,PT,WH)
VALUES ('".$mo."','".$pCode."',".$remove_CR.",".$amount.")";
}
$rs = mysql_query($sql,$conn);?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta content="minimum-scale=1.0, width=device-width, maximum-scale=0.6667, user-scalable=no" name="viewport" />
<link href="css/style.css" rel="stylesheet" media="screen" type="text/css" />
<script src="javascript/functions.js" type="text/javascript"></script>
<title>Untitled Document</title>
</head>

<body>
<div id="content">
<ul class="pageitem">
<font color="#FFFFFF">a</font><br />
        <span class="graytitle">Complete</span>
        <ul class="pageitem">
          <center><p>
            <?php
$DateOfRequest = date("Y-m-d H:i:s", mktime($_REQUEST["Hour"],$_REQUEST["Min"],$_REQUEST 
["Sec"],$_REQUEST["Month"],$_REQUEST["Day"],$_REQUEST["Year"]));             
	echo $name." has updated progress at station ".$eTask." successfully" ;//on .$DateOfRequest; 
	header("Refresh: 3; url=\"scanMO.php?eID=".$eID."&eTask=".$eTask."\"");
?>
          </p></center>
        </ul>
</ul>
</div>
</body>
</html>