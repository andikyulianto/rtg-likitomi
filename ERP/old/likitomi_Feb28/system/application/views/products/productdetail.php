    <div id="general" class="x-hide-display paddedDiv" >
    <?php
if ($action=='view'){ 
echo "<div width='100%' style='text-align:right'>";
if($resultProductCatalog->isdeleted!=0){ echo "<span class='alreadyDeleted' width='100%'>".$this->lang->line('msg_alredyarchived')."</span>";}
echo "</div>";
?>
<table width='100%'>
	<input type='hidden' id='x_product_id' value='<?=$resultProductCatalog->product_id?>'>
	<tr>
		<td><div id='nametitle'><?=$resultProductCatalog->product_code?></div>
		<?php if($resultProductCatalog->product_name !=="") echo $resultProductCatalog->product_name."<br/>";?>
		<?php if($customer_name !=="") { echo $customer_name?>
		<?php if($partner_isdeleted!=0) echo '<img title="The partner is deleted" src="'.base_url().'static/images/extjs/warning.gif"/>'; }?>
		</td>
		<td align='right'>
			<a href='<?=base_url()."index.php/salesorder/reportCatalog/".$resultProductCatalog->product_id?>' target='_blank'>
				<img class='imglink' src='<?=base_url()."static/images/extjs/printer.png"?>' 
					title="Preview Sales Catalog" />
			</a>
		</td>
	</tr>
</table>
<br/>

<div id='boxcontainer'>
<table>
	<tr>
        <td class='tblDetailViewLabel'>Part No.</td>
		<td class='tblDetailView'><?=$resultProductCatalog->customer_part_no?></td>
		<td class='tblDetailViewLabel'>Product Type</td>
		<td class='tblDetailView'><?=$resultProductCatalog->product_type?></td>
	</tr>
	</table>
</div>
<br/>
<table class='tblFixedBorder' cellspacing=2 cellpadding=2>
	<tr>
        <td class='tblProdViewLabel'>Code</td>
		<td class='tblProdViewLabel'>Flute</td>
		<td class='tblProdViewLabel'>DF</td>
		<td class='tblProdViewLabel'>BM</td>
		<td class='tblProdViewLabel'>BL</td>
		<td class='tblProdViewLabel'>CM</td>
		<td class='tblProdViewLabel'>CL</td>
		<td class='tblProdViewLabel'>Length</td>
		<td class='tblProdViewLabel'>Width</td>
		<td class='tblProdViewLabel'>Height</td>
		<td class='tblProdViewLabel'>Qty/Set</td>
	</tr>
<?php 
foreach($resultProducts as $prod){
?>	
<tr>
	<td class='tblProdView'><?=$prod->product_code?></td>
	<td class='tblProdView'><?=$prod->flute?></td>
	<td class='tblProdView'><?=$prod->DF?></td>
	<td class='tblProdView'><?=$prod->BM?></td>
	<td class='tblProdView'><?=$prod->BL?></td>
	<td class='tblProdView'><?=$prod->CM?></td>
	<td class='tblProdView'><?=$prod->CL?></td>
	<td class='tblProdView'><?=$prod->Length_mm?></td>
	<td class='tblProdView'><?=$prod->Width_mm?></td>
	<td class='tblProdView'><?=$prod->Height_mm?></td>
	<td class='tblProdView'><?=$prod->qty_set?></td>
</tr>
<?php }?>
</table>
<br/>

<div id='boxcontainer'>
<table>
	<tr>
        <td class='tblDetailViewLabel'>Ink Color 1</td>
		<td class='tblDetailView'><?=$resultProductCatalog->ink_1?></td>
		<td class='tblDetailViewLabel'>Ink Color 2</td>
		<td class='tblDetailView'><?=$resultProductCatalog->ink_2?></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>Ink Color 3</td>
		<td class='tblDetailView'><?=$resultProductCatalog->ink_3?></td>
		<td class='tblDetailViewLabel'>Ink Color 4</td>
		<td class='tblDetailView'><?=$resultProductCatalog->ink_4?></td>
	</tr>
	</table>
</div>
<br/>

<div id='boxcontainer'>
<table>
	<tr>
		<td class='tblDetailViewLabel'>Joint Type</td>
		<td class='tblDetailView'><?=$resultProductCatalog->joint_type?></td>
		<td class='tblDetailViewLabel'>Joint Details</td>
		<td class='tblDetailView'><?=$resultProductCatalog->joint_details?></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>Box Style</td>
		<td class='tblDetailView'><?=$resultProductCatalog->box_style?></td>
		<td class='tblDetailViewLabel'>Rope Color</td>
		<td class='tblDetailView'><?=$resultProductCatalog->rope_color?></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>PCS/Bundle</td>
		<td class='tblDetailView'><?=$resultProductCatalog->pcs_bundle?></td>
		<td class='tblDetailViewLabel'>Level</td>
		<td class='tblDetailView'><?=$resultProductCatalog->level?></td>
	</tr>
	</table>
</div>
<br/>

<div id='boxcontainer'>
<table >
	<tr>
		<td class='tblDetailViewLabel'>Paper Width (mm)</td>
		<td class='tblDetailView'><?=$resultProductCatalog->p_width_mm?></td>
		<td class='tblDetailViewLabel' rowspan=3>Remark</td>
		<td class='tblDetailView' rowspan=2><?=$resultProductCatalog->remark?></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>Paper Width (inch)</td>
		<td class='tblDetailView'><?=$resultProductCatalog->p_width_inch?></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>Qty. Allowance</td>
		<td class='tblDetailView'><?=$resultProductCatalog->qty_allowance?></td>
	</tr>
	
</table>
</div>
<br/>

<div id='boxcontainer'>
<table>
	<tr>
		<td class='tblDetailViewLabel'>Sketch</td>
		<td class='tblDetailView' nowrap>
			<?php if($resultProductCatalog->sketch!='') echo "<a href='".base_url().$resultProductCatalog->sketch."' target='_blank'>".base_url().$resultProductCatalog->sketch."</a>";?>
			&nbsp;
		</td>
		<td></td>
	</tr>
</table>
</div>
<br/>


<div id='boxcontainer'>
<table>
	<tr>
		<td class='tblDetailViewLabel'>Sketch Large</td>
		<td class='tblDetailView' nowrap>
			<?php if($resultProductCatalog->sketch_large!='') echo "<a href='".base_url().$resultProductCatalog->sketch_large."' target='_blank'>".base_url().$resultProductCatalog->sketch_large."</a>";?>
			&nbsp;
		</td>
		<td></td>
	</tr>
</table>
</div>
<br/>

<div id='boxcontainer'>
<table>
	<tr>
		<td class='tblDetailViewLabel'>Code RD</td>
		<td class='tblDetailView'><?=$resultProductCatalog->code_rd?></td>
		<td class='tblDetailViewLabel' rowspan=2>Next Process</td>
		<td class='tblDetailView' rowspan=2><?=$resultProductCatalog->next_process?></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>Code PD</td>
		<td class='tblDetailView'><?=$resultProductCatalog->code_pd?></td>	
	</tr>	
</table>
</div>
<br/>

<div id='boxcontainer'>
<table>
	<tr>
		<td class='tblDetailViewLabel'>Scoreline F</td>
		<td class='tblDetailView'><?=$resultProductCatalog->scoreline_f?></td>
		<td class='tblDetailViewLabel'>Cut</td>
		<td><?=$resultProductCatalog->cut?></td>
	</tr>
	<tr>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>Scoreline D</td>
		<td class='tblDetailView'><?=$resultProductCatalog->scoreline_d?></td>
		<td class='tblDetailViewLabel'>Slit</td>
		<td><?=$resultProductCatalog->slit?></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>Scoreline F2</td>
		<td class='tblDetailView'><?=$resultProductCatalog->scoreline_f2?></td>
		<td class='tblDetailViewLabel'>T. Length</td>
		<td><?=$resultProductCatalog->t_length?></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>Blank</td>
		<td class='tblDetailView'><?=$resultProductCatalog->blank?></td>
		<td class='tblDetailViewLabel' colspan=2>
			<?=$resultProductCatalog->scoreline_f?>+
			<?=$resultProductCatalog->scoreline_d?>+
			<?=$resultProductCatalog->scoreline_f2?>= 
<?php echo ($resultProductCatalog->scoreline_f+$resultProductCatalog->scoreline_d+$resultProductCatalog->scoreline_f2)?>
		</td>		
	</tr>
</table>
</div>
<br/>

<div id='boxcontainer'>
<table>
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('created_on')?></td>
		<td><?=$resultProductCatalog->created_on?></td>
		<td class='tblDetailViewLabel'><?=$this->lang->line('modified_on')?></td>
		<td><?=$resultProductCatalog->modified_on?></td>
	</tr>  
</table>
</div>

<?php
} //End View
?>   

 <?php
 $trows =3;
if (($action=='edit')||($action=='add')){  //Edit  or Add
if($action=='edit'){
	$product_id = $resultProductCatalog->product_id;
	$product_code = $resultProductCatalog->product_code;
	$product_name = $resultProductCatalog->product_name;
	$partner_id = $resultProductCatalog->partner_id;
	$product_type = $resultProductCatalog->product_type;
	$customer_part_no = $resultProductCatalog->customer_part_no;
	$ink_1 = $resultProductCatalog->ink_1;
	$ink_2 = $resultProductCatalog->ink_2;
	$ink_3 = $resultProductCatalog->ink_3;
	$ink_4 = $resultProductCatalog->ink_4;
	$joint_type = $resultProductCatalog->joint_type;
	$joint_details = $resultProductCatalog->joint_details;
	$box_style = $resultProductCatalog->box_style;
	$rope_color = $resultProductCatalog->rope_color;
	$pcs_bundle = $resultProductCatalog->pcs_bundle;
	$level = $resultProductCatalog->level;
	$p_width_mm = $resultProductCatalog->p_width_mm;
	$p_width_inch = $resultProductCatalog->p_width_inch;
	$qty_allowance = $resultProductCatalog->qty_allowance;
	$scoreline_f = $resultProductCatalog->scoreline_f;
	$scoreline_d = $resultProductCatalog->scoreline_d;
	$scoreline_f2 = $resultProductCatalog->scoreline_f2;
	$slit = $resultProductCatalog->slit;
	$blank = $resultProductCatalog->blank;
	$t_length = $resultProductCatalog->t_length;
	$cut = $resultProductCatalog->cut;
	$next_process = $resultProductCatalog->next_process;
	$code_pd = $resultProductCatalog->code_pd;
	$code_rd = $resultProductCatalog->code_rd;
	$sketch = $resultProductCatalog->sketch;
	$sketch_large = $resultProductCatalog->sketch_large;
	$remark = $resultProductCatalog->remark;
	$isdeleted = $resultProductCatalog->isdeleted;
	$created_on = $resultProductCatalog->created_on;
	$created_by = $resultProductCatalog->created_by;
	$modified_on = $resultProductCatalog->modified_on;
	$modified_by = $resultProductCatalog->modified_by;
	$cmd = "updateData()";
	$btntitle = $this->lang->line('update');
	$idArray = array();
	$codeArray= array();$fluteArray= array();
	$DFArray= array();$BMArray= array();$BLArray= array();
	$CMArray= array();$CLArray= array();$lengthArray= array();
	$widthArray= array();$heightArray= array();$qtysetArray= array();
	$cnt=0;
	foreach($resultProducts as $prod){
		$idArray[$cnt] = $prod->auto_pid;
		$codeArray[$cnt] = $prod->product_code;
		$fluteArray[$cnt] = $prod->flute;
		$DFArray[$cnt] = $prod->DF;
		$BMArray[$cnt] = $prod->BM;
		$BLArray[$cnt] = $prod->BL;
		$CMArray[$cnt] = $prod->CM;
		$CLArray[$cnt] = $prod->CL;
		$lengthArray[$cnt] = $prod->Length_mm;
		$widthArray[$cnt] = $prod->Width_mm;
		$heightArray[$cnt] = $prod->Height_mm;
		$qtysetArray[$cnt] = $prod->qty_set;
		$cnt++;
	}
	for($i=$cnt;$i<$trows;$i++){
		$idArray[$i] = "";
		$codeArray[$i] = "";
		$fluteArray[$i] = "";
		$DFArray[$i] = "";
		$BMArray[$i] = "";
		$BLArray[$i] = "";
		$CMArray[$i] = "";
		$CLArray[$i] = "";
		$lengthArray[$i] = "";
		$widthArray[$i] = "";
		$heightArray[$i] = "";
		$qtysetArray[$i] = "";
	}
	echo "<div style='text-align:right;width:100%;'>ID: ".$product_id."</div><br/>";
}
if($action=='add'){
	$product_id = "";
	$product_code = "";
	$product_name = "";
	$partner_id = "";
	$customer_name = "";
	$product_type = "";
	$customer_part_no = "";
	$ink_1 = "";
	$ink_2 = "";
	$ink_3 = "";
	$ink_4 = "";
	$joint_type = "";
	$joint_details = "";
	$box_style = "";
	$rope_color = "";
	$pcs_bundle = "";
	$level = "";
	$p_width_mm = "";
	$p_width_inch = "";
	$qty_allowance = "";
	$scoreline_f = "";
	$scoreline_d = "";
	$scoreline_f2 = "";
	$slit = "";
	$blank = "";
	$t_length = "";
	$cut = "";
	$next_process = "";
	$code_pd = "";
	$code_rd = "";
	$sketch = "";$sketch_large = "";
	$remark = "";
	$isdeleted = "";
	$created_on = "";
	$created_by = "";
	$modified_on = "";
	$modified_by = "";
	$cmd = "saveData()";
	$btntitle = $this->lang->line('save');	
	for($i=0;$i<$trows;$i++){
		$idArray[$i] = "";
		$codeArray[$i] = "";
		$fluteArray[$i] = "";
		$DFArray[$i] = "";
		$BMArray[$i] = "";
		$BLArray[$i] = "";
		$CMArray[$i] = "";
		$CLArray[$i] = "";
		$lengthArray[$i] = "";
		$widthArray[$i] = "";
		$heightArray[$i] = "";
		$qtysetArray[$i] = "";
	}
	echo "<div style='text-align:right;width:100%;'>ID: Auto Generated</div><br/>";
}

?>
<table border=0>
	<input type='hidden' id='x_product_id' value='<?=$product_id?>'>
	<tr>
		<td>&nbsp;&nbsp;</td>
		<td>
			<table>
            <tr>
                <td class='tblDetailViewLabel'>Code</td>
                <td><input type='text' id='x_product_code' value='<?=$product_code?>' <?php if($salesCount>0)echo 'disabled';?>></td>
            </tr>
            <tr>
                <td class='tblDetailViewLabel'>Name</td>
                <td><input type='text' id='x_product_name' value='<?=$product_name?>'></td>
            </tr>
             <tr>
                <td class='tblDetailViewLabel'>Customer Name</td>
                <td>
                	<select id='x_customer_name' onchange="document.getElementById('x_partner_id').value=this.options[this.selectedIndex].value;">
                		<option value='' ></option>
						<?php foreach ($resultParnters as $resultParnter) {
							echo '<option value="'.$resultParnter->partner_id.'"';
							if($customer_name==$resultParnter->partner_name) echo "selected";
							echo '  >'.$resultParnter->partner_name.'</option>';
						} ?>
					</select>
				<input type='hidden' id='x_partner_id' value='<?=$partner_id?>'></td>
            </tr>
			<tr>
                
            </tr>
        </table>
		</td>
	</tr>
</table>
<br/>
<div id='boxcontainer'>
<table>
	<tr>
        <td class='tblDetailViewLabel'>Part No.</td>
		<td><input type='text' id='x_customer_part_no' value='<?=$customer_part_no?>'></td>
		<td class='tblDetailViewLabel'>Product Type</td>
        <td><input type='text' id='x_product_type' value='<?=$product_type?>'></td>
	</tr>
	</table>
</div>
<br/>

<table style='border: 1px solid #C8C8C8;' cellspacing=2 cellpadding=2 id='tblProductLine'>
	<tr>
        <td class='tblProdViewLabel'>Code</td>
		<td class='tblProdViewLabel'>Flute</td>
		<td class='tblProdViewLabel'>DF</td>
		<td class='tblProdViewLabel'>BM</td>
		<td class='tblProdViewLabel'>BL</td>
		<td class='tblProdViewLabel'>CM</td>
		<td class='tblProdViewLabel'>CL</td>
		<td class='tblProdViewLabel'>Length</td>
		<td class='tblProdViewLabel'>Width</td>
		<td class='tblProdViewLabel'>Height</td>
		<td class='tblProdViewLabel'>Qty/Set</td>
	</tr>
<?php
for($i=0;$i<$trows;$i++){
?>	
	<tr>
		<td><input type='hidden' id='x_pid_<?=$i?>' size='5' value="<?=$idArray[$i]?>" />
			<input type='text' id='x_code_<?=$i?>' size='5' value="<?=$codeArray[$i]?>" onblur='productLineLoad(this);' /></td>
		<td><input type='text' id='x_flute_<?=$i?>' size='2' value="<?=$fluteArray[$i]?>" /></td>
		<td><input type='text' id='x_DF_<?=$i?>' size='4' value="<?=$DFArray[$i]?>" /></td>
		<td><input type='text' id='x_BM_<?=$i?>' size='4' value="<?=$BMArray[$i]?>" /></td>
		<td><input type='text' id='x_BL_<?=$i?>' size='4' value="<?=$BLArray[$i]?>" /></td>
		<td><input type='text' id='x_CM_<?=$i?>' size='4' value="<?=$CMArray[$i]?>" /></td>
		<td><input type='text' id='x_CL_<?=$i?>' size='4' value="<?=$CLArray[$i]?>" /></td>
		<td><input type='text' id='x_length_<?=$i?>' size='2' value="<?=$lengthArray[$i]?>" /></td>
		<td><input type='text' id='x_width_<?=$i?>' size='2' value="<?=$widthArray[$i]?>" /></td>
		<td><input type='text' id='x_height_<?=$i?>' size='2' value="<?=$heightArray[$i]?>" /></td>
		<td><input type='text' id='x_qty_set_<?=$i?>' size='2' value="<?=$qtysetArray[$i]?>" /></td>
	</tr>
<?php
}
?>
</table>
<br/>

<div id='boxcontainer'>
<table>
	<tr>
        <td class='tblDetailViewLabel'>Ink Color 1</td>
		<td><input type='text' id='x_ink_1' value='<?=$ink_1?>'></td>
		<td class='tblDetailViewLabel'>Ink Color 2</td>
		<td><input type='text' id='x_ink_2' value='<?=$ink_2?>'></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>Ink Color 3</td>
		<td><input type='text' id='x_ink_3' value='<?=$ink_3?>'></td>
		<td class='tblDetailViewLabel'>Ink Color 4</td>
		<td><input type='text' id='x_ink_4' value='<?=$ink_4?>'></td>
	</tr>
	</table>
</div>
<br/>

<div id='boxcontainer'>
<table>
	<tr>
		<td class='tblDetailViewLabel'>Joint Type</td>
			<select id='x_joint_type'>
				<option value=""></option>
                <option value="Glue" <?php if($joint_type=='Glue')echo 'selected'; ?>>Glue</option>
                <option value="Red Stitch" <?php if($joint_type=='Red Stitch')echo 'selected'; ?>>Red Stitch</option>
				<option value="White Stitch" <?php if($joint_type=='White Stitch')echo 'selected'; ?>>White Stitch</option>
            </select>
		<td class='tblDetailViewLabel'>Joint Details</td>
		<td><input type='text' id='x_joint_details' value='<?=$joint_details?>'></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>Box Style</td>
		<td><select id='x_box_style'>
				<option value=""></option>
	            <option value="RSC" <?php if($box_style=='RSC')echo 'selected'; ?>>RSC</option>
				<option value="Tray" <?php if($box_style=='Tray')echo 'selected'; ?>>Tray</option>
				<option value="Diecut" <?php if($box_style=='Diecut')echo 'selected'; ?>>Diecut</option>
				<option value="Sleeve" <?php if($box_style=='Sleeve')echo 'selected'; ?>>Sleeve</option>
				<option value="Half slot container" <?php if($box_style=='Half slot container')echo 'selected'; ?>>Half slot container</option>
				<option value="Other" <?php if($box_style=='Other')echo 'selected'; ?>>Other</option>
	        </select>
		</td>
		<td class='tblDetailViewLabel'>Rope Color</td>
		<td><input type='text' id='x_rope_color' value='<?=$rope_color?>'></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>PCS/Bundle</td>
		<td><input type='text' id='x_pcs_bundle' value='<?=$pcs_bundle?>'></td>
		<td class='tblDetailViewLabel'>Level</td>
		<td><input type='text' id='x_level' value='<?=$level?>'></td>
	</tr>
	</table>
</div>
<br/>

<div id='boxcontainer'>
<table>
	<tr>
		<td class='tblDetailViewLabel'>Paper Width (mm)</td>
		<td><input type='text' id='x_p_width_mm' value='<?=$p_width_mm?>'></td>
		<td class='tblDetailViewLabel' rowspan=3>Remark</td>
		<td rowspan=2><textarea id='x_remark' row=3><?=$remark?></textarea></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>Paper Width (inch)</td>
		<td><input type='text' id='x_p_width_inch' value='<?=$p_width_inch?>'></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>Qty. Allowance</td>
		<td><input type='text' id='x_qty_allowance' value='<?=$qty_allowance?>'></td>
	</tr>	
</table>
</div>
<br/>

<div id='boxcontainer'>
<table>
	<tr>
		<td class='tblDetailViewLabel'>Sketch</td>
		<td> 
			<div id='prevSketch'>
			<?php if($sketch!='') {
				echo "Previous Uploaded: ".$sketch;
			} ?>
			</div>
			<div id="fi-form"></div>
			<input type='hidden' id='x_sketch' value="<?=$sketch?>">
		</td>
	</tr>
</table>
</div>
<br/>

<div id='boxcontainer'>
<table>
	<tr>
		<td class='tblDetailViewLabel'>Sketch Large</td>
		<td> 
			<div id='prevSketch_large'>
			<?php if($sketch_large!='') {
				echo "Previous Uploaded: ".$sketch_large;
			} ?>
			</div>
			<div id="fi-form_large"></div>
			<input type='hidden' id='x_sketch_large' value="<?=$sketch_large?>">
		</td>
	</tr>
</table>
</div>
<br/>

<div id='boxcontainer'>
<table>
	<tr>
		<td class='tblDetailViewLabel'>Code RD</td>
		<td><input type='text' id='x_code_rd' value='<?=$code_rd?>'></td>
		<td class='tblDetailViewLabel' rowspan=2>Next Process</td>
		<td><input type='text' id='x_next_process' value='<?=$next_process?>'></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>Code PD</td>
		<td><input type='text' id='x_code_pd' value='<?=$code_pd?>'></td>
	</tr>	
</table>
</div>
<br/>

<div id='boxcontainer'>
<table>
	<tr>
		<td class='tblDetailViewLabel'>Scoreline F</td>
		<td><input type='text' id='x_scoreline_f' value='<?=$scoreline_f?>'></td>
		<td class='tblDetailViewLabel'>Cut</td>
		<td><input type='text' id='x_cut' value='<?=$cut?>'></td>
	</tr>
	<tr>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>Scoreline D</td>
		<td><input type='text' id='x_scoreline_d' value='<?=$scoreline_d?>'></td>
		<td class='tblDetailViewLabel'>Slit</td>
		<td><input type='text' id='x_slit' value='<?=$slit?>'></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>Scoreline F2</td>
		<td><input type='text' id='x_scoreline_f2' value='<?=$scoreline_f2?>'></td>
		<td class='tblDetailViewLabel'>T. Length</td>
		<td><input type='text' id='x_t_length' value='<?=$t_length?>'></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>Blank</td>
		<td><input type='text' id='x_blank' value='<?=$blank?>'></td>
		<td class='tblDetailViewLabel' colspan=2>
			<?=$scoreline_f?>+
			<?=$scoreline_d?>+
			<?=$scoreline_f2?>= 
<?php echo ($scoreline_f+$scoreline_d+$scoreline_f2)?>
		</td>		
	</tr>
</table>
</div>
<br/>
<div  style="width:100%"><center>
<input type="button" value="<?=$btntitle?>" onclick="<?=$cmd?>;">  
<input type="button" value="<?=$this->lang->line('cancel')?>" onclick='cancelData();'>
</center></div>

<?php
} //End Edit and Add
?>  

</br>
&nbsp;
</div>
<div id="sketchdiv" class="x-hide-display paddedDiv">
<?php
if (($action=='view')||($action=='edit')){  
	if($resultProductCatalog->sketch!="") echo "<img src='".base_url().$resultProductCatalog->sketch."' />"; 
	else echo "<p class='details-info'>No Sketch Uploaded</p>";
}
else { echo "<p class='details-info'>Please Select One of the Products.</p>";}
?>
</div>
