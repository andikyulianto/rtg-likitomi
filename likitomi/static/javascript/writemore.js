function writeMore(paper_roll_detail_id, rfid_roll_id, paper_code, psize, initial_weight, current_weight, lane, position)
{
	var agent = navigator.userAgent;
	var patt1 = /Chrome/;
	var patt2 = /Firefox/;
	var chrome = agent.match(patt1);
	var firefox = agent.match(patt2);

	var height = top.document.documentElement.clientHeight + top.document.documentElement.scrollTop;
	var width = top.document.documentElement.clientWidth + top.document.documentElement.scrollLeft;

	var layer = document.createElement('div');
	layer.id = 'layer';
	layer.style.zIndex = '2';
	layer.style.position = 'absolute';
	layer.style.top = '0px';
	layer.style.left = '0px';
	if (chrome == 'Chrome'){
		layer.style.height = 600 +'px';
		layer.style.width = 800 +'px';
	} else if (firefox == 'Firefox'){
		layer.style.height = 600-5 +'px';
		layer.style.width = 800 +'px';
	}
	layer.style.backgroundColor = 'black';
	layer.style.opacity = '.6';
	layer.style.filter += ("progid:DXImageTransform.Microsoft.Alpha(opacity=60)");
	top.document.body.appendChild(layer);

	var div = document.createElement('div');
	div.id = 'box';
	div.style.zIndex = '3';
	div.style.position = (navigator.userAgent.indexOf('MSIE 6') > -1) ? 'absolute' : 'fixed';
	div.style.top = '60px'; 
	div.style.left = '200px'; 
	div.style.height = '450px';
	div.style.width = '300px';
	div.style.backgroundColor = 'lightgray';
	div.style.opacity = '1';
	div.style.border = '2px solid silver';
	div.style.padding = '20px';
	top.document.body.appendChild(div);

	var mes = document.createElement('b');
	mes.innerHTML = "<center>Please check the information.</center>".fontsize(4);
	div.appendChild(mes);

// Roll ID //
	var id = document.createElement('b');
	id.innerHTML = '<br />Roll ID: '.fontsize(4)+paper_roll_detail_id.toString().fontsize(4);
	div.appendChild(id);

// RFID //
	var id = document.createElement('b');
	id.innerHTML = '<br /><br />RFID: '.fontsize(4);
	div.appendChild(id);

	var rfid_box = document.createElement('input');
	rfid_box.id = 'rfid_box';
	rfid_box.type = 'text';
	rfid_box.maxLength = '4';
	rfid_box.style.width = '90px';
	rfid_box.style.fontSize = '200%';
	rfid_box.style.color = 'black';
	rfid_box.style.textAlign = 'center';
	rfid_box.value = paper_roll_detail_id;
	rfid_box.readOnly = true;
	rfid_box.style.backgroundColor = 'lightgray';
	div.appendChild(rfid_box);

// Paper Code //
	var pcode = document.createElement('b');
	pcode.innerHTML = '<br /><br />Paper Code: '.fontsize(4)+paper_code.toString().fontsize(4);
	div.appendChild(pcode);

// Size //
	var size = document.createElement('b');
	size.innerHTML = '<br /><br />Size: '.fontsize(4)+psize.toString().fontsize(4);
	div.appendChild(size);

// Weight //
	var init_weight = document.createElement('b');
	init_weight.innerHTML = '<br /><br />Initial Weight: '.fontsize(4)+initial_weight.toString().fontsize(4);
	div.appendChild(init_weight);

	var curr_weight = document.createElement('b');
	curr_weight.innerHTML = '<br /><br />Current Weight: '.fontsize(4)+current_weight.toString().fontsize(4);
	div.appendChild(curr_weight);

// Location //
	if (position == 'None'){ position = '';}
	var location = document.createElement('b');
	location.innerHTML = '<br /><br />Location: '.fontsize(4)+lane.toString().fontsize(4)+'-'.fontsize(4)+position.toString().fontsize(4);
	div.appendChild(location);

	var ok_id = document.createElement('a');
	ok_id.id = 'confirm';
	ok_id.style.left = '70px';
	ok_id.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"OK".fontsize(5).bold()+"</td></tr></table>";
	ok_id.onclick = function()
	{
		var rfidval = top.document.getElementById('rfid_box').value;
		submitTag();
		function submitTag(){
			document.getElementById("arfid_more").value = rfidval;
			if (rfidval.toString().length == 1){ strrfidval = '000'+rfidval.toString()}
			if (rfidval.toString().length == 2){ strrfidval = '00'+rfidval.toString()}
			if (rfidval.toString().length == 3){ strrfidval = '0'+rfidval.toString()}
			if (rfidval.toString().length == 4){ strrfidval = rfidval.toString()}
			document.getElementById("atag2write_more").value = document.getElementById('tag2write').value;
			var tag2write = document.getElementById('tag2write').value;
			if (tag2write.search("00000000000000") > -1 && tag2write.substring(1,5) != strrfidval) {
				var r = confirm("Roll ID tag '"+tag2write.substring(1,5)+"' will be changed to '"+strrfidval+"'.");
				if (r == true){
					document.getElementById("frm8").submit();
					top.document.body.removeChild(top.document.getElementById('layer'));
					top.document.body.removeChild(top.document.getElementById('box'));
				}
				else {
					pass++;
				}
			}
			else if (tag2write == ''){
				alert("Writing on location tag is not allowed.");
			}
			else {
				document.getElementById("frm8").submit();
				top.document.body.removeChild(top.document.getElementById('layer'));
				top.document.body.removeChild(top.document.getElementById('box'));
			}
		}
	}
	div.appendChild(ok_id);

	var cancel_id = document.createElement('a');
	cancel_id.id = 'confirm';
	cancel_id.style.right = '80px';
	cancel_id.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"Cancel".fontsize(4).bold()+"</td></tr></table>";
	cancel_id.onclick = function()
	{
		top.document.body.removeChild(top.document.getElementById('layer'));
		top.document.body.removeChild(top.document.getElementById('box'));
	}
	div.appendChild(cancel_id);
}
