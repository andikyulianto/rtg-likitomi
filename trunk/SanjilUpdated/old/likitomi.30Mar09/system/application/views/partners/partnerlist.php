<?php
	$firstChar ='';
	$cnt=0;
	$firstdata = 0;$totalRec= count($resultPartners);
	if($totalRec<=0) { 
?>
	<p class="details-info">No Records </p>
<?php 
	}else {
?>
	<table id="cwlistmain" class="cwTable">
<?php
   foreach ($resultPartners as $row)
	{	
		$cnt++;
		if($firstdata==0)$firstdata = $row->partner_id;
		$curFirstChar = strtoupper(substr($row->partner_name,0,1));
		if($firstChar!=$curFirstChar){ 
			$firstChar=$curFirstChar;
?>
<tr onClick=" return goTopPaper();"><td class='rowFirstChar' onClick=" return goTop();"><?=$curFirstChar?></td></tr>
<?php	} ?>
<tr onmouseover='cwOver(this);' onmouseout='cwOut(this);' class='cwTableRow' onclick='loadPartnerDetailFromRow("<?=$row->partner_id?>",this);cw_Click(this);'>
<td>
<?php
	if($action=='search') echo $partner_class->ew_Highlight($row->partner_name,$searchkeyword);
	else echo $row->partner_name;
?>
</td></tr>
<?php } ?></table>
<?php }?>
<?php
if($action=="search") {
	echo "<input type='hidden' id='searchcounter' value='$cnt'/>";
}
?>
<input type='hidden' id='firstitem' value='<?=$firstdata?>' />