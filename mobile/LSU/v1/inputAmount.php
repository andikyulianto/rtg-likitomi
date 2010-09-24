<?php
$mo = $_GET[mo];
$eID = $_GET[eID];
$eTask = $_GET[eTask];
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
 document.updateForm.amount.focus();
}

</script>
</head>

<body onload="setFocus()">

  <div id="topbar"> 
	<div id="leftnav"> 
    <a href="scanMO.php?mo=<?php print $mo; ?>&amp;eID=<?php print $eID;?>&amp;eTask=<?php print $eTask; ?>">Manufacturing number</a>
		</div> 
	<div id="rightnav"> 
    <a onclick="updateForm.submit();">Amount</a></div> 
</div>
</div>
<div id="content">
<ul class="pageitem">
		<li class="textbox"><span class="header">Enter no. of finished products</span><p>Please count and fill in the number into this form.</p></li>
  </ul>
<form action="updateMessage.php" method="get" name="updateForm">
		
        <ul class="pageitem">
        <font color="#FFFFFF">a</font><br />
        <span class="graytitle">Manufacturing number</span><ul class="pageitem">
			<li class="bigfield">
             <input name="eID" type="hidden" maxlength="4" value="<?php print $eID; ?>" />
             <input name="mo" value="<?php print $mo; ?>" />
    <input name="eTask" type="hidden" maxlength="4" value="<?php print $eTask; ?>" />
			</li></ul>
   
    <span class="graytitle">Amount</span> 
	<ul class="pageitem"><li class="bigfield"><input name="amount" type="text" /></li>
   
    </ul>
            
		</ul>
        
		</fieldset></form>
</div>
<div id="footer">

	<a href="http://iwebkit.net">Powered by iWebKit</a></div>

</body>

