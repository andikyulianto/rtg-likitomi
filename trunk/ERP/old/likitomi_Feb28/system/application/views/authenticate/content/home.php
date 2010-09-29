<div id="homeContent">
<h1>Likitomi (Thailand) Co.Ltd.</h1>
<table width='100%'>
	<tr>
		<td>
			<table>
				<tr>
					<td><p><a href="<?=base_url().'index.php/partners/'?>"><?=$this->lang->line('partners')?></a></p></td>
					<td>&nbsp;</td>
					<td><p><a href="<?=base_url().'index.php/products/'?>">Products</a></p></td>
					<td>&nbsp;</td>
					<td><p><a href="<?=base_url().'index.php/papers/'?>">Papers</a></p></td>
				</tr>
			</table>
			<br/><br/>
			<table><tr>
					<td>&nbsp;</td>
					<td><p><a href="<?=base_url().'index.php/salesorder/'?>">Sales Order</a></p></td>
					<td>&nbsp;</td>
					<td><p><a href="<?=base_url().'index.php/planning/'?>">Planning</a></p></td>
					<td>&nbsp;</td>
					<td><p><a href="<?=base_url().'index.php/reportplanning/'?>">Report Planning</a></p></td>
				</tr>
			</table>
			<br/><br/>
			<table><tr>
					<td>&nbsp;</td>
					<td><p><a href="<?=base_url().'index.php/warehouse/'?>">Warehouse</a></p></td>
					<td>&nbsp;</td>
					<td><p><a href="<?=base_url().'index.php/clampliftmanger/'?>">Clamplift Manager</a></p></td>
				</tr>
			</table>
			<br/><br/>
			<table><tr>
					<td>&nbsp;</td>
					<td><p><a href="<?=base_url().'index.php/translator/'?>">Translation</a></p></td>
				</tr>
			</table>
		</td>

		<td align='right' valign='top'>
			<table>
				<tr>
					<td> <b>Current Language : <?=$this->db_session->userdata('language')?> </b></td>
				</tr><tr>
					<td><p><a href="<?=base_url().'index.php/home/setlang/en'?>" >English</a></td>
				</tr><tr>
					<td><p><a href="<?=base_url().'index.php/home/setlang/th'?>">Thai</a></td>
				</tr>
			</table>
		</td>
	</tr>
</table>
</div><!-- /content -->