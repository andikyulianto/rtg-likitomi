<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta content="yes" name="apple-mobile-web-app-capable" />
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
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
 document.loginForm.eID.focus();
}

</script>
</head>

<body onload="setFocus()">


 
<div id="content">
	<ul class="pageitem">
		<li class="textbox"><span class="header">Login</span><p>In order to specify the user, please scan the barcode of your employee card.</p></li>
  </ul>
<form action="scanMO.php" method="get" name="loginForm">
		<fieldset><span class="graytitle">Employee ID</span>
		<ul class="pageitem">
			<li class="bigfield">
                        <input name="eID" type="text" maxlength="4" />
			</li>
            <li class="button">
			<input name="clearID" type="reset" value="Reset" onclick="setFocus()" /></li>
		</ul>
        
  </fieldset></form>
</div>

</body>

</html>
