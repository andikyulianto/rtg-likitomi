function manInput()
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
	div.style.backgroundColor = 'lavender';
	div.style.opacity = '.8';
	div.style.border = '2px solid silver';
	div.style.padding = '20px';
	document.body.appendChild(div);

	var mes = document.createElement('b');
	mes.style.fontFamily = 'Tahoma,Times,serif';
	mes.innerHTML = "Please enter the new weight. \n".fontsize(4);
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
		if (document.getElementById('inp').value != '')
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
		document.getElementById("manin").value = inbox;
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