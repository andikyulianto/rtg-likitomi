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
		<script type="text/javascript">
		var GETXML = "http://localhost/cgi-bin/getxml.py";

		</script>
		<script type="text/javascript" src="<?=base_url()?>resources/javascript/ext/ext-base.js"></script>
		<script type="text/javascript" src="<?=base_url()?>resources/javascript/ext-all.js"></script>		
		
		<style type="text/css">
			@import "<?=base_url()?>static/css/styles.css";	
			@import "<?=base_url()?>static/css/common.css";
			@import "<?=base_url()?>resources/css/ext-all.css";
			p {
			    background-color: #C3D9FF;
			    font-weight:bold;
				padding: 10px;
			}
			#executediv, #writediv,#loopdiv{
				padding:1px 0px 0px 40px;
			}
		</style>	
		
<script type='text/javascript'>
	var CGIURL = 'http://localhost/cgi-bin/';
	function computeCount(){
		document.getElementById('cprefix').innerHTML= document.getElementById('prefix').value.length;
		document.getElementById('csuffix').innerHTML= document.getElementById('suffix').value.length;
		document.getElementById('tagid').innerHTML = "0x"+document.getElementById('prefix').value+document.getElementById('suffix').value;
		document.getElementById('ctagid').innerHTML= document.getElementById('tagid').innerHTML.length-2;
	}
	window.onload = function() {
		computeCount();
		window.scrollTo(0,32);
	}
	
	function readtag(){
		var tagid = document.getElementById('tagid').innerHTML;
		Ext.Ajax.request({
			url: CGIURL+'readtag.py',
			params : { tagid : tagid},
			success: function ( result, request ) { 
				document.getElementById('writelog').value = result.responseText;
				unloadAjax();
			},
			failure: function ( result, request) { 
				document.getElementById('writelog').value = result.responseText;
				unloadAjax();
			} 
		});
		Ext.Ajax.on({
		    'beforerequest': function(){
				loadAjax("Loading...");
			},
		    'requestcomplete': function(){}
		});	
		//document.getElementById('suffix').value = (parseInt(document.getElementById('suffix').value) + 1);
		computeCount();
	}
	function writetag(){
		var tagid = document.getElementById('tagid').innerHTML;
		Ext.Ajax.request({
			url: CGIURL+'writetag.py',
			params : { tagid : tagid},
			success: function ( result, request ) { 
				document.getElementById('writelog').value = result.responseText;
				unloadAjax();
			},
			failure: function ( result, request) { 
				document.getElementById('writelog').value = result.responseText;
				unloadAjax();
			} 
		});
		Ext.Ajax.on({
		    'beforerequest': function(){
				loadAjax("Loading...");
			},
		    'requestcomplete': function(){}
		});	
		//readtag();
	}
	function copyCommand()
	{
		document.getElementById('txtexcutecmd').value = document.getElementById('selcommand').value;
		document.getElementById('loopcmd').value = document.getElementById('selcommand').value;
	}
	function execute()
	{
		var commandtext = document.getElementById('txtexcutecmd').value;
		Ext.Ajax.request({
			url: CGIURL+'executecmd.py',
			params : { commandtext : commandtext},
			success: function ( result, request ) { 
				document.getElementById('executelog').value = result.responseText;
				unloadAjax();
			},
			failure: function ( result, request) { 
				document.getElementById('executelog').value = result.responseText;
				unloadAjax();
			} 
		});
		Ext.Ajax.on({
		    'beforerequest': function(){
				loadAjax("Loading...");
			},
		    'requestcomplete': function(){}
		});	
	}
	
	//loop
	function startloop() {
		timerID  = setTimeout("UpdateTimer()", document.getElementById('seltimeout').value);
	}
	function UpdateTimer() {
		var commandtext = document.getElementById('loopcmd').value;
		Ext.Ajax.request({
			url: CGIURL+'executecmd.py',
			params : { commandtext : commandtext},
			success: function ( result, request ) { 
				document.getElementById('looplog').value += result.responseText;
				unloadAjax();
			},
			failure: function ( result, request) { 
				document.getElementById('looplog').value += result.responseText;
				unloadAjax();
			} 
		});
		Ext.Ajax.on({
		    'beforerequest': function(){
				loadAjax("Loading...");
			},
		    'requestcomplete': function(){}
		});	
		timerID = setTimeout("UpdateTimer()", 1000);
	}
	function clearloop()
	{
		document.getElementById('looplog').value ="";
	}
	function stoploop()
	{
		if(timerID) {
		  clearTimeout(timerID);
		  timerID  = 0;
		}
	}
	
</script>
	<script type="text/javascript">
		var mask = new Ext.LoadMask(Ext.getBody(), { msg: "Loading..." });
		function loadAjax(msg){
			document.getElementById('ajax_loading').style.visibility="visible";
			document.getElementById('ajax_loading').style.display="block";
			document.getElementById('ajax_loading').innerHTML=msg;
			if(mask!=null)mask.show();
		}
		function unloadAjax(){
			document.getElementById('ajax_loading').innerHTML="";
			document.getElementById('ajax_loading').style.display="none";
			document.getElementById('ajax_loading').style.visibility="hidden";
			if(mask!=null)mask.hide();
		}
	</script>
</head>
<body>
<div id="topheader"></div>
<div id='ajax_loading'>Loading..</div>
<table class='tblcontainer' border='0' width='100%' height='100%' cellspacing="0" cellpadding="0">
	<tr>
    <td class='headertop'>
        <div id='headbar'>
            <table border=0 width=100% >
            	<tr>
            		<td width='320'>
            			<ul class="primary-links">
            				<li><a href='<?=base_url()."index.php/clampliftdriver/"?>'>Home</a></li>
							<li><span>Reader Scan</span></li>
							<li><a href='<?=base_url()."index.php/clampliftdriver/track/"?>'>Track</a></li>
						</ul>
            		</td>
					<td align='center'>
						<input type='button' value='Scan' />
						<input type='button' value='Auto Scan' />
						
					</td>
                    <td align='right' width='280'></td>
					<td width='40px'><a href='<?=base_url()."index.php/auth/logout"?>' id='tip-logout'>
						<img src='<?=base_url()."static/images/logout.png"?>' />
					</a></td>
				</tr>
            </table>
        </div>
    </td>
	</tr>
	<tr>
	    <td>
	
		</td>
	</tr>
</table>
</body>
</html>