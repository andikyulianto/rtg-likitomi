<?php
include("db.php");
remotedb_connect();
$conn = remotedb_connect ();
//retrive list of SO
$sql ="SELECT
DISTINCT sales_order.product_code_1, sales_order_id,amount_1
FROM
sales_order
group by
sales_order.product_code_1";
$rs = mysql_query($sql,$conn);
?>


<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta content="yes" name="apple-mobile-web-app-capable" />
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
<meta content="minimum-scale=1.0, width=device-width, maximum-scale=0.6667, user-scalable=no" name="viewport" />
<link href="css/style.css" rel="stylesheet" media="screen" type="text/css" />
<script src="javascript/effects.js" type="text/javascript"></script> 
<script src="javascript/slide.js" type="text/javascript"></script> 
<script src="javascript/tabs.js" type="text/javascript"></script>
<title>Likitomi : Real-time production report</title>
<meta content="likitomi,progress,report" name="keywords" />
<meta content="Overall report for process tracking" name="description" />
</head>
<body>
<div id="topbar">
	<div id="leftnav">
		<a href="index.php"><img alt="home" src="images/home.png" /></a></div>
	<div id="title"></div>
</div>
<div id="content"> 
	<ul class="pageitem"> 
		<li class="textbox"><span class="header">Product Code</span><p> 
		Please "touch" product item (listed as product code) in order to view the real-time progress.</p> 
		</li>  
        <?php
			while($row = mysql_fetch_array($rs))
			{
				$need = $row[2];
				$con2 = remotedb_connect ();
				$sql2 ="SELECT sum(CR) as CR,sum(CV) as CV,sum(PT) as PT,sum(WH) as WH
				FROM
				status
				WHERE 
				product_code ='".$row[0]."'
				 GROUP BY product_code";
				$rs2 = mysql_query($sql2,$con2);
				while($newRow = mysql_fetch_array($rs2))
				{
					 $stock = (int)$newRow[3];
				}
				if($need<=$stock)
				print "<li class='menu'><a href='getSOFromDate.php?PCode=".$row[0]."&SOID=".$row[1]."'> 
		<img alt='list' src='images/office/Package-Accept64.png' /><span class='name'>".$row[0]."</span><span class='arrow'></span></a></li>";
				else
				print "<li class='menu'><a href='getSOFromDate.php?PCode=".$row[0]."&SOID=".$row[1]."'> 
		<img alt='list' src='images/office/Package-Warning64.png' /><span class='name'>".$row[0]."</span><span class='arrow'></span></a></li>";
			}
		?>
  	</ul> 
    </div>

</body>
</html>