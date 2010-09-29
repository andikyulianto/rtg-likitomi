<?php $editable = ($action=='edit')?true:false;?>
<table width='100%'>
	<tr>
		<td width=140 class='tabselect'>1. Create Sales Order</td>
		<td width=6>&nbsp;</td>
		<td width=140 class='tabunselect' onclick='loadSalesOrder(0);'> 2. Review Sales Order</td>
		<td>&nbsp;</td>
	</tr>
	<tr>
		<td height='5' class='tbltabslineselect'></td>
		<td class='tbltabslinecenter'></td>
		<td class='tbltabslinecenter'></td>
		<td class='tbltabslineright'></td>
	</tr>
</table>
<br/>
<div id='boxcontainer'>
	<table width='100%'>
		<tr>
	        <td class='tblDetailViewLabel'>Date :</td>
			<td class='tblDetailView'><?=date("Y-m-d");?></td>
			<td class='tblDetailViewLabel'>Sales Order :</td>
			<td class='tblDetailView'><b>
				<?php if($editable) 
				{
					echo $resultSalesOrder->sales_order_id;
				}
				else {
					echo "(Auto Generated)";
				}
				?>
			</b></td>
		</tr>
	</table>	
</div>
<br/>
<div id='boxcontainer'>
	<table width='100%'>
		<tr>
			<td align='center' colspan='2'>
				<table class='tblFixedBorder'>
					<tr>
				        <td class='tblProdViewLabel'>Code</td>
						<td class='tblProdViewLabel'>Amount</td>
						<td class='tblProdViewLabel'>Stock</td>
					</tr>
<?php 
$cnt=0;
foreach($resultProducts as $prod){
	$cnt++;
?>	
					<tr>
						<td class='tblProdView'><input type='hidden' id='x_product_code_<?=$cnt?>' value='<?=$prod->product_code?>' /><?=$prod->product_code?></td>
						<td class='tblProdView'><input type='text' id='x_amount_<?=$cnt?>' size=5 value='' /></td>
						<td class='tblProdView'><?=$thisClass->getCumulativeStock($product_id,$prod->product_code);?></td>
					</tr>
<?php }?>
				</table>
				<input type='hidden' id='cntProducts' value='<?=$cnt?>' />
			</td>
			<td align='center' colspan='2'>
				<table class='tblFixedBorder' id='tblDeliveryAddressDiv' width='100%'>
					<tr>
				        <td class='tblProdViewLabel' id="tip-choosedelivery">Choose Delivery <input type='hidden' id='x_delivery' value="<?=$billing_address?>"/> </td>
					</tr>
					<tr>
				        <td class='tblProdViewWrap' onclick='prd_selAddress(this)'><?=$billing_address?></td>
					</tr>
<?php
if($deliveryAddresses->num_rows()>0){
foreach($deliveryAddresses->result() as $address){
?>
					<tr>
						<td class='tblProdViewWrap' onclick='prd_selAddress(this)'><?=$address->address;?></td>
					</tr>
<?php
}}?>
				</table>
			</td>
		</tr>
		</table>	
</div>
<br/>
<div id='boxcontainer'>
	<table width='100%'>
		<tr>
			<td class='tblDetailViewLabel'>Purchase Order Number :</td>
			<td class='tblDetailView'><textarea id='x_purchase_order'></textarea></td>
		</tr>
		<tr>
			<td class='tblDetailViewLabel'>Remarks :</td>
			<td class='tblDetailView'><textarea id='x_remarks'></textarea></td>
		</tr>
	</table>
</div>
<br/>
<center>
<input type="button" value="      Save      " onclick="addSalesOrder();">
</center>
