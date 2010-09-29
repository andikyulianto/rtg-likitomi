<script type="text/javascript">
	var perpage=<?=$perPage?>;
	var page = <?=$page?>;
	<?php 
		$action_cmd="";
		$firstdata = 0;
		$max = ($page+$perPage);
		$min = ($page-$perPage);
		if($action=='search')$action_cmd ="ajax_pagination_search";
		else $action_cmd ="ajax_pagination";
	?>
</script>
<?php
if($totalRec<=0) { ?>
<p class="details-info">No Records </p>
<?php }else {
	?>
<div id='ajaxpagination' class='fullCenter'>
	<input type=button value=" << " <?php if($min<0)echo "disabled";?> onclick="<?=$action_cmd?>('prev',<?=$page?>,<?=$perPage?>,'<?=$product_type?>');" />
	<span style="font-size:80%;">
	<?php echo "(".$page." - ";
		echo ($max>$totalRec)?$totalRec:$max;
		echo " of ".$totalRec.")";
	?></span>
	<input type=button value=" >> " <?php if($max>$totalRec)echo "disabled";?> onclick="<?=$action_cmd?>('next',<?=$page?>,<?=$perPage?>,'<?=$product_type?>');" />
<table id="cwlistmain" class="cwTable">
<?php
	$firstChar ='';$cnt=0;
   foreach ($resultProducts as $row)
{	
	$cnt++; if($firstdata==0)$firstdata = $row->product_id;
	$curFirstChar = strtoupper(substr($row->product_code,0,1));
	if($firstChar!=$curFirstChar){ 
		$firstChar=$curFirstChar;
?>
<tr><td class='rowFirstChar'><?=$curFirstChar?></td><td class='rowFirstChar' align='center'>Product Name</td></tr>
<?php	} ?>
<tr onmouseover='cwOver(this);' onmouseout='cwOut(this);' class='cwTableRow' onclick='loadProductDetailFromRow("<?=$row->product_id?>",this);cw_Click(this);'>
<td align="left"><?php
if($action=='search') echo $product_class->ew_Highlight($row->product_code,$searchkeyword);
else echo $row->product_code;?>
</td>
<td align='left'><?=$row->product_name;?>
</td>
</tr>
<?php } ?></table>
<?php
if($action=="search") {
	echo "<input type='hidden' id='searchcounter' value='".$totalRec."'/>";
}
?>
<input type='hidden' id='firstitem' value='<?=$firstdata?>' />
</div>
<?php }?>
