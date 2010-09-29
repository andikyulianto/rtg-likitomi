<div id="general" class="x-hide-display paddedDiv">
<?php
if ($action=='view'){ 
//$logourl = base_url()."static/images/logo.png";
echo "<div width='100%' style='text-align:right'>";
if($resultPartner->isdeleted!=0){ echo "<span class='alreadyDeleted' width='100%'>".$this->lang->line('msg_alredyarchived')."</span>";}
echo "</div>";
?>
<table width='100%'>
	<input type='hidden' id='x_partner_id' value='<?=$resultPartner->partner_id?>'>
	<tr>
		<td>&nbsp;</td>
		<td><div id='nametitle'><?=$resultPartner->partner_name?></div>
		<?php if($resultPartner->partner_type !=="") echo $resultPartner->partner_type."<br/>";?>
		<?php if($resultPartner->partner_name_thai !="") echo $resultPartner->partner_name_thai."<br/>";?>
		<?=$resultPartner->partner_code?>
		</td>
		<td align='right'>ID: <?=$resultPartner->partner_id?></td>
	</tr>
</table>
<br/>
<div id='boxcontainer'>
<table>
	<tr>
        <td class='tblDetailViewLabel'><?=$this->lang->line('ph_office')?></td>
        <td><?=$resultPartner->partner_phone_office?></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('fax')?></td>
		<td><?=$resultPartner->partner_fax?></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('other_phone')?></td>
		<td><?=$resultPartner->partner_other_phone?></td>
	</tr>
	</table>
</div>
<br/>

<div id='boxcontainer'>
<table>
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('billing')?></td>
		<td ><?=$resultPartner->partner_billing_address?></td>
	</tr>
	<?php
		$cntAdd=0;
		foreach ($resultPartnerAddresses as $address){
			$cntAdd++;
	?>
	<tr>
		<td class='tblDetailViewLabel'>Send Address_<?=$cntAdd?></td>
		<td><?=$address->address?></td>
	</tr>
			
	<?php } ?>
</table>
</div>
<br/>

<div id='boxcontainer'>
<table>
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('supplier_code')?></td>
		<td><?=$resultPartner->partner_supplier_code?></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('credit_term')?></td>
		<td><?=$resultPartner->partner_credit_term?></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('email')?></td>
		<td><?=$resultPartner->partner_email?></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('web')?></td>
		<td><?=$resultPartner->partner_website?></td>
	</tr>
</table>
</div>
<br/>
<div id='boxcontainer'>
<table>
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('contact_title')?></td>
		<td><?=$resultPartner->partner_contact_person?></td>
	</tr> 
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('contact_person')?></td>
		<td><?=$resultPartner->partner_contact_title?></td>
	</tr>
</table>
</div>
<br/>

<div id='boxcontainer'>
<table>
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('date_entered')?></td>
		<td><?=$resultPartner->created_on?><?php if($resultPartner->created_by!="") echo " by ".$resultPartner->created_by;?></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('date_mod')?></td>
		<td><?=$resultPartner->modified_on?><?php if($resultPartner->modified_by!="") echo " by ".$resultPartner->modified_by;?></td>
	</tr>  
	<tr>                   
		<td class='tblDetailViewLabel'><?=$this->lang->line('desc')?></td>
		<td ><?=$resultPartner->partner_description?></td>
	</tr>  
</table>
</div>
<?php
} //End View 
?>

<?php
if (($action=='edit')||($action=='add')){  //Edit  or Add
if($action=='edit'){
	$partner_id=$resultPartner->partner_id;
	$partner_name=$resultPartner->partner_name;
	$partner_name_thai=$resultPartner->partner_name_thai;
	$partner_code = $resultPartner->partner_code;
	$partner_type=$resultPartner->partner_type;
	$partner_phone_office=$resultPartner->partner_phone_office;
	$partner_fax=$resultPartner->partner_fax;
	$partner_other_phone=$resultPartner->partner_other_phone;
	$partner_email=$resultPartner->partner_email;
	$partner_website=$resultPartner->partner_website;
	$partner_contact_person=$resultPartner->partner_contact_person;
	$partner_contact_title=$resultPartner->partner_contact_title;
	$logo=$resultPartner->logo;
	$partner_description=$resultPartner->partner_description;
	$partner_billing_address=$resultPartner->partner_billing_address;
	$partner_credit_term=$resultPartner->partner_credit_term;
	$partner_supplier_code=$resultPartner->partner_supplier_code;
	$cmd = "updateData()";
	$btntitle = $this->lang->line('update');
}
if($action=='add'){
	$partner_id="";$partner_name="";
	$partner_name_thai="";$partner_code ="";$partner_type="";
	$partner_phone_office="";$partner_fax="";
	$partner_other_phone="";$partner_email="";
	$partner_website="";$partner_contact_person="";
	$partner_contact_title="";$partner_credit_term="";
	$partner_supplier_code="";
	$logo="";
	$partner_description="";
	$partner_billing_address="";
	$cmd = "saveData()";
	$btntitle = $this->lang->line('save');
}
//$logourl = base_url()."static/images/logo.png";
?>
<table border=0>
	<input type='hidden' id='x_partner_id' value='<?=$partner_id?>'>
	<tr>
		<td>&nbsp;</td>
		<td>
        <table>
            <tr>
                <td align='right'>Name:</td>
                <td><input type='text' id='x_partner_name' value='<?=$partner_name?>'></td>
            </tr>
            <tr>
                <td align='right'>Type:</td>
                <td>
                    <select id='x_partner_type'>
                        <option value="Customer"
                            <?php if($partner_type=='Customer')echo 'selected'; ?>>
                            <?=$this->lang->line('customer')?>
                        </option>
                        <option value="Supplier"
                            <?php if($partner_type=='Supplier')echo 'selected'; ?>>
                            <?=$this->lang->line('supplier')?>
                        </option>
                    </select>
                </td>
            </tr>
            <tr>
                <td align='right'>Name (Thai):</td>
                <td><input type='text' id='x_partner_name_thai' value='<?=$partner_name_thai?>'></td>
            </tr>
			<tr>
                <td align='right'>Code:</td>
                <td><input type='text' id='x_partner_code' value='<?=$partner_code?>'></td>
            </tr>
        </table>
		</td>
	</tr>
</table>
<br/>

<div id='boxcontainer'>
<table>
	<tr>
        <td class='tblDetailViewLabel'><?=$this->lang->line('ph_office')?></td>
        <td><input type='text' id='x_partner_phone_office' value='<?=$partner_phone_office?>'></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('fax')?></td>
		<td><input type='text' id='x_partner_fax' value='<?=$partner_fax?>'></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('other_phone')?></td>
		<td><input type='text' id='x_partner_other_phone' value='<?=$partner_other_phone?>'></td>
	</tr>
	</table>
</div>
<br/>


<div id='boxcontainer'>
<table id='addressTbl'>
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('billing')?></td>
		<td><textarea id='x_partner_billing_address' rows=3 ><?=$partner_billing_address?></textarea></td>
		<td onclick="addRow();"><img src='<?=base_url()."static/images/add.gif"?>'/></td>
	</tr>
	<?php
	$cntAdd=0;
	if($action=='edit'){
		foreach ($resultPartnerAddresses as $address){
			$cntAdd++;
	?>
	<tr>
		<td class='tblDetailViewLabel'>Send Address_<?=$cntAdd?></td>
		<td><input type='hidden' id='x_addressid_<?=$cntAdd?>' value='<?=$address->address_id?>' />
			<textarea id='x_address_<?=$cntAdd?>' rows=3><?=$address->address?></textarea>
		<td onclick="removeRow(this);"><img src='<?=base_url()."static/images/delete.gif"?>'/></td>
	</tr>
	<?php }} ?>
</table>
<div id='addressErr'></div><input id='cntSendAddress' type='hidden' value='<?=$cntAdd?>' />
</div>
<br/>

<div id='boxcontainer'>
<table>
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('supplier_code')?></td>
		<td><input type='text' id='x_partner_supplier_code' value='<?=$partner_supplier_code?>'></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('credit_term')?></td>
		<td><input type='text' id='x_partner_credit_term' value='<?=$partner_credit_term?>'></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('email')?></td>
		<td><input type='text' id='x_partner_email' value='<?=$partner_email?>'></td>
	</tr>
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('web')?></td>
		<td><input type='text' id='x_partner_website' value='<?=$partner_website?>'></td>
	</tr>
</table>
</div>
<br/>
<div id='boxcontainer'>
<table>
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('contact_title')?></td>
		<td><input type='text' id='x_partner_contact_title' value='<?=$partner_contact_title?>'></td>
	</tr> 
	<tr>
		<td class='tblDetailViewLabel'><?=$this->lang->line('contact_person')?></td>
		<td><input type='text' id='x_partner_contact_person' value='<?=$partner_contact_person?>'></td>
	</tr>
</table>
</div>
<br/>

<div id='boxcontainer'>
<table> 
	<tr>                   
		<td class='tblDetailViewLabel'><?=$this->lang->line('desc')?></td>
		<td><textarea id='x_partner_description' rows=3 ><?=$partner_description?></textarea></td>
	</tr>  
</table>
</div>
<br/>
<div  style="width:100%"><center>
<input type="button" value="<?=$btntitle?>" onclick="<?=$cmd?>;">  
<input type="button" value="<?=$this->lang->line('cancel')?>" onclick='cancelData();'>
</center></div>

<?php
} //End Edit 
?>
</div>