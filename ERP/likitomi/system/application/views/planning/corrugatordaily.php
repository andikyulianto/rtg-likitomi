<h2>
	<div align=center>Corrugator Daily Plan : <?=$plandate?></div>
</h2>
<br>
<table>
	<tr class='tdLabel'>
		<td rowspan="2">Time*</td>
		<td rowspan="2">Sheet Code</td>
		<td>Customer Name</td>
		<td>SO. NO.</td>
		<td rowspan="2">F</td>
		<td class='noborder'>Paper </td>
		<td>B-L</td>
		<td>B-M</td>
		<td class='noborder'>Used </td>
		<td>B-L*</td>
		<td>B-M*</td>
		<td rowspan="2">Paper Width</td>
		<td rowspan="2">Sheet Length</td>
		<td>Case*</td>
		<td rowspan="2">Blank</td>
		<td rowspan="2">Slit</td>
		<td rowspan="2" colspan="3">Scoreline</td>
		<td rowspan="2">Trim*</td>
		<td rowspan="2">Metre*</td>
		<td>LKGS *</td>
		<td rowspan="2">S/B</td>
		<td>Del.Date</td>
		<td rowspan="2" colspan="5">SCORER</td>
		
	</tr>
	<tr class='tdLabel'>
		<td>Product </td>
		<td>ORD NO.</td>
		<td>D-F</td>
		<td>C-L</td>
		<td>C-M</td>
		<td>D-F*</td>
		<td>C-L*</td>
		<td>C-M*</td>
		<td>Cut*</td>
		<td>MKG*</td>
		<td>Next Process</td>
	</tr>	
	
	<?php
	$cnt=0; $S1=$S2=$S3=0;
	$firstTime = (0.0006949*60)*8+(0.0006949*0);
	$timeStart = $firstTime;
	foreach ($resultCorrugatorDaily->result() as $key)
	{
		$cnt++;
		$S1 = $key->scoreline_f;
		$S2 = $key->scoreline_d;
		$S3 = $key->scoreline_f2;
		
		$case 	= $key->qty;
                if(($key->slit)!=0)
		$cut2 	= $case/$key->slit;
		$used_df = ($key->t_length*$cut2)/1000;
		$used_bl = ($key->BL=="")?"":($key->t_length*$cut2)/1000;
		$used_cl = ($key->CL=="")?"":($key->t_length*$cut2)/1000;
		
		$used_bm = ($key->BM=="")?"":(($key->t_length*$cut2)/1000)*1.36;
		$used_cm = ($key->CM=="")?"":(($key->t_length*$cut2)/1000)*1.48;
		
		$p_width_inch = $key->p_width_mm/25.6 ; //Adopted From Lotus File
		
		$trim	= ($key->p_width_mm - $key->blank*$key->slit);
		$metre	= ($key->t_length*$cut2)/1000; 
		
		$lkg	= $key->p_width_mm * $used_df * getGrade($key->DF) / 1000000;
		
		if($used_cm =="")
		{
			if($used_bm=="")
			{
				$mkg = "";
			}
			else $mkg = $key->p_width_mm * $used_bm * getGrade($key->BM) / 1000000;
		}
		else 
		{
			$mkg = $key->p_width_mm * $used_cm * getGrade($key->CM) / 1000000;
			
		}
		
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
		
		//Scorelines
			$A = 0;
			$B = 0;
			$C = 0;
			$D = 0;
			$E = 0;
			$F = 0;
			$G = 0;
			$H = 0;
		switch($key->slit)
		{
			case 1:
				$A = $S1 + ($S2+$S3)/2;
				$B = $S2 / 2;
				break;
			case 2:
				$A = $S1 + $S2 + $S3 ;
				$B = $S3;
				$D = $S2 + $S3;
				break;
			case 3:
				$A = $S1 + $S2 / 2  ;
				$B = $S2/2;
				$C = $S1 + $S2/2 + $S1 + $S2 + $S3;
				$D = $S2/2 + $S1 + $S3;
				$F = $S2/2 + $S1 + $S2 + $S3;
				$D = $S2 + $S3;
				break;
			case 4:
				$A = $S1 + $S2 + $S3 ;
				$B = $S3;
				$C = ($S1 + $S2 + $S3)*2;
				$D = $S2 + $S3;
				$F = $S3 + $S2 + $S1 + $S3;
				$H = $S3 + $S2 + $S1 + $S3 + $S2;
				break;			 
		}
	
	?>
	<tr class='tdView'>
		<td rowspan="2"><?=formatDate($timeStart)?>-<?=formatDate($timeStop)?></td>
		<td rowspan="2"><?=$key->product_code?></td>
		<td nowrap><?=$key->partner_name?></td>
		<td><?=$key->sales_order?></td>
		<td rowspan="2"><?=$key->flute?></td>
		<td class='blankTbl'></td>
		<td><?=$key->BL?></td>
		<td><?=$key->BM?></td>
		<td class='blankTbl'></td>
		<td><?=round($used_bl)?></td>
		<td><?=round($used_bm)?></td>
		<td><?=$key->p_width_mm?></td>
		<td><?=$key->t_length?></td>
		<td><?=round($case)?></td>
		<td rowspan="2"><?=$key->blank?></td>	
		<td rowspan="2"><?=$key->slit?></td>
		<td rowspan="2"><?=$key->scoreline_f?></td>
		<td rowspan="2"><?=$key->scoreline_d?></td>
		<td rowspan="2"><?=$key->scoreline_f2?></td>
		<td rowspan="2"><?=round($trim)?></td>
		<td rowspan="2"><?=round($metre)?></td>
		<td><?=round($lkg)?></td>
		<td td rowspan="2" class='blankTbl'></td>
		<td><?=$key->delivery_date?></td>
		<td><?=round($G)?></td><td><?=round($E)?></td><td><?=round($C)?></td><td><?=round($A)?></td><td>CL</td>
		
	</tr>
	<tr class='tdView'>
		<td><?=$key->product_name?></td>
		<?php $path = "/planning/barcode/".$key->autoid."/"; ?> 
		<td ><img src=<?php echo site_url($path)?>/><br> <?=$key->autoid ?></td> 
		<td><?=$key->DF?></td>
		<td><?=$key->CL?></td>
		<td><?=$key->CM?></td>
		<td><?=round($used_df)?></td>
		<td><?=round($used_cl)?></td>
		<td><?=round($used_cm)?></td>
		<td><?=round($p_width_inch)?></td>
		<td class='blankTbl'></td>
		<td><?=round($cut2)?></td>
		<td><?=round($mkg)?></td>
		<td><?=$key->next_process?></td>
		<td><?=round($H)?></td><td><?=round($F)?></td><td><?=round($D)?></td><td><?=round($B)?></td><td></td>
	</tr>
	
	<?php
	$timeStart = $timeStop; } ?>
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
<br/>
* Auto Generated
