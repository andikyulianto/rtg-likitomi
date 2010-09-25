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
		<script type="text/javascript" src="<?=base_url()?>static/javascript/clamplift.js"></script>
		<script type="text/javascript">
		var lastpos  = 0;
		var lasttime = "<?=date('H:m')?>"
		var lastlane = 0;
		var thispos = 0;
		var thistime = "";
		var thislane = 0;
		
		function getxml()
		{
			document.getElementById('btnlocate').disabled=true;
			document.getElementById('btnlocate').className='onprogress';
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
			xmlDoc.load(GETSTGXML);
			xmlObj=xmlDoc.documentElement;
			
			
			if ((thispos > 0) || (thislane > 0)) {
				lastpos  = thispos;
				lastlane = thislane;
				lasttime = thistime;
			}
			
			thistime = getCurTime();
			var total 	= xmlObj.getElementsByTagName("total")[0].childNodes[0].nodeValue;
			thispos 	= xmlObj.getElementsByTagName("location")[0].childNodes[1].childNodes[0].nodeValue;
			thislane	= xmlObj.getElementsByTagName("location")[0].childNodes[3].childNodes[0].nodeValue;
			
			setTracks();
			
			var allValues = new Array();
//			var allValues = new Array();
			var stgtags = xmlObj.getElementsByTagName("stgid");
			
//			if(stgtags.length>0)
//			{
//				clearRows();
//			}
			for (i = 0; i < stgtags.length; i++) {
				tagid = stgtags[i].childNodes[0].nodeValue;
				//check duplicate
//				duplicate = false;
//				for(j =0; j <allValues.length;j++)
//				{
//					if(allValues[j]==tagid) duplicate=true;
//				}
//				if(!duplicate)insertRow(tagid);

				allValues[i]=tagid;
			}
				/*
				
				if(antenna == ANT) 
				{
					tagvalue = tags[i].childNodes[1].childNodes[0].nodeValue;
					taglast = tagvalue.substr(22,25);
					laneindex = taglast.substr(0,2);
					tagint = parseFloat(taglast.substr(2));
					//alert(taglast.substr(2));
					//alert(tagint);
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
			
			*/
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
		
		function getCurTime()
		{
			var currentTime = new Date()
			var hours = currentTime.getHours()
			var minutes = currentTime.getMinutes()
			if (minutes < 10){
				minutes = "0" + minutes
			}
			curtime = hours + ":" + minutes + " ";
			return curtime;
		}
		
		function setTracks()
		{
			document.getElementById('lanenow').innerHTML = thislane;
			document.getElementById('positionnow').innerHTML = thispos;
			document.getElementById('timenow').innerHTML = thistime;
			var table = document.getElementById('tracktbl');
			table.className = "tbllane"+thislane;
					
			document.getElementById('lanelast').innerHTML = lastlane;
			document.getElementById('positionlast').innerHTML = lastpos;
			document.getElementById('timelast').innerHTML = lasttime;
			document.getElementById('trackoldtbl').className = "tbllane"+lastlane;
		}
		
		function insertRow(tagid)
		{
			var tbl = document.getElementById('tabletags');
			var lastRow = tbl.rows.length;
			try {
			 	var row = tbl.insertRow(lastRow);
				cell= row.insertCell(0);
				cell.innerHTML=lastRow;
				cell= row.insertCell(1);
				cell.innerHTML=tagid;
			} 
		    catch (ex) {
		    }
		}
		
		function clearRows()
		{
			var tbl = document.getElementById('tabletags');
			var lastRow = tbl.rows.length;
			for (k = lastRow-1; k >0 ; k--) {
				try {
					tbl.deleteRow(k);
				} 
				catch (ex) {
					alert("---"+k);
				}
			}
		}
		
		
        //Ticker Javascript
        var timerID = 0;
        var tStart = null;
        var loop = 3;
		var timeout = 1000;
        function UpdateTimer(){
            getxml();
            if (timerID) {
                clearTimeout(timerID);
                timerID = 0;
            }
            timerID = setTimeout("UpdateTimer()", timeout);
        }
        
        function Start(){
            timerID = setTimeout("UpdateTimer()", timeout);
			document.getElementById('start').disabled=true;
			document.getElementById('stop').disabled=false;
			document.getElementById('start').className='onprogress';
        }
        
        function Stop(){
            if (timerID) {
                clearTimeout(timerID);
                timerID = 0;
            }
			document.getElementById('start').disabled=false;
			document.getElementById('stop').disabled=true;
			document.getElementById('start').className='buttons';
        }
</script>
		<style type="text/css">
body {
    background: #FFFFFF;
    color: #4F5155;
    font-family: Lucida Grande, Verdana, Geneva, Sans-serif;
    font-size: 14px;
    margin: 0pt;
	cursor:hand;
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
	padding: 10px 40px;
}

.onprogress
{
	background-color:#5BEC83;
	border:1px solid #090909;
	font-size:120%;
	font-weight:bold;
	text-align:center;
	color:black;
	padding: 10px 40px;
}

td.headbar {
	background-color: #4F5155;
	color: #FFFFFF;
}



td.lane {
	font-size:900%;
	font-weight:bold;
	padding:30px;
	
}

#tracktbl td{	
	border:2px #0F0F0F solid;
	color:#0F0F0F;
}

table.tbllane1 td{
	background-color:#FFADAD;
}

table.tbllane2 td{
	 background-color:#66F487;
}

table.tbllane3 td{
	 background-color:#8EBBF6;
}

table.tbllane4 td{
	 background-color:#FF7400;
}

#lanenow{
	font-size:150%;
	font-weight:bold;	
}


</style>
	
</head>
<body onunload="javascript:Stop()">
<table>
	<tr>
		<td class='headbar' height='50'>
			<table>
				<tr>
					<td align='left'><input type='button' class='buttons' value='HOME' onclick='location.href="<?=base_url()?>index.php/clampliftdriver/";' /></td>
					<td align='center'><input type='button' onclick='Stop();getxml()' class='buttons' id='btnlocate' value=' LOCATE ' /></td>
					<td align='right'>
                    <table>
						<tr>
							<td><input type=button id="start" value="Start" class='buttons'  onclick="Start()"></td>
							<td><input type=button id="stop" value="Stop" class='buttons' onclick="Stop()"></td>
						</tr>
					</table>
					</td>
				</tr>
			</table>
		</td>
	</tr>
	<tr>
		<td height='1'></td>
	</tr>
	<tr>
		<td>
			<table>
				<tr>
					<td valign='middle' width='300px'>
						<center>
						<div id='locationdiv' style='width:240px'>
							<table class='tbllane0' id='tracktbl'>
								<tr>
									<td>  LANE </td> 
									<td align='center' height='40' id='lanenow'>0</td>
								</tr>
								<tr>
									<td colspan=2 class='lane' id='positionnow'>
										00
									</td>
								</tr>
								<tr>
									<td colspan=2  height='40' align='center' id='timenow'>
										<?=date('dS M,y')?>&nbsp;&nbsp;&nbsp; <?=date('H:m:s')?>
									</td>
								</tr>
							</table>
							</br/>
							<br/>
							<table border=1 id='trackoldtbl' class='tbllane0'>
								<tr align='center' >
									<td>Last</td> 
									<td> Lane</td>
									<td> Position</td>
									<td> Time</td>
								</tr>
								<tr align='center' >
									<td>Value</td> 
									<td height='40' id='lanelast'>0</td>
									<td id='positionlast'>00</td>
									<td width='80px' align='center' id='timelast'>
										<?=date('H:m:s')?>
									</td>
								</tr>
							</table>
						</div>
						</center>
						
					</td>
					<td width=1px bgcolor="#4F5155"></td>
					<td valign='top' >
						<center>
						<div id='tagsdiv' style='width:240px'>
							<table border=1 id='tabletags'>
							<tr>
								<th>SN</th><th>Tags</th>
							</tr>
						</table>
						</div>
						</center>
						

					</td>
				</tr>
			</table>
			
			
			
			
			
		</td>
	</tr>
</table>
</body>
</html>