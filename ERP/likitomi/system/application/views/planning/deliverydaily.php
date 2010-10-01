<h2>
	<div align=center>Delivery Daily Plan : <?=$plandate?></div>
</h2>
<br>
<table>
	  <tr class='tdLabel'>
	    <td rowspan="2">SO. NO.</td>
	    <td rowspan="2">PO. NO. </td>
	    <td rowspan="2">Product Code </td>
	    <td rowspan="2">Company</td>
	    <td rowspan="2">Product Name </td>
	    <td rowspan="2">F</td>
	    <td rowspan="2">SQM. M2 </td>
	    <td colspan="2">Amount</td>
	    <td colspan="2">Delivery</td>
	    <td rowspan="2">Actual</td>
	    <td rowspan="2">Delivery Remarks</td>
		<td rowspan="2">Paper Catalog Remarks</td>
	  </tr>
	  <tr class='tdLabel'>
	    <td>PCS</td>
	    <td>ALW +/- </td>
	    <td>Date</td>
	    <td>Amount</td>
	  </tr>
  
	<?php
	$cnt=0;
	foreach ($resultDeliveryDaily->result() as $key)
	{
		$cnt++;
		//FORMULA
                if(($key->cut)!=0)
		$sqm = ($key->p_width_inch*25.4*$key->t_length)/($key->cut*1000000);
		$sqm = round($sqm,3);
	?>
	<tr class='tdView'>
		<td><?=$key->sales_order?></td>
		<td><?=$key->purchase_order_no?></td>
		<td><?=$key->product_code?></td>
		<td><?=$key->partner_name?></td>
		<td><?=$key->product_name?></td>
		<td><?=$key->flute?></td>
		<td><?=$sqm?></td>
		<td><?=$key->qty?></td>
		<td><?=$key->qty_allowance?></td>
		<td><?=$key->delivery_date?></td>
		<td><?=$key->delivered_qty?></td>
		<td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
		<td><?=$key->D_remarks?></td>
		<td><?=$key->PC_remarks?></td>
	</tr>
	
	<?php } ?>
</table>