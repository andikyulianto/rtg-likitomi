	<table id='tbl_totalplanning' class="sortable">
		<thead>
			<tr>
				<th>Id</th>
				<th>SO</th>
				<th>PO.NO.</th>
				<th>Product Code</th>
				<th>Company</th>
				<th>Product Name</th>
				<th>P.W</th>	
				<th>Length</th>
				<th>Qty</th>
				<th>Delivery Date</th>
				<th>Last Modified</th>
				<th>Status</th>							
				<th>Corrugator Date</th>
				<th>&nbsp;Converter Date</th>
				<th class='unsortable'></th>
			</tr>
		</thead>
		<tbody>
<?php
if($items==0)
{ ?>
		<tr height='1px'>
			<td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
			<td></td><td></td><td></td><td></td><td></td><td></td><td></td>
		</tr>

<?php } else { 
	$cnt=0;
	foreach($deliveryList as $delivery)
	{
		$cnt++;
?>
		<tr>
			<td><?=$delivery['delivery_id']?></td>
			<td><?=$delivery['sales_order']?></td>
			<td><?=$delivery['purchase_order_no']?></td>
			<td><?=$delivery['product_code']?></td>
			<td><?=$delivery['partner_name']?></td>
			<td><?=$delivery['product_name']?></td>
			<td><?=$delivery['p_width_inch']?></td>	
			<td><?=$delivery['t_length']?></td>
			<td><?=$delivery['qty']?></td>					
			<td><?=$delivery['delivery_date']?></td>			
			<td><?=$delivery['modified_on']?></td>
			<td><?=$delivery['status']?></td>
			<td><?=$delivery['corrugator_date']?></td>
			<td><?=$delivery['converter_date']?></td>
			<td><input type='button' value='Delete' onclick='removeRow(this)'/></td>
		</tr>
<?php }}?>
		</tbody>
	</table>
	<input type='hidden' id='listofdeliveryadded' value='<?=$listofdeliveryadded?>' />