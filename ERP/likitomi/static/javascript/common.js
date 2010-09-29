/**
 * @author sanjilshrestha
 */
function activatePlaceholders() {
	var detect = navigator.userAgent.toLowerCase(); 
	if (detect.indexOf("safari") > 0) return false;
	var searchinput = document.getElementById('searchtext');
	var placeholder = searchinput.getAttribute("placeholder");
	if (placeholder.length > 0) {
		searchinput.value = placeholder;
		searchinput.onclick = function() {
			if (this.value == this.getAttribute("placeholder")) {
				this.value = "";
			}
			return false;
		}
		searchinput.onblur = function() {
			if (this.value.length < 1) {
				this.value = this.getAttribute("placeholder");
			}
		}
	}
}

function getParent(el, pTagName) {
	if (el == null) return null;
	else if (el.nodeType == 1 && el.tagName.toLowerCase() == pTagName.toLowerCase()) // Gecko bug, supposed to be uppercase
		return el;
	else
		return getParent(el.parentNode, pTagName);
}

function autoLoadFirstData() {
	var table = document.getElementById('cwlistmain');
	if (table != null) {
		var thisrow = table.rows[1];
		if (!thisrow.selected) {
			thisrow.selected = true;
			cw_SetColor(thisrow);
		}
		var firstDataObj = document.getElementById('firstitem');
		if (firstDataObj != null) {
			return firstDataObj.value;
		}
	}
	return 0;
}

function makeDateFields(){
	var edate=Ext.select("input.date-picker",true);
	var ignore = Ext.get('todaydate');
	var etime=Ext.select("input.time-picker",true);
	var today = new Date().format('Y-m-d');
	edate.each(function(el){
		var df = new Ext.form.DateField({"format":'Y-m-d',"altFormats":'j|j/n|j/n/y|j/n/Y|j-M|j-M-y|j-M-Y',"minValue":today});
		if(el!=ignore)
			df.applyToMarkup(el);
	})
	etime.each(function(el){
		var df = new Ext.form.TimeField({"format":'H:i',});
		df.applyToMarkup(el);
	})
}

function makeDateFields2(){
	var edate=Ext.select("input.date-picker",true);
	var ignore = Ext.get('todaydate');
	var etime=Ext.select("input.time-picker",true);
	var today = new Date().format('d-m-Y');
	edate.each(function(el){
		var df = new Ext.form.DateField({"format":'d-m-Y',"altFormats":'j|j/n|j/n/y|j/n/Y|j-M|j-M-y|j-M-Y',"minValue":today});
		if(el!=ignore)
			df.applyToMarkup(el);
	})
	etime.each(function(el){
		var df = new Ext.form.TimeField({"format":'H:i',});
		df.applyToMarkup(el);
	})
}

function validateText(obj){
	var row = getParent(obj,'TD');
	if(obj!=null){
		if (obj.value == "") {
			row.className = 'required';
			obj.focus();
			return false;
		}
		else 
			return true;
	}
	else return false;
}

function timeoutMessage(msg)
{
	document.getElementById('flashMessage').style.visibility="visible";
	document.getElementById('flashMessage').style.display="block";
	var el = Ext.get('flashMessage');
	el.update(msg);
	el.highlight("",{ duration: 3 });    
    el.switchOff({
        easing: 'easeIn',
        duration: 0.3,
        remove: false,
        useDisplay: false
    });
}


//Tooltips
function logoutTips(){
	new Ext.ToolTip({
		target: 'tip-logout',
		html: 'Click to Logout the System',
		trackMouse:false
	});
	Ext.QuickTips.init();
}