<?php
	$today = date("Y-m-d");
	$yesterday = date('Y-m-d', mktime(0, 0, 0, date("m") , date("d") - 1, date("Y")));
?>
<div id='tblDelHistory'>
<table width='100%'>
<?php
if($showheader){
?>
	<thead>
		<th class='DeliveryLabel' width='120px'></th>
		<th class='DeliveryLabel' width='120px'>Delivery Date</th>
		<th class='DeliveryLabel' width='120px'>Delivery Time</th>
		<th class='DeliveryLabel' width='120px'>Quantity</th>
		<th class='DeliveryLabel' width='120px'></th>
		<th class='DeliveryLabel' width='120px'>Last Updated</th>
		
	</thead>

<?php } ?>

<?php	
if($history->num_rows()>0)
{
	foreach($history->result() as $row)
	{
?>
		<tr class='dodd'>

<?php
		switch($row->field){
			case "Quantity": 
?>			
				<td width='120px' ></td>
				<td width='120px' ></td>
				<td width='120px'></td>
				<td width='120px'><span style='color:red'><?=$row->from?></span> to 
					<span style='color:green'><?=$row->to?></span></td>
<?php
				break;
			case "Time": 
?>
				<td width='120px' ></td>
				<td width='120px'></td>
				<td width='120px'><span style='color:red'><?=$row->from?></span> to 
					<span style='color:green'><?=$row->to?></span></td>
				<td width='120px'></td>
<?php
				break;
			case "Date":
?>
				<td colspan=2 width='240px' ><span style='color:red'><?=date("d-m-Y",strtotime($row->from))?></span> to 
					<span style='color:green'><?=date("d-m-Y",strtotime($row->to))?></span></td>
				<td width='120px'></td><td width='120px'></td>
<?php
				break;
			default: 
?>
				<td width='120px'></td>
				<td width='120px'></td>
				<td width='120px'></td>
				<td width='120px'></td>
<?php
		}
?>
		<td width='120px'>
<?php 	if($today==substr($row->created_on,0,10)) echo "Today";
		else if($yesterday==substr($row->created_on,0,10)) echo "Yesterday";
		else echo "";
		echo "</td><td>".$row->created_on."</td></tr>";
	}
}
?>

</table></div>