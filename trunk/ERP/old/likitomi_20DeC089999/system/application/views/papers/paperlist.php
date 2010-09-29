<?php
	$firstChar ='';
	$cnt=0;
	$firstdata = 0;$totalRec= count($resultPapers);
	if($totalRec<=0) { 
?>
	<p class="details-info">No Records </p>
<?php 
	}else {
?>
	<table id="cwlistmain" class="cwTable">
<?php
   foreach ($resultPapers as $row)
	{	
		$cnt++;
		if($firstdata==0)$firstdata = $row->paper_id;
		if($code=='grade') $curFirstChar = strtoupper(substr($row->paper_grade,0,2));
		else $curFirstChar = strtoupper(substr($row->paper_code,0,1));
		
		if($firstChar!=$curFirstChar){ 
			$firstChar=$curFirstChar;
?>
<tr onClick=" return goTopPaper();"><td class='rowFirstChar' ><?=$curFirstChar?></td>
<td class='rowFirstChar' align='center'>Grade</td>
<td class='rowFirstChar' align='right' >Name</td></tr>
<?php	
		} 
?>
<tr onmouseover='cwOver(this);' onmouseout='cwOut(this);' class='cwTableRow' onclick='loadPaperDetailFromRow("<?=$row->paper_id?>",this);cw_Click(this);'>
<td>
<?php
		if($action=='search') echo $paper_class->ew_Highlight($row->paper_code,$searchkeyword);
		else echo $row->paper_code;
?>
</td><td align='center'><?=$row->paper_grade?></td><td align='right'><?=$row->paper_name?></td></tr>
<?php } ?></table>
<?php }?>
<?php
if($action=="search") {
	echo "<input type='hidden' id='searchcounter' value='$cnt'/>";
}
?>
<input type='hidden' id='firstitem' value='<?=$firstdata?>' />