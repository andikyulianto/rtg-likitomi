function weightInput()
{
	var agent = navigator.userAgent;
//	alert(agent);
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
//	layer.style.height = height-5 + 'px';
//	layer.style.width = width-5 + 'px';
	if (chrome == 'Chrome'){
		layer.style.height = 600 +'px';
		layer.style.width = 800 +'px';
	} else if (firefox == 'Firefox'){
//		alert(firefox);
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
//	div.style.top = height/2-430/2 + 'px'; 
//	div.style.left = width/2-400/2 + 'px'; 
	div.style.top = '100px'; 
	div.style.left = '250px'; 
	div.style.height = '400px';
	div.style.width = '300px';
	div.style.backgroundColor = 'lightgray';
	div.style.opacity = '1';
	div.style.border = '2px solid silver';
	div.style.padding = '20px';
	top.document.body.appendChild(div);

	var mes = document.createElement('center');
	mes.innerHTML = "Please enter the new weight.".fontsize(4).bold();
	div.appendChild(mes);

	var wik = document.createElement('center');
	div.appendChild(wik);

	var w = document.createElement('b');
	w.innerHTML = 'Weight: '.fontsize(4);
	wik.appendChild(w);

	var i = document.createElement('input');
	i.id = 'inp';
	i.type = 'text';
//	i.size = '4';
	i.maxLength = '4';
	i.style.width = '90px';
	i.style.fontSize = '200%';
	i.style.color = 'black';
	i.style.textAlign = 'center';
	wik.appendChild(i);

	var k = document.createElement('b');
	k.innerHTML = ' kgs.'.fontsize(4);
	wik.appendChild(k);

	var one = document.createElement('a');
	one.id = 'numbtn';
	one.style.top = '100px';
	one.style.left = '60px';
	one.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"1".fontsize(6).bold()+"</td></tr></table>";
	one.onclick = function()
	{
		if (top.document.getElementById('inp').value.length < 4)
		top.document.getElementById('inp').value += '1';
	}
	div.appendChild(one);

	var two = document.createElement('a');
	two.id = 'numbtn';
	two.style.top = '100px';
	two.style.left = '140px';
	two.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"2".fontsize(6).bold()+"</td></tr></table>";
	two.onclick = function()
	{
		if (top.document.getElementById('inp').value.length < 4)
		top.document.getElementById('inp').value += '2';
	}
	div.appendChild(two);

	var three = document.createElement('a');
	three.id = 'numbtn';
	three.style.top = '100px';
	three.style.left = '220px';
	three.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"3".fontsize(6).bold()+"</td></tr></table>";
	three.onclick = function()
	{
		if (top.document.getElementById('inp').value.length < 4)
		top.document.getElementById('inp').value += '3';
	}
	div.appendChild(three);

	var four = document.createElement('a');
	four.id = 'numbtn';
	four.style.top = '170px';
	four.style.left = '60px';
	four.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"4".fontsize(6).bold()+"</td></tr></table>";
	four.onclick = function()
	{
		if (top.document.getElementById('inp').value.length < 4)
		top.document.getElementById('inp').value += '4';
	}
	div.appendChild(four);

	var five = document.createElement('a');
	five.id = 'numbtn';
	five.style.top = '170px';
	five.style.left = '140px';
	five.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"5".fontsize(6).bold()+"</td></tr></table>";
	five.onclick = function()
	{
		if (top.document.getElementById('inp').value.length < 4)
		top.document.getElementById('inp').value += '5';
	}
	div.appendChild(five);

	var six = document.createElement('a');
	six.id = 'numbtn';
	six.style.top = '170px';
	six.style.left = '220px';
	six.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"6".fontsize(6).bold()+"</td></tr></table>";
	six.onclick = function()
	{
		if (top.document.getElementById('inp').value.length < 4)
		top.document.getElementById('inp').value += '6';
	}
	div.appendChild(six);

	var seven = document.createElement('a');
	seven.id = 'numbtn';
	seven.style.top = '240px';
	seven.style.left = '60px';
	seven.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"7".fontsize(6).bold()+"</td></tr></table>";
	seven.onclick = function()
	{
		if (top.document.getElementById('inp').value.length < 4)
		top.document.getElementById('inp').value += '7';
	}
	div.appendChild(seven);

	var eight = document.createElement('a');
	eight.id = 'numbtn';
	eight.style.top = '240px';
	eight.style.left = '140px';
	eight.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"8".fontsize(6).bold()+"</td></tr></table>";
	eight.onclick = function()
	{
		if (top.document.getElementById('inp').value.length < 4)
		top.document.getElementById('inp').value += '8';
	}
	div.appendChild(eight);

	var nine = document.createElement('a');
	nine.id = 'numbtn';
	nine.style.top = '240px';
	nine.style.left = '220px';
	nine.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"9".fontsize(6).bold()+"</td></tr></table>";
	nine.onclick = function()
	{
		if (top.document.getElementById('inp').value.length < 4)
		top.document.getElementById('inp').value += '9';
	}
	div.appendChild(nine);

	var clr = document.createElement('a');
	clr.id = 'numbtn';
	clr.style.top = '310px';
	clr.style.left = '60px';
	clr.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"clr".fontsize(5).bold()+"</td></tr></table>";
	clr.onclick = function()
	{
		top.document.getElementById('inp').value = '';
	}
	div.appendChild(clr);

	var zero = document.createElement('a');
	zero.id = 'numbtn';
	zero.style.top = '310px';
	zero.style.left = '140px';
	zero.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"0".fontsize(6).bold()+"</td></tr></table>";
	zero.onclick = function()
	{
		if (top.document.getElementById('inp').value.length < 4 && top.document.getElementById('inp').value != '')
		top.document.getElementById('inp').value += '0';
	}
	div.appendChild(zero);

	var bs = document.createElement('a');
	bs.id = 'numbtn';
	bs.style.top = '310px';
	bs.style.left = '220px';
	bs.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"bs".fontsize(5).bold()+"</td></tr></table>";
	bs.onclick = function()
	{
		var len = top.document.getElementById('inp').value.length;
		top.document.getElementById('inp').value = top.document.getElementById('inp').value.substr(0,len-1);
	}
	div.appendChild(bs);

	var ok = document.createElement('a');
	ok.id = 'confirm';
	ok.style.left = '60px';
	ok.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"OK".fontsize(4).bold()+"</td></tr></table>";
	ok.onclick = function()
	{
		var inbox = top.document.getElementById('inp').value;
		//alert(inbox);
		//alert(document.getElementById("actual").value);
		if (parseInt(inbox) < document.getElementById("actual").value) {
			document.getElementById("temp").value = inbox;
			//alert(document.getElementById("temp").value);
			document.getElementById("frm1").submit();
			top.document.body.removeChild(top.document.getElementById('layer'));
			top.document.body.removeChild(top.document.getElementById('box'));
		} else {
			alert("The submitted weight is not less than previous weight!");
			top.document.getElementById('inp').value = '';
		}
	}
	div.appendChild(ok);

	var cancel = document.createElement('a');
	cancel.id = 'confirm';
	cancel.style.right = '65px';
	cancel.innerHTML = "<table style='height:100%; width:100%;'><tr><td style='cursor:pointer;'>"+"Cancel".fontsize(4).bold()+"</td></tr></table>";
	cancel.onclick = function()
	{
		top.document.body.removeChild(top.document.getElementById('layer'));
		top.document.body.removeChild(top.document.getElementById('box'));
	}
	div.appendChild(cancel);
}
