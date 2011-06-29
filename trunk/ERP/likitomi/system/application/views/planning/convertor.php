<br>
<?php 
$array = array('COLOR','TIME','SPEED/TIME USE', 'SALE ORDER','ORDER NO.', 'P CODE /PD NO.','CUSTOMER','PRODUCT NAME','AMOUNT','DELIVERY DATE','NOTE','NEXT PROCESS'); 
$count = count($array);
//initialize for each machine
$twoCLflag = 0;
$threeCMflag = 0;
$threeCSflag = 0;
$threeCWflag = 0;
$threeCMflag = 0;
$twoCSflage = 0;
$twoCLItems = 0;
$threeCMItems = 0;
$threeCSItems = 0;
$j =0;

foreach ($resultConvertor->result() as $key){
echo $key->next_process;

if($twoCLflag==0)
{
////////////////////////// '2CL' //////////////////////////
if(!strcmp($key->next_process,'2CL'))
{
$twoCLflag++;
$st = 25;
$speed = 60;
$machine_name = '2CL';
$flute = 'B';
//initial time start
$firstTime = (0.0006949*60)*8+(0.0006949*0);
$timeStart = $firstTime;

?>
<h2>
	<div align=center>Convertor plan: <?=$plandate?></div>
</h2>
<table>
	<tr class='tdLabel'>
		<td>Machine</td>
		<td>Item</td>
		<?php  foreach ($resultConvertor->result() as $key) { 
		if($key->next_process=='2CL'){?>
		<td colspan='3'>Order<?=++$j?></td>
		<?php } } ?>
	</tr>
	<tr class='tdView'>
	<td rowspan='13'><?=$machine_name?></td>
	</tr>

	
<?php

//color
	echo "<tr class='tdView'><td>".$array[0]."</td>";
	foreach ($resultConvertor->result() as $key){
		if($key->next_process=='2CL'){
		if ($key->ink_1!= '') $result = $key->ink_1; 
		else $result ='';
		if ($key->ink_2!= '') $result = $result.','.$key->ink_2; 
		if ($key->ink_3!= '') $result = $result.','.$key->ink_3;
		if ($key->ink_4!= '') $result = $result.','.$key->ink_4;

		echo "<td></td>	<td colspan='2'>".$result."</td>";
	}}
echo "</tr>";
//time
	echo "<tr class='tdView'><td>".$array[1]."</td>";
	foreach ($resultConvertor->result() as $key){
		if($key->next_process=='2CL'){
		$timeuse = $key->qty / $speed;
		
		$timeStop = $timeStart + round($timeuse+30) * 0.0006949;

		echo "<td>ST</td><td>".formatDate($timeStart)."</td><td>".formatDate($timeStop)."</td>" ;
		$timeStart = $timeStop;
	}}
		
		echo "</tr>";
//speed
	echo "<tr class='tdView'><td>".$array[2]."</td>";
	foreach ($resultConvertor->result() as $key){
		if($key->next_process=='2CL'){
		$timeuse = $key->qty / $speed;
		echo "<td>".$st."</td><td class='blankTbl'>".$speed."</td><td>".round($timeuse,2)."</td>" ;
	}}
		echo "</tr>";
//sale order
	echo "<tr class='tdView'><td>".$array[3]."</td>";
	foreach ($resultConvertor->result() as $key){
		if($key->next_process=='2CL'){
		echo "<td class='blankTbl'></td><td>".$key->sales_order."</td><td></td>" ;
	}}
		echo "</tr>";
//Order No.
	echo "<tr class='tdView'><td>".$array[4]."</td>";
	$path = "/planning/barcode/".$key->autoid."/";
	foreach ($resultConvertor->result() as $key){
		if($key->next_process=='2CL'){
		echo "<td class='blankTbl'></td><td><img src='".site_url($path)."' /><br>".$key->autoid."</td><td class='blankTbl'></td>" ;
	}}
		echo "</tr>";
//P code / Po. No.
	echo "<tr class='tdView'><td>".$array[5]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='2CL'){
		echo "<td>".$flute."</td><td>".$key->product_code."</td><td>".substr($key->product_code,3,3)."</td>" ;
	}}
		echo "</tr>";
//Customer
	echo "<tr class='tdView'><td>".$array[6]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='2CL'){
		echo "<td class='blankTbl'></td><td>".$key->partner_name."</td><td></td>" ;
	}}
		echo "</tr>";
//Product name
	echo "<tr class='tdView'><td>".$array[7]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='2CL'){
		echo "<td class='blankTbl'></td><td>".$key->product_name."</td><td></td>" ;
	}}
		echo "</tr>";
//Amount
	echo "<tr class='tdView'><td>".$array[8]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='2CL'){
		echo "<td class='blankTbl'></td><td>".$key->qty."</td><td></td>" ;
	}}
		echo "</tr>";
//Delivery date
	echo "<tr class='tdView'><td>".$array[9]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='2CL'){
		echo "<td class='blankTbl'></td><td>".$key->delivery_date."</td><td></td>" ;
	}}
		echo "</tr>";

//Note
	echo "<tr class='tdView'><td>".$array[10]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='2CL'){
		echo "<td class='blankTbl'></td><td></td><td></td>" ;
	}}
		echo "</tr>";
//Note
	echo "<tr class='tdView'><td>".$array[11]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='2CL'){
		echo "<td class='blankTbl'></td><td></td><td></td>" ;
	}}
		echo "</tr>";
//}

?>


</table>
<br/>
* Auto Generated

<?php 
} //end if
} 
////////////////////////// close if == '2CL' //////////////////////////

////////////////////////// 3CM //////////////////////////
$j=0;
if(!strcmp($key->next_process,'3CM'))
{
if($threeCMflag==0)
{
$threeCMflag++;
$st = 25;
$speed = 60;
$machine_name = '3CM';
$firstTime = (0.0006949*60)*8+(0.0006949*0);
$timeStart = $firstTime;
$flute = 'B';

?>
<h2>
	<div align=center>Convertor plan: <?=$plandate?></div>
</h2>
<table>
	<tr class='tdLabel'>
		<td>Machine</td>
		<td>Item</td>
		<?php foreach ($resultConvertor->result() as $key){
		if($key->next_process=='3CM'){?>
		<td colspan='3'>Order<?=++$j?></td>
		<?php }} ?>
	</tr>
	<tr class='tdView'>
	<td rowspan='13'><?=$machine_name?></td>
	</tr>

	
<?php

//color
	echo "<tr class='tdView'><td>".$array[0]."</td>";
	foreach ($resultConvertor->result() as $key){
		if($key->next_process=='3CM'){
		if ($key->ink_1!= '') $result = $key->ink_1; 
		else $result ='';
		if ($key->ink_2!= '') $result = $result.','.$key->ink_2; 
		if ($key->ink_3!= '') $result = $result.','.$key->ink_3;
		if ($key->ink_4!= '') $result = $result.','.$key->ink_4;

		echo "<td></td>	<td colspan='2'>".$result."</td>";
	}}
echo "</tr>";
//time
	echo "<tr class='tdView'><td>".$array[1]."</td>";
	foreach ($resultConvertor->result() as $key){
		if($key->next_process=='3CM'){
		$timeuse = $key->qty / $speed;
		
		$timeStop = $timeStart + round($timeuse+30) * 0.0006949;

		echo "<td>ST</td><td>".formatDate($timeStart)."</td><td>".formatDate($timeStop)."</td>" ;
		$timeStart = $timeStop;
	}}
		
		echo "</tr>";
//speed
	echo "<tr class='tdView'><td>".$array[2]."</td>";
	foreach ($resultConvertor->result() as $key){
		if($key->next_process=='3CM'){
		$timeuse = $key->qty / $speed;
		echo "<td>".$st."</td><td class='blankTbl'>".$speed."</td><td>".round($timeuse,2)."</td>" ;
	}}
		echo "</tr>";
//sale order
	echo "<tr class='tdView'><td>".$array[3]."</td>";
	foreach ($resultConvertor->result() as $key){
		if($key->next_process=='3CM'){
		echo "<td class='blankTbl'></td><td>".$key->sales_order."</td><td></td>" ;
	}}
		echo "</tr>";
//Order No.
	echo "<tr class='tdView'><td>".$array[4]."</td>";
	$path = "/planning/barcode/".$key->autoid."/";
	foreach ($resultConvertor->result() as $key){
		if($key->next_process=='3CM'){
		echo "<td class='blankTbl'></td><td><img src='".site_url($path)."' /><br>".$key->autoid."</td><td class='blankTbl'></td>" ;
	}}
		echo "</tr>";
//P code / Po. No.
	echo "<tr class='tdView'><td>".$array[5]."</td>";
	foreach ($resultConvertor->result() as $key){
		if($key->next_process=='3CM'){
		echo "<td>".$flute."</td><td>".$key->product_code."</td><td>".substr($key->product_code,3,3)."</td>" ;
	}}
		echo "</tr>";
//Customer
	echo "<tr class='tdView'><td>".$array[6]."</td>";
	foreach ($resultConvertor->result() as $key){
		if($key->next_process=='3CM'){
		echo "<td class='blankTbl'></td><td>".$key->partner_name."</td><td></td>" ;
	}}
		echo "</tr>";
//Product name
	echo "<tr class='tdView'><td>".$array[7]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CM'){
		echo "<td class='blankTbl'></td><td>".$key->product_name."</td><td></td>" ;
	}}
		echo "</tr>";
//Amount
	echo "<tr class='tdView'><td>".$array[8]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CM'){
		echo "<td class='blankTbl'></td><td>".$key->qty."</td><td></td>" ;
	}}
		echo "</tr>";
//Delivery date
	echo "<tr class='tdView'><td>".$array[9]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CM'){
		echo "<td class='blankTbl'></td><td>".$key->delivery_date."</td><td></td>" ;
	}}
		echo "</tr>";

//Note
	echo "<tr class='tdView'><td>".$array[10]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CM'){
		echo "<td class='blankTbl'></td><td></td><td></td>" ;
	}}
		echo "</tr>";
//Note
	echo "<tr class='tdView'><td>".$array[11]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CM'){
		echo "<td class='blankTbl'></td><td></td><td></td>" ;
	}}
		echo "</tr>";
//}

?>


</table>
<br/>
* Auto Generated

<?php 
}//end if threeCMflag 
}
////////////////////////// close if == '3CM' //////////////////////////


////////////////////////// 3CL //////////////////////////
$j=0;
if(!strcmp($key->next_process,'3CL'))
{
if($threeCLflag==0)
{
$threeCLflag++;
$st = 25;
$speed = 60;
$machine_name = '3CL';
$firstTime = (0.0006949*60)*8+(0.0006949*0);
$timeStart = $firstTime;
$flute = 'B';

?>
<h2>
	<div align=center>Convertor plan: <?=$plandate?></div>
</h2>
<table>
	<tr class='tdLabel'>
		<td>Machine</td>
		<td>Item</td>
		<?php foreach ($resultConvertor->result() as $key){
		if($key->next_process=='3CL'){?>
		<td colspan='3'>Order<?=++$j?></td>
		<?php }} ?>
	</tr>
	<tr class='tdView'>
	<td rowspan='13'><?=$machine_name?></td>
	</tr>

	
<?php

//color
	echo "<tr class='tdView'><td>".$array[0]."</td>";
	foreach ($resultConvertor->result() as $key){
		if($key->next_process=='3CL'){
		if ($key->ink_1!= '') $result = $key->ink_1; 
		else $result ='';
		if ($key->ink_2!= '') $result = $result.','.$key->ink_2; 
		if ($key->ink_3!= '') $result = $result.','.$key->ink_3;
		if ($key->ink_4!= '') $result = $result.','.$key->ink_4;

		echo "<td></td>	<td colspan='2'>".$result."</td>";
	}}
echo "</tr>";
//time
	echo "<tr class='tdView'><td>".$array[1]."</td>";
	foreach ($resultConvertor->result() as $key){
		if($key->next_process=='3CL'){
		$timeuse = $key->qty / $speed;
		
		$timeStop = $timeStart + round($timeuse+30) * 0.0006949;

		echo "<td>ST</td><td>".formatDate($timeStart)."</td><td>".formatDate($timeStop)."</td>" ;
		$timeStart = $timeStop;
	}}
		
		echo "</tr>";
//speed
	echo "<tr class='tdView'><td>".$array[2]."</td>";
	foreach ($resultConvertor->result() as $key){
		if($key->next_process=='3CL'){
		$timeuse = $key->qty / $speed;
		echo "<td>".$st."</td><td class='blankTbl'>".$speed."</td><td>".round($timeuse,2)."</td>" ;
	}}
		echo "</tr>";
//sale order
	echo "<tr class='tdView'><td>".$array[3]."</td>";
	foreach ($resultConvertor->result() as $key){
		if($key->next_process=='3CL'){
		echo "<td class='blankTbl'></td><td>".$key->sales_order."</td><td></td>" ;
	}}
		echo "</tr>";
//Order No.
	echo "<tr class='tdView'><td>".$array[4]."</td>";
	$path = "/planning/barcode/".$key->autoid."/";
	foreach ($resultConvertor->result() as $key){
		if($key->next_process=='3CL'){
		echo "<td class='blankTbl'></td><td><img src='".site_url($path)."' /><br>".$key->autoid."</td><td class='blankTbl'></td>" ;
	}}
		echo "</tr>";
//P code / Po. No.
	echo "<tr class='tdView'><td>".$array[5]."</td>";
	foreach ($resultConvertor->result() as $key){
		if($key->next_process=='3CL'){
		echo "<td>".$flute."</td><td>".$key->product_code."</td><td>".substr($key->product_code,3,3)."</td>" ;
	}}
		echo "</tr>";
//Customer
	echo "<tr class='tdView'><td>".$array[6]."</td>";
	foreach ($resultConvertor->result() as $key){
		if($key->next_process=='3CL'){
		echo "<td class='blankTbl'></td><td>".$key->partner_name."</td><td></td>" ;
	}}
		echo "</tr>";
//Product name
	echo "<tr class='tdView'><td>".$array[7]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CL'){
		echo "<td class='blankTbl'></td><td>".$key->product_name."</td><td></td>" ;
	}}
		echo "</tr>";
//Amount
	echo "<tr class='tdView'><td>".$array[8]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CL'){
		echo "<td class='blankTbl'></td><td>".$key->qty."</td><td></td>" ;
	}}
		echo "</tr>";
//Delivery date
	echo "<tr class='tdView'><td>".$array[9]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CL'){
		echo "<td class='blankTbl'></td><td>".$key->delivery_date."</td><td></td>" ;
	}}
		echo "</tr>";

//Note
	echo "<tr class='tdView'><td>".$array[10]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CL'){
		echo "<td class='blankTbl'></td><td></td><td></td>" ;
	}}
		echo "</tr>";
//Note
	echo "<tr class='tdView'><td>".$array[11]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CL'){
		echo "<td class='blankTbl'></td><td></td><td></td>" ;
	}}
		echo "</tr>";
//}

?>


</table>
<br/>
* Auto Generated

<?php 
}//end if threeCLflag 
}
////////////////////////// close if == '3CL' //////////////////////////


////////////////////////// 3CS //////////////////////////
if(!strcmp($key->next_process,'3CS'))
{
if($threeCSflag ==0)
{
$threeCSflag++;
$st = 45;
$speed = 120;
$machine_name = '3CS';
//initial time start
$firstTime = (0.0006949*60)*8+(0.0006949*0);
$timeStart = $firstTime;
$flute = 'B';


?>
<h2>
	<div align=center>Convertor plan: <?=$plandate?></div>
</h2>
<table>
	<tr class='tdLabel'>
		<td>Machine</td>
		<td>Item</td>
		<?php foreach ($resultConvertor->result() as $key){
		if($key->next_process=='3CS'){?>
		<td colspan='3'>Order<?=++$j?></td>
		<?php }} ?>
	</tr>
	<tr class='tdView'>
	<td rowspan='13'><?=$machine_name?></td>
	</tr>

	
<?php

//color
	echo "<tr class='tdView'><td>".$array[0]."</td>";
	foreach ($resultConvertor->result() as $key){
		if($key->next_process=='3CS'){
		if ($key->ink_1!= '') $result = $key->ink_1; 
		else $result ='';
		if ($key->ink_2!= '') $result = $result.','.$key->ink_2; 
		if ($key->ink_3!= '') $result = $result.','.$key->ink_3;
		if ($key->ink_4!= '') $result = $result.','.$key->ink_4;

		echo "<td></td>	<td colspan='2'>".$result."</td>";
	}}
echo "</tr>";
//time
	echo "<tr class='tdView'><td>".$array[1]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CS'){
		$timeuse = $key->qty /$speed;
		//time for preparation 30 mins
		$timeStop = $timeStart + round($timeuse+30) * 0.0006949;
		//echo $timeStop;
		echo "<td>ST</td><td>".formatDate($timeStart)."</td><td>".formatDate($timeStop)."</td>" ;
		$timeStart = $timeStop;
	}}

		echo "</tr>";
//speed
	echo "<tr class='tdView'><td>".$array[2]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CS'){
		$timeuse = $key->qty / $speed;
		echo "<td>".$st."</td><td class='blankTbl'>".$speed."</td><td>".round($timeuse,2)."</td>" ;
	}}
		echo "</tr>";
//sale order
	echo "<tr class='tdView'><td>".$array[3]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CS'){
		echo "<td class='blankTbl'></td><td>".$key->sales_order."</td><td></td>" ;
	}}
		echo "</tr>";
//Order No.
	echo "<tr class='tdView'><td>".$array[4]."</td>";
	$path = "/planning/barcode/".$key->autoid."/";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CS'){
		echo "<td class='blankTbl'></td><td><img src='".site_url($path)."' /><br>".$key->autoid."</td><td class='blankTbl'></td>" ;
	}}
		echo "</tr>";
//P code / Po. No.
	echo "<tr class='tdView'><td>".$array[5]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CS'){
		echo "<td>".$flute."</td><td>".$key->product_code."</td><td>".substr($key->product_code,3,3)."</td>" ;
	}}
		echo "</tr>";
//Customer
	echo "<tr class='tdView'><td>".$array[6]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CS'){
		echo "<td class='blankTbl'></td><td>".$key->partner_name."</td><td></td>" ;
	}}
		echo "</tr>";
//Product name
	echo "<tr class='tdView'><td>".$array[7]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CS'){
		echo "<td class='blankTbl'></td><td>".$key->product_name."</td><td></td>" ;
	}}
		echo "</tr>";
//Amount
	echo "<tr class='tdView'><td>".$array[8]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CS'){
		echo "<td class='blankTbl'></td><td>".$key->qty."</td><td></td>" ;
	}}
		echo "</tr>";
//Delivery date
	echo "<tr class='tdView'><td>".$array[9]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CS'){
		echo "<td class='blankTbl'></td><td>".$key->delivery_date."</td><td></td>" ;
	}}
		echo "</tr>";

//Note
	echo "<tr class='tdView'><td>".$array[10]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CS'){
		echo "<td class='blankTbl'></td><td></td><td></td>" ;
	}}
		echo "</tr>";
//Note
	echo "<tr class='tdView'><td>".$array[11]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CS'){
		echo "<td class='blankTbl'></td><td></td><td></td>" ;
	}}
		echo "</tr>";
//}

?>


</table>
<br/>
* Auto Generated

<?php 
}//end if threeCSflag 
}
////////////////////////// close if == '3CS' //////////////////////////
$j=0;
////////////////////////// 3CW //////////////////////////

if(!strcmp($key->next_process,'3CW'))
{
if($threeCWflag ==0)
{
$threeCWflag++;
$st = 25;
$speed = 60;
$machine_name = '3CW';
$firstTime = (0.0006949*60)*8+(0.0006949*0);
$timeStart = $firstTime;
$flute = 'B';

?>
<h2>
	<div align=center>Convertor plan: <?=$plandate?></div>
</h2>
<table>
	<tr class='tdLabel'>
		<td>Machine</td>
		<td>Item</td>
		<?php	foreach ($resultConvertor->result() as $key){
		if($key->next_process=='3CW'){ ?>
		<td colspan='3'>Order<?=++$j?></td>
		<?php }} ?>
	</tr>
	<tr class='tdView'>
	<td rowspan='13'><?=$machine_name?></td>
	</tr>

	
<?php

//color
	echo "<tr class='tdView'><td>".$array[0]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CW'){
		if ($key->ink_1!= '') $result = $key->ink_1; 
		else $result ='';
		if ($key->ink_2!= '') $result = $result.','.$key->ink_2; 
		if ($key->ink_3!= '') $result = $result.','.$key->ink_3;
		if ($key->ink_4!= '') $result = $result.','.$key->ink_4;

		echo "<td></td>	<td colspan='2'>".$result."</td>";
	}}
echo "</tr>";
//time
	echo "<tr class='tdView'><td>".$array[1]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CW'){
		$timeuse = $key->qty / $speed;
		
		$timeStop = $timeStart + round($timeuse+30) * 0.0006949;

		echo "<td>ST</td><td>".formatDate($timeStart)."</td><td>".formatDate($timeStop)."</td>" ;
		$timeStart = $timeStop;
	}}
		
		echo "</tr>";
//speed
	echo "<tr class='tdView'><td>".$array[2]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CW'){
		$timeuse = $key->qty / $speed;
		echo "<td>".$st."</td><td class='blankTbl'>".$speed."</td><td>".round($timeuse,2)."</td>" ;
	}}
		echo "</tr>";
//sale order
	echo "<tr class='tdView'><td>".$array[3]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CW'){
		echo "<td class='blankTbl'></td><td>".$key->sales_order."</td><td></td>" ;
	}}
		echo "</tr>";
//Order No.
	echo "<tr class='tdView'><td>".$array[4]."</td>";
	$path = "/planning/barcode/".$key->autoid."/";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CW'){
		echo "<td class='blankTbl'></td><td><img src='".site_url($path)."' /><br>".$key->autoid."</td><td class='blankTbl'></td>" ;
	}}
		echo "</tr>";
//P code / Po. No.
	echo "<tr class='tdView'><td>".$array[5]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CW'){
		echo "<td>".$flute."</td><td>".$key->product_code."</td><td>".substr($key->product_code,3,3)."</td>" ;
	}}
		echo "</tr>";
//Customer
	echo "<tr class='tdView'><td>".$array[6]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CW'){
		echo "<td class='blankTbl'></td><td>".$key->partner_name."</td><td></td>" ;
	}}
		echo "</tr>";
//Product name
	echo "<tr class='tdView'><td>".$array[7]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CW'){
		echo "<td class='blankTbl'></td><td>".$key->product_name."</td><td></td>" ;
	}}
		echo "</tr>";
//Amount
	echo "<tr class='tdView'><td>".$array[8]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CW'){
		echo "<td class='blankTbl'></td><td>".$key->qty."</td><td></td>" ;
	}}
		echo "</tr>";
//Delivery date
	echo "<tr class='tdView'><td>".$array[9]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CW'){
		echo "<td class='blankTbl'></td><td>".$key->delivery_date."</td><td></td>" ;
	}}
		echo "</tr>";

//Note
	echo "<tr class='tdView'><td>".$array[10]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CW'){
		echo "<td class='blankTbl'></td><td></td><td></td>" ;
	}}
		echo "</tr>";
//Note
	echo "<tr class='tdView'><td>".$array[11]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='3CW'){
		echo "<td class='blankTbl'></td><td></td><td></td>" ;
	}}
		echo "</tr>";
//}

?>


</table>
<br/>
* Auto Generated

<?php 
} //end if flag 
}
////////////////////////// close if == '3CW' //////////////////////////
$j=0;
////////////////////////// 2CS //////////////////////////
if(!strcmp($key->next_process,'2CS'))
{
if($twoCSflage ==0)
{
$twoCSflage++;

$st = 25;
$speed = 60;
$machine_name = '2CS';
$firstTime = (0.0006949*60)*8+(0.0006949*0);
$timeStart = $firstTime;
$flute = 'B';

?>
<h2>
	<div align=center>Convertor plan: <?=$plandate?></div>
</h2>
<table>
	<tr class='tdLabel'>
		<td>Machine</td>
		<td>Item</td>
		<?php	foreach ($resultConvertor->result() as $key){
		if($key->next_process=='2CS'){ ?>
		<td colspan='3'>Order<?=++$j?></td>
		<?php }} ?>
	</tr>
	<tr class='tdView'>
	<td rowspan='13'><?=$machine_name?></td>
	</tr>

	
<?php

//color
	echo "<tr class='tdView'><td>".$array[0]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='2CS'){
		if ($key->ink_1!= '') $result = $key->ink_1; 
		else $result ='';
		if ($key->ink_2!= '') $result = $result.','.$key->ink_2; 
		if ($key->ink_3!= '') $result = $result.','.$key->ink_3;
		if ($key->ink_4!= '') $result = $result.','.$key->ink_4;

		echo "<td></td>	<td colspan='2'>".$result."</td>";
	}}
echo "</tr>";
//time
	echo "<tr class='tdView'><td>".$array[1]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='2CS'){
		$timeuse = $key->qty / $speed;
		
		$timeStop = $timeStart + round($timeuse+30) * 0.0006949;

		echo "<td>ST</td><td>".formatDate($timeStart)."</td><td>".formatDate($timeStop)."</td>" ;
		$timeStart = $timeStop;
		}}
		echo "</tr>";
//speed
	echo "<tr class='tdView'><td>".$array[2]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='2CS'){
		$timeuse = $key->qty / $speed;
		echo "<td>".$st."</td><td class='blankTbl'>".$speed."</td><td>".round($timeuse)."</td>" ;
	}}
		echo "</tr>";
//sale order
	echo "<tr class='tdView'><td>".$array[3]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='2CS'){
		echo "<td class='blankTbl'></td><td>".$key->sales_order."</td><td></td>" ;
	}}
		echo "</tr>";
//Order No.
	echo "<tr class='tdView'><td>".$array[4]."</td>";
	$path = "/planning/barcode/".$key->autoid."/";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='2CS'){
		echo "<td class='blankTbl'></td><td><img src='".site_url($path)."' /><br>".$key->autoid."</td><td class='blankTbl'></td>" ;
	}}
		echo "</tr>";
//P code / Po. No.
	echo "<tr class='tdView'><td>".$array[5]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='2CS'){
		echo "<td>".$flute."</td><td>".$key->product_code."</td><td>".substr($key->product_code,3,3)."</td>" ;
	}}
		echo "</tr>";
//Customer
	echo "<tr class='tdView'><td>".$array[6]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='2CS'){
		echo "<td class='blankTbl'></td><td>".$key->partner_name."</td><td></td>" ;
	}}
		echo "</tr>";
//Product name
	echo "<tr class='tdView'><td>".$array[7]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='2CS'){
		echo "<td class='blankTbl'></td><td>".$key->product_name."</td><td></td>" ;
	}}
		echo "</tr>";
//Amount
	echo "<tr class='tdView'><td>".$array[8]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='2CS'){
		echo "<td class='blankTbl'></td><td>".$key->qty."</td><td></td>" ;
	}}
		echo "</tr>";
//Delivery date
	echo "<tr class='tdView'><td>".$array[9]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='2CS'){
		echo "<td class='blankTbl'></td><td>".$key->delivery_date."</td><td></td>" ;
	}}
		echo "</tr>";

//Note
	echo "<tr class='tdView'><td>".$array[10]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='2CS'){
		echo "<td class='blankTbl'></td><td></td><td></td>" ;
	}}
		echo "</tr>";
//Note
	echo "<tr class='tdView'><td>".$array[11]."</td>";
	foreach ($resultConvertor->result() as $key){
	if($key->next_process=='2CS'){
		echo "<td class='blankTbl'></td><td></td><td></td>" ;
	}}
		echo "</tr>";
//} 

?>


</table>
<br/>
* Auto Generated

<?php 
} //end flag 
}
////////////////////////// close if == '2CS' //////////////////////////

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
