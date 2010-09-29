<script type="text/javascript">
	var alltables = new Array("tblDelDate","tblSalesOrder","tblLastModified","tblStatus");
	var filterbyarray = new Array("delivery_date","sales_order","modified_on","status");
	var COLIGNORED = 3;
	var toggleTP = false;
	var today = new Date().format('Y-m-d');
	
	function sel_SetColor(row) 
	{
		row.className = (row.selected)?"selectedRow":"";
	}
	
	function sel_Click(row) 
	{
		var table = getParent(row,'TABLE');
		if(!document.getElementById('chkmultiple').checked){
			clearTableAllExcept("null");
		}
		row.selected = !row.selected;
		sel_SetColor(row);
		postTable(table.id);
	}
	
	function sel_ClearSelected(tblName) 
	{
		clearTable(tblName);
		postTable(tblName);
	}
	
	function clearTable(tblName)
	{
		var table = document.getElementById(tblName);
		for (var i = 0; i < table.rows.length; i++) 
		{
			var thisrow = table.rows[i];
			if (thisrow.selected) 
			{
				thisrow.selected = false;
				sel_SetColor(thisrow);
			}
		}
	}
	
	function clearTableAllExcept(tblName)
	{
		for (i=0;i<alltables.length;i++)
		{
			if(tblName!=alltables[i]) clearTable(alltables[i]);
		}
	}
	
	function sel_SelectAll(tblName) 
	{
		var table = document.getElementById(tblName);
		for (var i = 0; i < table.rows.length; i++) 
		{
			var thisrow = table.rows[i];
			thisrow.selected = true;
			sel_SetColor(thisrow);
		}
		postTable(tblName);
	}
	
	function postTable(tblName)
	{
		var postTableList = "";
		var table = document.getElementById(tblName);
		for (var i = 0; i < table.rows.length; i++) 
		{
			var thisrow = table.rows[i];
			if (thisrow.selected) 
			{
				postTableList +=thisrow.cells[0].innerHTML+"|";
			}
		}
		var filterby="";
		for (i = 0; i < alltables.length; i++) {
			if(tblName==alltables[i]){
				filterby=filterbyarray[i];
				clearTableAllExcept(tblName);
			}
		}
		
		var loadMask = new Ext.LoadMask(Ext.get('searchresult'), { msg: "Loading..." });
		
		//Ajax Load
		Ext.Ajax.request({
			url: BASEURL + 'index.php/planning/filter/',
			params : { 
				filterby 	: filterby,
				selvalue	: postTableList,
			},
			success: function ( result, request ) { 
				//document.getElementById('searchresult').innerHTML = result.responseText;
				var el = Ext.get('searchresult');
				el.update(result.responseText);
				//el.slideIn('t', { duration: 0.2 });
				
				var table = document.getElementById('tblDelResult');
				if(document.getElementById('chksortable').checked)
				 	ts_makeSortable(table);
				runShowHide('tblDelResult');
				makeDateFields();
				toggleTP= true;
				previewTP();
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});	
		Ext.Ajax.on({
		    'beforerequest': function(){
				if(loadMask!=null)loadMask.show();
			},
		    'requestcomplete': function(){
				if(loadMask!=null)loadMask.hide();
			}
		});
	}
	
	var win;			
	function showHistory(obj,delivery_id){		
		if(!win){
			win = new Ext.Window({
				applyTo     : 'deliveryHistoryDiv',
				layout      : 'fit',
				width       : 640,
				height      : 360,
				closeAction :'hide',
				plain       : true,
				contentEl	: 'deliveryHistoryDetails',
				buttons: [{
					text     : 'Close',
					handler  : function(){
						win.hide();
					}
				}]
			});
		}
		win.show(obj);
		Ext.Ajax.request({
			url: BASEURL + 'index.php/planning/getDeliveryHistory/',
			params : { 
				delivery_id 	: delivery_id
			},
			success: function ( result, request ) { 
				document.getElementById('deliveryHistoryDetails').innerHTML= result.responseText;
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});
			
	};
	  
	function runShowHide(tableid)
	{
		var show = 'block';
		var hide = 'none';
		var tbl  = document.getElementById(tableid);
		var rows = tbl.getElementsByTagName('thead');
		for (var row = 0; row < rows.length; row++) {
			var cels = rows[row].getElementsByTagName('th');
			for(var cell=0;cell<cels.length-COLIGNORED;cell++)
			{
				var chkobj = document.getElementById('chk'+cell);
				if(!chkobj.checked) cels[cell].style.display="none";
			}
		}
		var deliveryid ="";		
		var rows = tbl.getElementsByTagName('tr');
		for (var row = 0; row < rows.length; row++) {
			var cels = rows[row].getElementsByTagName('td');
			for(var cell=0;cell<cels.length-COLIGNORED;cell++)
			{
				var chkobj = document.getElementById('chk'+cell);				
				if(!chkobj.checked) cels[cell].style.display="none";
				if (cell == 0) {
					deliveryid = cels[cell].innerHTML;
				}
			}
			if (checkaddedlist(deliveryid)&&(tableid=='tblDelResult'))
			{
				rows[row].className = 'highlight';
				rows[row].cells[cels.length-1].innerHTML="Added";
			}
		}
	}
	  
	function add2planning(btn)
	{
		var srcrow = getParent(btn,'TR');  
		addrow(srcrow);
		updateCounter();
	}
	
	function addAll()
	{
		var srcTable = document.getElementById('tblDelResult');
		var srcrows  = srcTable.rows;
		for (var row=1;row<srcTable.rows.length;row++)
		{
			if(srcrows[row].className !='highlight')
			{
				addrow(srcrows[row]);
			}
		}
		updateCounter();
	}
	function addrow(srcrow)
	{
		var deliveryid = "0";
		var destTable = document.getElementById('tbl_totalplanning');
		var lastRow = destTable.rows.length;
		try {
		 	var row = destTable.insertRow(lastRow);
			//row.setAttribute('id',"'"+(lastRow+1)+"'");
			var cels = srcrow.getElementsByTagName('td');
			var cellid=0
			for(cellid=0;cellid<cels.length-COLIGNORED;cellid++)
			{					
				cell = row.insertCell(cellid);
				//cell.className= 'tblView';
				cell.innerHTML=srcrow.cells[cellid].innerHTML;
				if(cellid==0) deliveryid = srcrow.cells[cellid].innerHTML;
			}
		
			cell = row.insertCell(cellid);
			srccell = srcrow.cells[cellid];
			inputs = srccell.getElementsByTagName('input');			
			cell.innerHTML=inputs[0].value +" " + inputs[1].value;
			
			cellid++;
			cell = row.insertCell(cellid);
			srccell = srcrow.cells[cellid];
			inputs = srccell.getElementsByTagName('input');			
			cell.innerHTML=inputs[0].value +" " + inputs[1].value;
			cellid++;
			cell = row.insertCell(cellid);
			cell.innerHTML="<input type='button' value='Delete' onclick='removeRow(this)'/>";
		
			document.getElementById('listofdeliveryadded').value = 
				document.getElementById('listofdeliveryadded').value + deliveryid+"|";
			
			//clear src row
			srcrow.className = 'highlight';
			srcrow.cells[cellid].innerHTML="Added";
			
			/*cellid++;
			cell = row.insertCell(cellid);
			cell.innerHTML=srcrow.rowIndex;
			cell.setAttribute('onclick',"sortinlineedit(this)");*/
		} 
		catch (ex) {}
	}
	
	function removeRow(btn)
	{
		var row = getParent(btn,'TR');  
		var tbl = document.getElementById('tbl_totalplanning');
		var newlist = "";
		try {	
			var removeId = row.cells[0].innerHTML;
			tbl.deleteRow(row.rowIndex);
			var addedlist = document.getElementById('listofdeliveryadded').value;
	        if (addedlist != "") {
				var listarray = addedlist.split("|");
				for (i = 0; i <listarray.length-1; i++) 
				{
					if (removeId != listarray[i]) 
					{
					 	newlist += listarray[i]+ "|";
					}
				 }
				 document.getElementById('listofdeliveryadded').value = newlist;
			}
		} 
		catch (ex) {
			alert(ex);
		}
		updateCounter();
	}
	function checkaddedlist(id)
	{
        var addedlist = document.getElementById('listofdeliveryadded').value;
        if (addedlist != "") {
			var listarray = addedlist.split("|");
			for (i = 0; i <listarray.length-1; i++) 
			{
				 if (id == listarray[i]) return true;
			 }
		} 
		return false;
	}
	
	function updateCounter()
	{
		totaladded = 0;
		var addedlist = document.getElementById('listofdeliveryadded').value;
        if (addedlist != "") 
		{
			var listarray = addedlist.split("|");
			totaladded = listarray.length-1;
		}
		var el = Ext.get('counter');
		el.update(totaladded);
		el.frame("ff0000", 1, { duration: 0.8 });
		el.highlight();
		//document.getElementById('counter').innerHTML = totaladded;
	}
	
	function previewTP()
	{
		toggleTP = !toggleTP;
		if (toggleTP) {
			document.getElementById('searchresult').style.display = 'none';
			document.getElementById('div_totalplanning').style.display = 'block';
			document.getElementById('btnPreview').value = 'Back to Search Page';
			var table = document.getElementById('tbl_totalplanning');
			ts_makeSortable(table);
			runShowHide('tbl_totalplanning');
			var el = Ext.get('titleTP');
			//el.slideIn('t', { duration: 0.5 });
			el.highlight();
			el = Ext.get('btnPreview');
			el.highlight();
		}
		else {
			document.getElementById('searchresult').style.display = 'block';
			document.getElementById('div_totalplanning').style.display = 'none';
			document.getElementById('btnPreview').value = 'Preview Total Planning';
			var el = Ext.get('titleSearch');
			el.slideIn('l', { duration: 0.5 });
			el.highlight();
			el = Ext.get('btnPreview');
			el.highlight();
		}
	}
	
	function updatecolumn()
	{}
	
	function saveTP()
	{
		var today = document.getElementById('todaydate').value;
		var deliveryid ="";
		var corrugator_date="";
		var converter_date="";
		
		var table = document.getElementById('tbl_totalplanning');
		var rows = table.getElementsByTagName('tr');
		for (var row = 1; row < rows.length; row++) {
			var cels = rows[row].cells[0];
			deliveryid += cels.innerHTML + "|";
			cels = rows[row].cells[12];
			corrugator_date += cels.innerHTML + "|";
			cels = rows[row].cells[13];
			converter_date += cels.innerHTML + "|";
		}
		var loadMask = new Ext.LoadMask(Ext.get('div_totalplanning'), { msg: "Saving..." });
		if(loadMask!=null)loadMask.show();
		//Ajax Load
		Ext.Ajax.request({
			url: BASEURL + 'index.php/planning/savetotalplan/',
			params : { 
				today 		: today,
				deliveryid	: deliveryid,
				corrugator_date : corrugator_date,
				converter_date	: converter_date				
			},
			success: function ( result, request ) { 
				if(loadMask!=null)loadMask.hide();
				document.getElementById('lastsavestatus').innerHTML='Last Saved :<?=date("Y-m-d H:m:s")?>';
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});	
		Ext.Ajax.on({
		    'requestcomplete': function(){
				if(loadMask!=null)loadMask.hide();	
			}
		});
	}
	
	function loadPreviousPlan()
	{
		var date = document.getElementById('todaydate').value;
		var loadMask = new Ext.LoadMask(Ext.get('div_totalplanning'), { msg: "Saving..." });
		if(loadMask!=null)loadMask.show();
		//Ajax Load
		Ext.Ajax.request({
			url: BASEURL + 'index.php/planning/loadplan/',
			params : { 
				today 		: date				
			},
			success: function ( result, request ) { 
				if(loadMask!=null)loadMask.hide();
				document.getElementById('inner_totalplanning').innerHTML= result.responseText;
				runShowHide('tbl_totalplanning');
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});	
		Ext.Ajax.on({
		    'requestcomplete': function(){
				if(loadMask!=null)loadMask.hide();	
			}
		});
		
	}
</script>

<div id='topfilterdiv'></div>

<table>
	<tr><td height='160px'>
		<div id='headbar'> 		
		<table>
			<tr>
				<td></td><td align='center'><span class='spantitle'>Config</span></td>
				<td></td><td align='center'><span class='spantitle'>Delivery Date</span></td>
				<td></td><td align='center'><span class='spantitle'>Sales Order</span></td>
				<td></td><td align='center'><span class='spantitle'>Modified Date</span></td>
				<td></td><td align='center'><span class='spantitle'>Status</span></td>
				<td></td><td align='center'><span class='spantitle'>Show</span></td>
				<td></td><td align='center'><span class='spantitle'>Log</span></td>
			</tr>
			<tr>
				<td class='tblBlank'></td>
				<td><div id='divcheckbox'>
						<table class='tblcheckbox'>
							<tr><td><input type='checkbox' id='chkmultiple' checked/>Multiple Row</td></tr>
							<tr><td><input type='checkbox' id='chksortable' checked/>Sorttable Table</td></tr>
						</table>
					</div>
				</td>
				<td class='tblBlank'></td>
				<td>
					<div id='divcheckbox'>						
						<?=tableTemplate("tblDelDate",$delDateArray);?>
					</div>
				</td>
				<td class='tblBlank'></td>
				<td>
					<div id='divcheckbox'>					
						<?=tableTemplate("tblSalesOrder",$salesOrderArray);?>
					</div>
				</td>
				<td class='tblBlank'></td>
				<td>
					<div id='divcheckbox'>					
						<?=tableTemplate("tblLastModified",$lastmodified);?>
					</div>
				</td>
				<td class='tblBlank'></td>
				<td>
					<div id='divcheckbox'>					
						<?=tableTemplate("tblStatus",$status);?>
					</div>
				</td>
				<td class='tblBlank'></td>
				<td><div id='divcheckbox'>
						<table class='tblcheckbox'>
							<tr><td><input type='checkbox' id='chk0' checked onchange='updatecolumn()'/>Delivery Id</td></tr>
							<tr><td><input type='checkbox' id='chk1' checked onchange='updatecolumn()'/>Sales Order</td></tr>
							<tr><td><input type='checkbox' id='chk2' checked onchange='updatecolumn()'/>PO.NO</td></tr>
							<tr><td><input type='checkbox' id='chk3' checked onchange='updatecolumn()'/>Product Code</td></tr>
							<tr><td><input type='checkbox' id='chk4' onchange='updatecolumn()'/>Company</td></tr>
							<tr><td><input type='checkbox' id='chk5' onchange='updatecolumn()'/>Product Name</td></tr>
							<tr><td><input type='checkbox' id='chk6' checked onchange='updatecolumn()'/>Width</td></tr>
							<tr><td><input type='checkbox' id='chk7' checked onchange='updatecolumn()'/>Length</td></tr>
							<tr><td><input type='checkbox' id='chk8' checked onchange='updatecolumn()'/>Quantity</td></tr>
							<tr><td><input type='checkbox' id='chk9' checked onchange='updatecolumn()'/>Delivery</td></tr>
							<tr><td><input type='checkbox' id='chk10' checked onchange='updatecolumn()'/>Last Mod.</td></tr>
							<tr><td><input type='checkbox' id='chk11' checked onchange='updatecolumn()'/>Status</td></tr>
							
						</table>
					</div>
				</td>
				<td class='tblBlank'></td>
				<td>
					<div id='divcheckbox'>
						<table class='tblcheckbox'>
							<tr>
								<td align='center'>Total Added : <span id='counter'>0</span></td>
							</tr>
						</table>
					</div>
				</td>
				<td>
					<table class='tblCheckBox' width='200px'>
						<tr><td><a href='<?=base_url()."index.php"?>'>Home Screen</a></td></tr>
						<tr><td><input type='button' value='Preview Total Planning' id='btnPreview' onclick='previewTP();'></td></tr>
						<tr><td></td></tr>
						<tr><td><a href="<?=base_url().'index.php/reportplanning/'?>">Report Planning</a></td></tr>
					</table>
				</td>
			</tr>
		</table>
		</div>
	</td>
	
	</tr>
	<tr>
		<td>
			<div id='searchresult'> <h2 align='center' id='titleSearch'>NO search selected</h2><br/></div>
			<div id='div_totalplanning' style='display:none'>
				<?php $tomorrow = mktime(0, 0, 0, date("m"), date("d")+1, date("y"));?>
				<table width='90%'>
					<tr><td><input type='button' value='Save' onclick='saveTP();'/> <span id='lastsavestatus' > Not Saved</span></td>
					<td align='right'><h2 id='titleTP'>Total Planning : &nbsp;&nbsp;</h2></td>
					<td width='110'><input type='text' id='todaydate' value="<?=date('Y-m-d',$tomorrow)?>" class="date-picker"  size="9" /> 
					</td>
					<td><input type='button' onclick='loadPreviousPlan()' value='Load'/></td></tr>
				</table>
				
				<br/>
				<div id='inner_totalplanning' >
				</div>
			</div>
		</td>
	</tr>
</table>


<div id="deliveryHistoryDiv" class="x-hidden">
    <div class="x-window-header">Delivery History</div>
	<div id='deliveryHistoryDetails'>Loading.... </div>
</div>


<?php
function tableTemplate($tblName, $arrayName)
{
	$printdiff = false;
	if(($tblName=='tblDelDate')||($tblName=='tblLastModified')) {
		$printdiff=true;
	}
	
	$output  = "";
	$output .= "<table id='".$tblName."' class='tblCheckBox' width='100%'>";
	foreach($arrayName as $key=>$value)
	{
		$diffvalue="<td></td>";
		if($printdiff)
		{	$day = get_time_difference(date('Y-m-d'),$value);
			$diffvalue= "<td>".$day."</td>";
		}
		$output .= "<tr onclick='sel_Click(this);' ><td>".$value."</td>".$diffvalue."</tr>";
	}
	$output .= "</table>";
	return $output;	
}

function get_time_difference($start,$end)
{
	$uts['start']      =    strtotime( $start );
    $uts['end']        =    strtotime( $end );
    if( $uts['start']!==-1 && $uts['end']!==-1 )
    {
        if( $uts['end'] >= $uts['start'] )
        {
            $diff    =    $uts['end'] - $uts['start'];
            if( $days=intval((floor($diff/86400))) )
                $diff = $diff % 86400;
            $diff    =    intval( $diff );            
            return "+".$days."d";
        }
        else
        {
            $diff    =  $uts['start'] - $uts['end'];
            if( $days=intval((floor($diff/86400))) )
                $diff = $diff % 86400;
            $diff    =    intval( $diff );            
            return "-".$days."d";
        }
    }
    else
    {
        //trigger_error( "Invalid date/time data detected", E_USER_WARNING );
    }
    return( false );
}
?>

<script type='text/javascript'>
	var todayinput = Ext.get('todaydate');
	var df1 = new Ext.form.DateField({"format":'Y-m-d',"altFormats":'j|j/n|j/n/y|j/n/Y|j-M|j-M-y|j-M-Y',"minValue":today});
	df1.applyToMarkup(todayinput);
	loadPreviousPlan();
</script>

