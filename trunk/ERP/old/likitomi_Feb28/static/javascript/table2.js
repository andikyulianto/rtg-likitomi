/**
 * @author sanjilshrestha
 */

var row2moverclass = 'cwTableHighlightRow'; 
var row2selectedclass = 'cwTableSelectRow'; 

function cwOver(row) {
	row.mover = true; 
	if (typeof(row.oClassName) == "undefined")
		row.oClassName = row.className;
	if (typeof(row.oCssText) == "undefined")
		row.oCssText = row.style.cssText;
	if (!row.selected) {
		row.className = row2moverclass;
		row.style.cssText = "";
	}
}

function cwOut(row) {
	row.mover = false; // Mouse out
	if (!row.selected)
		cw_SetColor(row);
}

function cw_SetColor(row) {
	if (row.selected) {
		if (typeof(row.oClassName) == "undefined")
			row.oClassName = row.className;
		if (typeof(row.oCssText) == "undefined")
			row.oCssText = row.style.cssText;
		row.className = row2selectedclass;
	} else {
		if (typeof(row.oClassName) != "undefined")
			row.className = row.oClassName;
		if (typeof(row.oCssText) != "undefined")
			row.style.cssText = row.oCssText;
	}
}

function cw_Click(row) { 
	var bselected = row.selected;
	cw_ClearSelected(); // Clear all other selected rows
	row.selected = true;//!bselected; // Toggle
	cw_SetColor(row);
}

function cw_ClearSelected() {
	var table = document.getElementById('cwlistmain');
	if (table != null) {
		for (var i = 0; i < table.rows.length; i++) {
			var thisrow = table.rows[i];
			if (thisrow.selected && !thisrow.deleterow) {
				thisrow.selected = false;
				cw_SetColor(thisrow);
			}
		}
	}
}

var scroller;
function goTop(){
	var scroll = document.getElementById('listdivcontainer').scrollTop;
	if (scroll>300)scroll -= scroll/15;
	else scroll -= 20;

	document.getElementById('listdivcontainer').scrollTop=scroll;
	if(scroll <= 0) if(scroller) clearTimeout(scroller);
	if(scroll>0) scroller = setTimeout("goTop()",10);
}


function goTopPaper(){
	var scroll = document.getElementById('listdivcontainer').scrollTop;
	if (scroll>300)scroll -= scroll/15;
	else scroll -= 20;

	document.getElementById('listdivcontainer').scrollTop=scroll;
	if(scroll <= 0) if(scroller) clearTimeout(scroller);
	if(scroll>0) scroller = setTimeout("goTopPaper()",10);
}



