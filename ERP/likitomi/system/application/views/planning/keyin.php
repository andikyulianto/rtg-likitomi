<h2>
	<div align=center>Order Key In : <?=$plandate?></div>
</h2>
<br>
<table>
	<tr class='tdLabel'>
		<td>Start</td>
		<td>SO.NO</td>
		<td>Prod</td>
		<td>Customer Name</td>
		<td>Amount</td>
		<td>P.Width</td>
		<td>Blank</td>
		<td>T.Length</td>
		<td colspan='3'>Score Line</td>
		<td>F</td>
		<td colspan='5'>Paper Combination</td>
		<td>Del Date</td>
		<td>M2/pcs</td>
		<td rowspan="2">Delivery Remarks</td>
		<td rowspan="2">Paper Catalog Remarks</td>
		<td rowspan="2">Sales Order Remarks</td>
	</tr>
	<tr class='tdLabel'>
		<td>Stop</td>
		<td>Order No</td>
		<td>Code</td>
		<td>Product Name</td>
		<td>Cut*</td>
		<td>Slit</td>
		<td></td>
		<td>Cut</td>
		<td>F</td><td>D</td><td>F</td>
		<td>S/B</td>
		<td>DF</td><td>BM</td><td>BL</td><td>CM</td><td>CL</td>
		<td>Next</td>
		<td>Total</td>
		
	</tr>
	
	
	<?php
	$cnt=0;
	$firstTime = (0.0006949*60)*8+(0.0006949*0);
	$timeStart = $firstTime;
	foreach ($resultKeyin->result() as $key)
	{
		$cnt++;
		//FORMULA
                if(($key->cut*$key->slit*1000000)!=0)
		$m2 = ($key->p_width_inch*25.4*$key->t_length)/($key->cut*$key->slit*1000000);
		$total = $m2*$key->qty; 
                if(($key->cut*$key->slit)!=0)
		$cut2 = $key->qty/($key->cut*$key->slit);
		
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
	
	?>
	<tr class='tdView'>
		<td><?=formatDate($timeStart)?></td>
		<td><?=$key->sales_order?></td>
		<td><?=$key->product_code?></td>
		<td nowrap><?=$key->partner_name?></td>
		<td><?=$key->qty?></td>
		<td><?=$key->p_width_inch?></td>
		<td><?=$key->blank?></td>
		<td><?=$key->t_length?></td>
		<td colspan='3'  class='blankTbl'></td>
		<td><?php if($key->flute=="BC") echo "W";else echo $key->flute;?></td>
		<td colspan='5'  class='blankTbl'></td>
		<td><?=$key->delivery_date?></td>
		<td><?=round($m2,3)?></td>
		<td rowspan="2"><?=$key->D_remarks?></td>
		<td rowspan="2"><?=$key->PC_remarks?></td>
		<td rowspan="2"><?=$key->SO_remarks?></td>
	</tr>
	<tr class='tdView'>
		<td></td>
		<?php $path = "/planning/barcode/".$key->autoid."/"; ?> 
		<td ><img src=<?php echo site_url($path)?>/><br> <?=$key->autoid ?></td> 
		<td class='blankTbl'></td>
		<td><?=$key->product_name?></td>
		<td><?=round($cut2)?></td>
		<td><?=$key->slit?></td>
		<td class='blankTbl'></td>
		<td><?=$key->cut?></td>
		<td><?=$key->scoreline_f?></td><td><?=$key->scoreline_d?></td><td><?=$key->scoreline_f2?></td>
		<td class='blankTbl'></td>
		<td><?=$key->DF?></td>
		<td><?=$key->BM?></td>
		<td><?=$key->BL?></td>
		<td><?=$key->CM?></td>
		<td><?=$key->CL?></td>
		<td><?=$key->next_process?></td>
		<td><?=round($total)?></td>
	</tr>
	<?php
	$timeStart = $timeStop;
	 } ?>
</table>
<br/>
* Auto Generated

<?php 

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
