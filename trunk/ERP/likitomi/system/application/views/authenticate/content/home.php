<div id="homeContent">
<h1>Likitomi (Thailand) Co.Ltd.</h1>
<table width='100%'>
	<tr>
		<td>
			<table>
				<tr>
					<td><p><a href="<?=base_url().'index.php/partners/'?>"><?=$this->lang->line('partners')?></a></p></td>
					<td>&nbsp;</td>
					<td><p><a href="<?=base_url().'index.php/products/'?>"><?=$this->lang->line('products')?></a></p></td>
					<td>&nbsp;</td>
					<td><p><a href="<?=base_url().'index.php/papers/'?>"><?=$this->lang->line('papers')?></a></p></td>
				</tr>
			</table>
			<br/><br/>
			<table><tr>
					<td>&nbsp;</td>
					<td><p><a href="<?=base_url().'index.php/salesorder/'?>"><?=$this->lang->line('salesorder')?></a></p></td>
					<td>&nbsp;</td>
					<td><p><a href="<?=base_url().'index.php/planning/'?>"><?=$this->lang->line('planning')?></a></p></td>
					<td>&nbsp;</td>
					<td><p><a href="<?=base_url().'index.php/reportplanning/'?>"><?=$this->lang->line('reportplanning')?></a></p></td>
				</tr>
			</table>
			<br/><br/>
			<table><tr>
					<td>&nbsp;</td>
					<td><p><a href="<?=base_url().'index.php/warehouse/'?>"><?=$this->lang->line('warehouse')?></a></p></td>
					<td>&nbsp;</td>
					<td><p><a href="<?=base_url().'index.php/clampliftmanger/'?>"><?=$this->lang->line('clampliftmanger')?></a></p></td>
				</tr>
			</table>
			<br/><br/>
			<table><tr>
					<td>&nbsp;</td>
					<td><p><a href="<?=base_url().'index.php/translator/'?>"><?=$this->lang->line('translator')?></a></p></td>
				</tr>
			</table>
		</td>

		<td align='right' valign='top'>
			<table>
				<tr>
					<td> <b>Current Language : <?=$this->db_session->userdata('language')?> </b></td>
				</tr><tr>
					<td><p><a href="<?=base_url().'index.php/home/setlang/en'?>" ><?=$this->lang->line('english')?></a></td>
				</tr><tr>
					<td><p><a href="<?=base_url().'index.php/home/setlang/th'?>"><?=$this->lang->line('thai')?></a></td>
				</tr>
			</table>
		</td>
	</tr>
</table>
</div><!-- /content -->
