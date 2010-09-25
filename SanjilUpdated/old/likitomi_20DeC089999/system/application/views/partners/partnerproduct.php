<div id="product" class="x-hide-display paddedDiv">
<?php echo "<div width='100%' style='text-align:right'>";
if($resultPartner->isdeleted!=0){ echo "<span class='alreadyDeleted' width='100%'>This Document is Deleted </span>";}
echo "</div>";
?>
<table width='100%'>
	<input type='hidden' id='x_partner_id' value='<?=$resultPartner->partner_id?>'>
	<tr>
		<td>&nbsp;</td>
		<td><div id='nametitle'><?=$resultPartner->partner_name?></div>
		<?php if($resultPartner->partner_type !=="") echo $resultPartner->partner_type."<br/>";?>
		<?php if($resultPartner->partner_name_thai !="") echo $resultPartner->partner_name_thai."<br/>";?>
		<?=$resultPartner->partner_code?>
		</td>
		<td align='right'>ID: <?=$resultPartner->partner_id?></td>
	</tr>
</table>
<br/>
Products For this <?=$resultPartner->partner_type?> <span class='counter'><?=$productcnt?></span>
<br/><br/>

<div id='boxcontainer'>
<table>
<?php 
	foreach ($resultProduct as $row) 
		{
?>
	<tr>
		<td class='tblDetailViewLabel'><?=$row->product_code?></td>
		<td><?=$row->product_name?></td>
	</tr>
<?php } ?>
</table>
</div>
</div>