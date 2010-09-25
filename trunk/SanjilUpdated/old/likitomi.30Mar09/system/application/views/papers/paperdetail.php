<div id="general" class="x-hide-display paddedDiv">
<?php
if ($action=='view'){ 
$resultPaper = $resultPapers->row(0);
echo "<div width='100%' style='text-align:right'>";
if($resultPaper->isdeleted!=0){ echo "<span class='alreadyDeleted' width='100%'>".$this->lang->line('msg_alredyarchived')."</span>";}
echo "</div>";
?>
<table border=0>
	<input type='hidden' id='x_paper_id' value='<?=$resultPaper->paper_id?>'>
	<tr>
		<td>&nbsp;&nbsp;</td>
		<td><div id='nametitle'><?=$resultPaper->paper_code?></div>
		<?=$resultPaper->paper_remark?>
		</td>
	</tr>
</table>
<br/>
<div id='boxcontainer'>
<table>
	<tr>
        <td class='tblDetailViewLabel'><?=$this->lang->line('detail_name')?></td>
        <td><?=$resultPaper->paper_name?></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('detail_grade')?></td>
		<td><?=$resultPaper->paper_grade?></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('detail_liner')?></td>
		<td><?=$resultPaper->med_liner?></td>
	</tr>
	</table>
</div>
<br/>
<div id='boxcontainer'>
<table>
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('supplier_name')?></td>
		<td><?=$resultPaper->partner_name?> <?php if($resultPaper->partnerisdeleted==1) echo "<img src='".base_url()."static/images/extjs/warning.gif' title='The partner is deleted' />"; ?></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>Phone</td>
		<td><?=$resultPaper->partner_phone_office?></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>Fax</td>
		<td><?=$resultPaper->partner_fax?></td>
	</tr>
</table>
</div>
<br/>
<?php 
for ($i=1; $i<$resultPapers->num_rows();$i++) {
?>
<div id='boxcontainer'>
<table>
	<tr>
		<td class='tblDetailViewLabel'>Supplier Name</td>
		<td><?=$resultPapers->row($i)->partner_name?> <?php if($resultPapers->row($i)->partnerisdeleted==1) echo "<img src='".base_url()."static/images/extjs/warning.gif' title='The partner is deleted' />"; ?></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>Phone</td>
		<td><?=$resultPapers->row($i)->partner_phone_office?></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>Fax</td>
		<td><?=$resultPapers->row($i)->partner_fax?></td>
	</tr>
</table>
</div>
<br/>
<?php } ?>
<div id='boxcontainer'>
<table>
	<tr>
        <td class='tblDetailViewLabel'>Created on</td>
        <td><?=$resultPaper->created_on?><?php if($resultPaper->created_by!="") echo " by ".$resultPaper->created_by?></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'>Modified on</td>
		<td><?=$resultPaper->modified_on?><?php if($resultPaper->modified_by!="") echo " by ".$resultPaper->modified_by;?></td>
	</tr>
	</table>
</div>
<?php
} //End View 
if (($action=='edit')||($action=='add')){  //Edit  or Add
if($action=='edit'){
	$resultPaper = $resultPapers->row(0);
	$paper_id=$resultPaper->paper_id;
	$paper_code=$resultPaper->paper_code;
	$paper_name=$resultPaper->paper_name;
	$paper_grade=$resultPaper->paper_grade;
	$med_liner = $resultPaper->med_liner;
	$paper_remark=$resultPaper->paper_remark;
	$partner_id=$resultPaper->pid;
	$tblppid = $resultPaper->tblppid;
	$num = $resultPapers->num_rows();
	$cmd = "updateData()";
	$btntitle = $this->lang->line('update');
}
if($action=='add'){
	$paper_id="";$paper_code="";
	$paper_name="";
	$paper_grade="";
	$med_liner ="";
	$paper_remark="";
	$partner_id=0;
	$tblppid = 0;
	$num=0;
	$cmd = "saveData()";
	$btntitle = $this->lang->line('save');
}
?>

<input type='hidden' id='x_paper_id' value='<?=$paper_id?>'>
<div id='boxcontainer'>
	<table>
	    <tr>
	        <td class='tblDetailViewLabel'>Code:</td>
	        <td><input type='text' id='x_paper_code' value='<?=$paper_code?>'></td>
	    </tr>
		<tr>
			<td class='tblDetailViewLabel'>Remarks</td>
			<td><textarea id='x_paper_remark' rows=3 ><?=$paper_remark?></textarea></td>
		</tr>
	</table>
</div>
<br/>
<div id='boxcontainer'>
<table>
	<tr>
        <td class='tblDetailViewLabel'><?=$this->lang->line('detail_name')?></td>
        <td><input type='text' id='x_paper_name' value='<?=$paper_name?>'></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('detail_grade')?></td>
		<td><input type='text' id='x_paper_grade' value='<?=$paper_grade?>'></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('detail_liner')?></td>
		<td><input type='text' id='x_med_liner' value='<?=$med_liner?>'></td>
	</tr>
	</table>
</div>
<br/>

<?php 
$cntAdd=1;?>
<div id='boxcontainer'>
<table id='partnerTbl'>
	<tr>
		<td class='tblDetailViewLabel'>Partner <?=$cntAdd?></td>
		<td><input type='hidden' id='x_ppid_<?=$cntAdd?>' value='<?=$tblppid?>' />
			<select id='x_partner_name_<?=$cntAdd?>'>
			<?=$paper_class->getNamesArray($partner_id);?>
			</select>
		</td>
		<td onclick="addRow();"><img src='<?=base_url()."static/images/add.gif"?>'/></td>
	</tr>	
<?php 
for ($i=1;$i<$num;$i++) {
	$cntAdd++;
?>
<tr>
	<td class='tblDetailViewLabel'>Partner <?=$cntAdd?></td>
	<td><input type='hidden' id='x_ppid_<?=$cntAdd?>' value='<?=$resultPapers->row($i)->tblppid?>' />
		<select id='x_partner_name_<?=$cntAdd?>'>
		<?=$paper_class->getNamesArray($resultPapers->row($i)->pid);?>
		</select>
	</td>
	<td onclick="removeRow(this);"><img src='<?=base_url()."static/images/delete.gif"?>'/></td>
</tr>
<?php
} ?>
</table>
<div id='partnerErr'></div><input id='cntPartners' type='hidden' value='<?=$cntAdd?>' />
</div>
<br/>


<div  style="width:100%"><center>
<input type="button" value="<?=$btntitle?>" onclick="<?=$cmd?>;">  
<input type="button" value="<?=$this->lang->line('cancel')?>" onclick='cancelData();'>
</center>
</div>
<?php
} //End Edit
?>

</div>