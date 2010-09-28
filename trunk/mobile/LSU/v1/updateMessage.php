<?php
//error_reporting(E_ALL & ~E_NOTICE);
$mo = $_GET["mo"];
$eID = $_GET["eID"];
$eTask = $_GET["eTask"];
$amount = $_GET["amount"];
$product_name = $_GET["productName"];
$product_code = $_GET["productCode"];

include("db.php");
remotedb_connect();

$conn1 = remotedb_connect ();
$sql1 ="select product_code from planning where mo='".$mo."'";
$rs1 = mysql_query($sql1,$conn1);
while($row1 = mysql_fetch_array($rs1))
{
	$pCode = $row1[0];
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
        $expect= $row3[0];
}

$conn = remotedb_connect ();
//retrive list of SO
if($eTask == 'CR')
{
$sql ="UPDATE status SET mo='".$mo."',CR=".$amount.",amount=".$expect.",modified_by='".$name."'  WHERE product_code ='".$pCode."'";
}
if($eTask == 'CV')
{
$remain = $expect-$amount;
if($remain <0)
$remain = 0;

$sql ="UPDATE status SET mo='".$mo."',CR=".$remain.",CV=".$amount.",amount=".$expect.",modified_by='".$name."'  WHERE product_code ='".$pCode."'";
}
if($eTask == 'PT')
{
$remain = $expect-$amount;
if($remain <0)
$remain = 0;
$sql ="UPDATE status SET mo='".$mo."',CV=".$remain.",PT=".$amount.",amount=".$expect.",modified_by='".$name."'  WHERE product_code ='".$pCode."'";
}
if($eTask == 'WH')
{
$remain = $expect-$amount;
if($remain <0)
$remain = 0;
$sql ="UPDATE status SET mo='".$mo."',PT=".$remain.",WH=".$amount.",amount=".$expect.",modified_by='".$name."'  WHERE product_code ='".$pCode."'";

}
$rs = mysql_query($sql,$conn);
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=tis-620" />
<meta content="minimum-scale=1.0, width=device-width, maximum-scale=0.6667, user-scalable=no" name="viewport" />
<link href="css/style.css" rel="stylesheet" media="screen" type="text/css" />
<script src="javascript/functions.js" type="text/javascript"></script>
<title>Untitled Document</title>
</head>

<body>
<div id="topbar">
        <div id="title"> Login As <?php echo $name." (".$eTask.")"; ?></div>
	<div id="rightbutton"> 
		<a href="index.php" class="noeffect">Logout</a> </div> 
</div>
<div id="content">
<ul class="pageitem">
<font color="#FFFFFF">a</font><br />
        <span class="graytitle">Complete</span>
        <ul class="pageitem">
          <center><p>
            <?php
$DateOfRequest = date("Y-m-d H:i:s", time());             
	echo $name." has finished ".$product_name."(".$product_code.")"." at station ".$eTask." successfully with ".$amount." items on ".$DateOfRequest; 
	header("Refresh: 3; url=\"scanMO.php?eID=".$eID."&eTask=".$eTask."\"");
?>
          </p></center>
        </ul>
</ul>
</div>
</body>
</html>