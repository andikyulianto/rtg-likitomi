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
<!--
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
-->
<table cellspacing=2 cellpadding=2>
	<tr>
		<td class='tblProdViewLabel' rowspan=2>Code</td>
		<td class='tblProdViewLabel' rowspan=2>Flute</td>
		<td class='tblProdViewLabel' colspan=5>Board Combination</td>
		<td class='tblProdViewLabel' colspan=2>Paper width</td>
		<td class='tblProdViewLabel' colspan=2>Product size</td>
		<td class='tblProdViewLabel' rowspan=2>Qty/set</td></tr>
	<tr>
        
		<td class='tblProdViewLabel'>DF</td>
		<td class='tblProdViewLabel'>BM</td>
		<td class='tblProdViewLabel'>BL</td>
		<td class='tblProdViewLabel'>CM</td>
		<td class='tblProdViewLabel'>CL</td>
		
		<td class='tblProdViewLabel'>inch</td>
		<td class='tblProdViewLabel'>mm</td>		
		<td class='tblProdViewLabel'>Blank</td>
		<td class='tblProdViewLabel'>Length</td>
	</tr>
<?php 
$i = 0;
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

	<td class='tblProdView'><?=$prod->paper_width?></td>
	<td class='tblProdView'><?=$prod->paper_width_mm?></td>
	<td class='tblProdView'><?=$prod->blank?></td>
	<td class='tblProdView'><?=$prod->length?></td>
	<td class='tblProdView'><?=$prod->qty_set?></td>
</tr>
<?php 

}?>
</table>
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
	Inner dimension
	<br/>
	<br/>
<table>
	<tr>
		<td class='tblDetailViewLabel'>L :</td>
		<td class='tblDetailView' nowrap><?=$resultProductCatalog->inner_l?></td>
		<td class='tblDetailViewLabel'>W :</td>
		<td class='tblDetailView' nowrap><?=$resultProductCatalog->inner_w?></td>		
		<td class='tblDetailViewLabel'>H :</td>
		<td class='tblDetailView' nowrap><?=$resultProductCatalog->inner_h?></td>
	</tr>
	
	
</table>
</div>
<br/>


<div id='boxcontainer'>
Process<br><br>
<table width="500px">
<tr>
<td><input type="checkbox" id='x_checkbox_cr' <?php if($resultProductCatalog->req_cr=='1') echo 'checked'; else echo ''; ?> disabled="disabled"> CR </td>
<td><input type="checkbox" id='x_checkbox_2cl' <?php if($resultProductCatalog->req_2cl=='1') echo 'checked'; else echo ''; ?> disabled="disabled"> 2CL </td>
<td><input type="checkbox" id='x_checkbox_gh' <?php if($resultProductCatalog->req_gh=='1') echo 'checked'; else echo ''; ?> disabled="disabled"> Glue Handle </td>
<td><input type="checkbox" id='x_checkbox_rd' <?php if($resultProductCatalog->req_rd=='1') echo 'checked'; else echo ''; ?> disabled="disabled"> RD </td>
<td><input type="checkbox" id='x_checkbox_wh' <?php if($resultProductCatalog->req_wh=='1') echo 'checked'; else echo ''; ?> disabled="disabled"> WH </td>
</tr> 

<tr>
<td></td>
<td><input type="checkbox" id='x_checkbox_3cm' <?php if($resultProductCatalog->req_3cm=='1') echo 'checked'; else echo ''; ?> disabled="disabled"> 3CM </td>
<td><input type="checkbox" id='x_checkbox_hs' <?php if($resultProductCatalog->req_hs=='1') echo 'checked'; else echo ''; ?> disabled="disabled"> HS </td>
<td><input type="checkbox" id='x_checkbox_ss' <?php if($resultProductCatalog->req_ss=='1') echo 'checked'; else echo ''; ?> disabled="disabled"> SS </td>
</tr>

<tr>
<td></td>
<td><input type="checkbox" id='x_checkbox_3cs' <?php if($resultProductCatalog->req_3cs=='1') echo 'checked'; else echo ''; ?> disabled="disabled"> 3CS </td>
<td><input type="checkbox" id='x_checkbox_fg' <?php if($resultProductCatalog->req_fg=='1') echo 'checked'; else echo ''; ?> disabled="disabled"> FG </td>
<td><input type="checkbox" id='x_checkbox_remove' <?php if($resultProductCatalog->req_remove=='1') echo 'checked'; else echo ''; ?> disabled="disabled"> Remove Scraps </td>
</tr>
<tr>
<td></td>
<td><input type="checkbox" id='x_checkbox_4cd' <?php if($resultProductCatalog->req_4cd=='1') echo 'checked'; else echo ''; ?> disabled="disabled"> 4CD </td>
<td></td>
<td><input type="checkbox" id='x_checkbox_foam' <?php if($resultProductCatalog->req_foam=='1') echo 'checked'; else echo ''; ?> disabled="disabled"> Foam </td>
</tr>
<tr>
<td></td>
<td><input type="checkbox" id='x_checkbox_3cl' <?php if($resultProductCatalog->req_3cl=='1') echo 'checked'; else echo ''; ?> disabled="disabled"> 3CL </td>
<td></td>
<td><input type="checkbox" id='x_checkbox_tape' <?php if($resultProductCatalog->req_tape=='1') echo 'checked'; else echo ''; ?> disabled="disabled"> Tape </td>
</tr>
</table>
<br>
</div>
<br>

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
	<!--	<td class='tblDetailViewLabel'>T. Length</td>
		<td><?=$resultProductCatalog->t_length?></td>
	-->
	</tr>
	<tr>
	<!--	<td class='tblDetailViewLabel'>Blank</td>
		<td class='tblDetailView'><?=$resultProductCatalog->blank?></td>
	-->
		<td class='tblDetailViewLabel'><br/>
			<?=$resultProductCatalog->scoreline_f?>+
			<?=$resultProductCatalog->scoreline_d?>+
			<?=$resultProductCatalog->scoreline_f2?>= </td>
			<td class='tblDetailView'><br/>
<?php echo ($resultProductCatalog->scoreline_f+$resultProductCatalog->scoreline_d+$resultProductCatalog->scoreline_f2)?>
		</td>		
	</tr>
</table>
</div>
<br>



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
	<br/><br/>
	<table>
	<tr>
		<td class='tblDetailViewLabel'>Code RD</td>
		<td class='tblDetailView'><?=$resultProductCatalog->code_rd?></td>
		<td class='tblDetailViewLabel'>Code PD</td>
		<td class='tblDetailView'><?=$resultProductCatalog->code_pd?></td>	
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
	<!--	
		<td class='tblDetailViewLabel'>Paper Width (mm)</td>
		<td class='tblDetailView'><?=$resultProductCatalog->p_width_mm?></td>
	-->
		<td class='tblDetailViewLabel' rowspan=3>Remark</td>
		<td class='tblDetailView' rowspan=2><?=$resultProductCatalog->remark?></td>
	</tr>
	<!--<tr>
		<td class='tblDetailViewLabel'>Paper Width (inch)</td>
		<td class='tblDetailView'><?=$resultProductCatalog->p_width_inch?></td>
	</tr>-->
	<tr>
		<td class='tblDetailViewLabel'>Qty. Allowance</td>
		<td class='tblDetailView'><?=$resultProductCatalog->qty_allowance?></td>
	</tr>
	
</table>
</div>
<br/>






<div id='boxcontainer'>
Production Configuration for PC
<br>
</br>
<table>
<tr></tr>
<tr>
<td colspan=4>
	
		<table>
			<tr>
				<td class='tblProdViewLabel' rowspan=2></td>
				<td class='tblProdViewLabel' colspan=5>Board Combination</td>
				<td class='tblProdViewLabel' colspan=2>Paper width </td>
				<td class='tblProdViewLabel' rowspan=2>slit</td>

			<tr>
				
				<td class='tblProdViewLabel'>DF</td>
				<td class='tblProdViewLabel'>BM</td>
				<td class='tblProdViewLabel'>BL</td>
				<td class='tblProdViewLabel'>CM</td>
				<td class='tblProdViewLabel'>CL</td>
				<td class='tblProdViewLabel'>inch</td>
				<td class='tblProdViewLabel'>mm</td>
				

			</tr>
			<tr>
				<td class='tblProdView'>From Sale</td>
				<td class='tblProdView'><?=$prod->DF?></td>
				<td class='tblProdView'><?=$prod->BM?></td>
				<td class='tblProdView'><?=$prod->BL?></td>
				<td class='tblProdView'><?=$prod->CM?></td>
				<td class='tblProdView'><?=$prod->CL?></td>
				<td class='tblProdView'><?=$prod->paper_width?></td>
				<td class='tblProdView'><?=$prod->paper_width_mm?></td>
				<td class='tblProdView'><?=$resultProductCatalog->slit?></td>
				
				

			</tr>
			<tr>
				<td class='tblProdView'>For PC</td>
				<td class='tblProdView'><?=$resultProductCatalog->pc_df?></td>
				<td class='tblProdView'><?=$resultProductCatalog->pc_bm?></td>
				<td class='tblProdView'><?=$resultProductCatalog->pc_bl?></td>
				<td class='tblProdView'><?=$resultProductCatalog->pc_cm?></td>
				<td class='tblProdView'><?=$resultProductCatalog->pc_cl?></td>
				<td class='tblProdView'><?=$resultProductCatalog->pc_paper_width?></td>
				<td class='tblProdView'><?=$resultProductCatalog->pc_paper_width_mm?></td>
				<td class='tblProdView'><?=$resultProductCatalog->pc_slit?></td>
			</tr>

		</table>


</td>
<tr><td><br/><br/></td></tr>
</tr>
<tr>
		
		<td class='tblDetailViewLabel'>CR Length</td>
		<td  class='tblDetailView'><?=$resultProductCatalog->cr_length?></td>

		<td class='tblDetailViewLabel'>CR Blank</td>
		<td class='tblDetailView'><?=$resultProductCatalog->cr_blank?></td>
</tr>
<tr>
		<td class='tblDetailViewLabel'>CV Length</td>
		<td class='tblDetailView'><?=$resultProductCatalog->cv_length?></td>

		<td class='tblDetailViewLabel'>CV Blank</td>
		<td class='tblDetailView'><?=$resultProductCatalog->cv_blank?></td>
	</tr>
	
	
		<tr>
		<td class='tblDetailViewLabel'>PT Length</td>
		<td class='tblDetailView'><?=$resultProductCatalog->pt_length?></td>

		<td class='tblDetailViewLabel'>PT Blank</td>
		<td class='tblDetailView'><?=$resultProductCatalog->pt_blank?></td>
	</tr>
	</table>

</div>
<br>


<div id='boxcontainer'>
For history
<br/><br>
<table>
	<tr>
		<td class='tblDetailViewLabel'>Extra Blank +</td>
		<td class='tblDetailView'><?=$resultProductCatalog->add_blank?></td>
		<td class='tblDetailViewLabel'>Extra Length +</td>
		<td class='tblDetailView'><?=$resultProductCatalog->add_t_length?></td>
	</tr>
</table>
</div>
<br/>


<div id='boxcontainer'>
Amount of sheet production
<br/><br/>
<table>
	<tr>
		<td class='tblDetailViewLabel'>CR</td>
		<td><?=$resultProductCatalog->cr_ratio_2?>:<?=$resultProductCatalog->cr_ratio_1?></td>
		<td class='tblDetailViewLabel'>CV</td>
		<td><?=$resultProductCatalog->cv_ratio_1?>:<?=$resultProductCatalog->cv_ratio_2?></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>PT</td>
		<td><?=$resultProductCatalog->pt_ratio_1?>:<?=$resultProductCatalog->pt_ratio_2?></td>
	<td></td>
	<td></td>
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
	$inner_l = $resultProductCatalog->inner_l;
	$inner_w = $resultProductCatalog->inner_w;
	$inner_h = $resultProductCatalog->inner_h;
//	$product_type = $resultProductCatalog->product_type;
//	$customer_part_no = $resultProductCatalog->customer_part_no;
	$cr_length = $resultProductCatalog->cr_length;
	$cr_blank = $resultProductCatalog->cr_blank;
	$cv_length = $resultProductCatalog->cv_length;
	$cv_blank = $resultProductCatalog->cv_blank;
	$pt_length = $resultProductCatalog->pt_length;
	$pt_blank = $resultProductCatalog->pt_blank;
	
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
	$pc_df = $resultProductCatalog->pc_df;
	$pc_bl = $resultProductCatalog->pc_bl;
	$pc_bm = $resultProductCatalog->pc_bm;
	$pc_cl = $resultProductCatalog->pc_cl;
	$pc_cm = $resultProductCatalog->pc_cm;
	$pc_paper_width = $resultProductCatalog->pc_paper_width;
	$pc_paper_width_mm = $resultProductCatalog->pc_paper_width_mm;
	$pc_slit = $resultProductCatalog->pc_slit;
	$add_blank = $resultProductCatalog->add_blank;
	$add_t_length = $resultProductCatalog->add_t_length;
	$add_amount = $resultProductCatalog->add_amount;
	$cr_ratio_1 = $resultProductCatalog->cr_ratio_1;
	$cv_ratio_1 = $resultProductCatalog->cv_ratio_1;
	$pt_ratio_1 = $resultProductCatalog->pt_ratio_1;
	$cr_ratio_2 = $resultProductCatalog->cr_ratio_2;
	$cv_ratio_2 = $resultProductCatalog->cv_ratio_2;
	$pt_ratio_2 = $resultProductCatalog->pt_ratio_2;
	$remark = $resultProductCatalog->remark;
	$req_cr = $resultProductCatalog->req_cr;
	$req_2cl = $resultProductCatalog->req_2cl;
	$req_3cm = $resultProductCatalog->req_3cm;
	$req_3cs = $resultProductCatalog->req_3cs;
	$req_4cd = $resultProductCatalog->req_4cd;
	$req_3cl = $resultProductCatalog->req_3cl;
	$req_gh = $resultProductCatalog->req_gh;
	$req_fg = $resultProductCatalog->req_fg;
	$req_rd = $resultProductCatalog->req_rd;
	$req_ss = $resultProductCatalog->req_ss;
	$req_hs = $resultProductCatalog->req_hs;
	$req_remove = $resultProductCatalog->req_remove;
	$req_foam = $resultProductCatalog->req_foam;
	$req_tape = $resultProductCatalog->req_tape;
	$req_wh = $resultProductCatalog->req_wh;
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
	$CMArray= array();$CLArray= array();$pwidthArray= array();
	$blankArray= array();$lengthArray= array();$qtysetArray= array();
	$cnt=0;
	foreach($resultProducts as $prod){
		$idArray[$cnt] = $prod->auto_id;
		$codeArray[$cnt] = $prod->product_code;
		$fluteArray[$cnt] = $prod->flute;
		$DFArray[$cnt] = $prod->DF;
		$BMArray[$cnt] = $prod->BM;
		$BLArray[$cnt] = $prod->BL;
		$CMArray[$cnt] = $prod->CM;
		$CLArray[$cnt] = $prod->CL;
		$pwidthArray[$cnt] = $prod->paper_width;
		$pwidthmmArray[$cnt] = $prod->paper_width_mm;
		$blankArray[$cnt] = $prod->blank;
		$lengthArray[$cnt] = $prod->length;
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
		$pwidthArray[$i] = "";
		$pwidthmmArray[$i] = "";
		$blankArray[$i] = "";
		$lengthArray[$i] = "";
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
//	$product_type = "";
//	$customer_part_no = "";
	$inner_l = "";
	$inner_w = "";
	$inner_h = "";
	$ink_1 = "";
	$ink_2 = "";
	$ink_3 = "";
	$ink_4 = "";
	$cr_length = "";
	$cr_blank ="";
	$cv_length = "";
	$cv_blank = "";
	$pt_length = "";
	$pt_blank = "";
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
	$sketch = "";
	$sketch_large = "";
	$pc_df = "";
	$pc_bl = "";
	$pc_bm = "";
	$pc_cl = "";
	$pc_cm = "";
	$pc_paper_width = "";
	$pc_paper_width_mm = "";
	$pc_slit = "";
	$add_blank = "";
	$add_t_length = "";
	$add_amount = "";
	$cr_ratio_1 = "1";
	$cv_ratio_1 = "1";
	$pt_ratio_1 = "1";
	$cr_ratio_2 = "1";
	$cv_ratio_2 = "1";
	$pt_ratio_2 = "1";
	$remark = "";
	$isdeleted = "";
	$created_on = "";
	$created_by = "";
	$modified_on = "";
	$modified_by = "";
	$req_cr = "1";
	$req_2cl = "0";
	$req_3cm = "0";
	$req_3cs = "0";
	$req_4cd = "0";
	$req_3cl = "0";
	$req_gh = "0";
	$req_fg = "0";
	$req_rd = "0";
	$req_ss = "0";
	$req_hs = "0";
	$req_remove = "0";
	$req_foam = "0";
	$req_tape = "0";
	$req_wh = "1";
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
		$pwidthArray[$i] = "";
		$pwidthmmArray[$i] = "";
		$blankArray[$i] = "";
		$lengthArray[$i] = "";
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
                <td><input type='text' id='x_product_code' value='<?=$product_code?>' <?php if($salesCount>0);?>>*</td>
            </tr>
            <tr>
                <td class='tblDetailViewLabel'>Name</td>
                <td><input type='text' id='x_product_name' value='<?=$product_name?>'>*</td>
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
<!--
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
-->
<table  cellspacing=2 cellpadding=2 id='tblProductLine'>
	<tr>
		<td class='tblProdViewLabel' rowspan=2>Code</td>
		<td class='tblProdViewLabel' rowspan=2>Flute</td>
		<td class='tblProdViewLabel' colspan=5>Board Combination</td>
		<td class='tblProdViewLabel' colspan=2>Paper width</td>
		<td class='tblProdViewLabel' colspan=2>Product size</td>
		<td class='tblProdViewLabel' rowspan=2>Qty/ <br/>set</td>
	</tr>
	<tr>
		<td class='tblProdViewLabel'>DF</td>
		<td class='tblProdViewLabel'>BM</td>
		<td class='tblProdViewLabel'>BL</td>
		<td class='tblProdViewLabel'>CM</td>
		<td class='tblProdViewLabel'>CL</td>
		<td class='tblProdViewLabel'>inch</td>
		<td class='tblProdViewLabel'>mm</td>
		<td class='tblProdViewLabel'>Blank</td>
		<td class='tblProdViewLabel'>Length</td>
		<td ></td>
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
		<td><input type='text' id='x_real_paper_width_<?=$i?>' size='1' value="<?=$pwidthArray[$i]?>" /></td>
		<td><input type='text' id='x_real_paper_width_mm_<?=$i?>' size='1' value="<?=$pwidthmmArray[$i]?>" /></td>
		<td><input type='text' id='x_real_blank_<?=$i?>' size='2' value="<?=$blankArray[$i]?>" /></td>
		<td><input type='text' id='x_real_length_<?=$i?>' size='2' value="<?=$lengthArray[$i]?>" /></td>
		<td><input type='text' id='x_qty_set_<?=$i?>' size='1' value="<?=$qtysetArray[$i]?>" /></td>
		<td><?php if($i==0) echo "*"; ?></td>
	</tr>
<?php
if($i==0)
{

	$DF = $DFArray[0];
	$BM = $BMArray[0];
	$BL = $BLArray[0];
	$CM = $CMArray[0];
	$CL = $CLArray[0];
	$paper_width = $pwidthArray[0];
	$paper_width_mm = $pwidthmmArray[0];
	
}
}
?>
</table>
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
	<tr><td><br/><br/></td></tr>
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
	Inner dimension
	<br/>
	<br/>
<table>
	<tr>
		<td class='tblDetailViewLabel'>L :</td>
		<td class='tblDetailView'><input type='text' id='x_inner_l' value="<?=$inner_l?>"></td>
		<td class='tblDetailViewLabel'>W :</td>
		<td class='tblDetailView'><input type='text' id='x_inner_w' value="<?=$inner_w?>"></td>		
		<td class='tblDetailViewLabel'>H :</td>
		<td class='tblDetailView'><input type='text' id='x_inner_h' value="<?=$inner_h?>"></td>
	</tr>
	
	
</table>
</div>
<br/>


<div id='boxcontainer'>
Process*<br><br>
<table width="500px">
	<tr>
<td>
<input type="checkbox" id='x_checkbox_cr' <?php if($req_cr=='1') echo 'checked';  ?>> CR </td>
<td><input type="checkbox" id='x_checkbox_2cl' <?php if($req_2cl=='1') echo 'checked'; ?>> 2CL </td>
<td><input type="checkbox" id='x_checkbox_gh' <?php if($req_gh=='1') echo 'checked'; else echo ''; ?>> Glue Handle </td>
<td><input type="checkbox" id='x_checkbox_rd' <?php if($req_rd=='1') echo 'checked'; else echo ''; ?>> RD </td>
<td><input type="checkbox" id='x_checkbox_wh' <?php if($req_wh=='1') echo 'checked'; else echo ''; ?>> WH </td>
</tr> 
<tr>
<td></td>
<td><input type="checkbox" id='x_checkbox_3cm' <?php if($req_3cm=='1') echo 'checked'; else echo ''; ?>> 3CM </td>
<td><input type="checkbox" id='x_checkbox_hs' <?php if($req_hs=='1') echo 'checked'; else echo ''; ?>> HS </td>
<td><input type="checkbox" id='x_checkbox_ss' <?php if($req_ss=='1') echo 'checked'; else echo ''; ?>> SS </td>
</tr>
<tr>
<td></td>
<td><input type="checkbox" id='x_checkbox_3cs' <?php if($req_3cs=='1') echo 'checked'; else echo ''; ?>> 3CS </td>
<td><input type="checkbox" id='x_checkbox_fg' <?php if($req_fg=='1') echo 'checked'; else echo ''; ?>> FG </td>
<td><input type="checkbox" id='x_checkbox_remove' <?php if($req_remove=='1') echo 'checked'; else echo ''; ?>> Remove Scraps </td>
</tr>
<tr>
<td></td>
<td><input type="checkbox" id='x_checkbox_4cd' <?php if($req_4cd=='1') echo 'checked'; else echo ''; ?>> 4CD </td>
<td></td>
<td><input type="checkbox" id='x_checkbox_foam' <?php if($req_foam=='1') echo 'checked'; else echo ''; ?>> Foam </td>
</tr>
<tr>
<td></td>
<td><input type="checkbox" id='x_checkbox_3cl' <?php if($req_3cl=='1') echo 'checked'; else echo ''; ?>> 3CL </td>
<td></td>
<td><input type="checkbox" id='x_checkbox_tape' <?php if($req_tape=='1') echo 'checked'; else echo ''; ?>> Tape </td>
</tr>
</table>
<br>
</div>
<br>

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
<!--		<td class='tblDetailViewLabel'>T. Length</td>
		<td><input type='text' id='x_t_length' value='<?=$t_length?>'></td>-->
	</tr>
	<tr>
<!--		<td class='tblDetailViewLabel'>Blank</td>
		<td><input type='text' id='x_blank' value='<?=$blank?>'></td>-->
		<td class='tblDetailViewLabel'>
			<?=$scoreline_f?>+
			<?=$scoreline_d?>+
			<?=$scoreline_f2?>= 
		</td>
		<td class='tblDetailView'>
<?php echo ($scoreline_f+$scoreline_d+$scoreline_f2)?>
		</td>		
	</tr>
</table>
</div>
<br>

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
	<br/>
	<br/>
	<table>
	<tr>
		<td class='tblDetailViewLabel'>Code RD</td>
		<td><input type='text' id='x_code_rd' value='<?=$code_rd?>'></td>

		<td class='tblDetailViewLabel'>Code PD</td>
		<td><input type='text' id='x_code_pd' value='<?=$code_pd?>'></td>
	</tr>	
</table>
</div>
<br/>

<div id='boxcontainer'>
<table>
	<tr>
		<td class='tblDetailViewLabel'>Joint Type</td>
		<td><select id='x_joint_type' style="width:97%" >
				<option value=""></option>
                <option value="Glue" <?php if($joint_type=='Glue')echo 'selected'; ?>>Glue</option>
                <option value="Red Stitch" <?php if($joint_type=='Red Stitch')echo 'selected'; ?>>Red Stitch</option>
				<option value="White Stitch" <?php if($joint_type=='White Stitch')echo 'selected'; ?>>White Stitch</option>
            </select></td>
		<td class='tblDetailViewLabel'>Joint Details</td>
		<td><input type='text' id='x_joint_details' value='<?=$joint_details?>'></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>Box Style</td>
		<td><select id='x_box_style' style="width:97%" >
				<option value=""></option>
	            <option value="RSC" <?php if($box_style=='RSC')echo 'selected'; ?>>RSC</option>
				<option value="Tray" <?php if($box_style=='Tray')echo 'selected'; ?>>Tray</option>
				<option value="Diecut" <?php if($box_style=='Diecut')echo 'selected'; ?>>Diecut</option>
				<option value="Sleeve" <?php if($box_style=='Sleeve')echo 'selected'; ?>>Sleeve</option>
				<option value="Half slot container" <?php if($box_style=='Half slot container')echo 'selected'; ?>>Half slot container</option>
				<option value="Wrap around" <?php if($box_style=='Wrap around')echo 'selected'; ?>>Wrap around</option>
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
<!--		
		<td class='tblDetailViewLabel'>Paper Width (mm)</td>
		<td><input type='text' id='x_p_width_mm' value='<?=$p_width_mm?>'></td>
		-->
		<td class='tblDetailViewLabel' rowspan=3>Remark</td>
		<td rowspan=3><textarea id='x_remark' row=3><?=$remark?></textarea></td>

	</tr>
	<!--
	<tr>
		<td class='tblDetailViewLabel'>Paper Width (inch)</td>
		<td><input type='text' id='x_p_width_inch' value='<?=$p_width_inch?>'></td>
	</tr>
-->
	<tr>
		<td class='tblDetailViewLabel'>Qty. Allowance</td>
		<td><input type='text' id='x_qty_allowance' value='<?=$qty_allowance?>'></td>
	</tr>	
</table>
</div>
<br/>



<div id='boxcontainer'>
Production Configuration for PC
<br>
</br>
<table>
	<tr>
<td colspan=4>
			<table>
			<tr>
				<td class='tblProdViewLabel' rowspan=2></td>
				<td class='tblProdViewLabel' colspan=5>Board Combination</td>
				<td class='tblProdViewLabel' colspan=2>Paper width </td>
				<td class='tblProdViewLabel' rowspan=2>Slit </td>

			<tr>
				<td class='tblProdViewLabel'>DF</td>
				<td class='tblProdViewLabel'>BM</td>
				<td class='tblProdViewLabel'>BL</td>
				<td class='tblProdViewLabel'>CM</td>
				<td class='tblProdViewLabel'>CL</td>
				<td class='tblProdViewLabel'>inch</td>
				<td class='tblProdViewLabel'>mm</td>


			</tr>
			<tr>
				<td class='tblProdView'>From Sale*</td>

				<td class='tblProdViewLabel'><?=$DF?></td>
				<td class='tblProdViewLabel'><?=$BM?></td>
				<td class='tblProdViewLabel'><?=$BL?></td>
				<td class='tblProdViewLabel'><?=$CM?></td>
				<td class='tblProdViewLabel'><?=$CL?></td>
				<td class='tblProdViewLabel'><?=$paper_width?></td>
				<td class='tblProdViewLabel'><?=$paper_width_mm?></td>
				<td class='tblProdViewLabel'><?=$slit?></td>

			</tr>
			<tr>
				<td class='tblProdView'>For PC</td>
				<td><input type='text' id='x_pc_df' value='<?=$pc_df?>' size=4></td>
				<td><input type='text' id='x_pc_bm' value='<?=$pc_bm?>' size=4></td>
				<td><input type='text' id='x_pc_bl' value='<?=$pc_bl?>' size=4></td>
				<td><input type='text' id='x_pc_cm' value='<?=$pc_cm?>' size=4></td>
				<td><input type='text' id='x_pc_cl' value='<?=$pc_cl?>' size=4></td>
				<td><input type='text' id='x_pc_paper_width' value='<?=$pc_paper_width?>' size=5></td>
				<td><input type='text' id='x_pc_paper_width_mm' value='<?=$pc_paper_width_mm?>' size=5></td>
				<td><input type='text' id='x_pc_slit' value='<?=$pc_slit?>' size=5></td>
			</tr>

		</table>



</td>
</tr>
<tr><td colspan=4>*will retrieve from top box<br/><br/></td></tr>
</tr>
	<tr>
		<td class='tblDetailViewLabel'>CR Length</td>
		<td><input type='text' id='x_cr_length' value='<?=$cr_length?>'></td>

		<td class='tblDetailViewLabel'>CR Blank</td>
		<td><input type='text' id='x_cr_blank' value='<?=$cr_blank?>'></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>CV Length</td>
		<td><input type='text' id='x_cv_length' value='<?=$cv_length?>'></td>

		<td class='tblDetailViewLabel'>CV Blank</td>
		<td><input type='text' id='x_cv_blank' value='<?=$cv_blank?>'></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>PT Length</td>
		<td><input type='text' id='x_pt_length' value='<?=$pt_length?>'></td>

		<td class='tblDetailViewLabel'>PT Blank</td>
		<td><input type='text' id='x_pt_blank' value='<?=$pt_blank?>'></td>
	</tr>
	</table>
</div>
<br>


<div id='boxcontainer'>
For history<br><br/>
<table><tr><td class='tblDetailViewLabel'>Extra Length +</td><td><input type='text' id='x_add_t_length' value='<?=$add_t_length?>' size="7"></td>
<td class='tblDetailViewLabel'>Extra Blank +</td><td><input type='text' id='x_add_blank' value='<?=$add_blank?>' size="7"></td>
	
</table>
</div>
<br/>

<div id='boxcontainer'>
Amount of sheet production *
<br/>
<br/>
<table><tr><td class='tblDetailViewLabel'>CR</td><td><input type='text' id='x_cr_ratio_2' value='<?=$cr_ratio_2?>' size="3"></td><td>:<input type='text' id='x_cr_ratio_1' value='<?=$cr_ratio_1?>' size="3"></td>
	<td class='tblDetailViewLabel'>CV</td><td><input type='text' id='x_cv_ratio_1' value='<?=$cv_ratio_1?>' size="3"></td><td>:<input type='text' id='x_cv_ratio_2' value='<?=$cv_ratio_2?>' size="3"></tr>
	<tr><td class='tblDetailViewLabel'>PT</td><td><input type='text' id='x_pt_ratio_1' value='<?=$pt_ratio_1?>' size="3"></td><td>:<input type='text' id='x_pt_ratio_2' value='<?=$pt_ratio_2?>' size="3"></td>
	<td></td><td></td></tr>
</table>
</div>
<br/>

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
