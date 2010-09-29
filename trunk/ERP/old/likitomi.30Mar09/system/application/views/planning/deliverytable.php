<h2 align='center' id='titleSearch'>Search Result</h2><br/>
<table class="sortable" id='tblDelResult'>
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
			<th class="unsortable">&nbsp;Corrugator Date&nbsp;&nbsp;</th>
			<th class="unsortable">&nbsp;&nbsp;Converter Date&nbsp;&nbsp;</th>
			<th class="unsortable" onclick='addAll()'>Add All</th>			
		</tr>
	</thead>
	<tbody>
		<?php
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
			<td><?=$delivery['status']?>
			<?php 
			if($delivery['status']=="updated"){
			?>
				<input type="button" id="show-btn" onclick="showHistory(this,'<?=$delivery['delivery_id']?>')" value="H" />
			<?php }?></td>
			<td><input type='text' id='corrugator_date_<?=$cnt?>' class="date-picker"  size="9" >
			<input type='text' id='corrugator_time_<?=$cnt?>' class="time-picker"  size="4" ></td>
			<td><input type='text' id='converter_date_<?=$cnt?>'  class="date-picker"  size="9" >
			<input type='text' id='converter_time_<?=$cnt?>' class="time-picker"  size="4" ></td>
			<td><input type='button' value='Add' onclick='add2planning(this);'/></td>
			
		</tr>			
		<?php }?>
	</tbody>
</table>
