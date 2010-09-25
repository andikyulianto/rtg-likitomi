<script type="text/javascript">
	window.addEvent('domready',function() { new SmoothScroll({ duration: 800 }); });
	var firstrowoffset = 0;
	var lastrowoffset = 0; 
	var id = 0; var paper_code="";
	function mainFunction(){
    // basic tabs 1, built from existing content
	    var tabs = new Ext.TabPanel({
	        renderTo: 'clamplifttabs',
	        activeTab: 0,
	        frame:false,
			border:false,
			plain:true,
	        defaults:{autoHeight: true},
	        items:[
	            {contentEl:'inmachinediv', title: ' In Machine '},
	            {contentEl:'nexttasksdiv', title: ' Next 5 Tasks '},
				{contentEl:'nextinusediv', title: ' Next In Use '},
	        ]
	    });
	}
	function paperPick(id,mname){
		Ext.Ajax.request({
			url: BASEURL + 'index.php/clamplift/paperPick/',
			params : { id: id, mname: mname },
			success: function ( result, request ) { 
				document.getElementById('clampliftcontainer').innerHTML = result.responseText;
				unloadAjax();
				Ext.onReady(mainFunction);
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});
		Ext.Ajax.on({
		    'beforerequest': function(){
				loadAjax("<?=$this->lang->line('ajax_loading_tasklist')?>");
			},
		    'requestcomplete': function(){
				unloadAjax();
			}
		});
	}
</script>

<div id='clampliftcontainer' >
<?php
global $inmachinecnt, $inqueuecnt, $finishedcnt, $totaltask;
$inmachinecnt=0;
$inqueuecnt=0;
$finishedcnt =0;
$totaltask =0;
?>

<?php $section = array($this->lang->line('Morning'),$this->lang->line('Afternoon'),$this->lang->line('Evening'),$this->lang->line('Late_Night')); ?>

<div id="headbar-background"></div>
<div id='headbar-short'>
	<table>
		<thead><tr>
			<td class='firstcell'>&nbsp;</td>
			<td class='middlecell'>DF</td>
			<td class='middlecell'>BM</td>
			<td class='middlecell'>BL</td>
			<td class='middlecell'>CM</td>
			<td class='middlecell'>CL</td>
		</tr></thead>
	</table>
</div>
<div id="sidebar-background"></div>
<div id="sidebar">
		
	<div id='clock' onclick='Ext.onReady(all);'>
		<center><object width="120" height="35">
			<param name="movie" value="<?=base_url().'static/flash/digitalclock.swf'?>">
			<embed src="<?=base_url().'static/flash/digitalclock.swf'?>" width="120" height="35">
			</embed>
		</object></center>
	</div>

	<table id="ewlistmain" class="ewTable">
		<!-- Table body -->
		<tr onmouseover='ew_MouseOver(this);' onmouseout='ew_MouseOut(this);' class='ewTableRow'>
			<td><a id='now' onclick='ea_Click(0)' href="#0"><?=$this->lang->line('Now')?></a></td>
		</tr>
		<?php for($i=0;$i<$totalSec;$i++) { ?> 
		<tr onmouseover='ew_MouseOver(this);' onmouseout='ew_MouseOut(this);' class='ewTableRow'>
			<td><a onclick='ea_Click(<?=($i+1)?>)' href="#<?=($i*$interval)?>"><?=$section[$i]?></a></td>
		</tr>
		<?php } ?>
	</table>
	<br/>
	<br/>
	
	<div style="font-size:90%" >
	<table class="ewTable">
		<tr class='ewTableRow'>
			<td>Total</td>
			<td align='right'><span class='counter' id='totaltask'></span></td>
		</tr>
		<tr class='ewTableRow'>
			<td>Completed</td>
			<td align='right'><span class='counter' id='finished'></span></td>
		</tr>
		<tr class='ewTableRow'>
			<td>Left to Pick</td>
			<td align='right'><span class='counter' id='queue'></span></td>
		</tr>
		<tr class='ewTableRow'>
			<td>Left to Drop</td>
			<td align='right'><span class='counter' id='inmachine'></span></td>
		</tr>
	</table></div>
</div>

<div id="content">
	<a name="0" id="0"></a>
	<br/>
	<br/>
<table class='taskTBL'>
	<tbody>
<?php

$RowCnt = 0; 
foreach ($taskTable as $task)
{
	if ($RowCnt % 2 == 0) $rowClass = "even";
	else $rowClass = "odd";
	if ($now == $RowCnt)
	{
		$rowClass ="highlight";	
		$now=$RowCnt;
	}
	$RowCnt++;
?>
	<tr class='<?=$rowClass?>'>
		<td class='firstcell '>
			<a name="<?=$RowCnt?>" id="<?=$RowCnt?>"></a>
			<a href="#<?=($RowCnt>1)?($RowCnt-1):0?>"><?=$task['time']?></a>
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
</div> <!--End of Container -->

<?php
	function printItem($id,$data,$class,$pono,$mname)
	{
		global $inmachinecnt, $inqueuecnt, $finishedcnt,$totaltask;
		$totaltask++;
		$output ="";
		$onclick ="";
		$statuslist = array('queue','inmachine','finished');
		
		switch($statuslist[$class]){
			case "inmachine": 
				$inmachinecnt++; 
				$onclick=""; 
				break;
			case "queue": 
				$inqueuecnt++; 
				$onclick='paperPick("'.$id.'","'.$mname.'");';
				break;
			case "finished": 
				$finishedcnt++; 
				$onclick="";
				break;
		}	
		if($data !="") 
		{
			$output ="<div id='itemdiv'";
			$output .= " onclick='".$onclick."'";
			$output .= " class='".$statuslist[$class]."'>".$data."<br/>".$pono."<br/>A11</div>";
		}
		return $output;
	}
?>

<script type='text/javascript'>
	var now_temp = <?=$now?>;
	if(now_temp > 0)document.getElementById('now').setAttribute('href','#'+now_temp+'');
	<?php
		global $inmachinecnt, $inqueuecnt, $finishedcnt,$totaltask;
		echo "document.getElementById('totaltask').innerHTML='$totaltask';";
		echo "document.getElementById('inmachine').innerHTML='$inmachinecnt';";
		echo "document.getElementById('queue').innerHTML='$inqueuecnt';";
		echo "document.getElementById('finished').innerHTML='$finishedcnt';";
	?>
</script>
</div>