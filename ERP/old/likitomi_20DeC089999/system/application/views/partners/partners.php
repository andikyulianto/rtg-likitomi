<script type="text/javascript">
/**
 * @author sanjilshrestha
 */
	var firstrowoffset = 0;
	var lastrowoffset = 0; 
	var searchRowIndex= <?=count($leftmenu)?>;
	
	window.onload = function() {
		activatePlaceholders();
		logoutTips();
	}

	function startSearch(the_key) {	
	    if (!the_key )
	    {
	        if(window.event!==null) the_key = window.event.keyCode;
	    }
		if(( the_key > 64 && the_key < 91)||( the_key > 95 && the_key < 111)){
			searchPartners();
		} 
		else if (the_key > 47 && the_key < 58) {
			searchPartners();
		} 
		else if(the_key==8){
			searchPartners();
		} 
		else if(the_key==13) {
			//document.getElementById('searchtext').value="";
			document.getElementById('searchtext').focus = false;
			var autoSelectId = autoLoadFirstData();
			if (autoSelectId != 0) {
				loadPartnerDetail(autoSelectId);
			}
		}
		
	}
	
	function searchPartners(){
		var searchkeyword = document.getElementById('searchtext').value;
		Ext.Ajax.request({
			url: BASEURL + 'index.php/partners/search/',
			params : { search : searchkeyword},
			success: function ( result, request ) { 
				document.getElementById('listdivcontainer').innerHTML = result.responseText;
				displaySearchCnt();
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});
	
		// Global Ajax events can be handled on every request!
		Ext.Ajax.on({
		    'beforerequest': function(){
				loadAjax("<?=$this->lang->line('ajax_loading_partners')?>");
			},
		    'requestcomplete': function(){
				unloadAjax();
			}
		});
	}
	
	function updateCounter(){
		Ext.Ajax.request({
			url: BASEURL + 'index.php/partners/getCounters/',
			params : { action : "counter"},
			success: function ( result, request ) { 
				var countValue = eval(result.responseText);
				<?php for($i=0;$i<count($leftmenu);$i++) { ?>
					document.getElementById('counter_<?=$i?>').innerHTML=countValue[<?=$i?>];
				<?php }?>	
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});
	}

	function loadPartners(partner_type){
		window.scrollTo(0,0);
		clearLoads();
		Ext.Ajax.request({
			url: BASEURL + 'index.php/partners/getNames/',
			params : { partner_type : partner_type},
			success: function ( result, request ) { 
				document.getElementById('listdivcontainer').innerHTML = result.responseText;
				
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});
	
		// Global Ajax events can be handled on every request!
		Ext.Ajax.on({
		    'beforerequest': function(){
				loadAjax("<?=$this->lang->line('ajax_loading_partners')?>");
			},
		    'requestcomplete': function(){
				unloadAjax();
			}
		});
	}
	
	function loadPartnerDetailFromRow(partner_id,row){
		if(!row.selected)loadPartnerDetail(partner_id);
	}
	
	function loadPartnerDetail(partner_id){
		document.getElementById('currentselection').value=partner_id;
		Ext.Ajax.request({
			url: BASEURL + 'index.php/partners/getDetails/',
			params : { partner_id : partner_id, action : 'view'},
			success: function ( result, request ) { 
				document.getElementById('detailDivContainer').innerHTML = result.responseText;
				Ext.onReady(partnerDetailDiv);
				unloadAjax();
				window.scrollTo(110,0);
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});
		Ext.Ajax.on({
		    'beforerequest': function(){
				loadAjax("<?=$this->lang->line('ajax_loading_partners')?>");
			},
		    'requestcomplete': function(){
				
			}
		});
	}
	
	function editPartnerDetail(action){
		if (document.getElementById('x_partner_id') != null) 
			partner_id = document.getElementById('x_partner_id').value;
		else (document.getElementById('currentselection') != null) 
			partner_id = document.getElementById('currentselection').value; 
	
		if(partner_id>0 || action=='add')
		{		
			Ext.Ajax.request({
				url: BASEURL + 'index.php/partners/getDetails/',
				params: {
					partner_id: partner_id,
					action: action
				},
				success: function(result, request){
					document.getElementById('detailDivContainer').innerHTML = result.responseText;
					Ext.onReady(partnerDetailDiv);
					updateCounter();
				},
				failure: function(result, request){
					Ext.MessageBox.alert('Failed', result.responseText);
				}
			});
			Ext.Ajax.on({
				'beforerequest': function(){
					loadAjax("<?=$this->lang->line('ajax_loading_partners')?>");
				},
				'requestcomplete': function(){
					unloadAjax();
				}
			});
		} 
		else {
			//To Do
			document.getElementById('detailDivContainer').innerHTML = " <p class='details-info'>"
					+"<?=$this->lang->line('msg_nothingtoedit')?></p>";
		}
	}
	
	function deletePartnerDetail(){
		if (document.getElementById('x_partner_id') != null) {
			partner_id = document.getElementById('x_partner_id').value;
			Ext.Ajax.request({
				url: BASEURL + 'index.php/partners/deleteDetails/',
				params: {
					partner_id: partner_id,
					action: 'delete'
				},
				success: function(result, request){
					clearWindow();
					timeoutMessage("<?=$this->lang->line('msg_successdelete')?>");
					updateCounter();
				},
				failure: function(result, request){
					Ext.MessageBox.alert('Failed', result.responseText);
				}
			});
			Ext.Ajax.on({
				'beforerequest': function(){
					loadAjax("<?=$this->lang->line('ajax_loading_partners')?>");
				},
				'requestcomplete': function(){
					unloadAjax();
				}
			});
		} 
		else {
			document.getElementById('detailDivContainer').innerHTML = " <p class='details-info'>"
					+"<?=$this->lang->line('msg_nothingtodelete')?></p>";
		}
	}
	
	function saveData(){
		var validate = validateText(document.getElementById('x_partner_name'));
		if (validate) {
			var address_cnt = Ext.get('cntSendAddress').dom.value;
			var addressall = "";
			var cnt = 0;
			while (address_cnt > 0) {
				cnt++;
				var obj = 'x_address_' + cnt;
				if (Ext.get(obj) != null) {
					addressall += Ext.get(obj).dom.value + "|";
					address_cnt--;
				}
			}
			Ext.Ajax.request({
				url: BASEURL + 'index.php/partners/saveDetail/',
				params: {
					partner_type: Ext.get('x_partner_type').dom.value,
					partner_name: Ext.get('x_partner_name').dom.value,
					partner_name_thai: Ext.get('x_partner_name_thai').dom.value,
					partner_code: Ext.get('x_partner_code').dom.value,
					partner_supplier_code: Ext.get('x_partner_supplier_code').dom.value,
					partner_credit_term: Ext.get('x_partner_credit_term').dom.value,
					partner_phone_office: Ext.get('x_partner_phone_office').dom.value,
					partner_fax: Ext.get('x_partner_fax').dom.value,
					partner_other_phone: Ext.get('x_partner_other_phone').dom.value,
					partner_email: Ext.get('x_partner_email').dom.value,
					partner_website: Ext.get('x_partner_website').dom.value,
					partner_contact_title: Ext.get('x_partner_contact_title').dom.value,
					partner_contact_person: Ext.get('x_partner_contact_person').dom.value,
					partner_billing_address: Ext.get('x_partner_billing_address').dom.value,
					partner_description: Ext.get('x_partner_description').dom.value,
					address_cnt: Ext.get('cntSendAddress').dom.value,
					partner_addresses: addressall
				},
				success: function(result, request){
					clearWindow();
					loadPartnerDetail(result.responseText);
					timeoutMessage("<?=$this->lang->line('msg_successsaved')?>");
					updateCounter();
				},
				failure: function(result, request){
					Ext.MessageBox.alert('Failed', result.responseText);
				}
			});
			Ext.Ajax.on({
				'beforerequest': function(){
					loadAjax("<?=$this->lang->line('ajax_saving_details')?>");
				},
				'requestcomplete': function(){
					unloadAjax();
				}
			});
		}
	}
	
	function updateData(){
		var validate = validateText(document.getElementById('x_partner_name'));
		if (validate) {
			var partner_id = Ext.get('x_partner_id').dom.value;
			var address_cnt = Ext.get('cntSendAddress').dom.value;
			var addressall = "";
			var addressids = "";
			var cnt = 0;
			while (address_cnt > 0) {
				cnt++;
				var obj = 'x_address_' + cnt;
				var objid = 'x_addressid_' + cnt;
				if (Ext.get(obj) != null) {
					addressall += Ext.get(obj).dom.value + "|";
					addressids += Ext.get(objid).dom.value + "|";
					address_cnt--;
				}
			}
			Ext.Ajax.request({
				url: BASEURL + 'index.php/partners/updateDetail/',
				params: {
					partner_id: partner_id,
					partner_type: Ext.get('x_partner_type').dom.value,
					partner_name: Ext.get('x_partner_name').dom.value,
					partner_name_thai: Ext.get('x_partner_name_thai').dom.value,
					partner_code: Ext.get('x_partner_code').dom.value,
					partner_supplier_code: Ext.get('x_partner_supplier_code').dom.value,
					partner_credit_term: Ext.get('x_partner_credit_term').dom.value,
					partner_phone_office: Ext.get('x_partner_phone_office').dom.value,
					partner_fax: Ext.get('x_partner_fax').dom.value,
					partner_other_phone: Ext.get('x_partner_other_phone').dom.value,
					partner_email: Ext.get('x_partner_email').dom.value,
					partner_website: Ext.get('x_partner_website').dom.value,
					partner_contact_title: Ext.get('x_partner_contact_title').dom.value,
					partner_contact_person: Ext.get('x_partner_contact_person').dom.value,
					partner_billing_address: Ext.get('x_partner_billing_address').dom.value,
					partner_description: Ext.get('x_partner_description').dom.value,
					address_cnt: Ext.get('cntSendAddress').dom.value,
					partner_addresses: addressall,
					partner_addresseids: addressids
				},
				success: function(result, request){
					clearWindow();
					loadPartnerDetail(partner_id);
					timeoutMessage("<?=$this->lang->line('msg_successsaved')?>");
					updateCounter();
				},
				failure: function(result, request){
					Ext.MessageBox.alert('Failed', result.responseText);
				}
			});
			Ext.Ajax.on({
				'beforerequest': function(){
					loadAjax("<?=$this->lang->line('ajax_updating_details')?>");
				},
				'requestcomplete': function(){
					unloadAjax();
				}
			});
		}
	}
	
	function cancelData(){
		loadPartnerDetail(partner_id);
	}	
	
	function deletePartner(){
		if (document.getElementById('x_partner_id') != null) {
			Ext.MessageBox.confirm('Confirm', "<?=$this->lang->line('msg_confirmarchive')?>", confirmDelete);
		} else {
			document.getElementById('detailDivContainer').innerHTML = " <p class='details-info'>"
					+"<?=$this->lang->line('msg_nothingtodelete')?></p>";
		}
	}
	
	function confirmDelete(btn){
        if (btn == 'yes') {
			deletePartnerDetail();
		}
    }
	
	function displaySearchCnt(){		
		if (document.getElementById('searchcounter') != null) {
			document.getElementById("ewlistmain").rows[searchRowIndex].cells[0].innerHTML="<?=$this->lang->line('search_result')?>";
			document.getElementById("ewlistmain").rows[searchRowIndex].cells[1].innerHTML="<span class='counter'>"
					+document.getElementById('searchcounter').value
					+"</span";
			ew_ClearSelected();
			document.getElementById("ewlistmain").rows[searchRowIndex].className="ewTableSelectRow";
			document.getElementById("ewlistmain").rows[searchRowIndex].oClassName="";
			document.getElementById("ewlistmain").rows[searchRowIndex].selected=true;
		}
	}
	
	function clearLoads(){
		document.getElementById("ewlistmain").rows[searchRowIndex].cells[0].innerHTML="";
		document.getElementById("ewlistmain").rows[searchRowIndex].cells[1].innerHTML="";
		document.getElementById('searchtext').value="";activatePlaceholders();
	}
	
	function listproducts(){
		if (document.getElementById('x_partner_id') != null) {
			partner_id = document.getElementById('x_partner_id').value;
			Ext.Ajax.request({
				url: BASEURL + 'index.php/partners/listproducts/',
				params: {
					partner_id: partner_id,
					action : "products"
				},
				success: function(result, request){
					document.getElementById('detailDivContainer').innerHTML = result.responseText;
					unloadAjax();
				},
				failure: function(result, request){
					Ext.MessageBox.alert('Failed', result.responseText);
				}
			});
			Ext.Ajax.on({
				'beforerequest': function(){
					loadAjax("<?=$this->lang->line('ajax_loading_partners')?>");
				},
				'requestcomplete': function(){}
			});
		} 
		else {
			//To Do
		}
	}
	
	function addRow()
	{
		var tbl = document.getElementById('addressTbl');
		var lastRow = tbl.rows.length;
		var iteration = lastRow;
		try {
		 	var row = tbl.insertRow(lastRow);
			cell0= row.insertCell(0);
			cell0.className= 'tblDetailViewLabel';
			cell0.innerHTML="Send Address_"+row.rowIndex;
			cell1 = row.insertCell(1);
			cell1.innerHTML ="<input type='hidden' id='x_addressid_"+row.rowIndex+"' value='0' />";
			cell1.innerHTML +="<textarea id='x_address_"+row.rowIndex+"' rows=3 ></textarea>";
			cell2=row.insertCell(2);
			cell2.setAttribute('onclick','removeRow(this);');
			cell2.innerHTML ='<img src="' + BASEURL + 'static/images/delete.gif'+'"/>';
			document.getElementById('cntSendAddress').value = parseInt(document.getElementById('cntSendAddress').value)+1;
			document.getElementById('x_address_'+row.rowIndex).focus();
		} 
	    catch (ex) {    
			document.getElementById('addressErr').innerHTML = ex;
			document.getElementById('addressErr').style.visibility="visible";
			document.getElementById('addressErr').style.display="block";
	    }  
	}
	function removeRow(td)
	{
		var row= getParent(td,'TR');
		var conf = true;//confirm("Press OK to delete and Cancel to return.");
		if (conf) {
			var tbl = document.getElementById('addressTbl');
			try {
				tbl.deleteRow(row.rowIndex);
				document.getElementById('cntSendAddress').value = parseInt(document.getElementById('cntSendAddress').value)-1;
			} 
			catch (ex) {
				document.getElementById('addressErr').innerHTML = ex;
				document.getElementById('addressErr').style.visibility="visible";
				document.getElementById('addressErr').style.display="block";
			}
		}

	}

	function partnerDetailDiv(){
		 var tabs = new Ext.TabPanel({
		    renderTo: 'detailDivContainer',
		    width:FIXWIDTH,
		    activeTab: 0,
		    frame:false,
			border:false,
			plain:true,
		    defaults:{autoHeight: true},
		    items:[
		        {contentEl:'general', title: ' General '},
		        {contentEl:'product', title: ' Product '}
		    ]
		});
	}
	
	function clearWindow()
	{
		document.getElementById('listdivcontainer').innerHTML="<p class='details-info'>"
				+"<?=$this->lang->line('msg_selectpartners')?></p>";
		document.getElementById('detailDivContainer').innerHTML = " <p class='details-info'>"
					+"<?=$this->lang->line('msg_selectpartners')?></p>";
	}
</script>
<input type='hidden' id='currentselection' value='0' />
<div id="topheader"></div>

<table class='tblcontainer' border='0' width='100%' height='100%' cellspacing="0" cellpadding="0">
	<tr>
    <td colspan=2 class='headertop'>
        <div id='headbar'>
            <table border=0 width=100% >
            	<tr>
            		<td width='320'>
            			<ul class="primary-links">
            				<li><a href='<?=base_url()."index.php"?>'>Home</a></li>
							<li><span>Partners</span></li>
							<li><a href='<?=base_url()."index.php/papers"?>'>Papers</a></li>
							<li><a href='<?=base_url()."index.php/products"?>'>Products</a></li>
						</ul>
            		</td>
					<td align='center'>
						<input type='button' value="<?=$this->lang->line('add')?>" onclick="editPartnerDetail('add');"/>
						<input type='button' value="<?=$this->lang->line('edit')?>" onclick="editPartnerDetail('edit');"/>
						<input type='button' value="<?=$this->lang->line('archive')?>" onclick='deletePartner()'/>
					</td>
                    <td align='right' width='280'>
                        <div id='searchform'>
                            <input id='searchtext' type="text" placeholder="<?=$this->lang->line('search_partners')?>" value="" onkeyup="startSearch(event.which);"/>
                        </div>
                    </td>
					<td width='40px'><a href='<?=base_url()."index.php/auth/logout"?>' id='tip-logout'>
						<img src='<?=base_url()."static/images/logout.png"?>' />
					</a></td>
				</tr>
            </table>
        </div>
    </td>
	</tr>
	<tr>
		<td class='leftbar'>
				<div id='container'><div id="firstbar"> <table id="ewlistmain" class="ewTable">
					<!-- Table body -->
					<?php for($i=0;$i<count($leftmenu);$i++) { ?> 
					<tr onmouseover='ew_MouseOver(this);' onmouseout='ew_MouseOut(this);' class='ewTableRow' onclick='ew_Click(this);loadPartners("<?=$types[$i]?>");'>
						<td><?=$leftmenu[$i]?></td>
						<td align='right'> <span class='counter' id='counter_<?=$i?>'><?=$leftmenu_count[$i]?></span></td>
					</tr>
					<?php } ?>
					<tr class=''>
						<td></td><td align='right'></td>
					</tr>
					<!--<tr onmouseover='ew_MouseOver(this);' onmouseout='ew_MouseOut(this);' class='ewTableRow' onclick='ew_Click(this);'>
						<td><?=$this->lang->line('most_used_partners')?></td>
						<td align='right'></td>
					</tr>
					<tr onmouseover='ew_MouseOver(this);' onmouseout='ew_MouseOut(this);' class='ewTableRow' onclick='ew_Click(this);'>
						<td><?=$this->lang->line('recently_used_partners')?></td>
						<td align='right'></td>
					</tr>-->
				</table></div></div>
		</td>
		<td>
			<table border='0'>
				<tr>
                <td class='leftbar2'>
                    <div id='container'>
                        <div id='listdivcontainer'>
                            <p class="details-info">
                                <?=$this->lang->line('msg_selectpartners')?>
                            </p>
                        </div>
                    </div>
                </td>
					<td valign='top' width='100%'>
						<div id="flashMessage" style="display:none;"></div>
<!-- Page Detail -->
<!-- Partner Detail -->
<div id='detailDivContainer'>
	<div id="general" class="x-hide-display"></div>
	<div id="product" class="x-hide-display"></div>
</div>
<!-- Partner Detail End -->
					</td>
				</tr>
			</table>
		</td>
	</tr>
</table>