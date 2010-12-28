
<h2>
	<div align=center>Corrugator Clamplift Plan : <?=$plandate?></div>
</h2>
<br>
<table>
	<tr class='tdLabel'>
		<td rowspan="2">Time</td>
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
		
	</tr>
	<tr class='tdLabel'>
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
	</tr>	
	
	<?php
	$cnt=0;
	$firstTime = (0.0006949*60)*8+(0.0006949*0);
	$timeStart = $firstTime;
	foreach ($resultCorrugatorClamplift->result() as $key)
	{
		$cnt++;
		
		$case 	= $key->qty;
                if(($key->slit)!=0)
		$cut2 	= $case/$key->slit;
		$used_df = ($key->t_length*$cut2)/1000;
		$used_bl = ($key->BL=="")?"":($key->t_length*$cut2)/1000;
		$used_cl = ($key->CL=="")?"":($key->t_length*$cut2)/1000;
		
		$used_bm = ($key->BM=="")?"":(($key->t_length*$cut2)/1000)*1.36;
		$used_cm = ($key->CM=="")?"":(($key->t_length*$cut2)/1000)*1.48;
		
		$p_width_inch = $key->p_width_mm/25.6 ; //Adopted From Lotus File
		
		$metre	= ($key->t_length*$cut2)/1000; 
		$timeuse = 0;
		if((strtoupper($key->flute)=="B")||(strtoupper($key->flute)=="C"))
		{
			$timeuse = ($metre/120)+4;
		}
		else if((strtoupper($key->flute)=="BC")||(strtoupper($key->flute)=="W"))
		{
			$timeuse = ($metre/100)+4;
		}
		else $timeuse = 0;
		
		$timeStop = $timeStart;
		//=IF(AD7=0,0,(A6+(AD7*0.0006949)))
		if($timeuse!=0)
		{
			$timeStop = $timeStart + $timeuse * 0.0006949;
		}
		//IF(A7>=(0.0006949*0*11.5),IF(A7<=(0.0006949*0*12.5),(A7)+(0.0006949*0),A7),A7)

		$used_df_lkg = $key->p_width_mm  * $used_df * getGrade($key->DF) / 1000000;
		$used_bl_lkg = $key->p_width_mm  * $used_bl * getGrade($key->BL) / 1000000; 
		$used_cl_lkg = $key->p_width_mm  * $used_cl * getGrade($key->CL) / 1000000; 
		
		$used_bm_lkg = $key->p_width_mm  * $used_bm * getGrade($key->BM) / 1000000; 
		$used_cm_lkg = $key->p_width_mm  * $used_cm * getGrade($key->CM) / 1000000; 
		
		$used_df_mkg = $used_df_lkg * 1.03;
		$used_bl_mkg = $used_bl_lkg * 1.03;
		$used_cl_mkg = $used_cl_lkg * 1.03;
		$used_bm_mkg = $used_bm_lkg * 1.03;
		$used_cm_mkg = $used_cm_lkg * 1.03;
		
	
	?>
	<tr class='tdView'>
		<td rowspan="2"><?=formatDate($timeStart)?></td>
		<td rowspan="2"><?=$key->product_code?></td>
		<td nowrap><?=$key->partner_name?></td>
		<td><?=$key->sales_order?></td>
		<td rowspan="2"><?=$key->flute?></td>
		<td class='blankTbl'></td>
		<td><?=$key->BL?></td>
		<td><?=$key->BM?></td>
		<td><?=$key->p_width_mm?></td>
		<td class='blankTbl'></td>
		<td><?=round($used_bl)?></td>
		<td><?=round($used_bm)?></td>
		<td>ACTUAL</td>
		<td><?=round($used_bl_lkg)?></td>
		<td><?=round($used_bm_lkg)?></td>	
		<td>+LOSS</td>
		<td><?=round($used_bl_mkg)?></td>
		<td><?=round($used_bm_mkg)?></td>
		<td><?=$key->t_length?></td>
		<td><?=round($case)?></td>
	</tr>
	<tr class='tdView'>
		<td><?=$key->product_name?></td>
		<!--MO number; Barcode will be added here--> 
		<!--<td><?=$key->autoid?></td>-->
		<?php $path = "/planning/barcode/".$key->autoid."/"; ?> 
		<td ><img src=<?php echo site_url($path)?>/><br> <?=$key->autoid ?></td> 

		
		<td><?=$key->DF?></td>
		<td><?=$key->CL?></td>
		<td><?=$key->CM?></td>
		<td><?=$key->p_width_inch?></td>
		<td><?=round($used_df)?></td>
		<td><?=round($used_cl)?></td>
		<td><?=round($used_cm)?></td>
		<td><?=round($used_df_lkg)?></td>
		<td><?=round($used_cl_lkg)?></td>
		<td><?=round($used_cm_lkg)?></td>
		<td><?=round($used_df_mkg)?></td>
		<td><?=round($used_cl_mkg)?></td>
		<td><?=round($used_cm_mkg)?></td>
		<td class='blankTbl'></td>
		<td><?=round($cut2)?></td>
		
	</tr>
	
	<?php 
	$timeStart = $timeStop;} ?>
</table>
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
