<?php

$eTask = $_GET["eTask"];
$eID = $_GET["eID"];
$mo = $_GET["mo"];
$name = $_GET["name"];

include("db.php");
remotedb_connect();
$conn = remotedb_connect ();

$sql ="select *
FROM status
WHERE mo= '".$mo."'";
$rs = mysql_query($sql,$conn);

while($row = mysql_fetch_array($rs))
{
    if($eTask == 'CR')
	if($row[3]==$row[8])
            $expect =0;
        else
            $expect =  $row[8];
        
    elseif($eTask == 'CV')
        $expect = $row[3];
    elseif($eTask == 'PT')
        $expect = $row[4];
    elseif($eTask == 'WH')
        $expect = $row[5];
    $modified_date = $row[9];
    $modified_name = $row[10];
}
$sql1 ="select pc.product_code,pc.product_name
FROM planning pl, product_catalog pc
WHERE mo= '".$mo."' AND pl.product_code=pc.product_code";
$rs1 = mysql_query($sql1,$conn);
while($row1 = mysql_fetch_array($rs1))
{
    $product_code = $row1[0];
    $product_name = $row1[1];
}
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta content="yes" name="apple-mobile-web-app-capable" />
<meta content="index,follow" name="robots" />
<meta content="text/html; charset=tis-620" http-equiv="Content-Type" />
<link href="pics/homescreen.gif" rel="apple-touch-icon" />
<meta content="minimum-scale=1.0, width=device-width, maximum-scale=0.6667, user-scalable=no" name="viewport" />
<link href="css/style.css" rel="stylesheet" media="screen" type="text/css" />
<script src="javascript/functions.js" type="text/javascript"></script>
<title>iWebKit Demo - Easy form elements!</title>
<meta content="iPod,iPhone,Webkit,iWebkit,Website,Create,mobile,Tutorial,free" name="keywords" />
<meta content="now completly styles thanks to css these form elements are lighter and easier to use than ever before." name="description" />
<!-- focus cursor -->
<script type="text/javascript">
function setFocus()
{
 document.updateForm.amount.focus();
}

</script>
</head>

<body onload="setFocus()">

<div id="topbar">
        <div id="title"> Login As <?php print $name." (".$eTask.")"; ?></div>
	<div id="rightbutton"> 
		<a href="index.php" class="noeffect">Logout</a> </div> 
</div>

<div id="content">
<ul class="pageitem">
		<li class="textbox"><span class="header">Enter amount of finished product</span><p>Please count and fill in the number into this form.</p></li>
  </ul>
<form action="updateMessage.php" method="get" name="updateForm">
		
        <ul class="pageitem">
        <font color="#FFFFFF">a</font><br />
        <span class="graytitle">Manufacturing number</span>
        <ul class="pageitem"><li class="bigfield">
             <input name="eID" type="hidden" maxlength="4" value="<?php print $eID; ?>" />
             <input name="moT" disabled="disable" value="<?php print $mo; ?>" />
             <input name="mo" type="hidden" value="<?php print $mo; ?>" />
             <input name="eTask" type="hidden" maxlength="4" value="<?php print $eTask; ?>" />
        </li></ul>
        <span class="graytitle">Product Name</span> 
	<ul class="pageitem"><li class="bigfield"><input name="product_nameT" type="text"  value='<?php echo $product_name ." [".$product_code."]";?>' disabled="disabled" />
        <input name="productName" type="hidden"  value='<?php echo $product_name;?>' />
        <input name="productCode" type="hidden" value='<?php echo $product_code;?>' />
        </li></ul>
        
    <!-- input amount -->
    <?php 
    if($eTask =='CR')
        print '<span class="graytitle">Amount from sale order'; 
    if($eTask =='CV')
        print '<span class="graytitle">Amount from CR'; 
    if($eTask =='PT')
        print '<span class="graytitle">Amount from CV'; 
    if($eTask =='WH')
        print '<span class="graytitle">Amount from WH'; 
         
         
         if($expect==0)
         {
            print '<ul class="pageitem"><li class="bigfield"><input name="Pamount" type="text"  value="0" disabled="disabled"/></li></ul>';
            print '<span class="graytitle">Amount of finished product</span>';
            print '<ul class="pageitem"><li class="bigfield"><input name="amount" type="text"  value="0" disabled="disabled"/></li></ul>';
            print '</ul></form></div><div id="topbar"><div id="leftnav"><a href="scanMO.php?mo='.$mo.'&amp;eID='.$eID.'&amp;eTask='.$eTask.'">Change MO</a></div></div>';
         }
        else 
        {
            print ' by '.$modified_name.' on '.$modified_date.'</span><ul class="pageitem"><li class="bigfield"><input name="Pamount" type="text"  value="'.$expect.'"/></li></ul>';
            print '<span class="graytitle">Amount of finished product</span>';
            print '<ul class="pageitem"><li class="bigfield"><input name="amount" type="text"  value="'.$expect.'"/></li></ul>';
            print '</ul></form></div><div id="topbar"><div id="leftnav"><a href="scanMO.php?mo='.$mo.'&amp;eID='.$eID.'&amp;eTask='.$eTask.'">Change MO</a></div><div id="rightnav"><a onclick="updateForm.submit();">submit Amount</a></div></div>';
        }
     ?>

        
		
<div id="footer">

	<a href="http://iwebkit.net">Powered by iWebKit</a></div>

</body>

