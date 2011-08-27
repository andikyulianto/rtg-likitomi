<center><table class="resultwarehouse" width="95%">
<!--  <tr>-->
<!--  	<th>Supplier</th>-->
<!--	<th>Invoice Date </th>-->
<!--	<th>Invoice No </th>-->
<!--  	<th>Paper Code </th>-->
<!--  	<th>Size </th>-->
<!--    <th>Roll ID </th>-->
<!--	<th>Latest Weight</th>-->
<!--  </tr>-->
  <tr>
<!--  	<th rowspan="2">Paper Code</th>-->
<!--	<th colspan="2">Paper Width</th>-->
<!--	<th colspan="2">Previous Stock</th>-->
<!--  	<th colspan="2">Import</th>-->
<!--	<th colspan="2">Bring Out</th>-->
<!--	<th colspan="2">Return</th>-->
<!--	<th colspan="2">Used Amount</th>-->
<!--	<th colspan="2">Bring Back</th>-->
<!--	<th colspan="2">Improve</th>-->
<!--	<th colspan="2">Current Stock</th>-->
  	<th rowspan="2">รหัสกระดาษ</th>
	<th colspan="2">ขนาดกระดาษ</th>
	<th colspan="2">ยอดยกมา</th>
  	<th colspan="2">นำเข้า</th>
	<th colspan="2">เบิกใช้</th>
	<th colspan="2">เหลือคืน</th>
	<th colspan="2">ยอดใช้</th>
	<th colspan="2">ส่งคืน</th>
	<th colspan="2">ปรับปรุง</th>
	<th colspan="2">คงเหลือ</th>
 </tr>  
 <tr>
 	<th>CM.</th><th>INCH</th>
 	<th>ROLL</th><th>KG.</th>
 	<th>ROLL</th><th>KG.</th>
 	<th>ROLL</th><th>KG.</th>
 	<th>ROLL</th><th>KG.</th>
 	<th>ROLL</th><th>KG.</th>
 	<th>ROLL</th><th>KG.</th>
 	<th>ROLL</th><th>KG.</th>
 	<th>ROLL</th><th>KG.</th>
 </tr>
  <?php
	$cnt=0;
//	$curRecord 	= array("","","","");
//	$lastRecord = array("","","","");
//	$repeatFlag = array("false","false","false","false");
	$curRecord 	= array("","","","","","","","","","","","","","","","","","","");
	$lastRecord = array("","","","","","","","","","","","","","","","","","","");
	$repeatFlag = array("false","false","false","false","false","false","false","false","false","false","false","false","false","false","false","false","false","false","false","false");
	
	foreach ($resultStock->result() as $key)
	{
		$cnt++;
//		$curRecord = array($key->supplier_id,$key->invoice_date,$key->invoice_no,$key->paper_code);
		$curRecord = array($key->paper_code,"",$key->size,"","","","","","","","","","","","","","",$key->size,$key->size);
		
		echo "<tr>";
		
//		for($i=0;$i<4;$i++)
		for($i=0;$i<19;$i++)
		{	
			if($lastRecord[$i]==$curRecord[$i]) 
			{
				$repeatFlag[$i] = true;	
			}
			else 
			{
//				if($i==0) $lastRecord = array("","","","");
				if($i==0) $lastRecord = array("","","","","","","","","","","","","","","","","","","");
				$lastRecord[$i]=$curRecord[$i];
				$repeatFlag[$i] = false;	
			}
			
			if(!$repeatFlag[$i]) {
				echo "<td class='noborderbottom' style='text-align:center;'>";
//				if($i==0) echo $thisClass->getSupplierById($curRecord[$i]);
				if ($i==17) {echo $thisClass->getNumRolls($curRecord[0],$curRecord[2]);}
				else if ($i==18) {
					echo $thisClass->getSumWeight($curRecord[0],$curRecord[2]);
				}
				else {echo $curRecord[$i];}
				echo "</td>";
			}
			else 
			{
				echo "<td class='noborder'>&nbsp;</td>";
			}
		}
	?>
<!--		<td class="withborder"><?=$key->paper_roll_detail_id?></td>-->
    	<td class="withborder" style='text-align:center;'><?php 
		$latestwt = $thisClass->getLatestWeight($key->paper_roll_detail_id);
		if($latestwt>0) echo $latestwt;
		else echo "<i>$key->initial_weight</i>";
		
		?></td>

   </tr>
<?php } ?>
</table></center>
