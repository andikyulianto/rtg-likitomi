<?php
if (($action=='view')||($action=='edit')){ 
echo "<div width='100%' style='text-align:right'>";
if($resultProductCatalog->isdeleted!=0){ echo "<span class='alreadyDeleted' width='100%'>This Document is Deleted </span>";}
echo "</div>";
?>
<table width='100%'>
	<input type='hidden' id='x_product_id' value='<?=$resultProductCatalog->product_id?>'>
	<tr>
		<td><div id='nametitle'><?=$resultProductCatalog->product_code?></div>
		<?php if($resultProductCatalog->product_name !=="") echo $resultProductCatalog->product_name."<br/>";?>
		<?php if($customer_name !=="") echo $customer_name."<br/>"?>
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
<div id='salesOrderContainer'>
<?php
	$this->load->view('salesorder/createsalesorder');
?>	
</div>
<?php
}
else { echo "<p class='details-info'>Please Select One of the Products.</p>";}
?>