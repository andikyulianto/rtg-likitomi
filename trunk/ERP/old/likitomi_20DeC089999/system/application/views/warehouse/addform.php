<table width='100%'>
	<tr>
		<td width='400px'>
			<table class='tbl01' width='100%'>
				<tr>
					<td> Invoice : <input type='text' id='x_invoice_no'/></td>
					<td><table><tr><td>Supplier:</td><td>
					&nbsp; <input type="text" id="suppliers" size="20"/>
					</td></tr></table></td>
					<td>Date    : <?=date('Y-m-d')?></td>
				</tr>
			</table>
		</td>
	</tr>
	<tr>
		<td height='10px'>
		</td>
	</tr>
	<tr>
		<td>
			<table class='tbl02'>
				<tr>
					<th>Paper Code</th>
					<th>Supplier Roll ID</th>
					<th>Size</th>
					<th>Unit</th>
					<th>Initial Weight (Kg)</th>
					<th>Remarks</th>
					<th>RFID Tag</th>					
				</tr>
				<?php 
				for($cnt=1;$cnt<=$limit;$cnt++)
				{ ?>
				<tr>
					<td><input type='text' id='x_paper_code_<?=$cnt?>' class='combo_papers' size='9'/></td>
					<td><input type='text' id='x_supplier_roll_id_<?=$cnt?>' size='12'/></td>
					<td><input type='text' id='x_size_<?=$cnt?>' size='12'/></td>
					<td><select id='x_unit_<?=$cnt?>' width='10'>	
						<option value='mm' >mm</option>
						<option value='inch' selected>inch</option>
					</select></td>
					<td><input type='text' id='x_initial_weight_<?=$cnt?>' size='12'/></td>
					<td><input type='text' id='x_remarks_<?=$cnt?>' /></td>
					<td><input type='text' id='x_rfid_roll_id_<?=$cnt?>' /></td>			
				</tr>
				<?php } ?>
			</table>
		</td>
	</tr>
	<tr>
		<td>
			<input type='button' value='&nbsp;&nbsp;&nbsp;Save&nbsp;&nbsp;&nbsp; ' onclick="saveStockData()"/>
		</td>
	</tr>
</table>