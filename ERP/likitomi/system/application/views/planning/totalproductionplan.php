<h2>
	<div align=center>Total Production Plan : <?=$plandate?></div>
</h2>
<br>
<table>
	  <tr class='tdLabel'>
	    <td rowspan="3">SO.NO.</td>
	    <td rowspan="3">PO.NO</td>
	    <td colspan="2" rowspan="2">Product Code </td>
	    <td rowspan="3">Company</td>
	    <td rowspan="3">Product Name </td>
	    <td colspan="3" rowspan="2">Product. Spec </td>
	    <!-- <td rowspan="3">SQM. M2 * </td> -->
	    <td colspan="2" rowspan="2">Amount</td>
	    <td colspan="8" align="center">Production Plan </td>
	    <td rowspan="3">ACTUAL</td>
	    <td rowspan="3">REMARK</td>
	    <!--<td rowspan="3">Delivery Remarks</td>
	    <td rowspan="3">Paper Catalog Remarks</td>
	    <td rowspan="3">SO. Remarks</td>-->
	  </tr>
	  <tr class='tdLabel'>
	    <td colspan="2">Delivery</td>
	    <td colspan="3">Corrugator</td>
	    <td colspan="3">Convertor</td>
	  </tr>
	  <tr class='tdLabel'>
	    <td>Code</td>
	    <td>MC</td>
	    <td>P.W</td>
	    <td>Length</td>
	    <td>F</td>
	    <!--<td>Cut </td>-->
	    <td>PCS</td>
	    <td>ALW +/- </td>
	    <td>Date</td>
	    <td>Amount</td>
	    <td>Date</td>
	    <td>Amount</td>
	    <td>Time*</td>
	    <td>Date</td>
	    <td>Amount</td>
	    <td>Time*</td>
	  </tr>

	<?php
	$cnt=0;
	
			//assign constants of machine speed
	foreach ($machine->result() as $key)
	{
			
			if($key->machine_name == "2CL")
				$speed_2cl = $key->speed;
			if($key->machine_name == "3CM")
				$speed_3cm = $key->speed;
			if($key->machine_name == "3CS")
				$speed_3cs = $key->speed;
			if($key->machine_name == "3CL")
				$speed_3cl = $key->speed;
			if($key->machine_name == "4CD")
				$speed_4cd = $key->speed;
			if($key->machine_name == "GH")
				$speed_gh = $key->speed;
			if($key->machine_name == "HS")
				$speed_hs = $key->speed;
			if($key->machine_name == "FG")
				$speed_fg = $key->speed;
			if($key->machine_name == "RD")
				$speed_rd = $key->speed;
			if($key->machine_name == "SS")
				$speed_ss = $key->speed;
			if($key->machine_name == "remove")
				$speed_remove = $key->speed;
			if($key->machine_name == "foam")
				$speed_foam = $key->speed;
			if($key->machine_name == "tape")
				$speed_tape = $key->speed;
			
			
	}
	foreach ($resultTotalProductionPlan->result() as $key)
	{
		$cnt++;
		//FORMULA
                if(($key->cut*1000000*$key->slit)!=0)
		{
		$sqm = ($key->p_width_inch*25.4*$key->cr_length)/($key->cut*1000000*$key->slit);
		$sqm = round($sqm,3);
	}
		$case 	= $key->qty;
		if(($key->slit)!=0)
			$cut2 	= $case/$key->slit;
		$metre	= ($key->cr_length*$cut2)/2000;
		if((strtoupper($key->flute) =="B") or (strtoupper($key->flute)=="C"))
		{
			$timeuseCR = ($metre/120)+4;
		}
		else if((strtoupper($key->flute)=="BC") or (strtoupper($key->flute)=="W"))
		{
			$timeuseCR = ($metre/100)+4;
		}
		
				$mch ="";
		$speed =1;
			if($key->req_2cl)
			{
				$mch = "2CL ";
				$speed =$speed_2cl." ";
			}	
			if($key->req_3cm)
			{
				$mch = "3CM ";
				$speed =$speed_3cm." ";
			}
			if($key->req_3cs)
			{
				$mch = "3CS ";
				$speed =$speed_3cs." ";
			}
			if($key->req_3cl)
			{
				$mch = "3CL ";
				$speed =$speed_3cl." ";
			}
			if($key->req_4cd)
			{
				$mch = "4CD ";
				$speed =$speed_4cd." ";
			}
			
	$timecvused = $key->qty/$speed;
	
	
	
	
	?>
	<tr class='tdView'>
		<td><?=$key->sales_order?></td>
		<td><?=$key->purchase_order_no?></td>
		<td><?=$key->product_code?></td>
		<?php if($key->req_2cl==1) echo "<td>2CL</td>" ?>
		<?php if($key->req_3cm==1) echo "<td>3CM</td>" ?>
		<?php if($key->req_3cs==1) echo "<td>3CS</td>" ?>
		<?php if($key->req_3cl==1) echo "<td>3CL</td>" ?>
		<?php if($key->req_4cd==1) echo "<td>4CD</td>" ?>
		<td nowrap><?=$key->partner_name?></td>
		<td nowrap><?=$key->product_name?></td>
		<td><?=$key->paper_width_mm?><br/><?=$key->pc_paper_width?></td>
		<td><?=$key->length?></td>
		<td><?=$key->flute?></td>
		<!--<td><?=$key->cut?></td>-->
		<!--<td><?=$sqm?></td>-->
		<td><?=$key->qty?></td>
		<td><?=$key->qty_allowance?></td>
		<td><?=$key->delivery_date?></td>
		<td><?=$key->qty?></td>
		<td><?=$key->corrugator_date?></td>
		<td><?=$key->qty_cr?></td>
		<td><?=$timeuseCR?></td>
		<td><?=$key->converter_date?></td>
		<td><?=$key->qty_cv?></td>
		<td><?=round($timecvused,1)?></td>
		<td><?=$key->D_remarks?></td>
		<td></td>
		<!--<td><?=$key->PC_remarks?></td>
		<td><?=$key->SO_remarks?></td>-->
	</tr>
	
	<?php } ?>
</table>
<br/>
*Auto Calculated
