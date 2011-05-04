<br>
<?php 
$array = array('COLOR','TIME','SPEED/TIME USE', 'SALE ORDER','ORDER NO.', 'P CODE /PD NO.','CUSTOMER','PRODUCT NAME','AMOUNT','DELIVERY DATE','NOTE','NEXT PROCESS'); 
$count = count($array);
//initial time start
$firstTime = (0.0006949*60)*8+(0.0006949*0);
$timeStart = $firstTime;
//initialize for each machine

foreach ($resultConvertor->result() as $key){
//echo strcmp($key->next_process,"2CL")." ".$key->next_process;
////////////////////////// '2CL' //////////////////////////
if(!strcmp($key->next_process,'2CL'))
{
$st = 25;
$speed = 60;
$machine_name = '2CL';
$flute = 'B';
$firstTime = (0.0006949*60)*8+(0.0006949*0);
$timeStart = $firstTime;

?>
<h2>
	<div align=center>Convertor plan : <?=$plandate?></div>
</h2>
<table>
	<tr class='tdLabel'>
		<td>Machine</td>
		<td>Item</td>
		<?php  for ($j=0; $j<$resultConvertor->num_rows; $j++) { ?>
		<td colspan='3'>Order<?=$j+1?></td>
		<?php } ?>
	</tr>
	<tr class='tdView'>
	<td rowspan='13'><?=$machine_name?></td>
	</tr>

	
<?php

//color
	echo "<tr class='tdView'><td>".$array[0]."</td>";
	foreach ($resultConvertor->result() as $key){
		if ($key->ink_1!= '') $result = $key->ink_1; 
		else $result ='';
		if ($key->ink_2!= '') $result = $result.','.$key->ink_2; 
		if ($key->ink_3!= '') $result = $result.','.$key->ink_3;
		if ($key->ink_4!= '') $result = $result.','.$key->ink_4;

		echo "<td></td>	<td colspan='2'>".$result."</td>";
	}
echo "</tr>";
//time
	echo "<tr class='tdView'><td>".$array[1]."</td>";
	foreach ($resultConvertor->result() as $key){
		$timeuse = round($key->qty / $speed,2);
		
		$timeStop = $timeStart+$timeuse;

		echo "<td>ST</td><td>".formatDate($timeStart)."</td><td>".formatDate($timeStop)."</td>" ;
	}
		$timeStart = $timeStop;
		echo "</tr>";
//speed
	echo "<tr class='tdView'><td>".$array[2]."</td>";
	foreach ($resultConvertor->result() as $key){
		echo "<td>".$st."</td><td class='blankTbl'>".$speed."</td><td>".$timeuse."</td>" ;
	}
		echo "</tr>";
//sale order
	echo "<tr class='tdView'><td>".$array[3]."</td>";
	foreach ($resultConvertor->result() as $key){
		echo "<td class='blankTbl'></td><td>".$key->sales_order."</td><td></td>" ;
	}
		echo "</tr>";
//Order No.
	echo "<tr class='tdView'><td>".$array[4]."</td>";
	$path = "/planning/barcode/".$key->autoid."/";
	foreach ($resultConvertor->result() as $key){
		echo "<td class='blankTbl'></td><td><img src='".site_url($path)."' /><br>".$key->autoid."</td><td class='blankTbl'></td>" ;
	}
		echo "</tr>";
//P code / Po. No.
	echo "<tr class='tdView'><td>".$array[5]."</td>";
	foreach ($resultConvertor->result() as $key){
		echo "<td>".$flute."</td><td>".$key->product_code."</td><td>".substr($key->product_code,3,3)."</td>" ;
	}
		echo "</tr>";
//Customer
	echo "<tr class='tdView'><td>".$array[6]."</td>";
	foreach ($resultConvertor->result() as $key){
		echo "<td class='blankTbl'></td><td>".$key->partner_name."</td><td></td>" ;
	}
		echo "</tr>";
//Product name
	echo "<tr class='tdView'><td>".$array[7]."</td>";
	foreach ($resultConvertor->result() as $key){
		echo "<td class='blankTbl'></td><td>".$key->product_name."</td><td></td>" ;
	}
		echo "</tr>";
//Amount
	echo "<tr class='tdView'><td>".$array[8]."</td>";
	foreach ($resultConvertor->result() as $key){
		echo "<td class='blankTbl'></td><td>".$key->qty."</td><td></td>" ;
	}
		echo "</tr>";
//Delivery date
	echo "<tr class='tdView'><td>".$array[9]."</td>";
	foreach ($resultConvertor->result() as $key){
		echo "<td class='blankTbl'></td><td>".$key->delivery_date."</td><td></td>" ;
	}
		echo "</tr>";

//Note
	echo "<tr class='tdView'><td>".$array[10]."</td>";
	foreach ($resultConvertor->result() as $key){
		echo "<td class='blankTbl'></td><td></td><td></td>" ;
	}
		echo "</tr>";
//Note
	echo "<tr class='tdView'><td>".$array[11]."</td>";
	foreach ($resultConvertor->result() as $key){
		echo "<td class='blankTbl'></td><td></td><td></td>" ;
	}
		echo "</tr>";
//}


?>


</table>
<br/>
* Auto Generated

<?php 


} 
////////////////////////// close if == '2CL' //////////////////////////


} // close outter foreach loop
function formatDate($day)
{
	$hour  = floor($day*24); 
	$min   = floor((($day*24)-$hour)*60); 
	$time  = ($hour<10)?"0".$hour:$hour;//
	$time .= ":";
	$time .= ($min<10)?"0".$min:$min;
	return $time;
}

?>

