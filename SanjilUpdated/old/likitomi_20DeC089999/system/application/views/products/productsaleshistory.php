<div id="salesHistory" class="x-hide-display paddedDiv">

<table width='100%'>
	<input type='hidden' id='x_product_id' value='<?=$resultProductCatalog->product_id?>'>
	<tr>
		<td><div id='nametitle'><?=$resultProductCatalog->product_code?></div>
		<?php if($resultProductCatalog->product_name !=="") echo $resultProductCatalog->product_name."<br/>";?>
		<?php if($customer_name !=="") { echo $customer_name?>
		<?php if($partner_isdeleted!=0) echo '<img title="The partner is deleted" src="'.base_url().'static/images/extjs/warning.gif"/>'; }?>
		</td>
		<td align='right'>
			<a href='<?=base_url()."index.php/salesorder/reportCatalog/".$resultProductCatalog->product_id?>' target='_blank'>
				<img class='imglink' src='<?=base_url()."static/images/extjs/printer.png"?>' 
					title="Preview Sales Catalog" />
			</a>
		</td>
	</tr>
</table>
<br/>

<h2>
	<span class='counter' ><?=$salesCount?></span> Sales 
</h2>
<br>

<?php if($salesCount>0) { ?>

<div style='overflow:auto' width='100%'>
<table class='tblFixedBorder' cellspacing=2 cellpadding=2>
	  <tr>
	    <td class='tblProdViewLabel' width='30px'>Sales Order ID</td>
	    <td class='tblProdViewLabel'>Product Code </td>
	    <td class='tblProdViewLabel'>Delivery Date</td>
	    <td class='tblProdViewLabel'>Amount </td>
	    <td class='tblProdViewLabel'  width='30px'>Delivered Amount </td>
	    <td class='tblProdViewLabel'  width='30px'>Total Production Amount </td>
	    <td class='tblProdViewLabel'  width='30px'>Damaged Amount </td>
	    <td class='tblProdViewLabel'  width='30px'>Status</td>
	  </tr>
	  <?php
	$cnt=0;
	foreach ($resultProductSalesHistory->result() as $key)
	{
		$cnt++;
	?>
	<tr>
		<td class='tblProdView'><?=$key->sales_order_id?></td>
		<td class='tblProdView'><?=$key->product_code?></td>
		<td class='tblProdView'><?=$key->delivery_date?></td>
		<td class='tblProdView'><?=$key->qty?></td>
		<td class='tblProdView'><?=$key->delivered_qty?></td>
		<td class='tblProdView'><?=$key->total_production_qty?></td>
		<td class='tblProdView'><?=$key->damaged_qty?></td>
		<td class='tblProdView'><?=$key->status?></td>
	</tr>	
	<?php } ?>
</table>
</div>

<?php } else {?>
 <p class='details-info'><?=$this->lang->line('msg_nosales')?></p>
<?php }?>

</div>