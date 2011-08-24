<br>
<h2>
	<div align=center>Convertor Plan: <?=$plandate?></div>
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
	<td colspan=3>Scroline</td>
	<td>Blank</td>
	<td>T.length</td>
	<td>F</td>
	<td>Sale Order</td>
	<td>P.Code</td>
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
			
			if($key->machine_name == "2CL")
				$speed_2cl = $key->speed;
			if($key->machine_name == "3CM")
				$speed_3cm = $key->speed;
			if($key->machine_name == "3CS")
				$speed_3cs = $key->speed;
			if($key->machine_name == "3CL")
				$speed_3cl = $key->speed;
			if($key->machine_name == "4CD")
				$speed_4cd = $key->speed;
			if($key->machine_name == "GH")
				$speed_gh = $key->speed;
			if($key->machine_name == "HS")
				$speed_hs = $key->speed;
			if($key->machine_name == "FG")
				$speed_fg = $key->speed;
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
	foreach ($resultConvertor->result() as $key)
	{

		$mch ="";
		$speed =1;
			if($key->req_2cl)
			{
				$mch = "2CL ";
				$speed =$speed_2cl." ";
			}	
			if($key->req_3cm)
			{
				$mch = "3CM ";
				$speed =$speed_3cm." ";
			}
			if($key->req_3cs)
			{
				$mch = "3CS ";
				$speed =$speed_3cs." ";
			}
			if($key->req_3cl)
			{
				$mch = "3CL ";
				$speed =$speed_3cl." ";
			}
			if($key->req_4cd)
			{
				$mch = "4CD ";
				$speed =$speed_4cd." ";
			}
			if($key->req_gh)
			{
				$mch = "GH ";
				$speed =$speed_gh." ";
			}
			if($key->req_hs)
			{
				$mch = "HS ";
				$speed =$speed_hs." ";
			}
			if($key->req_fg)
			{
				$mch = "FG ";
				$speed =$speed_fg." ";
			}
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
	<td><?php $time = strtotime($key->plan_cv_start); 
	echo date('h:i',$time); ?></td>
	<td><?php $time = strtotime($key->plan_cv_end); 
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
		$path = "/planning/barcode/".$key->mo_cv_code."/";
		echo "<img src='".site_url($path)."' /><br>".$key->mo_cv_code;
		?>
	</td>
	<td><?=$key->scoreline_f?></td>
	<td><?=$key->scoreline_d?></td>
	<td><?=$key->scoreline_f2?></td>
	<td><?=$key->blank?></td>
	<td><?=$key->t_length?></td>
	<td><?=$key->flute?></td>
	<td><?=$key->sales_order?></td>
	<td><?=$key->purchase_order_no?></td>
	<td><?=$key->partner_name?></td>
	<td><?=$key->product_name?></td>
	<td><?=$key->delivery_date?></td>
	<td>
	<?php if($key->sketch!="")
		echo "<a href='".base_url()."".$key->sketch."'  target='_blank'>".$key->product_code."</a>";
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
 


