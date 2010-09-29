<?php
?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<title><?=$title?></title>
		<?=link_tag('static/images/favicon.ico', 'shortcut icon', 'image/x-icon');?>
		<?=link_tag('static/images/favicon.ico', 'icon', 'image/x-icon');?>
		
		<?=$scripts?>
		<style type="text/css">
			@import "<?=base_url()?>static/css/styles.css";	
			<?=$styles?>
		</style>	
	</head>
<body>
<center><table class="resultwarehouse" width="95%">
  <tr>
  	<th>Supplier</th>
	<th>Paper Code </th>
    <th>Roll ID </th>
	<th>Latest Weight</th>
	<th>Position</th>
	<th>Lane</th>
	<th>Height</th>
 </tr>  
  <?php
	$cnt=0;
	$curRecord 	= array("","","","");
	$lastRecord = array("","","","");
	$repeatFlag = array("false","false","false","false");
	
	foreach ($resultStock->result() as $key)
	{
		$cnt++;
		$curRecord = array($key->supplier_id,$key->paper_code);
		
		echo "<tr onclick=\"location.href='/clamplift/paperpick2.php?&rfidid=".$key->rfid_roll_id."';\">";
		
		for($i=0;$i<2;$i++)
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
		
		$query = $thisClass->getLatestMovement($key->paper_roll_detail_id);
		$latestwt =0;$xpos = ""; $ypos = ""; $zpos ="";
		if($query->num_rows()>0)
		{
			$rowMovement = $query->row();
			$xpos = $rowMovement->xpos;
			$ypos = $rowMovement->ypos;
			$zpos = $rowMovement->zpos;
			$latestwt = $rowMovement->actual_wt;
		}
		
		
	?>
		<td class="withborder"><?=$key->paper_roll_detail_id?></td>
    	<td class="withborder"><?php 
			if($latestwt>0) echo $latestwt;
			else echo "<i>$key->initial_weight</i>";
		?></td>
		
		<td class="withborder"><?=$xpos?></td>
		<td class="withborder"><?=$ypos?></td>
		<td class="withborder"><?=$zpos?></td>
   </tr>
<?php } ?>
</table></center>

</body></html>