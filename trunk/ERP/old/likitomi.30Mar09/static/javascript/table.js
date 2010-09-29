/**
 * @author sanjilshrestha
 */

var rowclass = 'ewTableRow'; 
var rowaltclass = 'ewTableAltRow'; 
var rowmoverclass = 'ewTableHighlightRow'; 
var rowselectedclass = 'ewTableSelectRow'; 

function ew_MouseOver(row) {
	row.mover = true; 
	if (typeof(row.oClassName) == "undefined")
		row.oClassName = row.className;
	if (typeof(row.oCssText) == "undefined")
		row.oCssText = row.style.cssText;
	if (!row.selected) {
		row.className = rowmoverclass;
		row.style.cssText = "";
	}
}

function ew_MouseOut(row) {
	row.mover = false; // Mouse out
	if (!row.selected)
		ew_SetColor(row);
}

function ew_SetColor(row) {
	if (row.selected) {
		if (typeof(row.oClassName) == "undefined")
			row.oClassName = row.className;
		if (typeof(row.oCssText) == "undefined")
			row.oCssText = row.style.cssText;
		row.className = rowselectedclass;
	} else {
		if (typeof(row.oClassName) != "undefined")
			row.className = row.oClassName;
		if (typeof(row.oCssText) != "undefined")
			row.style.cssText = row.oCssText;
	}
}

function ew_Click(row) { 
	var bselected = row.selected;
	ew_ClearSelected(); // Clear all other selected rows
	row.selected = true;//!bselected; // Toggle
	ew_SetColor(row);
}

function ea_Click(alink) {
	var table = document.getElementById('ewlistmain');
	var row = table.rows[alink];
	ew_Click(row);
}

function ew_ClearSelected() {
	var table = document.getElementById('ewlistmain');
	for (var i = firstrowoffset; i < table.rows.length-lastrowoffset; i++) {
		var thisrow = table.rows[i];
		if (thisrow.selected) {
			thisrow.selected = false;
			ew_SetColor(thisrow);
		}
	}
}

function ew_AutoSelectById(id){
	var table = document.getElementById('ewlistmain');
	for (var i = 0; i < table.rows.length; i++) {
		var thisrow = table.rows[i];
		if (thisrow.selected) {
			if(id != i ) {
				thisrow.selected = false;
				ew_SetColor(thisrow);
			}
		}else {
			if(id == i ) {
				thisrow.selected = true;
				ew_SetColor(thisrow);
			}
		}
	}
}


