<table class='taskTBL'>
	<tbody>
<?php

$RowCnt = 0; 
foreach ($taskTable as $task)
{
	if ($RowCnt % 2 == 0) $rowClass = "even";
	else $rowClass = "odd";
	$RowCnt++;
?>
	<tr class='<?=$rowClass?>'>
		<td class='firstcell '>
			<a name="<?=$RowCnt?>" id="<?=$RowCnt?>"></a>
			<?=$task['time']?>
		</td>
		<td class='middlecell'>
			<?php 
				$rowData =  explode('|', $task['rowDF']); 
				for ($i=0;$i<count($rowData);$i+=4){
					echo printItem($rowData[$i],
								$rowData[$i+1],
								substr($rowData[$i+2],0,1),
								$rowData[$i+3],
								"DF");
				}	
			?>
		</td>
		<td class='middlecell'>
			<?php 
				$rowData =  explode('|', $task['rowBM']); 
				for ($i=0;$i<count($rowData);$i+=4){
					echo printItem($rowData[$i],
								$rowData[$i+1],
								substr($rowData[$i+2],1,1),
								$rowData[$i+3],
								"BM");
				}	
			?>
		</td>
		<td class='middlecell'>
			<?php 
				$rowData =  explode('|', $task['rowBL']); 
				for ($i=0;$i<count($rowData);$i+=4){
					echo printItem($rowData[$i],
								$rowData[$i+1],
								substr($rowData[$i+2],2,1),
								$rowData[$i+3],
								"BL");
				}	
			?>
		</td>
		<td class='middlecell'>
			<?php 
				$rowData =  explode('|', $task['rowCM']); 
				for ($i=0;$i<count($rowData);$i+=4){
					echo printItem($rowData[$i],
								$rowData[$i+1],
								substr($rowData[$i+2],3,1),
								$rowData[$i+3],
								"CM");
				}	
			?>
		</td>
		<td class='middlecell'>
			<?php 
				$rowData =  explode('|', $task['rowCL']); 
				for ($i=0;$i<count($rowData);$i+=4){
					echo printItem($rowData[$i],
								$rowData[$i+1],
								substr($rowData[$i+2],4,1),
								$rowData[$i+3],
								"CL");
				}	
			?>
		</td>
	</tr>
<?php 
}?>

	</tbody>
</table>
