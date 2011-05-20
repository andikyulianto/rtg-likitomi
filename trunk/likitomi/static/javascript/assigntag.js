function assignTag()
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
	div.style.top = '85px'; 
	div.style.left = '200px'; 
	div.style.height = '400px';
	div.style.width = '300px';
	div.style.backgroundColor = 'lightgray';
	div.style.opacity = '1';
	div.style.border = '2px solid silver';
	div.style.padding = '20px';
	top.document.body.appendChild(div);

	var mes = document.createElement('b');
	mes.innerHTML = "<center>Please enter new tag information.</center>".fontsize(4);
	div.appendChild(mes);

// ID //
	var id = document.createElement('b');
	id.innerHTML = '<br />Tag ID:'.fontsize(4);
	div.appendChild(id);

	var id_box = document.createElement('input');
	id_box.id = 'id_box';
	id_box.type = 'text';
//	id_box.size = '2';
	id_box.maxLength = '4';
	id_box.style.width = '90px';
	id_box.style.fontSize = '200%';
	id_box.style.color = 'black';
	id_box.style.textAlign = 'center';
	div.appendChild(id_box);

// Paper Code //
	var pcode = document.createElement('b');
	pcode.innerHTML = '<br /><br />Paper Code:'.fontsize(4);
	div.appendChild(pcode);

	var pcode_box = document.createElement('div');
	pcode_box.style.backgroundColor = 'lightgray';
	pcode_box.style.position = 'absolute';
	pcode_box.style.height = '30px';
	pcode_box.style.top = '130px';
	pcode_box.style.left = '120px';
	div.appendChild(pcode_box);
	var pcode_form = document.createElement('form');
	pcode_box.appendChild(pcode_form);
	var pcode_select = document.createElement('select');
	pcode_select.id = 'pcode_select';
	pcode_select.style.height = '30px';
	pcode_form.appendChild(pcode_select);
	var i = 0;
	var spcodelist = document.getElementById('spcodelist').value;
	spcodelist = spcodelist.replace(/[\[\]\'u ]/g,'');
	var spcodearr = new Array();
	spcodearr = spcodelist.split(',');
	for (i=0;i<=spcodearr.length-1;i++){
		pcode_select.options[i] = new Option(spcodearr[i],spcodearr[i]);
	}

// Size //
	var size = document.createElement('b');
	size.innerHTML = '<br /><br />Size:'.fontsize(4);
	div.appendChild(size);

	var size_box = document.createElement('div');
	size_box.style.backgroundColor = 'lightgray';
	size_box.style.position = 'absolute';
	size_box.style.height = '30px';
	size_box.style.top = '170px';
	size_box.style.left = '60px';
	div.appendChild(size_box);
	var size_form = document.createElement('form');
	size_box.appendChild(size_form);
	var size_select = document.createElement('select');
	size_select.id = 'size_select';
	size_select.style.height = '30px';
	size_form.appendChild(size_select);
	var i = 0;
	var swidthlist = document.getElementById('swidthlist').value;
	swidthlist = swidthlist.replace(/[\[\]\L ]/g,'');
	var swidtharr = new Array();
	swidtharr = swidthlist.split(',');
	for (i=0;i<=swidtharr.length-1;i++){
		size_select.options[i] = new Option(swidtharr[i],swidtharr[i]);
	}

// Weight //
	var weight = document.createElement('b');
	weight.innerHTML = '<br /><br />Weight:'.fontsize(4);
	div.appendChild(weight);

	var weight_box = document.createElement('input');
	weight_box.id = 'weight_box';
	weight_box.type = 'text';
//	weight_box.size = '2';
	weight_box.maxLength = '4';
	weight_box.style.width = '90px';
	weight_box.style.fontSize = '150%';
	weight_box.style.color = 'black';
	weight_box.style.textAlign = 'center';
	div.appendChild(weight_box);

// Location //
	var location = document.createElement('b');
	location.innerHTML = '<br /><br />Location:'.fontsize(4);
	div.appendChild(location);

	var lane_box = document.createElement('input');
	lane_box.id = 'lane_box';
	lane_box.type = 'text';
//	lane_box.size = '1';
	lane_box.maxLength = '1';
	lane_box.style.width = '30px';
	lane_box.style.fontSize = '150%';
	lane_box.style.color = 'black';
	lane_box.style.textAlign = 'center';
	div.appendChild(lane_box);
	var dash = document.createElement('b');
	dash.innerHTML = ' - '.fontsize(4);
	div.appendChild(dash);
	var position_box = document.createElement('input');
	position_box.id = 'position_box';
	position_box.type = 'text';
//	position_box.size = '1';
	position_box.maxLength = '2';
	position_box.style.width = '50px';
	position_box.style.fontSize = '150%';
	position_box.style.color = 'black';
	position_box.style.textAlign = 'center';
	div.appendChild(position_box);

// Lane Pad //
	var lanepad = document.createElement('div');
	lanepad.id = 'lanepad';
	lanepad.style.position = 'absolute';
	lanepad.style.top = '-40px';
	lanepad.style.left = '180px';
	lanepad.style.visibility = 'hidden';
	div.appendChild(lanepad);

	var h = document.createElement('a');
	h.id = 'lanebtn';
	h.style.top = '100px';
	h.style.left = '50px';
	h.innerHTML = "<table style='width:100%;'><tr><td style='cursor:pointer;'>"+"H".fontsize(4).bold()+"</td></tr></table>";
	h.onclick = function()
	{
		top.document.getElementById('lane_box').value = 'H';
	}
	lanepad.appendChild(h);

	var g = document.createElement('a');
	g.id = 'lanebtn';
	g.style.top = '140px';
	g.style.left = '50px';
	g.innerHTML = "<table style='width:100%;'><tr><td style='cursor:pointer;'>"+"G".fontsize(4).bold()+"</td></tr></table>";
	g.onclick = function()
	{
		top.document.getElementById('lane_box').value = 'G';
	}
	lanepad.appendChild(g);

	var f = document.createElement('a');
	f.id = 'lanebtn';
	f.style.top = '170px';
	f.style.left = '50px';
	f.innerHTML = "<table style='width:100%;'><tr><td style='cursor:pointer;'>"+"F".fontsize(4).bold()+"</td></tr></table>";
	f.onclick = function()
	{
		top.document.getElementById('lane_box').value = 'F';
	}
	lanepad.appendChild(f);

	var e = document.createElement('a');
	e.id = 'lanebtn';
	e.style.top = '210px';
	e.style.left = '50px';
	e.innerHTML = "<table style='width:100%;'><tr><td style='cursor:pointer;'>"+"E".fontsize(4).bold()+"</td></tr></table>";
	e.onclick = function()
	{
		top.document.getElementById('lane_box').value = 'E';
	}
	lanepad.appendChild(e);

	var d = document.createElement('a');
	d.id = 'lanebtn';
	d.style.top = '240px';
	d.style.left = '50px';
	d.innerHTML = "<table style='width:100%;'><tr><td style='cursor:pointer;'>"+"D".fontsize(4).bold()+"</td></tr></table>";
	d.onclick = function()
	{
		top.document.getElementById('lane_box').value = 'D';
	}
	lanepad.appendChild(d);

	var c = document.createElement('a');
	c.id = 'lanebtn';
	c.style.top = '280px';
	c.style.left = '50px';
	c.innerHTML = "<table style='width:100%;'><tr><td style='cursor:pointer;'>"+"C".fontsize(4).bold()+"</td></tr></table>";
	c.onclick = function()
	{
		top.document.getElementById('lane_box').value = 'C';
	}
	lanepad.appendChild(c);

	var b = document.createElement('a');
	b.id = 'lanebtn';
	b.style.top = '310px';
	b.style.left = '50px';
	b.innerHTML = "<table style='width:100%;'><tr><td style='cursor:pointer;'>"+"B".fontsize(4).bold()+"</td></tr></table>";
	b.onclick = function()
	{
		top.document.getElementById('lane_box').value = 'B';
	}
	lanepad.appendChild(b);

	var a = document.createElement('a');
	a.id = 'lanebtn';
	a.style.top = '350px';
	a.style.left = '50px';
	a.innerHTML = "<table style='width:100%;'><tr><td style='cursor:pointer;'>"+"A".fontsize(4).bold()+"</td></tr></table>";
	a.onclick = function()
	{
		top.document.getElementById('lane_box').value = 'A';
	}
	lanepad.appendChild(a);

	var current_input;

	function idInput() {
//		console.log(this);
//		current_input = this;
		numpad_id.style.visibility = 'visible';
		numpad_weight.style.visibility = 'hidden';
		numpad_pos.style.visibility = 'hidden';
		lanepad.style.visibility = 'hidden';
		div.style.width = '420px';
	}
	function weightInput() {
		numpad_id.style.visibility = 'hidden';
		numpad_weight.style.visibility = 'visible';
		numpad_pos.style.visibility = 'hidden';
		lanepad.style.visibility = 'hidden';
		div.style.width = '420px';
	}
	function positionInput() {
		numpad_id.style.visibility = 'hidden';
		numpad_weight.style.visibility = 'hidden';
		numpad_pos.style.visibility = 'visible';
		lanepad.style.visibility = 'hidden';
		div.style.width = '420px';
	}
	function laneInput() {
		lanepad.style.visibility = 'visible';
		numpad_id.style.visibility = 'hidden';
		numpad_weight.style.visibility = 'hidden';
		numpad_pos.style.visibility = 'hidden';
		div.style.width = '300px';
	}
	function hidePads() {
		lanepad.style.visibility = 'hidden';
		numpad_id.style.visibility = 'hidden';
		numpad_weight.style.visibility = 'hidden';
		numpad_.style.visibility = 'hidden';
		div.style.width = '300px';
	}

	id_box.onfocus = function() { idInput(); };
	position_box.onfocus = function() { positionInput(); };
	weight_box.onfocus = function() { weightInput(); };
	lane_box.onfocus = function() { laneInput(); };
	pcode_select.onfocus = function() { hidePads(); };
	size_select.onfocus = function() { hidePads(); };

//	id_box.addEventListener("focus", idInput);
//	position_box.addEventListener("focus", positionInput);
//	weight_box.addEventListener("focus", weightInput);
//	lane_box.addEventListener("focus", laneInput);
//	pcode_select.addEventListener("focus", hidePads);
//	size_select.addEventListener("focus", hidePads);

// Num Pad // Tag ID
	var numpad_id = document.createElement('div');
	numpad_id.id = 'numpad';
	numpad_id.style.position = 'absolute';
	numpad_id.style.top = '-40px';
	numpad_id.style.left = '30px';
	numpad_id.style.visibility = 'hidden';
	div.appendChild(numpad_id);

	var trig = 0;

	var one_id = document.createElement('a');
	one_id.id = 'numbtn';
	one_id.style.top = '100px';
	one_id.style.left = '200px';
	one_id.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"1".fontsize(6).bold()+"</td></tr></table>";
	one_id.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('id_box').value = '';
			trig = 1;
		}
		if (top.document.getElementById('id_box').value.length < 4 && trig == 1)
		top.document.getElementById('id_box').value += '1';
	}
	numpad_id.appendChild(one_id);

	var two_id = document.createElement('a');
	two_id.id = 'numbtn';
	two_id.style.top = '100px';
	two_id.style.left = '280px';
	two_id.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"2".fontsize(6).bold()+"</td></tr></table>";
	two_id.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('id_box').value = '';
			trig = 1;
		}
		if (top.document.getElementById('id_box').value.length < 4 && trig == 1)
		top.document.getElementById('id_box').value += '2';
	}
	numpad_id.appendChild(two_id);

	var three_id = document.createElement('a');
	three_id.id = 'numbtn';
	three_id.style.top = '100px';
	three_id.style.left = '360px';
	three_id.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"3".fontsize(6).bold()+"</td></tr></table>";
	three_id.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('id_box').value = '';
			trig = 1;
		}
		if (top.document.getElementById('id_box').value.length < 4 && trig == 1)
		top.document.getElementById('id_box').value += '3';
	}
	numpad_id.appendChild(three_id);

	var four_id = document.createElement('a');
	four_id.id = 'numbtn';
	four_id.style.top = '170px';
	four_id.style.left = '200px';
	four_id.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"4".fontsize(6).bold()+"</td></tr></table>";
	four_id.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('id_box').value = '';
			trig = 1;
		}
		if (top.document.getElementById('id_box').value.length < 4 && trig == 1)
		top.document.getElementById('id_box').value += '4';
	}
	numpad_id.appendChild(four_id);

	var five_id = document.createElement('a');
	five_id.id = 'numbtn';
	five_id.style.top = '170px';
	five_id.style.left = '280px';
	five_id.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"5".fontsize(6).bold()+"</td></tr></table>";
	five_id.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('id_box').value = '';
			trig = 1;
		}
		if (top.document.getElementById('id_box').value.length < 4 && trig == 1)
		top.document.getElementById('id_box').value += '5';
	}
	numpad_id.appendChild(five_id);

	var six_id = document.createElement('a');
	six_id.id = 'numbtn';
	six_id.style.top = '170px';
	six_id.style.left = '360px';
	six_id.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"6".fontsize(6).bold()+"</td></tr></table>";
	six_id.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('id_box').value = '';
			trig = 1;
		}
		if (top.document.getElementById('id_box').value.length < 4 && trig == 1)
		top.document.getElementById('id_box').value += '6';
	}
	numpad_id.appendChild(six_id);

	var seven_id = document.createElement('a');
	seven_id.id = 'numbtn';
	seven_id.style.top = '240px';
	seven_id.style.left = '200px';
	seven_id.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"7".fontsize(6).bold()+"</td></tr></table>";
	seven_id.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('id_box').value = '';
			trig = 1;
		}
		if (top.document.getElementById('id_box').value.length < 4 && trig == 1)
		top.document.getElementById('id_box').value += '7';
	}
	numpad_id.appendChild(seven_id);

	var eight_id = document.createElement('a');
	eight_id.id = 'numbtn';
	eight_id.style.top = '240px';
	eight_id.style.left = '280px';
	eight_id.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"8".fontsize(6).bold()+"</td></tr></table>";
	eight_id.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('id_box').value = '';
			trig = 1;
		}
		if (top.document.getElementById('id_box').value.length < 4 && trig == 1)
		top.document.getElementById('id_box').value += '8';
	}
	numpad_id.appendChild(eight_id);

	var nine_id = document.createElement('a');
	nine_id.id = 'numbtn';
	nine_id.style.top = '240px';
	nine_id.style.left = '360px';
	nine_id.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"9".fontsize(6).bold()+"</td></tr></table>";
	nine_id.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('id_box').value = '';
			trig = 1;
		}
		if (top.document.getElementById('id_box').value.length < 4 && trig == 1)
		top.document.getElementById('id_box').value += '9';
	}
	numpad_id.appendChild(nine_id);

	var clr_id = document.createElement('a');
	clr_id.id = 'numbtn';
	clr_id.style.top = '310px';
	clr_id.style.left = '200px';
	clr_id.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"clr".fontsize(5).bold()+"</td></tr></table>";
	clr_id.onclick = function()
	{
		top.document.getElementById('id_box').value = '';
	}
	numpad_id.appendChild(clr_id);

	var zero_id = document.createElement('a');
	zero_id.id = 'numbtn';
	zero_id.style.top = '310px';
	zero_id.style.left = '280px';
	zero_id.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"0".fontsize(6).bold()+"</td></tr></table>";
	zero_id.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('id_box').value = '';
			trig = 1;
		}
		if (top.document.getElementById('id_box').value != '' && top.document.getElementById('id_box').value.length < 4 && trig == 1)
		top.document.getElementById('id_box').value += '0';
	}
	numpad_id.appendChild(zero_id);

	var bs_id = document.createElement('a');
	bs_id.id = 'numbtn';
	bs_id.style.top = '310px';
	bs_id.style.left = '360px';
	bs_id.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"bs".fontsize(5).bold()+"</td></tr></table>";
	bs_id.onclick = function()
	{
		var len = top.document.getElementById('id_box').value.length;
		top.document.getElementById('id_box').value = top.document.getElementById('id_box').value.substr(0,len-1);
	}
	numpad_id.appendChild(bs_id);

// Num Pad // Weight
	var numpad_weight = document.createElement('div');
	numpad_weight.id = 'numpad';
	numpad_weight.style.position = 'absolute';
	numpad_weight.style.top = '-40px';
	numpad_weight.style.left = '30px';
	numpad_weight.style.visibility = 'hidden';
	div.appendChild(numpad_weight);

	var trig = 0;

	var one_weight = document.createElement('a');
	one_weight.id = 'numbtn';
	one_weight.style.top = '100px';
	one_weight.style.left = '200px';
	one_weight.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"1".fontsize(6).bold()+"</td></tr></table>";
	one_weight.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('weight_box').value = '';
			trig = 1;
		}
		if (top.document.getElementById('weight_box').value.length < 4 && trig == 1)
		top.document.getElementById('weight_box').value += '1';
	}
	numpad_weight.appendChild(one_weight);

	var two_weight = document.createElement('a');
	two_weight.id = 'numbtn';
	two_weight.style.top = '100px';
	two_weight.style.left = '280px';
	two_weight.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"2".fontsize(6).bold()+"</td></tr></table>";
	two_weight.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('weight_box').value = '';
			trig = 1;
		}
		if (top.document.getElementById('weight_box').value.length < 4 && trig == 1)
		top.document.getElementById('weight_box').value += '2';
	}
	numpad_weight.appendChild(two_weight);

	var three_weight = document.createElement('a');
	three_weight.id = 'numbtn';
	three_weight.style.top = '100px';
	three_weight.style.left = '360px';
	three_weight.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"3".fontsize(6).bold()+"</td></tr></table>";
	three_weight.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('weight_box').value = '';
			trig = 1;
		}
		if (top.document.getElementById('weight_box').value.length < 4 && trig == 1)
		top.document.getElementById('weight_box').value += '3';
	}
	numpad_weight.appendChild(three_weight);

	var four_weight = document.createElement('a');
	four_weight.id = 'numbtn';
	four_weight.style.top = '170px';
	four_weight.style.left = '200px';
	four_weight.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"4".fontsize(6).bold()+"</td></tr></table>";
	four_weight.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('weight_box').value = '';
			trig = 1;
		}
		if (top.document.getElementById('weight_box').value.length < 4 && trig == 1)
		top.document.getElementById('weight_box').value += '4';
	}
	numpad_weight.appendChild(four_weight);

	var five_weight = document.createElement('a');
	five_weight.id = 'numbtn';
	five_weight.style.top = '170px';
	five_weight.style.left = '280px';
	five_weight.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"5".fontsize(6).bold()+"</td></tr></table>";
	five_weight.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('weight_box').value = '';
			trig = 1;
		}
		if (top.document.getElementById('weight_box').value.length < 4 && trig == 1)
		top.document.getElementById('weight_box').value += '5';
	}
	numpad_weight.appendChild(five_weight);

	var six_weight = document.createElement('a');
	six_weight.id = 'numbtn';
	six_weight.style.top = '170px';
	six_weight.style.left = '360px';
	six_weight.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"6".fontsize(6).bold()+"</td></tr></table>";
	six_weight.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('weight_box').value = '';
			trig = 1;
		}
		if (top.document.getElementById('weight_box').value.length < 4 && trig == 1)
		top.document.getElementById('weight_box').value += '6';
	}
	numpad_weight.appendChild(six_weight);

	var seven_weight = document.createElement('a');
	seven_weight.id = 'numbtn';
	seven_weight.style.top = '240px';
	seven_weight.style.left = '200px';
	seven_weight.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"7".fontsize(6).bold()+"</td></tr></table>";
	seven_weight.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('weight_box').value = '';
			trig = 1;
		}
		if (top.document.getElementById('weight_box').value.length < 4 && trig == 1)
		top.document.getElementById('weight_box').value += '7';
	}
	numpad_weight.appendChild(seven_weight);

	var eight_weight = document.createElement('a');
	eight_weight.id = 'numbtn';
	eight_weight.style.top = '240px';
	eight_weight.style.left = '280px';
	eight_weight.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"8".fontsize(6).bold()+"</td></tr></table>";
	eight_weight.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('weight_box').value = '';
			trig = 1;
		}
		if (top.document.getElementById('weight_box').value.length < 4 && trig == 1)
		top.document.getElementById('weight_box').value += '8';
	}
	numpad_weight.appendChild(eight_weight);

	var nine_weight = document.createElement('a');
	nine_weight.id = 'numbtn';
	nine_weight.style.top = '240px';
	nine_weight.style.left = '360px';
	nine_weight.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"9".fontsize(6).bold()+"</td></tr></table>";
	nine_weight.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('weight_box').value = '';
			trig = 1;
		}
		if (top.document.getElementById('weight_box').value.length < 4 && trig == 1)
		top.document.getElementById('weight_box').value += '9';
	}
	numpad_weight.appendChild(nine_weight);

	var clr_weight = document.createElement('a');
	clr_weight.id = 'numbtn';
	clr_weight.style.top = '310px';
	clr_weight.style.left = '200px';
	clr_weight.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"clr".fontsize(5).bold()+"</td></tr></table>";
	clr_weight.onclick = function()
	{
		top.document.getElementById('weight_box').value = '';
	}
	numpad_weight.appendChild(clr_weight);

	var zero_weight = document.createElement('a');
	zero_weight.id = 'numbtn';
	zero_weight.style.top = '310px';
	zero_weight.style.left = '280px';
	zero_weight.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"0".fontsize(6).bold()+"</td></tr></table>";
	zero_weight.onclick = function()
	{
		if (trig == 0)
		{
			top.document.getElementById('weight_box').value = '';
			trig = 1;
		}
		if (top.document.getElementById('weight_box').value != '' && top.document.getElementById('weight_box').value.length < 4 && trig == 1)
		top.document.getElementById('weight_box').value += '0';
	}
	numpad_weight.appendChild(zero_weight);

	var bs_weight = document.createElement('a');
	bs_weight.id = 'numbtn';
	bs_weight.style.top = '310px';
	bs_weight.style.left = '360px';
	bs_weight.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"bs".fontsize(5).bold()+"</td></tr></table>";
	bs_weight.onclick = function()
	{
		var len = top.document.getElementById('weight_box').value.length;
		top.document.getElementById('weight_box').value = top.document.getElementById('weight_box').value.substr(0,len-1);
	}
	numpad_weight.appendChild(bs_weight);

// Num Pad // Position
	var numpad_pos = document.createElement('div');
	numpad_pos.id = 'numpad';
	numpad_pos.style.position = 'absolute';
	numpad_pos.style.top = '-40px';
	numpad_pos.style.left = '30px';
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
			trig = 1;
		}
		if (top.document.getElementById('position_box').value.length < 2 && trig == 1)
		top.document.getElementById('position_box').value += '1';
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
			trig = 1;
		}
		if (top.document.getElementById('position_box').value.length < 2 && trig == 1)
		top.document.getElementById('position_box').value += '2';
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
			trig = 1;
		}
		if (top.document.getElementById('position_box').value.length < 2 && trig == 1)
		top.document.getElementById('position_box').value += '3';
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
			trig = 1;
		}
		if (top.document.getElementById('position_box').value.length < 2 && trig == 1)
		top.document.getElementById('position_box').value += '4';
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
			trig = 1;
		}
		if (top.document.getElementById('position_box').value.length < 2 && trig == 1)
		top.document.getElementById('position_box').value += '5';
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
			trig = 1;
		}
		if (top.document.getElementById('position_box').value.length < 2 && trig == 1)
		top.document.getElementById('position_box').value += '6';
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
			trig = 1;
		}
		if (top.document.getElementById('position_box').value.length < 2 && trig == 1)
		top.document.getElementById('position_box').value += '7';
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
			trig = 1;
		}
		if (top.document.getElementById('position_box').value.length < 2 && trig == 1)
		top.document.getElementById('position_box').value += '8';
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
			trig = 1;
		}
		if (top.document.getElementById('position_box').value.length < 2 && trig == 1)
		top.document.getElementById('position_box').value += '9';
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
			trig = 1;
		}
		if (top.document.getElementById('position_box').value != '' && top.document.getElementById('position_box').value.length < 2 && trig == 1)
		top.document.getElementById('position_box').value += '0';
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
	}
	numpad_pos.appendChild(bs_pos);

////////

	var ok_id = document.createElement('a');
	ok_id.id = 'confirm';
	ok_id.style.left = '70px';
	ok_id.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"OK".fontsize(5).bold()+"</td></tr></table>";
	ok_id.onclick = function()
	{
		var idval = top.document.getElementById('id_box').value;
		var pcodeval = top.document.getElementById('pcode_select').value;
		var sizeval = top.document.getElementById('size_select').value;
		var laneval = top.document.getElementById('lane_box').value;
		var positionval = top.document.getElementById('position_box').value;
		var weightval = top.document.getElementById('weight_box').value;
//		alert(idval+', '+pcodeval+', '+sizeval+', '+laneval+', '+positionval+', '+weightval);
//		alert(document.getElementById('tag2write').value);
		var pass = 0;
		var messi = '';
		if (idval != '') {
			var idvalue = '('+idval+'L,)';
			if (document.getElementById('tagidlist').value.search(idvalue) == -1) {
				pass++;
			} else {
				messi += "\n- This tag ID is not available.";
			}
//			alert(document.getElementById('tagidlist').value);
		} else {
			messi += "\n- Please enter tag ID.";
		}
		if (weightval != '') {
			pass++;
		} else {
			messi += '\n- Please enter weight.';
		}
		if (parseInt(positionval) > 13) {
			messi += '\n- The submitted position is not in range (1-13).';
		}
//		if (document.getElementById('tag2write').value.search('AAAA') != -1) {
//			pass++;
//		}
		
//		if (document.getElementById('tag2write').value.search('AAAA') != -1) {alert(document.getElementById('tag2write').value.search('AAAA'));}
		if (pass >= 2) {
			document.getElementById("atagid").value = idval;
			document.getElementById("apcode").value = pcodeval;
			document.getElementById("asize").value = sizeval;
			document.getElementById("alane").value = laneval;
			document.getElementById("aposition").value = positionval;
			document.getElementById("aweight").value = weightval;
			document.getElementById("oldtagid").value = document.getElementById('tag2write').value;
			document.getElementById("frm6").submit();
			top.document.body.removeChild(top.document.getElementById('layer'));
			top.document.body.removeChild(top.document.getElementById('box'));
		} else {
			alert(messi);
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
