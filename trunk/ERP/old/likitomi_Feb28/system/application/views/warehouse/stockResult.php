<center><table class="resultwarehouse" width="95%">
  <tr>
  	<th>Supplier</th>
	<th>Invoice Date </th>
	<th>Invoice No </th>
  	<th>Paper Code </th>
    <th>Roll ID </th>
	<th>Latest Weight</th>
 </tr>  
  <?php
	$cnt=0;
	$curRecord 	= array("","","","");
	$lastRecord = array("","","","");
	$repeatFlag = array("false","false","false","false");
	
	foreach ($resultStock->result() as $key)
	{
		$cnt++;
		$curRecord = array($key->supplier_id,$key->invoice_date,$key->invoice_no,$key->paper_code);
		
		echo "<tr>";
		
		for($i=0;$i<4;$i++)
		{	
			if($lastRecord[$i]==$curRecord[$i]) 
			{
				$repeatFlag[$i] = true;	
			}
			else 
			{
				if($i==0) $lastRecord = array("","","","");
				$lastRecord[$i]=$curRecord[$i];
				$repeatFlag[$i] = false;	
			}
			
			if(!$repeatFlag[$i]) {
				echo "<td class='noborderbottom'>";
				if($i==0) echo $thisClass->getSupplierById($curRecord[$i]);
				else echo $curRecord[$i];
				echo "</td>";
			}
			else 
			{
				echo "<td class='noborder'>&nbsp;</td>";
			}
		}
	?>
		<td class="withborder"><?=$key->paper_roll_detail_id?></td>
    	<td class="withborder"><?php 
		$latestwt = $thisClass->getLatestWeight($key->paper_roll_detail_id);
		if($latestwt>0) echo $latestwt;
		else echo "<i>$key->initial_weight</i>";
		
		?></td>
   </tr>
<?php } ?>
</table></center>
