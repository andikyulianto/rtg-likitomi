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
<body onload='copyCommand()'>
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
						<ul class="primary-links" >
							<li><a href="#execute">Execute</a></li>
							<li><a href="#write">Write/Read</a></li>
							<li><a href="#loop">Loop</a></li>
						</ul>
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

<a name="execute"></a>
<p height='40px'>&nbsp;</p>
<p>Execute Commands</p>		
<div id='executediv'>
<table >
	<tr>
		<td rowspan=2 valign='top'>
			<select id='selcommand' size='17' onchange='copyCommand()'>
				<option value='tag.db.get()' >tag.db.get()</option>
				<option value='tag.db.scan_tags(ms = 1000)' >tag.db.scan_tags(ms = 1000)</option>
				<option value='tag.reporting.taglist_fields=tag_id'>tag.reporting.taglist_fields=tag_id</option>
				<option value='tag.read_id()'>tag.read_id()</option>
				<option value='reader.is_alive()'>reader.is_alive()</option>
				<option value='reader.login(admin,readeradmin)'>reader.login(admin,readeradmin)</option>
				<option value='setup.operating_mode'>setup.operating_mode</option>
				<option value='antennas.mux_sequence'>antennas.mux_sequence</option>
				<option value='antennas.detected'>antennas.detected</option>
				<option value='setup.protocols'>setup.protocols</option>
				<option value='tag.db.purge()'>tag.db.purge()</option>
			</select>
			
			
		</td>
		<td><input type=text value='' id='txtexcutecmd' size='28' /> 
		<input type=button value='Execute' onclick='execute()'/>
		</td>
	</tr>
	<tr>
		<td><textarea id="executelog" rows=15 cols=40  wrap="soft"> </textarea></td>
	</tr>
</table>
</div> 
<hr>	
<br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/>


<a name="write"></a>
<p height='40px'>&nbsp;</p>
<p>Write Tags</p>		
<div id='writediv'>
<table width='500px'>
	<tr>
		<td width='80px'>Prefix</td>
		<td><input type='text' id='prefix' value='30000000000000000000B0' size='21' onkeyup='computeCount()'/></td>
		<td align=right><span id='cprefix'></span></td>
	</tr>
	<tr>
		<td>Suffix</td>
		<td><input type='text' id='suffix' value='01' size='3' onkeyup='computeCount()'/></td>
		<td align=right><span id='csuffix'></span></td>
	</tr>
	<tr>
		<td>Tagid</td>
		<td><span id='tagid'></span></td>
		<td align=right><span id='ctagid'></span></td>
	</tr>
	<tr>
		<td>
			<input type="button" value=" Read " onclick="readtag()"/><br/>
			<input type="button" value=" Write " onclick="writetag()"/>
		</td>
		<td colspan=2><textarea id="writelog" rows=20 cols=70  wrap="soft"> </textarea></td>
	</tr>
</table>
</div> 
<hr>	
<br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/>


<a name="loop"></a>
<p height='40px'>&nbsp;</p>
<p>Execute Commands</p>		
<div id='loopdiv'>
<table >
	<tr>
		<td><select id='seltimeout' >
			<?php 
				for ($i=3;$i<=20;$i++)
				{
					echo "<option value='".($i*100)."'>".($i*100)."</option>";
				}
			?>
		</select>
		</td>
		<td><input type=text value='' id='loopcmd' size='28' /> </td>
		<td>
		<input type=button value='Start Loop' onclick='startloop()'/>
		<input type=button value='Stop Loop' onclick='stoploop()'/>
		<input type=button value='Clear' onclick='clearloop()'/>
		</td>
	</tr>
	<tr>
		<td colspan='3'><textarea id="looplog" rows=15 cols=80  wrap="soft"> </textarea></td>
	</tr>
</table>
</div> 
<hr>	
<br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/>

	
	</td>
	</tr>
</table>
</body>
</html>