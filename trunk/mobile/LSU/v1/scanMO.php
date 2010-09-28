<?php
error_reporting(E_ALL & ~E_NOTICE);
$eTask = $_GET['eTask'];
$eID = $_GET['eID'];
$mo = $_GET['mo'];

include("db.php");
remotedb_connect();
$conn = remotedb_connect ();
//retrive list of SO
$sql ="select *
FROM employee
WHERE eID = '".$eID."'";
$rs = mysql_query($sql,$conn);
while($row = mysql_fetch_array($rs))
{
        $name = $row[1];
	$eTask = $row[3];

}
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta content="yes" name="apple-mobile-web-app-capable" />
<meta content="index,follow" name="robots" />
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
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
 document.updateForm.mo.focus();
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
    <li class="textbox"><span class="header">Enter </span>In order to specify the user, please scan the barcode of your employee card.</li>
  </ul>
  <form action="inputAmount.php" method="get" name="updateForm">
    <ul class="pageitem">
      <font color="#FFFFFF">a</font><br />
     
      <!-- input Manufacturing code -->
      <span class="graytitle">Manufacturing number</span>
      <ul class="pageitem">
        <li class="bigfield">
          <input name="mo" type="text" value="<?php print $mo; ?>"  />
          <input name="eID" type="hidden" maxlength="4" value="<?php print $eID; ?>" />
          
          <input name="eTask" type="hidden" maxlength="4" value="<?php print $eTask; ?>" />
          <input name="name" type="hidden" maxlength="20" value="<?php print $name; ?>" />
        </li>
      </ul>
      <!-- product name -->
          <span class="graytitle">Product Name</span> 
	<ul class="pageitem"><li class="bigfield"><input name="product_name" type="text"  value='' disabled="disabled"/></li>
   
    </ul>
      <!-- input amount -->
      <?php if($eTask =='CR')
      {?>
      <span class="graytitle">Amount from sale order</span> 
    
    <?php }
    if($eTask =='CV')
      {?>
      <span class="graytitle">Amount from CR</span> 
    <?php } 
    if($eTask =='PT')
      {?>
      <span class="graytitle">Amount from CV</span> 
    <?php } 
    if($eTask =='WH')
      {?>
      <span class="graytitle">Amount from WH</span>     <?php } ?>
      
	<ul class="pageitem"><li class="bigfield"><input name="Expectedamount" type="text"  value="" disabled="disabled" /></li>
    </ul>

          <span class="graytitle">Amount of finished product</span> 
	<ul class="pageitem"><li class="bigfield"><input name="amount" type="text"  value=""   disabled="disabled"/></li>
    </ul></ul>
  </form>
<div id="topbar"> 
	<div id="leftnav"> </div> 
	<div id="rightnav"> <a onClick="updateForm.submit();">Submit MO</a></div> 
</div>
</div>
<div id="footer">

	<a href="http://iwebkit.net">Powered by iWebKit</a></div>
</body>



