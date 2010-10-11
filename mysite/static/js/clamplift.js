function changeLoc()
{
	var width = document.documentElement.clientWidth + document.documentElement.scrollLeft;

	var layer = document.createElement('div');
	layer.style.zIndex = 2;
	layer.id = 'layer';
	layer.style.position = 'absolute';
	layer.style.top = '0px';
	layer.style.left = '0px';
	layer.style.height = document.documentElement.scrollHeight + 'px';
	layer.style.width = width + 'px';
	layer.style.backgroundColor = 'black';
	layer.style.opacity = '.6';
	layer.style.filter += ("progid:DXImageTransform.Microsoft.Alpha(opacity=60)");
	document.body.appendChild(layer);

	var div = document.createElement('div');
	div.style.zIndex = 3;
	div.id = 'box';
	div.style.position = (navigator.userAgent.indexOf('MSIE 6') > -1) ? 'absolute' : 'fixed';
	div.style.top = '50px'; 
	div.style.left = (width / 2) - (400 / 2) + 'px'; 
	div.style.height = '480px';
	div.style.width = '420px';
	div.style.backgroundColor = 'lightgray';
	div.style.opacity = '1';
	div.style.border = '2px solid silver';
	div.style.padding = '20px';
	document.body.appendChild(div);

	var mes = document.createElement('b');
	mes.style.fontFamily = 'Tahoma,Times,serif';
	mes.innerHTML = "<b>Please enter lane and location.</b><br />".fontsize(5);
	div.appendChild(mes);

	var l = document.createElement('b');
	l.style.fontFamily = 'Tahoma,Times,serif';
	l.innerHTML = 'Lane >>> '.fontsize(4);
	div.appendChild(l);

	var ilane = document.createElement('input');
	ilane.style.fontSize = '200%';
	ilane.style.fontFamily = 'Tahoma,Times,serif';
	ilane.style.color = 'tomato';
	ilane.style.textAlign = 'right';
	ilane.maxlength = '4';
	ilane.size = '1';
	ilane.type = 'text';
	ilane.id = 'ilane';
	div.appendChild(ilane);
	
	var d = document.createElement('b');
	d.style.fontFamily = 'Tahoma,Times,serif';
	d.innerHTML = '-'.fontsize(4);
	div.appendChild(d);
	
	var iposition = document.createElement('input');
	iposition.style.fontSize = '200%';
	iposition.style.fontFamily = 'Tahoma,Times,serif';
	iposition.style.color = 'tomato';
	iposition.maxlength = '4';
	iposition.size = '2';
	iposition.type = 'text';
	iposition.id = 'iposition';
	div.appendChild(iposition);
	
	var p = document.createElement('b');
	p.style.fontFamily = 'Tahoma,Times,serif';
	p.innerHTML = ' <<< Position'.fontsize(4);
	div.appendChild(p);
	
	var a = document.createElement('a');
	a.id = 'lanebutton';
	a.style.top = '120px';
	a.style.left = '80px'; 
	a.innerHTML = 'A'.bold().fontsize(4);
	a.onclick = function()
	{
		document.getElementById('ilane').value = 'A';
	}
	div.appendChild(a);
	
	var b = document.createElement('a');
	b.id = 'lanebutton';
	b.style.top = '170px';
	b.style.left = '80px'; 
	b.innerHTML = 'B'.bold().fontsize(4);
	b.onclick = function()
	{
		document.getElementById('ilane').value = 'B';
	}
	div.appendChild(b);
	
	var c = document.createElement('a');
	c.id = 'lanebutton';
	c.style.top = '195px';
	c.style.left = '80px'; 
	c.innerHTML = 'C'.bold().fontsize(4);
	c.onclick = function()
	{
		document.getElementById('ilane').value = 'C';
	}
	div.appendChild(c);
	
	var d = document.createElement('a');
	d.id = 'lanebutton';
	d.style.top = '245px';
	d.style.left = '80px'; 
	d.innerHTML = 'D'.bold().fontsize(4);
	d.onclick = function()
	{
		document.getElementById('ilane').value = 'D';
	}
	div.appendChild(d);
	
	var e = document.createElement('a');
	e.id = 'lanebutton';
	e.style.top = '270px';
	e.style.left = '80px'; 
	e.innerHTML = 'E'.bold().fontsize(4);
	e.onclick = function()
	{
		document.getElementById('ilane').value = 'E';
	}
	div.appendChild(e);
	
	var f = document.createElement('a');
	f.id = 'lanebutton';
	f.style.top = '320px';
	f.style.left = '80px'; 
	f.innerHTML = 'F'.bold().fontsize(4);
	f.onclick = function()
	{
		document.getElementById('ilane').value = 'F';
	}
	div.appendChild(f);
	
	var g = document.createElement('a');
	g.id = 'lanebutton';
	g.style.top = '345px';
	g.style.left = '80px'; 
	g.innerHTML = 'G'.bold().fontsize(4);
	g.onclick = function()
	{
		document.getElementById('ilane').value = 'G';
	}
	div.appendChild(g);
	
	var h = document.createElement('a');
	h.id = 'lanebutton';
	h.style.top = '395px';
	h.style.left = '80px'; 
	h.innerHTML = 'H'.bold().fontsize(4);
	h.onclick = function()
	{
		document.getElementById('ilane').value = 'H';
	}
	div.appendChild(h);

	var one = document.createElement('a');
	one.id = 'posbutton';
	one.style.top = '120px';
	one.style.left = '220px'; 
	one.innerHTML = '1'.bold().fontsize(6);
	one.onclick = function()
	{
		if (document.getElementById('iposition').value.length < 2)
		document.getElementById('iposition').value += '1';
	}
	div.appendChild(one);

	var two = document.createElement('a');
	two.id = 'posbutton';
	two.style.top = '120px';
	two.style.left = '300px'; 
	two.innerHTML = '2'.bold().fontsize(6);
	two.onclick = function()
	{
		if (document.getElementById('iposition').value.length < 2)
		document.getElementById('iposition').value += '2';
	}
	div.appendChild(two);

	var three = document.createElement('a');
	three.id = 'posbutton';
	three.style.top = '120px';
	three.style.left = '380px'; 
	three.innerHTML = '3'.bold().fontsize(6);
	three.onclick = function()
	{
		if (document.getElementById('iposition').value.length < 2)
		document.getElementById('iposition').value += '3';
	}
	div.appendChild(three);

	var four = document.createElement('a');
	four.id = 'posbutton';
	four.style.top = '200px';
	four.style.left = '220px'; 
	four.innerHTML = '4'.bold().fontsize(6);
	four.onclick = function()
	{
		if (document.getElementById('iposition').value.length < 2)
		document.getElementById('iposition').value += '4';
	}
	div.appendChild(four);

	var five = document.createElement('a');
	five.id = 'posbutton';
	five.style.top = '200px';
	five.style.left = '300px'; 
	five.innerHTML = '5'.bold().fontsize(6);
	five.onclick = function()
	{
		if (document.getElementById('iposition').value.length < 2)
		document.getElementById('iposition').value += '5';
	}
	div.appendChild(five);

	var six = document.createElement('a');
	six.id = 'posbutton';
	six.style.top = '200px';
	six.style.left = '380px'; 
	six.innerHTML = '6'.bold().fontsize(6);
	six.onclick = function()
	{
		if (document.getElementById('iposition').value.length < 2)
		document.getElementById('iposition').value += '6';
	}
	div.appendChild(six);

	var seven = document.createElement('a');
	seven.id = 'posbutton';
	seven.style.top = '280px';
	seven.style.left = '220px'; 
	seven.innerHTML = '7'.bold().fontsize(6);
	seven.onclick = function()
	{
		if (document.getElementById('iposition').value.length < 2)
		document.getElementById('iposition').value += '7';
	}
	div.appendChild(seven);

	var eight = document.createElement('a');
	eight.id = 'posbutton';
	eight.style.top = '280px';
	eight.style.left = '300px'; 
	eight.innerHTML = '8'.bold().fontsize(6);
	eight.onclick = function()
	{
		if (document.getElementById('iposition').value.length < 2)
		document.getElementById('iposition').value += '8';
	}
	div.appendChild(eight);

	var nine = document.createElement('a');
	nine.id = 'posbutton';
	nine.style.top = '280px';
	nine.style.left = '380px'; 
	nine.innerHTML = '9'.bold().fontsize(6);
	nine.onclick = function()
	{
		if (document.getElementById('iposition').value.length < 2)
		document.getElementById('iposition').value += '9';
	}
	div.appendChild(nine);

	var clr = document.createElement('a');
	clr.id = 'posbutton';
	clr.style.top = '360px';
	clr.style.left = '220px'; 
	clr.innerHTML = 'clr'.bold().fontsize(6);
	clr.onclick = function()
	{
		document.getElementById('iposition').value = '';
	}
	div.appendChild(clr);

	var zero = document.createElement('a');
	zero.id = 'posbutton';
	zero.style.top = '360px';
	zero.style.left = '300px'; 
	zero.innerHTML = '0'.bold().fontsize(6);
	zero.onclick = function()
	{
		if (document.getElementById('iposition').value != '' && document.getElementById('iposition').value.length < 2)
		document.getElementById('iposition').value += '0';
	}
	div.appendChild(zero);

	var ok = document.createElement('a');
	ok.id = 'confirm';
	ok.style.left = '70px'; 
	ok.innerHTML = "OK".fontsize(5).bold();
	//ok.href = 'javascript:void(0)';
	ok.onclick = function() 
	{
		var lanebox = document.getElementById('ilane').value;
		var posbox = document.getElementById('iposition').value;
		document.getElementById("lane").value = lanebox;
		document.getElementById("pos").value = posbox;
		document.getElementById("frm3").submit();
		document.body.removeChild(document.getElementById('layer'));
		document.body.removeChild(document.getElementById('box'));
	}
	div.appendChild(ok);

	var cancel = document.createElement('a');
	cancel.id = 'confirm';
	cancel.style.right = '80px'; 
	cancel.innerHTML = "Cancel".fontsize(5).bold();
	//cancel.href = 'javascript:void(0)';
	cancel.onclick = function() 
	{
		document.body.removeChild(document.getElementById('layer'));
		document.body.removeChild(document.getElementById('box'));
	}
	div.appendChild(cancel);
}

function weightInput()
{
	var width = document.documentElement.clientWidth + document.documentElement.scrollLeft;

	var layer = document.createElement('div');
	layer.style.zIndex = 2;
	layer.id = 'layer';
	layer.style.position = 'absolute';
	layer.style.top = '0px';
	layer.style.left = '0px';
	layer.style.height = document.documentElement.scrollHeight + 'px';
	layer.style.width = width + 'px';
	layer.style.backgroundColor = 'black';
	layer.style.opacity = '.6';
	layer.style.filter += ("progid:DXImageTransform.Microsoft.Alpha(opacity=60)");
	document.body.appendChild(layer);

	var div = document.createElement('div');
	div.style.zIndex = 3;
	div.id = 'box';
	div.style.position = (navigator.userAgent.indexOf('MSIE 6') > -1) ? 'absolute' : 'fixed';
	div.style.top = '50px'; 
	div.style.left = (width / 2) - (400 / 2) + 'px'; 
	div.style.height = '480px';
	div.style.width = '320px';
	div.style.backgroundColor = 'lightgray';
	div.style.opacity = '1';
	div.style.border = '2px solid silver';
	div.style.padding = '20px';
	document.body.appendChild(div);

	var mes = document.createElement('b');
	mes.style.fontFamily = 'Tahoma,Times,serif';
	mes.innerHTML = "Please enter the new weight. \n".fontsize(5);
	div.appendChild(mes);

	var w = document.createElement('b');
	w.style.fontFamily = 'Tahoma,Times,serif';
	w.innerHTML = 'Weight: '.fontsize(4);
	div.appendChild(w);

	var i = document.createElement('input');
	i.style.fontSize = '200%';
	i.style.fontFamily = 'Tahoma,Times,serif';
	i.style.color = 'tomato';
	i.maxlength = '4';
	i.size = '4';
	i.type = 'text';
	i.id = 'inp';
	div.appendChild(i);

	var k = document.createElement('b');
	k.style.fontFamily = 'Tahoma,Times,serif';
	k.innerHTML = ' kilograms'.fontsize(4);
	div.appendChild(k);

	var one = document.createElement('a');
	one.id = 'gridbutton';
	one.style.top = '120px';
	one.style.left = '70px'; 
	one.innerHTML = '1'.bold().fontsize(6);
	one.onclick = function()
	{
		document.getElementById('inp').value += '1';
	}
	div.appendChild(one);

	var two = document.createElement('a');
	two.id = 'gridbutton';
	two.style.top = '120px';
	two.style.left = '150px'; 
	two.innerHTML = '2'.bold().fontsize(6);
	two.onclick = function()
	{
		document.getElementById('inp').value += '2';
	}
	div.appendChild(two);

	var three = document.createElement('a');
	three.id = 'gridbutton';
	three.style.top = '120px';
	three.style.left = '230px'; 
	three.innerHTML = '3'.bold().fontsize(6);
	three.onclick = function()
	{
		document.getElementById('inp').value += '3';
	}
	div.appendChild(three);

	var four = document.createElement('a');
	four.id = 'gridbutton';
	four.style.top = '200px';
	four.style.left = '70px'; 
	four.innerHTML = '4'.bold().fontsize(6);
	four.onclick = function()
	{
		document.getElementById('inp').value += '4';
	}
	div.appendChild(four);

	var five = document.createElement('a');
	five.id = 'gridbutton';
	five.style.top = '200px';
	five.style.left = '150px'; 
	five.innerHTML = '5'.bold().fontsize(6);
	five.onclick = function()
	{
		document.getElementById('inp').value += '5';
	}
	div.appendChild(five);

	var six = document.createElement('a');
	six.id = 'gridbutton';
	six.style.top = '200px';
	six.style.left = '230px'; 
	six.innerHTML = '6'.bold().fontsize(6);
	six.onclick = function()
	{
		document.getElementById('inp').value += '6';
	}
	div.appendChild(six);

	var seven = document.createElement('a');
	seven.id = 'gridbutton';
	seven.style.top = '280px';
	seven.style.left = '70px'; 
	seven.innerHTML = '7'.bold().fontsize(6);
	seven.onclick = function()
	{
		document.getElementById('inp').value += '7';
	}
	div.appendChild(seven);

	var eight = document.createElement('a');
	eight.id = 'gridbutton';
	eight.style.top = '280px';
	eight.style.left = '150px'; 
	eight.innerHTML = '8'.bold().fontsize(6);
	eight.onclick = function()
	{
		document.getElementById('inp').value += '8';
	}
	div.appendChild(eight);

	var nine = document.createElement('a');
	nine.id = 'gridbutton';
	nine.style.top = '280px';
	nine.style.left = '230px'; 
	nine.innerHTML = '9'.bold().fontsize(6);
	nine.onclick = function()
	{
		document.getElementById('inp').value += '9';
	}
	div.appendChild(nine);

	var clr = document.createElement('a');
	clr.id = 'gridbutton';
	clr.style.top = '360px';
	clr.style.left = '70px'; 
	clr.innerHTML = 'clr'.bold().fontsize(6);
	clr.onclick = function()
	{
		document.getElementById('inp').value = '';
	}
	div.appendChild(clr);

	var zero = document.createElement('a');
	zero.id = 'gridbutton';
	zero.style.top = '360px';
	zero.style.left = '150px'; 
	zero.innerHTML = '0'.bold().fontsize(6);
	zero.onclick = function()
	{
		if (document.getElementById('inp').value != '')
		document.getElementById('inp').value += '0';
	}
	div.appendChild(zero);

	var dot = document.createElement('a');
	dot.id = 'gridbutton';
	dot.style.top = '360px';
	dot.style.left = '230px'; 
	dot.innerHTML = '.'.bold().fontsize(6);
	dot.onclick = function()
	{
		if (document.getElementById('inp').value != '' && document.getElementById('inp').value.indexOf(".") == -1)
		document.getElementById('inp').value += '.';
	}
	div.appendChild(dot);

	var ok = document.createElement('a');
	ok.id = 'confirm';
	ok.style.left = '70px'; 
	ok.innerHTML = "OK".fontsize(5).bold();
	//ok.href = 'javascript:void(0)';
	ok.onclick = function() 
	{
		var inbox = document.getElementById('inp').value;
		document.getElementById("manweight").value = inbox;
		document.getElementById("frm1").submit();
		document.body.removeChild(document.getElementById('layer'));
		document.body.removeChild(document.getElementById('box'));
	}
	div.appendChild(ok);

	var cancel = document.createElement('a');
	cancel.id = 'confirm';
	cancel.style.right = '80px'; 
	cancel.innerHTML = "Cancel".fontsize(5).bold();
	//cancel.href = 'javascript:void(0)';
	cancel.onclick = function() 
	{
		document.body.removeChild(document.getElementById('layer'));
		document.body.removeChild(document.getElementById('box'));
	}
	div.appendChild(cancel);
}


function submit()
{
	document.getElementById("frm1").submit();
}


function undoSubmit()
{
	document.getElementById("frm2").submit();
}

function hideUndo()
{
	//alert("undo");
	document.getElementById("undo").style.visibility="hidden";
}

/*
function prevList()
{
	var width = document.documentElement.clientWidth + document.documentElement.scrollLeft;
	
	var layer = document.createElement('div');
	layer.style.zIndex = 2;
	layer.id = 'layer';
	layer.style.position = 'absolute';
	layer.style.top = '0px';
	layer.style.left = '0px';
	layer.style.height = document.documentElement.scrollHeight + 'px';
	layer.style.width = width + 'px';
	layer.style.backgroundColor = 'black';
	layer.style.opacity = '.6';
	layer.style.filter += ("progid:DXImageTransform.Microsoft.Alpha(opacity=60)");
	document.body.appendChild(layer);
	
	var leng = {{ leng }};

	var div = document.createElement('div');
	div.style.zIndex = 3;
	div.id = 'box';
	div.style.position = (navigator.userAgent.indexOf('MSIE 6') > -1) ? 'absolute' : 'fixed';
	div.style.top = '50px'; 
	div.style.left = (width / 2) - (400 / 2) + 'px'; 
	div.style.height = (leng * 80) + 100 + 'px';
	div.style.width = '320px';
	div.style.backgroundColor = 'lavender';
	div.style.opacity = '.8';
	div.style.border = '2px solid silver';
	div.style.padding = '20px';
	document.body.appendChild(div);
	
	//var up_datetime_list = {{ up_datetime_list }};
	var to_weight_list = {{ to_weight_list }};
	var list = new Array();
	var i = 0;
	for (i=0; i<leng; i++)
	{
	list[i] = document.createElement('a');
	list[i].id = 'gridbutton'
	list[i].style.top = (i*80) + 20 + 'px';
	list[i].innerHTML = to_weight_list[i];
	list[i].onclick = function()
		{
		alert(to_weight_list[i]);
		}
	div.appendChild(list[i]);
	}
	
	var cancel = document.createElement('a');
	cancel.id = 'confirm';
	cancel.style.right = '80px'; 
	cancel.innerHTML = "Cancel".fontsize(5).bold();
	//cancel.href = 'javascript:void(0)';
	cancel.onclick = function() 
	{
		document.body.removeChild(document.getElementById('layer'));
		document.body.removeChild(document.getElementById('box'));
	}
	div.appendChild(cancel);
}
*/
