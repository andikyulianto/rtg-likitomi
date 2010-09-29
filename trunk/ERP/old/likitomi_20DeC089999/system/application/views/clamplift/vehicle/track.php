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
		var lastx=0; 
		var lasty=0;
		var ANT = 1;
		<?php 
			$MAX = 43; 
		?>
		var MAX = <?=$MAX;?>;
		var GETXML = "http://localhost/cgi-bin/getxml.py";
		
		function trackxml()
		{
			document.getElementById('btnlocate').disabled=true;
			document.getElementById('btnlocate').className='onprogres';
			
			var table 	= document.getElementById('tblmap');
			if (lastx > 0 && lasty > 0) {
				cleartable();
			}
			var xmlDoc;
			if (window.ActiveXObject)
			{
				xmlDoc=new ActiveXObject("Microsoft.XMLDOM");
			}
			else if (document.implementation.createDocument)
			{
				xmlDoc=document.implementation.createDocument("","",null);
			}
			else
			{
				alert('Your browser cannot handle this script');
			}
			xmlDoc.async=false;
			xmlDoc.onreadystatechange=verify;
			xmlDoc.load(GETXML);
			xmlObj=xmlDoc.documentElement;
			
			var total 	= xmlObj.getElementsByTagName("total")[0].childNodes[0].nodeValue;
			var tags 	= xmlObj.getElementsByTagName("tags");
			
			var totalCount = 0;
			var posX = 0;
			var posY = 0;
			var yindex = 0;
			for (i=0;i<tags.length;i++)
			{
				antenna = tags[i].childNodes[9].childNodes[0].nodeValue;
				
				if(antenna == ANT) 
				{
					tagvalue = tags[i].childNodes[1].childNodes[0].nodeValue;
					taglast = tagvalue.substr(22,25);
					laneindex = taglast.substr(0,2);
					tagint = parseFloat(taglast.substr(2));
					
					type = tags[i].childNodes[3].childNodes[0].nodeValue;
					
					repeat = tags[i].childNodes[11].childNodes[0].nodeValue;
					repeat = parseInt(repeat);
					if(laneindex=="AB") yindex = 1;
					else if(laneindex=="BC") yindex = 2;
					else if(laneindex=="CD") yindex = 3;
					else if(laneindex=="DE") yindex = 4;
					else yindex=0;
					totalCount += repeat;
					posX += tagint * repeat;
					posY += yindex * repeat;
					
					x = tagint;
					if(x<0) x=0;
					if(x><?=$MAX?>) x=<?=$MAX?>;
					y = yindex*2;
					//alert(x+','+y+','+tagint);
					table.rows[y].cells[x].className= "tagclass";
					//alert(totalCount);
				}
			}
			document.getElementById('totaltags').innerHTML=totalCount;
			if(totalCount<1){
				vehicleX = 0;
				vehicleY = 0;
			}else {
				vehicleX = Math.round(posX/totalCount);
				vehicleY = Math.round(posY/totalCount)*2;
			}
			textxy = vehicleY+','+vehicleX;
			//+","+table.rows[vehicleY].cells[vehicleX].offsetLeft;
			
			ddrivetip(textxy,vehicleY,table.rows[vehicleY].cells[vehicleX].offsetLeft);
			
			if (lastx > 0 && lasty > 0) {
				table.rows[lasty].cells[lastx].className= "oldvehicleclass";
			}
			table.rows[vehicleY].cells[vehicleX].className= "vehicleclass";
			lastx = vehicleX;
			lasty = vehicleY;
			document.getElementById('btnlocate').disabled=false;
			document.getElementById('btnlocate').className='buttons';
		}
		
        function verify(){
            // 0 Object is not initialized
            // 1 Loading object is loading data
            // 2 Loaded object has loaded data
            // 3 Data from object can be worked with
            // 4 Object completely initialized
            if (xmlDoc.readyState != 4) {
				alert("Proble");
                return false;
            }
        }
		
		
		//Tooltips
		
		function ddrivetip(thetext,tipy, tipx){
			var tipobj=document.getElementById("theToolTip");
			var pointerobj=document.getElementById("ToolTipPointer");
			tipobj.innerHTML=thetext;
			tipwidth=64;
			
			tipy=52+tipy*62; 
	 		tipx=tipx-tipwidth/2+4;	
						
			
			tipobj.style.width=tipwidth+'px';
			tipobj.style.left=tipx+'px';
			pointerobj.style.left=tipx+tipwidth/2-2+'px';
			tipobj.style.top=tipy+'px';
			pointerobj.style.top=tipy-9+'px';
			tipobj.style.visibility="visible";
			pointerobj.style.visibility="visible";
		}

		function hideddrivetip()
		{
			tipobj.style.visibility="hidden";
			pointerobj.style.visibility="hidden";
			tipobj.style.left="-1000px";
			tipobj.style.backgroundColor='';
			tipobj.style.width='';
		}

		function cleartable()
		{
			var table 	= document.getElementById('tblmap');
			for (var i = 0; i < table.rows.length; i++) {
				var thisrow = table.rows[i];
				for (var j = 1; j < thisrow.cells.length; j++) {
					thiscell = thisrow.cells[j];
					thiscell.className ="";
				}
			}
				
		}
		
		//Ticker Javascript
		var timerID = 0;
		var tStart  = null;
		var loop = 3;
		function UpdateTimer() {
			loop--;
			if(loop<0){
				loop=document.getElementById('selLoop').value;
				trackxml();
			}
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
		}

		function Start() {
		   tStart   = new Date();
		
		   document.theTimer.theTime.value = "00:00";
		
		   timerID  = setTimeout("UpdateTimer()", 1000);
		}
		
		function Stop(){
		   if(timerID) {
		      clearTimeout(timerID);
		      timerID  = 0;
		   }
		
		   tStart = null;
		}
		
		function Reset() {
		   tStart = null;
		
		   document.theTimer.theTime.value = "00:00";
		   loop = document.getElementById('selLoop').value;
		}

		</script>
		<style type="text/css">
body {
    background: #FFFFFF;
    color: #4F5155;
    font-family: Lucida Grande, Verdana, Geneva, Sans-serif;
    font-size: 14px;
    margin: 0pt;
	cursor:default;
}

table {
    border-collapse: collapse;
	width:100%;
}
.buttons 
{
	background-color:#F0F0F0;
	border:1px solid #090909;
	font-size:120%;
	font-weight:bold;
	text-align:center;
	color:black;
	width:100px;
}

.onprogres
{
	background-color:#5BEC83;
	border:1px solid #090909;
	font-size:120%;
	font-weight:bold;
	text-align:center;
	color:black;
	width:100px;
}

td.headbar {
	background-color: #4F5155;
	color: #FFFFFF;
}

tr.papers
{
	background: url('<?=base_url()?>static/images/papers.png');
}
td.titlename{
	background: #4F5155 url();
	color:#FFFFFF;
	font-weight:bold;
	border:#FFFFFF 1px solid;
}

td.footer{
	background: #EF411F url();
	color:#FFFFFF;
	font-weight:bold;
	border:#FFFFFF 1px solid;
}

td.tagclass{
	background: #00FFFF url();
}

td.vehicleclass{
	background: red url();
}

td.oldvehicleclass{
	background: green url();
}

/* ----- tool tip specific styles ----- */ 
#theToolTip {
	-moz-border-radius: 10px;
    position: absolute;
    left: -300px;
    width: 64px;
    border: 1px solid #999999;
    padding: 8px;
    background-color: #333333 ;
	color: #FFFFFF;
	/*visibility: hidden;*/
    z-index: 100;
    /*Remove below line to remove shadow. Below line should always appear last within this CSS*/
    filter: progid:DXImageTransform.Microsoft.Shadow(color=gray,direction=135,strength=4);
	text-align:center;
} 

#ToolTipPointer {
    position: absolute;
    left: -300px;
    z-index: 101;
    /*visibility: hidden;*/
} 
#theToolTip p {
    font-size: 1.1em;
    color: #333333;
    line-height: 1.4em;
    margin-right: 10px;
    margin-top: 0;
} 

#ToolTipTextWrap {
    font-weight: bold;
    font-size: 1.2em;
    color: #592C16;
    margin-right: 10px;
}


		</style>
	
</head>
<body  onload="Reset()" onunload="Stop()">
<table>
	<tr>
		<td class='headbar' height='30'>
			<table>
				<tr>
					<td align='left'><input type='button' class='buttons' value='HOME' onclick='location.href="<?=base_url()?>index.php/clampliftdriver/";' /></td>
					<td align='center'><input type='button' onclick='trackxml()' class='buttons' id='btnlocate' value=' LOCATE ' /></td>
					<td width=400>
                    <center><form name="theTimer">
                    	<table>
							<tr>
								<td><select id='selLoop'>
										<?php 
										for ($i=3;$i<=10;$i++)
										{
											echo "<option value='$i'>$i</option>";
										}
									?>
									</select>
								</td>
								<td><input type=text name="theTime" size=5></td>
								<td><input type=button name="start" value="Start" class='buttons'  onclick="Start()"></td>
								<td><input type=button name="stop" value="Stop" class='buttons' onclick="Stop()"></td>
								<td><input type=button name="reset" value="Reset" class='buttons' onclick="Reset()"></td>
							</tr>
						</table>
					</form></center>
					</td>
					<td align='right' width='40px'><span id='totaltags'></span></td>
				</tr>
			</table>
		</td>
	</tr>
	<tr>
		<td height='1'></td>
	</tr>
	<tr>
		<td>
			<div id='mapid' >
			<table id='tblmap' height='400' width='200px' border='1' bordercolor="#F0F0F0">
				<?php
					$title = array("","A", "", "B","", "C","", "D","", "E","", "F","", "G");
					for($i=0;$i<=9;$i++)
					{
						$class= ($i%2!=0)?'papers':'';
						echo "<tr class='".$class."'>";
						 $h =($i==0)?20:62;
						echo "<td class='titlename' height='$h' width='2' id='".$i."0'> ".$title[$i] ."</td>";
						for($j=1;$j<=$MAX;$j++)
						{
							echo "<td  id='".$i.$j."'>&nbsp;</td>";
						}
						echo "</tr>";
					}
				?>
			</table>
			</div>
		</td>
	</tr>
</table>
<div id="theToolTip"></div>
<img id="ToolTipPointer" src="<?=base_url()?>static/images/tooltiparrow.gif"/>

</body>
</html>