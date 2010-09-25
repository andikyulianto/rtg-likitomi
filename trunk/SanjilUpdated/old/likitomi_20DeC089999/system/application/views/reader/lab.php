<style type="text/css">
	table {
	    border-collapse: collapse;
	}
	img{
		padding:0px;
		margin:0px
	}
	#map td {
	    padding: 10px 11px;
	}
	#datetime {
	    font-size: 120%;
	    font-weight: bold;
	}
	a{
		color:transparent;
		text-decoration:none;
	}
</style>
<script language="JavaScript">
    document.onkeydown = checkKeycode
    function checkKeycode(e){
        var keycode;
        if (window.event) 
            keycode = window.event.keyCode;
        else 
            if (e) 
                keycode = e.which;
        if(keycode == 37 ){
			location.href="<?=base_url().'index.php/reader/lab/'.($filecnt-1).'/'.$ant?>";
		}
		if(keycode == 39 ){
			location.href="<?=base_url().'index.php/reader/lab/'.($filecnt+1).'/'.$ant?>";
		}
		
    }
	function showindex(index)
	{
		document.getElementById('tblindex').innerHTML=index;
	}
</script>

<?php 
$flagA1 = false;
$flagA4 = false;
if($ant==1) $flagA1 = true;
if($ant==4) $flagA4 = true;
if($ant==5) {
	$flagA1 = true;
	$flagA4 = true;
}
$ant1 = explode(',', $antenna1, 100);
$ant4 = explode(',', $antenna4, 100);

$tag = array(
			"0","68","70","74","76","79","81","0","0","0",
			"14","1","12","23","34","45","56","67","78","0",
			"0","2","13","24","35","46","57","-1","-1","0",
			"15","3","-1","25","-1","47","58","69","80","0",
			"20","4","-1","26","-1","48","59","-1","-1","0",
			"21","5","16","27","38","49","60","71","82","0",
			"36","6","17","28","39","50","61","72","83","0",
			"37","7","18","29","40","51","62","73","84","87",
			"0","8","19","30","41","52","63","-1","-1","0",
			"0","9","-1","31","-1","53","64","75","86","0",
			"0","10","-1","32","-1","54","65","-1","-1","0",
			"42","11","22","33","44","55","66","77","88","0",
			"0","43","85","0","0","0","0","0","0","0","0","0",
			);
?>
<table width='100%' >
<tr>

	<td>
		
<center>
<table id='map' border=1>
<?php
	$cnt=0;
	$x = 0;
	$y = 0;
	$xycnt=0;$xround = 0;$yround = 0;
	for($i=0;$i<=12;$i++)
	{
		echo "<tr>";
		for($j=0;$j<10;$j++)
		{
			$tagcnt = $tag[$cnt];
			if($tagcnt=="0")  $title = "0";
			else if($tagcnt=="-1") $title = "-1";
			else if($tagcnt<100) {
				$title = 0;
				if($flagA1) $title += $ant1[$tagcnt];
				if($flagA4) $title += $ant4[$tagcnt];
				if($ant1[$tagcnt]>0) 
				{
					$x = $x + $i+1;
					$y=  $y + $j+1;
					$xycnt++;
				}
			}
			else $title = $tagcnt;
			echo "<td id='".($i+1).($j+1)."' width='26px' height='26px' bgcolor='#".getClass($title).";' onclick='showindex(".$tag[$cnt].")'>".getTitle($title)."</td>";
			$cnt++;
		}
		echo "</tr>";
	}
	if($xycnt>0) 
	{
		$xround = round($x/$xycnt);
		$yround = round($y/$xycnt);
	}
?>
</table>
<table width="522px" cellspacing="1" cellpadding="4" border="0">
    <tbody>
        <tr>
            <td width="25%" height='20px' bgcolor="#daf3cb" align="center"></td>
            <td width="25%" bgcolor="#aade8a" align="center"></td>
            <td width="25%" bgcolor="#6dc738" align="center"></td>
            <td width="25%" bgcolor="#4e991f" align="center"></td>
        </tr>
        <tr>
            <td nowrap="nowrap" align="center">
                <span class="c">1 - 30</span>
            </td>
            <td nowrap="nowrap" align="center">
                <span class="c">31 - 75</span>
            </td>
            <td nowrap="nowrap" align="center">
                <span class="c">76 - 150</span>
            </td>
            <td nowrap="nowrap" align="center">
                <span class="c">151+</span>
            </td>
        </tr>
    </tbody>
</table>
</center>
	</td>
		<td valign='top'>
		<table width='100%' bgcolor="#DDDDDD">
			<tr>
				<td align='left'><a href="<?=base_url().'index.php/reader/lab/'.($filecnt-1).'/'.$ant?>" ><img src="<?=base_url().'/static/images/2leftarrow.png'?>" /> </a></td>
				<td><p id='datetime' align='center'><?=$datetime?></p></td>
				<td align='right'><a href="<?=base_url().'index.php/reader/lab/'.($filecnt+1).'/'.$ant?>" ><img src="<?=base_url().'/static/images/2rightarrow.png'?>" /></a></td>
			</tr>
		</table>
		<table width='100%' bgcolor="#EEEEEE">
			<tr>
				<td align='right'><span id='tblindex' align='right'></span></td>
			</tr>
			<tr>
				<td align='right'>XY <?=$xround?>, <?=$yround?>  </td>
			</tr>
		</table>		
	</td>
</tr>
</table>
<?php 

function getClass($cnt){
	if($cnt == "-1") return "dddddddd";
	else if($cnt >= 1 && $cnt < 30) return "daaf33cb";
	else if($cnt >= 30 && $cnt < 75) return "aadde88a";
	else if($cnt >= 75 && $cnt < 150) return "6ddc7738";
	else if($cnt >= 150) return "4ee9991f";
	
	return "ffffffff";
}
function getTitle($cnt)
{
	if($cnt=="0") return "&nbsp;";
	else if($cnt=="-1") return "&nbsp;";
	return "(".$cnt.")";
		
}
?>

<script>
	window.onload = function() {
		document.getElementById('<?=$xround.$yround?>').innerHTML="<img src=\'<?=base_url().'static/images/pin.gif'?>\' />";
	}
</script>
