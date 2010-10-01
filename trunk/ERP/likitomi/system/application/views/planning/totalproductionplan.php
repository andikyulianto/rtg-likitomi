<h2>
	<div align=center>Total Production Plan : <?=$plandate?></div>
</h2>
<br>
<table>
	  <tr class='tdLabel'>
	    <td rowspan="3">SO.NO.</td>
	    <td rowspan="3">PO.NO</td>
	    <td rowspan="3">Product Code </td>
	    <td rowspan="3">Company</td>
	    <td rowspan="3">Product Name </td>
	    <td colspan="4" rowspan="2">Product. Spec </td>
	    <td rowspan="3">SQM. M2 * </td>
	    <td colspan="2" rowspan="2">Amount</td>
	    <td colspan="8" align="center">Production Plan </td>
	    <td rowspan="3">Delivery Remarks</td>
		<td rowspan="3">Paper Catalog Remarks</td>
	    <td rowspan="3">SO. Remarks</td>
	  </tr>
	  <tr class='tdLabel'>
	    <td colspan="2">Delivery</td>
	    <td colspan="3">Corrugator</td>
	    <td colspan="3">Convertor</td>
	  </tr>
	  <tr class='tdLabel'>
	    <td>P.W</td>
	    <td>Length</td>
	    <td>F</td>
	    <td>Cut </td>
	    <td>PCS</td>
	    <td>ALW +/- </td>
	    <td>Date</td>
	    <td>Amount</td>
	    <td>Date</td>
	    <td>Amount</td>
	    <td>Time</td>
	    <td>Date</td>
	    <td>Amount</td>
	    <td>Time</td>
	  </tr>

	<?php
	$cnt=0;
	foreach ($resultTotalProductionPlan->result() as $key)
	{
		$cnt++;
		//FORMULA
                if(($key->cut*1000000*$key->slit)!=0)
		$sqm = ($key->p_width_inch*25.4*$key->t_length)/($key->cut*1000000*$key->slit);
		$sqm = round($sqm,3);
	?>
	<tr class='tdView'>
		<td><?=$key->sales_order?></td>
		<td><?=$key->purchase_order_no?></td>
		<td><?=$key->product_code?></td>
		<td nowrap><?=$key->partner_name?></td>
		<td nowrap><?=$key->product_name?></td>
		<td><?=$key->p_width_inch?></td>
		<td><?=$key->t_length?></td>
		<td><?=$key->flute?></td>
		<td><?=$key->cut?></td>
		<td><?=$sqm?></td>
		<td><?=$key->qty?></td>
		<td><?=$key->qty_allowance?></td>
		<td><?=$key->delivery_date?></td>
		<td><?=$key->qty?></td>
		<td><?=$key->corrugator_date?></td>
		<td><?=$key->qty?></td>
		<td><?=$key->corrugator_time?></td>
		<td><?=$key->converter_date?></td>
		<td><?=$key->qty?></td>
		<td><?=$key->converter_time?></td>
		<td><?=$key->D_remarks?></td>
		<td><?=$key->PC_remarks?></td>
		<td><?=$key->SO_remarks?></td>
	</tr>
	
	<?php } ?>
</table>
<br/>
*Auto Calculated