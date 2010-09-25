<style type="text/css">
p {
    background-color: #C3D9FF;
    font-weight:bold;
	padding: 10px;
}
#writediv, #readdiv{
	padding:1px 0px 0px 40px;
}
</style>

<script type='text/javascript' >
	var CGIURL = 'http://localhost/cgi-bin/';
	function computeCount(){
		document.getElementById('cprefix').innerHTML= document.getElementById('prefix').value.length;
		document.getElementById('csuffix').innerHTML= document.getElementById('suffix').value.length;
		document.getElementById('tagid').innerHTML = "0x"+document.getElementById('prefix').value+document.getElementById('suffix').value;
		document.getElementById('ctagid').innerHTML= document.getElementById('tagid').innerHTML.length-2;
	}
	window.onload = function() {
		computeCount();
		Reset();
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
		document.getElementById('suffix').value = (parseInt(document.getElementById('suffix').value) + 1);
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
	}
	
</script>
<script language="JavaScript">

<!--
// please keep these lines on when you copy the source
// made by: Nicolas - http://www.javascript-page.com

var timerID = 0;
var tStart  = null;

function UpdateTimer() {
   if(timerID) {
      clearTimeout(timerID);
      clockID  = 0;
   }

   if(!tStart)
      tStart   = new Date();

   var   tDate = new Date();
   var   tDiff = tDate.getTime() - tStart.getTime();

   tDate.setTime(tDiff);

   document.theTimer.theTime.value = "" 
                                   + tDate.getMinutes() + ":" 
                                   + tDate.getSeconds();
   
   timerID = setTimeout("UpdateTimer()", 1000);
   readtag();
}

function Start() {
   tStart   = new Date();

   document.theTimer.theTime.value = "00:00";

   timerID  = setTimeout("UpdateTimer()", 1000);
}

function Stop() {
   if(timerID) {
      clearTimeout(timerID);
      timerID  = 0;
   }

   tStart = null;
}

function Reset() {
   tStart = null;
   document.theTimer.theTime.value = "00:00";
}

//-->

</script>

<div id="topheader"></div>

<table class='tblcontainer' border='0' width='100%' height='100%' cellspacing="0" cellpadding="0">
	<tr>
    <td class='headertop'>
        <div id='headbar'>
            <table border=0 width=100% >
            	<tr>
            		<td width='320'>
            			<ul class="primary-links">
            				<li><a href='<?=base_url()."index.php"?>'>Home</a></li>
							<li><span>Reader Management</span></li>
						</ul>
            		</td>
					<td align='center'>
						<ul class="primary-links" >
							<li><a href="#write">Write</a></li>
							<li><a href="#read">Read</a></li>
							<li><a href="#lab">Lab</a></li>
							<li><a href="#config">Configure</a></li>
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
<div>
<a name="write"></a>
<br/><br/>
<p>Write Tags</p>		
<div id='writediv'>
<table width='500px'>
	<tr>
		<td>Prefix</td>
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
		<td><textarea id="writelog" rows=15 cols=40  wrap="soft"> </textarea></td>
		<td>&nbsp;</td>
	</tr>
</table>
</div> 
<hr>
<br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/>

<a name="read"></a>
<br/><br/>
<p>Read Tags</p>		
<div id='readdiv'>
    <form name="theTimer">
        <input type=text name="theTime" size=5 />
		<input type=button name="start" value="Start" onclick="Start()"/>
		<input type=button name="stop" value="Stop" onclick="Stop()" />
		<input type=button name="reset" value="Reset" onclick="Reset()"/>
		<br/>
    </form>
</div>
<hr>
<br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/>


<hr>
<br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/>

<hr>
<br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/>

<hr>
<br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/>

<a name="lab"></a>
<br/><br/>
<p>Lab Test</p>		
<div id='labdiv'>
    <form name="theTimer">
        <input type=text name="theTime" size=5 />
		<input type=button name="start" value="Start" onclick="Start()"/>
		<input type=button name="stop" value="Stop" onclick="Stop()" />
		<input type=button name="reset" value="Reset" onclick="Reset()"/>
		<br/>
    </form>
</div>
<hr>
END 
</div>

	</td>
	</tr>
</table>
