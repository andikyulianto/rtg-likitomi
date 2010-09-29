<?php
header("Expires: Mon, 26 Jul 1997 05:00:00 GMT"); // Date in the past
header("Last-Modified: " . gmdate("D, d M Y H:i:s") . " GMT"); // Always modified
header("Cache-Control: private, no-store, no-cache, must-revalidate"); // HTTP/1.1 
header("Cache-Control: post-check=0, pre-check=0", false);
header("Pragma: no-cache"); // HTTP/1.0
?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<title><?=$title?></title>
		<style type="text/css">
body {
    background: #FFFFFF;
    color: #4F5155;
    font-family: Lucida Grande, Verdana, Geneva, Sans-serif;
    font-size: 14px;
    margin: 0pt;
	cursor:default;
}
#footer {
    clear: both;
    color: #777777;
    font-size: 11px;
    padding: 5px;
    text-align: center;
}

table.tblbuttons td{
	padding:20px;
	
}

a{
	text-decoration:none;
	color:inherit;
}

#buttons
{
	-moz-border-radius:20px;
	background-color:#F0F0F0;
	border:1px solid #090909;
	font-size:300%;
	font-weight:bold;
	padding:20px;
	text-align:center;
	width:320px;
}

img{
	border:medium none;
}
#buttons:hover
{
	background-color:yellow;
}
		</style>	
</head>
	<body>
<div id="homeContent">
	<table width='100%' style='border-bottom:1px solid'>
		<tr>
			<td><h1>Likitomi (Thailand) Co.Ltd.</h1></td>
			<td align='right'><?=date('l, F d, Y')?></td>
			<td align='right'><a href="javascript:window.close();" ><img src='<?=base_url()?>static/images/poweroff.png'/></a></td>
		</tr>
	</table>
<center>
<table align='center' height='400' class='tblbuttons'>
	<tr>
		<td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td>		
	</tr>
	<tr>
		<td class='buttons'><a href=''> <div id='buttons'> PICK </div> </a></td>
		<td width='60px'>&nbsp;</td>
		<td class='buttons'><a href=''> <div id='buttons'> RETURN </div> </a></td>
	</tr>
	<tr>
		<td class='buttons'><a href=''><a href='<?=base_url()?>index.php/clampliftdriver/scan/'>  <div id='buttons'> SCAN </div> </a></td>
		<td width='60px'>&nbsp;</td>
		<td class='buttons'><a href='<?=base_url()?>index.php/clampliftdriver/track/'> <div id='buttons'> TRACK </div> </a></td>
	</tr>
	<tr>
		<td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td>		
	</tr>
</table></center>
</div>


<div class="clear"></div>

</div> 
	<div id="footer">
    <hr/>
	Page requested at <?=date('H:m:s',$_SERVER['REQUEST_TIME'])?> from <?=$_SERVER['SERVER_NAME']?> and rendered in {elapsed_time} seconds.Memory Usuage: {memory_usage}.<br />
	This application is developed as part of RTG-Budget Joint Industrial Research Project Fiscal Year, 2007-2008<br/>
	at <a href="http://www.ait.asia" target="_blank" >Asian Institute of Technology</a> for 
	<a href="http://www.likitomi.co.th/" target="_blank">Likitomi (Thailand) Company Limited</a>. 
	<div style="margin-top:5px">
		<a href="http://aptana.com/" target="_blank" ><img src="<?=base_url()?>static/images/built_with_aptana.gif" 
			alt="built with aptana" title="Aptana" border="0" /></a>							
		<a href="http://codeigniter.com/" target='_blank'><img src="<?=base_url()?>static/images/codeigniter.gif" title="Codeigniter" border="0" /></a>
	</div>	
    </div>
</body>
</html>