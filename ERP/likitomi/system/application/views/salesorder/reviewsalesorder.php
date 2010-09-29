<?php 
	$max = ($page+1);
	$min = ($page-1);
?>
<table width='100%'>
	<tr>
		<td width=140 class='tabunselect' onclick='createSalesOrderPage();'>1. Create Sales Order</td>
		<td width=6>&nbsp;</td>
		<td width=140 class='tabselect'> 2. Review Sales Order</td>
		<td align='right'>
			<a href='<?=base_url()."index.php/salesorder/reportSalesOrder/".$resultSales->sales_order_id?>' target='_blank'>
				<img class='imglink' src='<?=base_url()."static/images/extjs/printer.png"?>' 
					title="Preview Sales Order" />
			</a>
			<input type='button' value='<<' onclick='loadSalesOrder(<?=$min?>)' <?php if($min<0)echo "disabled";?> /> 
				&nbsp;&nbsp;<?=($page+1)?> / <?=$totalRec?>&nbsp;&nbsp;
			<input type='button' value='>>' onclick='loadSalesOrder(<?=$max?>)' <?php if($max>=$totalRec)echo "disabled";?> /> 
		</td>
	</tr>
	<tr>
		<td height='5' class='tbltabslinecenter'></td>
		<td class='tbltabslinecenter'></td>
		<td class='tbltabslineselect'></td>
		<td class='tbltabslineright'></td>
	</tr>
</table>
<br/>

<div id='boxcontainer'>
	<table width='100%'>
		<tr>
	        <td class='tblDetailViewLabel'>Date :</td>
			<td class='tblDetailView'><?=date("d-m-Y",strtotime($resultSales->sales_order_date));?></td>
			<td class='tblDetailViewLabel'>Sales Order :</td>
			<td class='tblDetailView'><?=$resultSales->sales_order_id?>
				<input type='hidden' value='<?=$resultSales->sales_order_id?>' id='x_sales_order' /> 
			</td>
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
					</tr>
<?php 
if(($resultSales->product_code_1!="")||($resultSales->product_code_1!=NULL))
{ ?>
	<tr>
		<td class='tblProdView'><?=$resultSales->product_code_1?></td>
		<td class='tblProdView'>
			<span onclick="inlineEditSales(this,'amount_1');"><?=$resultSales->amount_1?></span>
			<input type='hidden' value='<?=$resultSales->amount_1?>' id='xh_amount1' /></td>
	</tr>
<?php }
?>	
<?php 
if(($resultSales->product_code_2!="")||($resultSales->product_code_2!=NULL))
{ ?>
	<tr>
		<td class='tblProdView'><?=$resultSales->product_code_2?></td>
		<td class='tblProdView'>
			<span onclick="inlineEditSales(this,'amount_2');"><?=$resultSales->amount_2?></span>
			<input type='hidden' value='<?=$resultSales->amount_2?>' id='xh_amount2' /></td>
	</tr>
<?php }
?>	
<?php 
if(($resultSales->product_code_3!="")||($resultSales->product_code_3!=NULL))
{ ?>
	<tr>
		<td class='tblProdView'><?=$resultSales->product_code_3?></td>
		<td class='tblProdView'>
			<span onclick="inlineEditSales(this,'amount_3');"><?=$resultSales->amount_3?></span>
			<input type='hidden' value='<?=$resultSales->amount_3?>' id='xh_amount3' /></td>
	</tr>
<?php }
?>	
<?php 
if(($resultSales->product_code_4!="")||($resultSales->product_code_4!=NULL))
{ ?>
	<tr>
		<td class='tblProdView'><?=$resultSales->product_code_4?></td>
		<td class='tblProdView'>
			<span onclick="inlineEditSales(this,'amount_4');"><?=$resultSales->amount_4?></span>
			<input type='hidden' value='<?=$resultSales->amount_4?>' id='xh_amount4' /></td>
	</tr>
<?php }
?>	
				</table>
			</td>
			<td align='center' colspan='2'>
				<table class='tblFixedBorder' width='100%'>
					<tr>
				        <td class='tblProdViewLabel'>Delivery</td>
					</tr>
					<tr>
				        <td class='tblProdViewWrap'><?=$resultSales->delivery_at?></td>
					</tr>
				</table>
			</td>
		</tr>
		</table>	
</div>
<br/>
<? if(($resultSales->remarks=="")||($resultSales->remarks=="-")|| ($resultSales->remarks==NULL)) 
$remarks="No Remarks";
else $remarks=$resultSales->remarks; 

if(($resultSales->purchase_order_no=="")||($resultSales->purchase_order_no=="-")|| ($resultSales->purchase_order_no==NULL)) 
$po="No PO";
else $po=$resultSales->purchase_order_no; 
?>
<div id='boxcontainer'>
	<table width='100%'>
		<tr>
			<td class='tblDetailViewLabel'>Purchase Order Number :</td>
			<td class='tblDetailView'> <span onclick='inlineEditSales(this,"purchase_order_no");'><?=$po?></span></td>
			<td class='tblDetailViewLabel'>Remarks :</td>
			<td class='tblDetailView'> <span onclick='inlineEditSales(this,"remarks");'><?=$remarks?></span></td>
		</tr>
	</table>
</div>
<br/>
<table width='100%'>
	<tr>
		<td><h2>Delivery Details </h2></td>
		<td align='right'>		</td>
	</tr>
</table>
<table class='tblFixedBorder' width='100%' id='tblDelivery' >
	<tr>
		<td class='DeliveryLabel' width='40px'>Id</td>
		<td class='DeliveryLabel' width='120px'>Product Code</td>
		<td class='DeliveryLabel' width='120px'>Delivery Date*</td>
		<td class='DeliveryLabel' width='120px'>Delivery Time*</td>
		<td class='DeliveryLabel' width='120px'>Quantity*</td>
		<td class='DeliveryLabel' width='120px'>Status</td>
		<td class='DeliveryLabel'>Last Updated</td>
		<td class='DeliveryLabel'  width='20px'></td>
	</tr>
<?php
$qtyscheduled = 0;
if($totalRecDelivery>0){
	$cnt=0;$itemcnt=0;
	foreach($deliveryLists->result() as $deliveryList){
		$cnt++;$itemcnt++;
		$qtyscheduled +=$deliveryList->qty;
		//$row=($cnt%2==0)?'dodd':'';
?>
	<tr>
		<td class='DeliveryView'><?=$deliveryList->delivery_id?><input type='hidden' id='x_delivery_id_<?=$itemcnt?>' value='<?=$deliveryList->delivery_id?>' /></td>
		<td class='DeliveryView'><?=$deliveryList->product_code?></td>
		<td class='DeliveryView'><span onclick='inlinedit(this,3)'><?=date("d-m-Y",strtotime($deliveryList->delivery_date))?></span></td>
		<td class='DeliveryView'><span onclick='inlinedit(this,4)'><?=substr($deliveryList->delivery_time,0,5)?></span></td>
		<td class='DeliveryView'><span onclick='inlinedit(this,5)'><?=$deliveryList->qty?></span></td>
		<td class='DeliveryView'><?=$deliveryList->status?></td>
		<td class='DeliveryView'><?=$deliveryList->modified_on?></td>
		<td class='DeliveryView' onclick='deleteDelivery(this)'><img src='<?=base_url()."static/images/extjs/delete.gif"?>'/></td>
	</tr>
	
<?php
		$itemcnt++;
		$histdata['history'] = $salesClass->getDeliveryHistory($deliveryList->delivery_id);
		$histdata['showheader'] = false;
		echo "<tr><td></td><td colspan=6>";
		$this->load->view('salesorder/deliveryhistory',$histdata);
		echo "</td><td class='DeliveryView'></td></tr>";
		
	}// end foreach
}
?>
	<tr>
		<td class='tblProdView'>Auto</td>
		<td class='tblProdView'><select id='x_sel_product_code' >
			<?php
			if(($resultSales->product_code_1!="")||($resultSales->product_code_1!=NULL))
				echo "<option value='$resultSales->product_code_1' >$resultSales->product_code_1</option>";
			if(($resultSales->product_code_2!="")||($resultSales->product_code_2!=NULL))
				echo "<option value='$resultSales->product_code_2' >$resultSales->product_code_2</option>";
			if(($resultSales->product_code_3!="")||($resultSales->product_code_3!=NULL))
				echo "<option value='$resultSales->product_code_3' >$resultSales->product_code_3</option>";
			if(($resultSales->product_code_4!="")||($resultSales->product_code_4!=NULL))
				echo "<option value='$resultSales->product_code_4' >$resultSales->product_code_4</option>";
			?>
		</select></td>
		<td class='tblProdView'><input type='text' id='x_delivery_date' class="date-picker"  size="10" ></td>
		<td class='tblProdView'><input type='text' id='x_delivery_time' class="time-picker"  size="4" ></td>
		<td class='tblProdView'><input type='text' id='x_qty' value='' size="11" ></td>
		<td class='tblProdView'>new</td>
		<td class='tblProdView'></td>
		<td class='tblProdView'><input type='button' onclick='sumAmount(this);' value=' Save ' /></td>	
	</tr>
</table>
<br/>
*: Can be Edited. To edit click on the value.
<input type='hidden' id='remaining_amt' value='<?=($resultSales->amount_1-$qtyscheduled)?>' />
