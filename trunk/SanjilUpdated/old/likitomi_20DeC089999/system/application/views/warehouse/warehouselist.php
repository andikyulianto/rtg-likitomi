<?php
	$cnt=0;
	$firstdata = 0;
	$totalRec= count($resultWarehouse);
	if($totalRec<=0) { 
?>
	<p class="details-info">No Records </p>
<?php 
	}else {
?>
	<table id="cwlistmain" class="cwTable">
		<tr><td class='rowFirstChar'>Invoice Number</td><td class='rowFirstChar'>Invoice Date</td> </tr>
<?php
   foreach ($resultWarehouse as $row)
	{	
		$cnt++;
		if($firstdata==0)$firstdata = $row->invoice_no;
?>
<tr onmouseover='cwOver(this);' onmouseout='cwOut(this);' class='cwTableRow' onclick='loadWarehouseDetailFromRow("<?=$row->invoice_no?>",this);cw_Click(this);'>
<td>
<?php
	if($action=='search') echo $warehouse_class->ew_Highlight($row->invoice_no,$searchkeyword);
	else echo $row->invoice_no;
?>
</td>
<td><?=$row->invoice_date?></td>
</tr>
<?php } ?></table>
<?php }?>
<input type='hidden' id='firstitem' value='<?=$firstdata?>' />