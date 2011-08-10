<?php
if ($action=='view'){ 
?>
<table width='100%'>
	<tr>
		<td width='400px'>
			<table class='tbl01' width='100%'>
				<tr>
					<td width='50'> Invoice : </td>
					<td class='viewLabel'>
						<?=$resultInvoiceDetail[0]->invoice_no?>
						<input type='hidden' id='x_invoice_no' value ='<?=$resultInvoiceDetail[0]->invoice_no?>'/>
					</td>
					<td width='50'> Invoice Date: </td><td class='viewLabel'><?=$resultInvoiceDetail[0]->invoice_date?></td>
				</tr>
				<tr>
					<td width='80'> Supplier : </td><td class='viewLabel'><?=$thisClass->getSupplierById($resultInvoiceDetail[0]->supplier_id)?></td>
					<td width='80'></td><td class='viewLabel'></td> <!--replaced old paper_code-->
<!--					<td width='80'> Paper Code : </td><td class='viewLabel'><?=$resultInvoiceDetail[0]->paper_code?></td>--> <!--old paper_code-->
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
					<th><?=$this->lang->line('supplier_roll_id')?></th>
					<th><?=$this->lang->line('paper_code')?></th> <!--new paper_code-->
					<th><?=$this->lang->line('size')?></th>
					<th><?=$this->lang->line('unit')?></th>
					<th><?=$this->lang->line('initial_weight')?>(Kg)</th>
					<th><?=$this->lang->line('remarks')?></th>
<!--					<th><?=$this->lang->line('notes')?></th>-->
<!--					<th><?=$this->lang->line('rfid_tag')?></th>-->
					<th><?=$this->lang->line('likitomi_roll_id')?></th>
				</tr>
<?php
			foreach($resultInvoiceDetail as $row){
?>
				<tr>
					<td><?=$row->supplier_roll_id?></td>
					<td><?=$row->paper_code?></td> <!--new paper_code-->
					<td><?=$row->size?></td>
					<td><?=$row->uom?></td>
					<td><?=$row->initial_weight?> (Kg)</td>
					<td><?=$row->remarks?></td>
<!--					<td><?=$row->notes?></td>-->
<!--					<td><?=$row->rfid_roll_id?></td>-->
					<td><?=$row->likitomi_roll_id?></td>
				</tr>
<?
}				
?>
			</table>
		</td>
	</tr>
</table>
<?php } //End View 
?>

<?php
if (($action=='edit')||($action=='add')){  //Edit  or Add
if($action=='edit'){
//	$paper_code			= $resultInvoiceDetail[0]->paper_code; //old paper_code
	$supplier_id		= $resultInvoiceDetail[0]->supplier_id;
	$invoice_no			= $resultInvoiceDetail[0]->invoice_no;
	$invoice_date		= $resultInvoiceDetail[0]->invoice_date;
	$isdeleted			= $resultInvoiceDetail[0]->isdeleted;
	$supplier_name		= $thisClass->getSupplierById($supplier_id);
	$cmd = "saveData('update')";
	$btntitle = $this->lang->line('update');
}
if($action=='add'){
	$paper_roll_detail_id = "";	//$paper_code = ""; //old paper_code
	$supplier_id="";
	$supplier_name = "";			$supplier_roll_id = "";
	$paper_code=""; //new paper_code
	$initial_weight = "";		$remarks = "";
	$notes = "";	$size = "";	$uom = "";
	$rfid_roll_id = "";	$likitomi_roll_id = "";			$invoice_no = "";
	$invoice_date = date('Y-m-d');			
	$isdeleted = "0";
	$cmd = "saveData('save')";
	$btntitle = $this->lang->line('save');
}
?>


<table width='100%'>
	
	<tr>
		<td width='400px'>
			<table class='tbl01' width='100%'>
				<tr>
					<td width='50'> Invoice : </td><td><input type='text' id='x_invoice_no' value ='<?=$invoice_no?>' 
					<?php if($action=='edit') echo "disabled='disabled' class='nouse' "?>/></td>
					<td width='50'> Invoice Date: </td><td><input type='text' id='x_invoice_date' size="12" value="<?=$invoice_date?>" 
					<?php if($action=='edit') echo "disabled='disabled' class='nouse'  "?> size="10"/></td>
				</tr>
				<tr>
					<td width='80'> Supplier : </td><td><input type="text" id="x_supplier" size="40" value='<?=$supplier_id?>'/></td>
					<td width='80'></td><td></td> <!--replaced old paper_code-->
<!--					<td width='80'> Paper Code : </td><td><input type="text" id="x_paper_code" class='combo_papers' size="13" value='<?=$paper_code?>'/></td>--> <!--old paper_code-->
				</tr>
			</table>
		</td>
	</tr>
	<tr>
		<td>
			<input type="button" class='button' value="&nbsp;&nbsp;&nbsp;<?=$btntitle?>&nbsp;&nbsp;&nbsp;" onclick="<?=$cmd?>;">  
			<input type="button" class='button' value="&nbsp;<?=$this->lang->line('cancel')?>&nbsp;" onclick='cancelData();'>
		</td>
	</tr>
	<tr>
		<td>
			<table class='tbl02'>
				<tr>
					<th>&nbsp;</th>
					<th><?=$this->lang->line('supplier_roll_id')?></th>
					<th><?=$this->lang->line('paper_code')?></th> <!--new paper_code-->
					<th><?=$this->lang->line('size')?></th>
					<th><?=$this->lang->line('unit')?></th>
					<th><?=$this->lang->line('initial_weight')?>(Kg)</th>
					<th><?=$this->lang->line('remarks')?></th>
<!--					<th><?=$this->lang->line('rfid_tag')?></th>					-->
					<th><?=$this->lang->line('likitomi_roll_id')?></th>
				</tr>
<?php
			$cnt=0;
if($action=='edit'){
			foreach($resultInvoiceDetail as $row){	
			$cnt++;		
?>
				<tr>
					<td onClick="window.scrollBy(0,300)"><?=$cnt?></td>
					<td><input type='text' id='x_supplier_roll_id_<?=$cnt?>' size='14' value='<?=$row->supplier_roll_id?>'/></td>
					<td><input type='text' id='x_paper_code_<?=$cnt?>' size='14' value='<?=$row->paper_code?>'/></td> <!--new paper_code-->
					<td><input type='text' id='x_size_<?=$cnt?>' size='4'  value='<?=$row->size?>'/></td>
					<td><select id='x_unit_<?=$cnt?>' width='8'>	
						<option value='mm' <?php if($row->uom=="mm") echo 'selected'?> >mm</option>
						<option value='inch' <?php if($row->uom=="inch") echo 'selected'?> >inch</option>
					</select></td>
					<td><input type='text' id='x_initial_weight_<?=$cnt?>' size='10'  value='<?=$row->initial_weight?>'/></td>
					<td><input type='text' id='x_remarks_<?=$cnt?>' size='14' value='<?=$row->remarks?>'/></td>
					<input type='hidden' id='x_rfid_roll_id_<?=$cnt?>'size='10' value='<?=$row->rfid_roll_id?>'/>
					<td><input type='text' id='x_likitomi_roll_id_<?=$cnt?>'size='14' value='<?=$row->likitomi_roll_id?>'/></td>
				</tr>
<?php
}}
$cnt++;
	for($i=$cnt;$i<=$limit;$i++)
{				
?>
				<tr>
					<td onClick="window.scrollBy(0,300)"><?=$i?></td>
					<td><input type='text' id='x_supplier_roll_id_<?=$i?>' size='14' value=''/></td>
					<td><input type='text' id='x_paper_code_<?=$i?>' size='14' value=''/></td> <!--new paper_code-->
					<td><input type='text' id='x_size_<?=$i?>' size='4'  value=''/></td>
					<td><select id='x_unit_<?=$i?>' width='8'>	
						<option value='mm'>mm</option>
						<option value='inch' selected >inch</option>
					</select></td>
					<td><input type='text' id='x_initial_weight_<?=$i?>' size='10'  value=''/></td>
					<td><input type='text' id='x_remarks_<?=$i?>' size='14' value=''/></td>
					<input type='hidden' id='x_rfid_roll_id_<?=$i?>'size='10' value=''/>
					<td><input type='text' id='x_likitomi_roll_id_<?=$i?>'size='14' value=''/></td>
				</tr>
<?php 
}
?>
			</table>
		</td>
	</tr>
	<tr>
		<td>
			<input type="button" value="<?=$btntitle?>" onclick="<?=$cmd?>;">  
			<input type="button" value="<?=$this->lang->line('cancel')?>" onclick='cancelData();'>
		</td>
	</tr>
</table>
<br/>

<?php
} //End Edit 
?>
