<?php 
$jsonData = array();
$cnt=0;
?>
<div id='syncdatadiv'>
<table width='100%'>
	<tr>
		<td><h2>
	<div align=center>Corrugator Clamplift Plan : <?=$plandate?></div>
</h2></td>
	<td align='right'>
		<input type='button' class='button' value='Delete This' onclick="deletethisday('<?=$plandate?>')"/>
	<!--	<span id='syncdatamsg'> <?=$getsynctime?></span>&nbsp;&nbsp;<input type='button' value='Sync Now' onclick='syncplandata()'/>
	--></td>
	</tr>
</table>
<br>
<table>
	<tr class='tdLabel'>
		<td>Start Time</td>
		<td rowspan="2">Sheet Code</td>
		<td>Customer Name</td>
		<td>SO. NO.</td>
		<td rowspan="2">F</td>
		<td>Paper </td>
		<td>B-L</td>
		<td>B-M</td>
		<td rowspan="2">Paper Width </td>
		<td>Used (L) </td>
		<td>B-L</td>
		<td>B-M</td>
		<td>Used (Kgs) </td>
		<td>B-L</td>
		<td>B-M</td>
		<td>Used (Kgs) </td>
		<td>B-L</td>
		<td>B-M</td>
		<td rowspan="2">Sheet Length</td>
		<td>Case</td>
		<td>Actual </td>
		<td>B-L</td>
		<td>B-M</td>
	</tr>
	<tr class='tdLabel'>
		<td>Stop Time</td>
		<td>Product </td>
		<td>ORD NO.</td>
		<td>D-F</td>
		<td>C-L</td>
		<td>C-M</td>
		<td>D-F</td>
		<td>C-L</td>
		<td>C-M</td>
		<td>D-F</td>
		<td>C-L</td>
		<td>C-M</td>
		<td>D-F</td>
		<td>C-L</td>
		<td>C-M</td>
		<td>Cut</td>
		<td>D-F</td>
		<td>C-L</td>
		<td>C-M</td>
	</tr>	
	
	<?php
	$cnt=0;
	foreach ($resultCorrugatorClamplift->result() as $key)
	{	
		$jsonData[$cnt]['start_time'] 		= substr($key->start_time,0,5);
		$jsonData[$cnt]['stop_time'] 		= substr($key->stop_time,0,5);
		$jsonData[$cnt]['product_code'] 	= $key->product_code;
		$jsonData[$cnt]['partner_name'] 	= $key->partner_name;
		$jsonData[$cnt]['product_name']		= $key->product_name;
		$jsonData[$cnt]['sales_order'] 		= $key->sales_order;
		$jsonData[$cnt]['flute'] 			= $key->flute;
		$jsonData[$cnt]['DF'] 				= $key->DF;
		$jsonData[$cnt]['BL'] 				= $key->BL;
		$jsonData[$cnt]['BM'] 				= $key->BM;
		$jsonData[$cnt]['CL'] 				= $key->CL;
		$jsonData[$cnt]['CM']				= $key->CM;
		$jsonData[$cnt]['p_width_mm'] 		= $key->p_width_mm;
		$jsonData[$cnt]['p_width_inch'] 	= $key->p_width_mm;
		$jsonData[$cnt]['used_df'] 			= $key->used_df;
		$jsonData[$cnt]['used_bl'] 			= $key->used_bl;
		$jsonData[$cnt]['used_bm'] 			= $key->used_bm;
		$jsonData[$cnt]['used_cl'] 			= $key->used_cl;
		$jsonData[$cnt]['used_cm'] 			= $key->used_cm;
		$jsonData[$cnt]['used_df_lkg'] 		= $key->used_df_lkg;
		$jsonData[$cnt]['used_bl_lkg'] 		= $key->used_bl_lkg;
		$jsonData[$cnt]['used_bm_lkg'] 		= $key->used_bm_lkg;
		$jsonData[$cnt]['used_cl_lkg'] 		= $key->used_cl_lkg;
		$jsonData[$cnt]['used_cm_lkg'] 		= $key->used_cm_lkg;
		$jsonData[$cnt]['used_df_mkg'] 		= $key->used_df_mkg;
		$jsonData[$cnt]['used_bl_mkg'] 		= $key->used_bl_mkg;
		$jsonData[$cnt]['used_bm_mkg'] 		= $key->used_bm_mkg;
		$jsonData[$cnt]['used_cl_mkg'] 		= $key->used_cl_mkg;
		$jsonData[$cnt]['used_cm_mkg'] 		= $key->used_cm_mkg;
		$jsonData[$cnt]['t_length']			= $key->t_length;
		$jsonData[$cnt]['case']				= $key->case;
		$jsonData[$cnt]['autoid']			= $key->autoid;
		$jsonData[$cnt]['cut']				= $key->cut;
		
		$cnt++;
		
		
	
	?>
	<tr class='tdView'>
		<td><?=substr($key->start_time,0,5)?></td>
		<td rowspan="2"><?=$key->product_code?></td>
		<td nowrap><?=$key->partner_name?></td>
		<td><?=$key->sales_order?></td>
		<td rowspan="2"><?=$key->flute?></td>
		<td class='blankTbl'></td>
		<td><?=$key->BL?></td>
		<td><?=$key->BM?></td>
		<td><?=$key->p_width_mm?></td>
		<td class='blankTbl'></td>
		<td><?=$key->used_bl?></td>
		<td><?=$key->used_bm?></td>
		<td>ACTUAL</td>
		<td><?=$key->used_bl_lkg?></td>
		<td><?=$key->used_bm_lkg?></td>	
		<td>+LOSS</td>
		<td><?=$key->used_bl_mkg?></td>
		<td><?=$key->used_bm_mkg?></td>
		<td><?=$key->t_length?></td>
		<td><?=$key->case?></td>
		<td class='blankTbl'></td>
		<td>2</td>
		<td>5</td>
	</tr>
	<tr class='tdView'>
		<td><?=substr($key->stop_time,0,5)?></td>
		<td ><?=$key->product_name?></td>
		<td><?=$key->autoid?></td>
		<td><?=$key->DF?></td>
		<td><?=$key->CL?></td>
		<td><?=$key->CM?></td>
		<td><?=$key->p_width_inch?></td>
		<td><?=$key->used_df?></td>
		<td><?=$key->used_cl?></td>
		<td><?=$key->used_cm?></td>
		<td><?=$key->used_df_lkg?></td>
		<td><?=$key->used_cl_lkg?></td>
		<td><?=$key->used_cm_lkg?></td>
		<td><?=$key->used_df_mkg?></td>
		<td><?=$key->used_cl_mkg?></td>
		<td><?=$key->used_cm_mkg?></td>
		<td class='blankTbl'></td>
		<td><?=$key->cut?></td>
		<td>3</td>
		<td>4</td>
		<td>6</td>
	</tr>
	<?php 
	} ?>
</table>
</div>
<div id='jsondata' style="display:none;">
	<?php 
	echo '{"clamplift" :'.$this->json->encode($jsonData).',"opdate":"'.$plandate.'"}';
	?>
	
</div>

<?php

function getGrade($machine)
{
	$charArray = str_split($machine);
	$grade = "";
	foreach ($charArray as $c)
	{
		if(ctype_digit($c)) 
		{
			$grade .= $c;
		}
	}
	return parseInt($grade);
}

function parseInt($string) {
	// return intval($string);
	if(preg_match('/(\d+)/', $string, $array)) {
		return $array[1];
	} else {
		return 0;
	}
} 

function formatDate($day)
{
	$hour  = floor($day*24); 
	$min   = floor((($day*24)-$hour)*60); 
	$time  = ($hour<10)?"0".$hour:$hour;//
	$time .= ":";
	$time .= ($min<10)?"0".$min:$min;
	return $time;
}

?>
