<script type="text/javascript">
		var lastx=0; 
		var lasty=0;
		
		function trackxml()
		{
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
			xmlDoc.load("http://localhost/cgi-bin/getxml.py");
			xmlObj=xmlDoc.documentElement;
			
			var total 	= xmlObj.getElementsByTagName("total")[0].childNodes[0].nodeValue;
			var tags 	= xmlObj.getElementsByTagName("tags");
			
			container = document.getElementById('mapid');
			
			document.getElementById('mapid').innerHTML = "";
			var totalCount =0;
			var posX = 0;
			var posY = 0;
			for (i=0;i<tags.length;i++)
			{
				tagvalue = tags[i].childNodes[1].childNodes[0].nodeValue;
				taglast = tagvalue.substr(22,25);
				container.innerHTML += "taglast ="+taglast;
				laneindex = taglast.substr(0,2);
				container.innerHTML += "lane ="+laneindex;
				
				tagint = parseFloat(taglast.substr(2).toString());
				container.innerHTML += "tagint ="+taglast.substr(2);
				
				type = tags[i].childNodes[3].childNodes[0].nodeValue;
				
				antenna = tags[i].childNodes[9].childNodes[0].nodeValue;
				repeat = tags[i].childNodes[11].childNodes[0].nodeValue;
				repeat = parseInt(repeat);
				if(laneindex=="A") posY += 1;
				if(laneindex=="B") posY += 2;
				if(laneindex=="C") posY += 3
				totalCount += repeat;
				posX += tagint * repeat;
				
				container.innerHTML += "TAG = "+ tagint+ ";  ";
				container.innerHTML += "Type = "+ type+ ";  ";
				container.innerHTML += "Ant = "+ antenna+ ";  ";
				container.innerHTML += "Rep = "+ repeat+ ";  ";
				
				container.innerHTML += "<br/> ";
				
			  }
			  vehicleX = Math.round(posX/totalCount);
			  vehicleY = Math.round(posY/totalCount)*2;
			  container.innerHTML += "<br/> ";
			  container.innerHTML += "Location = "+ vehicleX+ ",  "+vehicleY;
			
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
</script>

<body onload='trackxml()'>
	<div id='mapid' ></div>
</body>
