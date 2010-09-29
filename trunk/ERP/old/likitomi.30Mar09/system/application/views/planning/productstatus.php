<h2>
	<div align=center>Project Status : <?=$plandate?></div>
</h2>
<br>
	<table>
	  <tr class='tdLabel'>
		<td>SO. NO.</td>
		<td>PO. NO.</td>
		<td>Product Code </td>
		<td>Partner Name </td>
		<td>Product Name </td>
		<td>Delivered Date </td>
		<td>Amount</td>
		<td>Delivered Amount </td>
		<td>Total Production Amount </td>
		<td>Damaged Amount </td>
		<td>Status</td>
		<td> </td>
	  </tr>
	  
	<?php
	$cnt=0;
	foreach ($resultProductStatus->result() as $key)
	{
		$cnt++;
		//FORMULA
	?>
	  <tr class='tdView'>
	  	<td><?=$key->sales_order?></td>
		<td><?=$key->purchase_order_no?></td>
		<td><?=$key->product_code?></td>
		<td><?=$key->partner_name?></td>
		<td><?=$key->product_name?></td>
		<td><?=$key->delivery_date?></td>
		<td><?=$key->qty?></td>
		<td><input id="x_delivered_qty" type="text" value="<?=$key->delivered_qty?>" size="6"/></td>
		<td><input id="x_total_production_qty" type="text" value="<?=$key->total_production_qty?>" size="6"/></td>
		<td><input id="x_damaged_qty" type="text" value="<?=$key->damaged_qty?>" size="6"/></td>
		<td><?=$key->status?></td>
		<td><input type="submit" name="btnSave" value="Save" onclick="updateProjectStatusData('<?=$key->delivery_id?>')"/></td>
	  </tr>
	  <?php } ?>
</table>
