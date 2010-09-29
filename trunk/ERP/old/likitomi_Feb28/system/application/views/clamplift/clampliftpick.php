<?php
require_once("clampliftFunction.php");
?>
<div id="headbar-background"></div>

<div id='headbar-short' style="width:100%;">
	<table>
		<thead><tr >
			<td></td>
			<td align=center width=100%><div>Move From: Warehouse TO Machine:DF</div> </td>
			<td></td>
		</tr></thead>
	</table>
</div>
<br/><br/><br/>
<div id='paperwrapper'>
	<table>
		<tr>
			<td>
				<div id="papercontainer">
					<table> <tr><td>
						<table>
						<tr><td>Paper Code</td><td>HAC125</td></tr>
						<tr><td>Supplier</td><td>HK</td></tr>
						<tr><td>RFID: ID</td><td>1234567890</td></tr>
						<tr><td>Location</td><td>11<br/> Zone A<br/> Outter <br/> TOP</td></tr>
					</table>
					</td>
					<td>
						<table border=1 width='200px' height='100px'>
							<tr>
								<td width='40px'>&nbsp;</td><td width='40px'>&nbsp;</td><td width='40px'>&nbsp;</td><td width='40px'>&nbsp;</td><td width='50px' rowspan=2>ZONE A</td>
							</tr>
							<tr>
								<td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td>
							</tr>
							<tr>
								<td>&nbsp;</td><td>&nbsp;</td><td style='background-color: #D1E9C5;'>&nbsp;</td><td>&nbsp;</td><td rowspan=2>Lane 21</td>
							</tr>
							<tr>
								<td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td>
							</tr>
						</table>
					</td>
					</tr>
					</table>
				</div>
			</td>
			<td></td>
			<td></td>
		</tr>
	</table>
</div>
<br/>
<br/>
<?php
$id=1;$code='PKL250';
?>

<!-- container for the existing markup tabs -->
<div id="clamplifttabs">
	<div id="inmachinediv" class="x-hide-display">
		<?=$clamplift->getPaperByStatus();?>
	</div>
	<div id="nexttasksdiv" class="x-hide-display">
		<?=$clamplift->getNextUse($id,$code);?>
	</div>
	<div id="nextinusediv" class="x-hide-display">
	<?=$clamplift->getNextTask($id);?>
	</div>
</div>
