<script type='text/javascript' >
/**
 * @author sanjilshrestha
 */
	var alltables = new Array("tblInvoice","tblPaperCode","tblSuppliers","tblInvoiceDate","tblMovementDate");
	var LOADING_TEXT	= "<?=$this->lang->line('ajax_loading_warehouse')?>";
	
	window.onload = function() {
		logoutTips();
	}
	
	function sel_SetColor(row) 
	{
		row.className = (row.selected)?"selectedRow":"";
	}
	
	function sel_Click(row)
	{
		var table = getParent(row, 'TABLE');        
        if (!document.getElementById('chkmultiplecol').checked) {
            clearTableAllExcept(table.id);
        }
        if (!document.getElementById('chkmultiplerow').checked) {
            clearTable(table.id);
        }
        row.selected = !row.selected;
		sel_SetColor(row);
		postTable(table.id);
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
            if (tblName != alltables[i]) {
				clearTable(alltables[i]);
            }
		}
	}
	
	function postTable(tblName){
		var invoice_all		= new Array();
		var papercode_all 	= new Array();
		var supplier_all 	= new Array();
		var invoicedate_all	= new Array();
		var movement_all	= new Array();
		
		var query_mode = 0;
		if(document.getElementById('chkhistory').checked) query_mode=1;
		var table = document.getElementById(alltables[0]);
		var cnt = 0; 
		for (var i = 0; i < table.rows.length; i++) 
		{
			var thisrow = table.rows[i];
			if (thisrow.selected) {
				invoice_all[cnt++] = thisrow.cells[0].innerHTML;
			}	
		}
		cnt = 0; 
		var table = document.getElementById(alltables[1]);
		for (var i = 0; i < table.rows.length; i++) 
		{
			var thisrow = table.rows[i];
			if (thisrow.selected) {
				papercode_all[cnt++] = thisrow.cells[0].innerHTML;
			}	
		}
		cnt = 0;
		var table = document.getElementById(alltables[2]);
		for (var i = 0; i < table.rows.length; i++) 
		{
			var thisrow = table.rows[i];
			if (thisrow.selected) {
				supplier_all[cnt++] = thisrow.cells[0].id;
			}	
		}
		cnt = 0;
		var table = document.getElementById(alltables[3]);
		for (var i = 0; i < table.rows.length; i++) 
		{
			var thisrow = table.rows[i];
			if (thisrow.selected) {
				invoicedate_all[cnt++] = thisrow.cells[0].innerHTML;
			}	
		}
		cnt = 0;
		var table = document.getElementById(alltables[4]);
		for (var i = 0; i < table.rows.length; i++) 
		{
			var thisrow = table.rows[i];
			if (thisrow.selected) {
				movement_all[cnt++] = thisrow.cells[0].innerHTML;
			}	
		}
		//Ajax Load
		Ext.Ajax.request({
			url: BASEURL + 'index.php/stock/filter/',
			params : { 
				invoice_all		: JSON.stringify(invoice_all),
				papercode_all	: JSON.stringify(papercode_all),
				supplier_all 	: JSON.stringify(supplier_all),
				invoicedate_all	: JSON.stringify(invoicedate_all),
				movement_all	: JSON.stringify(movement_all),
				query_mode		: query_mode,
			},
			success: function ( result, request ) { 
				document.getElementById('searchresult').innerHTML = result.responseText;			
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});	
		Ext.Ajax.on({
		    'beforerequest': function(){
				loadAjax(LOADING_TEXT);
			},
		    'requestcomplete': function(){
				unloadAjax();
			}
		});
	}
	
</script>
<div id="topheader"></div>
<table class='tblcontainer' border='0' width='100%' height='100%' cellspacing="0" cellpadding="0">
	<tr>
    <td colspan=2 class='headertop'>
        <div id='headbar'>
            <table border=0 width=100% >
            	<tr>
            		<td width='240'>
	            		<ul class="primary-links">
            				<li><a href='<?=base_url()."index.php"?>'>Home</a></li>
							<li><a href='<?=base_url()."index.php/warehouse/"?>'>Warehouse</a></li>
							<li><span>Paper Stock</span></li>
						</ul>
					</td>  
					<td align='center'></td>                 
					<td width='40'><a href='<?=base_url()."index.php/auth/logout"?>' id='tip-logout'>
						<img src='<?=base_url()."static/images/logout.png"?>' />
					</a></td>
				</tr>
            </table>
        </div>
    </td>
	</tr>
	<tr>
		<td valign='top'>
			<div id="flashMessage" style="display:none;"></div>
<div id='topfilterdiv'></div>	
<table width="100%">
	<tr><td height='160px'>
		<div id='headbar2'> 		
		<table>
			<tr>
				<td></td><td align='center'><span class='spantitle'>Config</span></td>
				<td></td><td align='center'><span class='spantitle'>Invoice</span></td>
				<td></td><td align='center'><span class='spantitle'>Paper Code</span></td>
				<td></td><td align='center'><span class='spantitle'>Suppliers</span></td>
				<td></td><td align='center'><span class='spantitle'>Invoice Date</span></td>
				<td></td><td align='center'><span class='spantitle'>Movement Date</span></td>
			</tr>
			<tr>
				<td class='tblBlank'></td>
				<td><div id='divcheckbox'>
						<table class='tblcheckbox'>
							<tr><td><input type='checkbox' id='chkmultiplerow'/>Multiple Row</td></tr>
							<tr><td><input type='checkbox' id='chkmultiplecol'/>Multiple Column</td></tr>
							<tr><td><input type='checkbox' id='chkhistory' checked/>History</td></tr>
						</table>
					</div>
				</td>
				<td class='tblBlank'></td>
				<td>
					<div id='divcheckbox'>						
						<?=tableTemplate("tblInvoice",$invoiceArray);?>
					</div>
				</td>
				<td class='tblBlank'></td>
				<td>
					<div id='divcheckbox'>					
						<?=tableTemplate("tblPaperCode",$paperCodeArray);?>
					</div>
				</td>
				<td class='tblBlank'></td>
				<td>
					<div id='divcheckbox'>					
						<?=tableTemplate("tblSuppliers",$suppliersArray);?>
					</div>
				</td>
				<td class='tblBlank'></td>
				<td>
					<div id='divcheckbox'>					
						<?=tableTemplate("tblInvoiceDate",$invoiceDateArray);?>
					</div>
				</td>
				<td class='tblBlank'></td>
				<td>
					<div id='divcheckbox'>					
						<?=tableTemplate("tblMovementDate",$movementDateArray);?>
					</div>
				</td>
			</tr>
		</table>
		</div>
	</td>
	
	</tr>
	<tr>
		<td>
			<div id='searchresult'> 
				<h2 align='center' id='titleSearch'>NO search selected</h2><br/>
			</div>
		</td>
	</tr>
</table>	
		</td>
	</tr>
</table>

<?php
function tableTemplate($tblName, $arrayName)
{
	$printdiff = false;
	if($tblName=='tblMovementDate') {
		$printdiff=true;
	}
	if($tblName=='tblInvoiceDate') {
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
		if($value != "")
		$output .= "<tr onclick='sel_Click(this);' ><td";
		if($tblName=='tblSuppliers') $output .= " id='".$key."' ";
		$output .= ">".$value."</td>".$diffvalue."</tr>";
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

