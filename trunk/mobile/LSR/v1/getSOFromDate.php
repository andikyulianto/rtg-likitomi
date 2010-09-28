<?php
$PCode = $_GET['PCode'];
$SOID =$_GET['SOID'];


include("db.php");
remotedb_connect();
$conn = remotedb_connect ();
$sql ="SELECT sum(CR) as CR,sum(CV) as CV,sum(PT) as PT,sum(WH) as WH
FROM
status
WHERE 
product_code ='".$PCode."'
 GROUP BY product_code";
$rs = mysql_query($sql,$conn);
while($row = mysql_fetch_array($rs))
{
$process["CR"] = (int)$row[0];
$process["CV"] = (int)$row[1];
$process["PT"] = (int)$row[2];
$process["WH"] = (int)$row[3];
}

//retrive list of SO
/*
$sql ="SELECT
delivery_date,amount_1
FROM
delivery de,sales_order so
WHERE 
de.sales_order =  so.sales_order_id
AND
de.sales_order ='".$SOID."'";
*/
$sql="SELECT
delivery.delivery_date,
delivery.delivery_time,
delivery.qty
FROM
delivery ,
total_planning
WHERE
delivery.delivery_id =  total_planning.delivery_id
AND
delivery.product_code ='".$PCode."'";
//echo $sql;
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
<style type="text/css">
<!--
#calendar table {
	font-size: 8px;
	color: #FFF;
	font-weight: bold;
}
#content .pageitem .menu a #calendar table tr td font {
	font-size: 18px;
	text-align: center;
}
#content .pageitem .menu table tr td {
	font-size: 8pt;
	color: #FFF;
	font-weight: bold;
}
#content .pageitem .menu table {
	text-align: center;
}
.content {
	color: #000;
	font-size: 18px;
}
#content .pageitem .pageitem #calendar table tr td font {
	font-size: 18px;
}
#content .pageitem .pageitem table {
	font-weight: bold;
	font-size: 18px;
}
#content .pageitem #calendar table tr td font {
	font-size: 18px;
}
#content .pageitem table .center tr td #calendar1 table tr th {
	color: #FFF;
	font-size: 9pt;
}
#content .pageitem table .center tr td #calendar1 table tr td font {
	font-weight: bold;
	position: relative;
}
#content .pageitem table .center tr td #calendar1 table {
	text-align: center;
	position: relative;
	top: auto;
	left: auto;
	right: auto;
	bottom: auto;
	font-weight: bold;
}
-->
</style>
</head>
<body>
<div id="topbar">
	<div id="leftnav">
		<a href="index.php"><img alt="home" src="images/home.png" /></a>
        <a href="getSOFromDate.php?PCode=<?php echo $PCode; ?>&SOID=<?php echo $SOID; ?>">Product Code</a>
  </div>
</div>
<div id="content">
  <ul class="pageitem">
  
  <li class="textbox"><span class="header">Product Code: <?php print $PCode; ?></span>
      <p> This is the quantity of production line in the sale product &quot;<?php print $PCode; ?>&quot; which is sorted by date.</p>
    </li>
   <div id ="output"></div>
    <table width="98%"border="1" cellpadding="2"  cellspacing="0" bordercolor="#99CCFF" align="center" >
      <span class="center">
        <tr >
          <th width="16%">Date</th>
          <th width="14%">Time</th>
          <th width="14%">Need</th>
          <th width="14%">CR</th>
          <th width="14%">CV</th>
          <th width="14%">PT</th>
          <th width="14%">WH</th>
        </tr>
      </span>
       <!-- Begin looping row -->
       <?php
			while($row = mysql_fetch_array($rs))
			{
				$output["CR"] = 0;
				$output["CV"] = 0;
				$output["PT"] = 0;
				$output["WH"] = 0;
				//extract date time
				$amount = $row[2];
				$dateTime = getdate(strtotime($row[0].' '.$row[1]));
				if (strlen($dateTime['minutes'])<2)
				$dateTime['minutes'] = "0".$dateTime['minutes'];
				$need = (int)$amount;

					
					if($process["WH"]>=0 && $need>=0)
					{
						if($process["WH"]>=$need)
						{
							$process["WH"]-=$need;
							$output["WH"] ="<img alt='list' src='images/office/Package-Accept32.png' />";
							$need = 0;
						}
						else
						{
							$need -=$process["WH"];
							$output["WH"] = $process["WH"];
							$process["WH"] = 0;
						}
					}
					if($process["PT"]>=0 && $need>=0)
					{
						if($process["PT"]>$need)
						{
							$process["PT"]-=$need;
							$output["PT"] =$need;
							$need = 0;
						}
						else
						{
							$need -=$process["PT"];
							$output["PT"] = $process["PT"];
							$process["PT"] = 0;
						}
					}
					if($process["CV"]>=0 && $need>=0)
					{
						if($process["CV"]>$need)
						{
							$process["CV"]-=$need;
							$output["CV"] =$need;
							$need = 0;
						}
						else
						{
							$need -=$process["CV"];
							$output["CV"] = $process["CV"];
							$process["CV"] = 0;
						}
					}
					if($process["CR"]>=0 && $need>=0)
					{
						if($process["CR"]>$need)
						{
							$process["CR"]-=$need;
							$output["CR"] =$need;
							$need = 0;
						}
						else
						{
							$need -=$process["CR"];
							$output["CR"] = $process["CR"];
							$process["CR"] = 0;
						}
					}
				
				print "<tr>
        <td><div id='calendar1'>";
		if($row[0]!=NULL)
		print "<table width='100%' height='46' border='0' cellpadding='2'  cellspacing='0'  >
            <tr >
              <th height='15' align='center' valign='bottom' >".substr($dateTime['month'],0,3)."</th>
            </tr>
            <tr>
              <td width='100%' height='15' align='center' valign='top'>".$dateTime['mday']."</td>
            </tr>
          </table></div></td>
        <td>".$dateTime['hours']."h".$dateTime['minutes']."</td>";
		 else
		 print "<table width='100%' height='46' border='0' cellpadding='2'  cellspacing='0'  >
            <tr >
              <th height='15' align='center' valign='bottom' ></th>
            </tr>
            <tr>
              <td width='100%' height='15' align='center' valign='top'>CM</td>
            </tr>
          </table></div></td>
        <td>CM</td>";
		 print "<td>".$row[2]."</td>
        <td>".$output["CR"]."</td>
        <td>".$output["CV"]."</td>
        <td>".$output["PT"]."</td>
        <td>".$output["WH"]."</td>
      </tr>";
	  
			}
		?>
        <!--End produce looping row -->
      
      
    </table>
    <br />
  </ul>
</div>
</body>
</html>