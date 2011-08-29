<br>
<h2>
	<div align=center>Pad and Partition plan: <?=$plandate?></div>
</h2>
<br>
<center>

	<table>
	<tdead><tr class='tdLabel'>
	<td>Time In</td>
	<td>Time Out</td>
	<td>Pcs.</td>
	<td>Product code</td>

	<td>Machine</td>
	<td>Color</td>
	<td>Time</td>
	<td>Speed</td>	
	<td>MO</td>
<!--	<td colspan=3>Scroline</td> -->
	<td>Length</td>
	<td>Blank</td>
	<td>F</td>
	<td>Sale Order</td>
	<td>Customer</td>
	<td>Product Name</td>
	<td>Delievery date</td>
	<td>Sketch</td>
</tr>
</thead>
<tbody>
<?php

	//assign constants of machine speed
	foreach ($machine->result() as $key)
	{

			if($key->machine_name == "RD")
				$speed_rd = $key->speed;
			if($key->machine_name == "SS")
				$speed_ss = $key->speed;
			if($key->machine_name == "remove")
				$speed_remove = $key->speed;
			if($key->machine_name == "foam")
				$speed_foam = $key->speed;
			if($key->machine_name == "tape")
				$speed_tape = $key->speed;
			
			
	}
?>
<?php
	foreach ($resultPartition->result() as $key)
	{

		$mch ="";
		$speed =1;
			
			if($key->req_rd)
			{
				$mch = "RD ";
				$speed =$speed_rd." ";
			}
			if($key->req_ss)
			{
				$mch = "SS ";
				$speed =$speed_ss." ";
			}
			if($key->req_remove)
			{
				$mch = "Remove Scraps ";
				$speed =$speed_remove." ";
			}
			if($key->req_foam)
			{
				$mch = "Foam ";
				$speed =$speed_foam." ";
			}
			if($key->req_tape)
			{
				$mch = "Tape ";
				$speed =$speed_tape." ";
			}
			

	
?>
<tr class='tdView'>
	<td><?php $time = strtotime($key->plan_pt_start); 
	echo date('h:i',$time); ?></td>
	<td><?php $time = strtotime($key->plan_pt_end); 
	echo date('h:i',$time); ?></td>
	<td><?=$key->qty?></td>
	<td><?=$key->product_code?></td>

	<td>
	<?=$mch?>
	</td>
	<td><?php
		if($key->ink_1!="")
			echo $key->ink_1;
		if($key->ink_2!="")
			echo ",".$key->ink_2;
		if($key->ink_3!="")
			echo ",".$key->ink_3;
		
	?></td>
	<td><?=round($key->qty/$speed)?></td>
	<td><?=$speed?></td>	
	<td><?php
		$path = "/planning/barcode/".$key->mo_pt_code."/";
		echo "<img src='".site_url($path)."' /><br>".$key->mo_pt_code;
		?>
	</td>
<!--	<td><?=$key->scoreline_f?></td>
	<td><?=$key->scoreline_d?></td>
	<td><?=$key->scoreline_f2?></td>
	-->
	<td><?=$key->t_length?></td>
	<td><?=$key->blank?></td>
	<td><?=$key->flute?></td>
	<td><?=$key->sales_order?></td>
	<td><?=$key->partner_name?></td>
	<td><?=$key->product_name?></td>
	<td><?=$key->delivery_date?></td>
	<td>
	<?php if($key->sketch!="")
		echo "<a href='".base_url()."".$key->sketch."'  target='_blank'>".$key->product_code." [M]"."</a>";
	?>
	<?php if($key->sketch_large!="")
		echo "<a href='".base_url()."".$key->sketch_large."'  target='_blank'>".$key->product_code." [L]"."</a>";
	?></td>
</tr>
<?php
	}
?>
</tbody>

			</table>
 </center>
<br>
<br>
 


