function locTag(realtag, tagstatus)
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
	mes.innerHTML = "<center>Please enter lane and position.</center>".fontsize(4);
	div.appendChild(mes);

// Location //
	var lane = document.createElement('b');
	lane.innerHTML = '<br />Lane > '.fontsize(5);
	div.appendChild(lane);

	var lane_box = document.createElement('input');
	lane_box.id = 'lane_box';
	lane_box.type = 'text';
	lane_box.maxLength = '1';
	lane_box.style.width = '35px';
	lane_box.style.fontSize = '200%';
	lane_box.style.color = 'black';
	lane_box.style.textAlign = 'center';
	div.appendChild(lane_box);
	var dash = document.createElement('b');
	dash.innerHTML = ' - '.fontsize(4);
	div.appendChild(dash);
	var position_box = document.createElement('input');
	position_box.id = 'position_box';
	position_box.type = 'text';
	position_box.maxLength = '2';
	position_box.style.width = '55px';
	position_box.style.fontSize = '200%';
	position_box.style.color = 'black';
	position_box.style.textAlign = 'center';
	div.appendChild(position_box);

	var position = document.createElement('b');
	position.innerHTML = ' < Position'.fontsize(5);
	div.appendChild(position);

// Lane Pad //
	var lanepad = document.createElement('div');
	lanepad.id = 'lanepad';
	lanepad.style.position = 'absolute';
	lanepad.style.top = '40px';
	lanepad.style.left = '10px';
	lanepad.style.visibility = 'hidden';
	div.appendChild(lanepad);

	var four_lane = document.createElement('a');
	four_lane.id = 'lanenumbtn';
	four_lane.style.top = '100px';
	four_lane.style.left = '50px';
	four_lane.innerHTML = "<table style='width:100%;'><tr><td style='cursor:pointer;'>"+"4".fontsize(6).bold()+"</td></tr></table>";
	four_lane.onclick = function()
	{
		top.document.getElementById('lane_box').value = '4';
		top.document.getElementById('tolane').value = '4';
	}
	lanepad.appendChild(four_lane);

	var three_lane = document.createElement('a');
	three_lane.id = 'lanenumbtn';
	three_lane.style.top = '170px';
	three_lane.style.left = '50px';
	three_lane.innerHTML = "<table style='width:100%;'><tr><td style='cursor:pointer;'>"+"3".fontsize(6).bold()+"</td></tr></table>";
	three_lane.onclick = function()
	{
		top.document.getElementById('lane_box').value = '3';
		top.document.getElementById('tolane').value = '3';
	}
	lanepad.appendChild(three_lane);

	var two_lane = document.createElement('a');
	two_lane.id = 'lanenumbtn';
	two_lane.style.top = '240px';
	two_lane.style.left = '50px';
	two_lane.innerHTML = "<table style='width:100%;'><tr><td style='cursor:pointer;'>"+"2".fontsize(6).bold()+"</td></tr></table>";
	two_lane.onclick = function()
	{
		top.document.getElementById('lane_box').value = '2';
		top.document.getElementById('tolane').value = '2';
	}
	lanepad.appendChild(two_lane);

	var one_lane = document.createElement('a');
	one_lane.id = 'lanenumbtn';
	one_lane.style.top = '310px';
	one_lane.style.left = '50px';
	one_lane.innerHTML = "<table style='width:100%;'><tr><td style='cursor:pointer;'>"+"1".fontsize(6).bold()+"</td></tr></table>";
	one_lane.onclick = function()
	{
		top.document.getElementById('lane_box').value = '1';
		top.document.getElementById('tolane').value = '1';
	}
	lanepad.appendChild(one_lane);

//	var h = document.createElement('a');
//	h.id = 'lanebtn';
//	h.style.top = '100px';
//	h.style.left = '50px';
//	h.innerHTML = "<table style='width:100%;'><tr><td style='cursor:pointer;'>"+"H".fontsize(4).bold()+"</td></tr></table>";
//	h.onclick = function()
//	{
//		top.document.getElementById('lane_box').value = 'H';
//	}
//	lanepad.appendChild(h);

//	var g = document.createElement('a');
//	g.id = 'lanebtn';
//	g.style.top = '140px';
//	g.style.left = '50px';
//	g.innerHTML = "<table style='width:100%;'><tr><td style='cursor:pointer;'>"+"G".fontsize(4).bold()+"</td></tr></table>";
//	g.onclick = function()
//	{
//		top.document.getElementById('lane_box').value = 'G';
//	}
//	lanepad.appendChild(g);

//	var f = document.createElement('a');
//	f.id = 'lanebtn';
//	f.style.top = '170px';
//	f.style.left = '50px';
//	f.innerHTML = "<table style='width:100%;'><tr><td style='cursor:pointer;'>"+"F".fontsize(4).bold()+"</td></tr></table>";
//	f.onclick = function()
//	{
//		top.document.getElementById('lane_box').value = 'F';
//	}
//	lanepad.appendChild(f);

//	var e = document.createElement('a');
//	e.id = 'lanebtn';
//	e.style.top = '210px';
//	e.style.left = '50px';
//	e.innerHTML = "<table style='width:100%;'><tr><td style='cursor:pointer;'>"+"E".fontsize(4).bold()+"</td></tr></table>";
//	e.onclick = function()
//	{
//		top.document.getElementById('lane_box').value = 'E';
//	}
//	lanepad.appendChild(e);

//	var d = document.createElement('a');
//	d.id = 'lanebtn';
//	d.style.top = '240px';
//	d.style.left = '50px';
//	d.innerHTML = "<table style='width:100%;'><tr><td style='cursor:pointer;'>"+"D".fontsize(4).bold()+"</td></tr></table>";
//	d.onclick = function()
//	{
//		top.document.getElementById('lane_box').value = 'D';
//	}
//	lanepad.appendChild(d);

//	var c = document.createElement('a');
//	c.id = 'lanebtn';
//	c.style.top = '280px';
//	c.style.left = '50px';
//	c.innerHTML = "<table style='width:100%;'><tr><td style='cursor:pointer;'>"+"C".fontsize(4).bold()+"</td></tr></table>";
//	c.onclick = function()
//	{
//		top.document.getElementById('lane_box').value = 'C';
//	}
//	lanepad.appendChild(c);

//	var b = document.createElement('a');
//	b.id = 'lanebtn';
//	b.style.top = '310px';
//	b.style.left = '50px';
//	b.innerHTML = "<table style='width:100%;'><tr><td style='cursor:pointer;'>"+"B".fontsize(4).bold()+"</td></tr></table>";
//	b.onclick = function()
//	{
//		top.document.getElementById('lane_box').value = 'B';
//	}
//	lanepad.appendChild(b);

//	var a = document.createElement('a');
//	a.id = 'lanebtn';
//	a.style.top = '350px';
//	a.style.left = '50px';
//	a.innerHTML = "<table style='width:100%;'><tr><td style='cursor:pointer;'>"+"A".fontsize(4).bold()+"</td></tr></table>";
//	a.onclick = function()
//	{
//		top.document.getElementById('lane_box').value = 'A';
//	}
//	lanepad.appendChild(a);

	function positionInput() {
		numpad_pos.style.visibility = 'visible';
		lanepad.style.visibility = 'hidden';
		div.style.width = '300px';
	}
	function laneInput() {
		lanepad.style.visibility = 'visible';
		numpad_pos.style.visibility = 'hidden';
		div.style.width = '300px';
	}

	position_box.onfocus = function() { positionInput(); };
	lane_box.onfocus = function() { laneInput(); };

// Num Pad // Position
	var numpad_pos = document.createElement('div');
	numpad_pos.id = 'numpad';
	numpad_pos.style.position = 'absolute';
	numpad_pos.style.top = '40px';
	numpad_pos.style.left = '-140px';
	numpad_pos.style.visibility = 'hidden';
	div.appendChild(numpad_pos);

	var trig = 0;

	var one_pos = document.createElement('a');
	one_pos.id = 'numbtn';
	one_pos.style.top = '100px';
	one_pos.style.left = '200px';
	one_pos.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"1".fontsize(6).bold()+"</td></tr></table>";
	one_pos.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('position_box').value = '';
			top.document.getElementById('topos').value = '';
			trig = 1;
		}
		if (top.document.getElementById('position_box').value.length < 2 && trig == 1){
			top.document.getElementById('position_box').value += '1';
			top.document.getElementById('topos').value = top.document.getElementById('position_box').value;
		}
	}
	numpad_pos.appendChild(one_pos);

	var two_pos = document.createElement('a');
	two_pos.id = 'numbtn';
	two_pos.style.top = '100px';
	two_pos.style.left = '280px';
	two_pos.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"2".fontsize(6).bold()+"</td></tr></table>";
	two_pos.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('position_box').value = '';
			top.document.getElementById('topos').value = '';
			trig = 1;
		}
		if (top.document.getElementById('position_box').value.length < 2 && trig == 1){
			top.document.getElementById('position_box').value += '2';
			top.document.getElementById('topos').value = top.document.getElementById('position_box').value;
		}
	}
	numpad_pos.appendChild(two_pos);

	var three_pos = document.createElement('a');
	three_pos.id = 'numbtn';
	three_pos.style.top = '100px';
	three_pos.style.left = '360px';
	three_pos.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"3".fontsize(6).bold()+"</td></tr></table>";
	three_pos.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('position_box').value = '';
			top.document.getElementById('topos').value = '';
			trig = 1;
		}
		if (top.document.getElementById('position_box').value.length < 2 && trig == 1){
			top.document.getElementById('position_box').value += '3';
			top.document.getElementById('topos').value = top.document.getElementById('position_box').value;
		}
	}
	numpad_pos.appendChild(three_pos);

	var four_pos = document.createElement('a');
	four_pos.id = 'numbtn';
	four_pos.style.top = '170px';
	four_pos.style.left = '200px';
	four_pos.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"4".fontsize(6).bold()+"</td></tr></table>";
	four_pos.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('position_box').value = '';
			top.document.getElementById('topos').value = '';
			trig = 1;
		}
		if (top.document.getElementById('position_box').value.length < 2 && trig == 1){
			top.document.getElementById('position_box').value += '4';
			top.document.getElementById('topos').value = top.document.getElementById('position_box').value;
		}
	}
	numpad_pos.appendChild(four_pos);

	var five_pos = document.createElement('a');
	five_pos.id = 'numbtn';
	five_pos.style.top = '170px';
	five_pos.style.left = '280px';
	five_pos.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"5".fontsize(6).bold()+"</td></tr></table>";
	five_pos.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('position_box').value = '';
			top.document.getElementById('topos').value = '';
			trig = 1;
		}
		if (top.document.getElementById('position_box').value.length < 2 && trig == 1){
			top.document.getElementById('position_box').value += '5';
			top.document.getElementById('topos').value = top.document.getElementById('position_box').value;
		}
	}
	numpad_pos.appendChild(five_pos);

	var six_pos = document.createElement('a');
	six_pos.id = 'numbtn';
	six_pos.style.top = '170px';
	six_pos.style.left = '360px';
	six_pos.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"6".fontsize(6).bold()+"</td></tr></table>";
	six_pos.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('position_box').value = '';
			top.document.getElementById('topos').value = '';
			trig = 1;
		}
		if (top.document.getElementById('position_box').value.length < 2 && trig == 1){
			top.document.getElementById('position_box').value += '6';
			top.document.getElementById('topos').value = top.document.getElementById('position_box').value;
		}
	}
	numpad_pos.appendChild(six_pos);

	var seven_pos = document.createElement('a');
	seven_pos.id = 'numbtn';
	seven_pos.style.top = '240px';
	seven_pos.style.left = '200px';
	seven_pos.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"7".fontsize(6).bold()+"</td></tr></table>";
	seven_pos.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('position_box').value = '';
			top.document.getElementById('topos').value = '';
			trig = 1;
		}
		if (top.document.getElementById('position_box').value.length < 2 && trig == 1){
			top.document.getElementById('position_box').value += '7';
			top.document.getElementById('topos').value = top.document.getElementById('position_box').value;
		}
	}
	numpad_pos.appendChild(seven_pos);

	var eight_pos = document.createElement('a');
	eight_pos.id = 'numbtn';
	eight_pos.style.top = '240px';
	eight_pos.style.left = '280px';
	eight_pos.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"8".fontsize(6).bold()+"</td></tr></table>";
	eight_pos.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('position_box').value = '';
			top.document.getElementById('topos').value = '';
			trig = 1;
		}
		if (top.document.getElementById('position_box').value.length < 2 && trig == 1){
			top.document.getElementById('position_box').value += '8';
			top.document.getElementById('topos').value = top.document.getElementById('position_box').value;
		}
	}
	numpad_pos.appendChild(eight_pos);

	var nine_pos = document.createElement('a');
	nine_pos.id = 'numbtn';
	nine_pos.style.top = '240px';
	nine_pos.style.left = '360px';
	nine_pos.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"9".fontsize(6).bold()+"</td></tr></table>";
	nine_pos.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('position_box').value = '';
			top.document.getElementById('topos').value = '';
			trig = 1;
		}
		if (top.document.getElementById('position_box').value.length < 2 && trig == 1){
			top.document.getElementById('position_box').value += '9';
			top.document.getElementById('topos').value = top.document.getElementById('position_box').value;
		}
	}
	numpad_pos.appendChild(nine_pos);

	var clr_pos = document.createElement('a');
	clr_pos.id = 'numbtn';
	clr_pos.style.top = '310px';
	clr_pos.style.left = '200px';
	clr_pos.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"clr".fontsize(5).bold()+"</td></tr></table>";
	clr_pos.onclick = function()
	{
		top.document.getElementById('position_box').value = '';
		top.document.getElementById('topos').value = '';
	}
	numpad_pos.appendChild(clr_pos);

	var zero_pos = document.createElement('a');
	zero_pos.id = 'numbtn';
	zero_pos.style.top = '310px';
	zero_pos.style.left = '280px';
	zero_pos.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"0".fontsize(6).bold()+"</td></tr></table>";
	zero_pos.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('position_box').value = '';
			top.document.getElementById('topos').value = '';
			trig = 1;
		}
		if (top.document.getElementById('position_box').value != '' && top.document.getElementById('position_box').value.length < 2 && trig == 1){
			top.document.getElementById('position_box').value += '0';
			top.document.getElementById('topos').value = top.document.getElementById('position_box').value;
		}
	}
	numpad_pos.appendChild(zero_pos);

	var bs_pos = document.createElement('a');
	bs_pos.id = 'numbtn';
	bs_pos.style.top = '310px';
	bs_pos.style.left = '360px';
	bs_pos.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"bs".fontsize(5).bold()+"</td></tr></table>";
	bs_pos.onclick = function()
	{
		var len = top.document.getElementById('position_box').value.length;
		top.document.getElementById('position_box').value = top.document.getElementById('position_box').value.substr(0,len-1);
		top.document.getElementById('topos').value = top.document.getElementById('position_box').value;
	}
	numpad_pos.appendChild(bs_pos);

////////

	var ok_id = document.createElement('a');
	ok_id.id = 'confirm';
	ok_id.style.left = '10px';
	ok_id.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"OK".fontsize(5).bold()+"</td></tr></table>";
	ok_id.onclick = function()
	{
		var laneval = top.document.getElementById('lane_box').value;
		var positionval = top.document.getElementById('position_box').value;
		var pass = 0;
		var messi = '';
		if (laneval != '' && positionval != ''){
			if (parseInt(positionval) <= 13){ // Position are set here!
				function submitTag(){
					document.getElementById("alane_loc").value = laneval;
					document.getElementById("aposition_loc").value = positionval;
//					document.getElementById("aweight").value = weightval;
					document.getElementById("atag2write_loc").value = document.getElementById('tag2write').value;
					var tag2write = document.getElementById('tag2write').value;
					document.getElementById("frm9").submit();
					top.document.body.removeChild(top.document.getElementById('layer'));
					top.document.body.removeChild(top.document.getElementById('box'));
				}
				submitTag();
			} else if (parseInt(positionval) > 13){
				alert("The submitted position is not in range (1-13).");
			}
		}
		else {
			if (laneval == ''){ messi += '- Please enter lane.\n'; }
			if (positionval == ''){ messi += '- Please enter position.\n'; }
			alert(messi);
		}
	}
	div.appendChild(ok_id);

	var cancel_id = document.createElement('a');
	cancel_id.id = 'confirm';
	cancel_id.style.right = '10px';
	cancel_id.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"Cancel".fontsize(4).bold()+"</td></tr></table>";
	cancel_id.onclick = function()
	{
		top.document.body.removeChild(top.document.getElementById('layer'));
		top.document.body.removeChild(top.document.getElementById('box'));
	}
	div.appendChild(cancel_id);

	var container = document.createElement('div');
	container.style.position = "absolute";
	container.style.bottom = "30px";
	container.style.left = "105px";
	div.appendChild(container);

	var fromrfid = document.createElement('b');
	if (tagstatus == 'unknown') {realtag = "New";}
	fromrfid.innerHTML = realtag+" >>> ";
	container.appendChild(fromrfid);

	var tolane = document.createElement('input');
	tolane.id = 'tolane';
	tolane.type = 'text';
	tolane.maxLength = '1';
	tolane.style.width = '20px';
	tolane.style.fontWeight = 'bold';
	tolane.style.fontSize = '110%';
	tolane.style.color = 'black';
	tolane.style.textAlign = 'center';
	tolane.readOnly = true;
	tolane.style.backgroundColor = 'lightgray';
	container.appendChild(tolane);

	var dash = document.createElement('b');
	dash.innerHTML = ' - ';
	container.appendChild(dash);

	var topos = document.createElement('input');
	topos.id = 'topos';
	topos.type = 'text';
	topos.maxLength = '2';
	topos.style.width = '30px';
	topos.style.fontWeight = 'bold';
	topos.style.fontSize = '110%';
	topos.style.color = 'black';
	topos.style.textAlign = 'center';
	topos.readOnly = true;
	topos.style.backgroundColor = 'lightgray';
	container.appendChild(topos);
}
