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
			searchPapers();
		} 
		else if (the_key > 47 && the_key < 58) {
			searchPapers();
		} 
		else if(the_key==8){
			searchPapers();
		} 
		else if(the_key==13) {
			//document.getElementById('searchtext').value="";
			document.getElementById('searchtext').focus = false;
			var autoSelectId = autoLoadFirstData();
			if (autoSelectId != 0) {
				loadPaperDetail(autoSelectId);
			}
		}	
	}
	
	function searchPapers(){
		var searchkeyword = document.getElementById('searchtext').value;
		Ext.Ajax.request({
			url: BASEURL + 'index.php/papers/search/',
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
				loadAjax("<?=$this->lang->line('ajax_loading_papers')?>");
			},
		    'requestcomplete': function(){
				unloadAjax();
			}
		});
	}
	
	function updateCounter(){
		Ext.Ajax.request({
			url: BASEURL + 'index.php/papers/getCounters/',
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

	function loadPapers(paper_code){
		window.scrollTo(0,0);
		clearLoads();
		Ext.Ajax.request({
			url: BASEURL + 'index.php/papers/getNames/',
			params : { paper_code : paper_code},
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
				loadAjax("<?=$this->lang->line('ajax_loading_papers')?>");
			},
		    'requestcomplete': function(){
				unloadAjax();
			}
		});
	}
	
	function loadPaperDetailFromRow(paper_id,row){
		if(!row.selected)loadPaperDetail(paper_id);
	}
	
	function loadPaperDetail(paper_id){
		document.getElementById('currentselection').value=paper_id;
		Ext.Ajax.request({
			url: BASEURL + 'index.php/papers/getDetails/',
			params : { paper_id : paper_id, action : 'view'},
			success: function ( result, request ) { 
				document.getElementById('detailDivContainer').innerHTML = result.responseText;
				Ext.onReady(paperDetailDiv);
				unloadAjax();
				window.scrollTo(110,0);
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});
		Ext.Ajax.on({
		    'beforerequest': function(){
				loadAjax("<?=$this->lang->line('ajax_loading_papers')?>");
			},
		    'requestcomplete': function(){
				
			}
		});
	}
	
	function editPaperDetail(action){
		if (document.getElementById('x_paper_id') != null) 
			paper_id = document.getElementById('x_paper_id').value;
		else (document.getElementById('currentselection') != null) 
			paper_id = document.getElementById('currentselection').value; 
	
		if(paper_id>0 || action=='add')
		{		
			Ext.Ajax.request({
				url: BASEURL + 'index.php/papers/getDetails/',
				params: {
					paper_id: paper_id,
					action: action
				},
				success: function(result, request){
					document.getElementById('detailDivContainer').innerHTML = result.responseText;
					Ext.onReady(paperDetailDiv);
					updateCounter();
				},
				failure: function(result, request){
					Ext.MessageBox.alert('Failed', result.responseText);
				}
			});
			Ext.Ajax.on({
				'beforerequest': function(){
					loadAjax("<?=$this->lang->line('ajax_loading_papers')?>");
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
	
	function deletePaperDetail(){
		if (document.getElementById('x_paper_id') != null) {
			paper_id = document.getElementById('x_paper_id').value;
			Ext.Ajax.request({
				url: BASEURL + 'index.php/papers/deleteDetails/',
				params: {
					paper_id: paper_id,
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
					loadAjax("<?=$this->lang->line('ajax_loading_papers')?>");
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
		var validate = validateText(document.getElementById('x_paper_code'));
		if (validate) {
			var cntPartners = Ext.get('cntPartners').dom.value;
			var partnerids = "";
			var cnt = 0;
			while (cntPartners > 0) {
				cnt++;
				var objid = 'x_partner_name_' + cnt;
				if (Ext.get(objid) != null) {
					partnerids += Ext.get(objid).dom.value + "|";
					cntPartners--;
				}
			}
			Ext.Ajax.request({
				url: BASEURL + 'index.php/papers/saveDetail/',
				params: {
					paper_code: Ext.get('x_paper_code').dom.value,
					paper_name: Ext.get('x_paper_name').dom.value,
					paper_grade: Ext.get('x_paper_grade').dom.value,
					med_liner: Ext.get('x_med_liner').dom.value,
					paper_remark: Ext.get('x_paper_remark').dom.value,
					partnerids: partnerids
				},
				success: function(result, request){
					clearWindow();
					loadPaperDetail(result.responseText);
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
		var validate = validateText(document.getElementById('x_paper_code'));
		if (validate) {
			var paper_id = Ext.get('x_paper_id').dom.value;
			var cntPartners = Ext.get('cntPartners').dom.value;
			var partnerids = "";
			var ppids = "";
			var cnt = 0;
			while (cntPartners > 0) {
				cnt++;
				var objid = 'x_partner_name_' + cnt;
				var objppid = 'x_ppid_' + cnt;
				if (Ext.get(objid) != null) {
					partnerids += Ext.get(objid).dom.value + "|";
					ppids += Ext.get(objppid).dom.value + "|";
					cntPartners--;
				}
			}
			Ext.Ajax.request({
				url: BASEURL + 'index.php/papers/updateDetail/',
				params: {
					paper_id: paper_id,
					paper_code: Ext.get('x_paper_code').dom.value,
					paper_name: Ext.get('x_paper_name').dom.value,
					paper_grade: Ext.get('x_paper_grade').dom.value,
					med_liner: Ext.get('x_med_liner').dom.value,
					paper_remark: Ext.get('x_paper_remark').dom.value,
					partnerids: partnerids,
					ppids: ppids
				},
				success: function(result, request){
					loadPaperDetail(paper_id);
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
		loadPaperDetail(paper_id);
	}	
	
	function deletePaper(){
		if (document.getElementById('x_paper_id') != null) {
			Ext.MessageBox.confirm('Confirm', "<?=$this->lang->line('msg_confirmarchive')?>", confirmDelete);
		} else {
			document.getElementById('detailDivContainer').innerHTML = " <p class='details-info'>"
					+"<?=$this->lang->line('msg_nothingtodelete')?></p>";
		}
	}
	
	function confirmDelete(btn){
        if (btn == 'yes') {
			deletePaperDetail();
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
	
	function addRow()
	{
		var tbl = document.getElementById('partnerTbl');
		var lastRow = tbl.rows.length;
		var iteration = lastRow;
		try {
		 	var row = tbl.insertRow(lastRow);
			cell0= row.insertCell(0);
			cell0.className= 'tblDetailViewLabel';
			cell0.innerHTML="Partner "+(row.rowIndex+1)+"";
			cell1 = row.insertCell(1);
			cell1.innerHTML ="<input type='hidden' id='x_ppid_"+(row.rowIndex+1)+"' value='0' />";
			cell1.innerHTML +="<select id='x_partner_name_"+(row.rowIndex+1)+"' ><?=$paper_class->getNamesArray(0)?>";
			cell1.innerHTML +="";
			cell1.innerHTML +="</select>";
			cell2=row.insertCell(2);
			cell2.setAttribute('onclick','removeRow(this);');
			cell2.innerHTML ='<img src="' + BASEURL + 'static/images/delete.gif'+'"/>';
			document.getElementById('cntPartners').value = parseInt(document.getElementById('cntPartners').value)+1;
			document.getElementById('x_partner_name_'+(row.rowIndex+1)).focus();
		} 
	    catch (ex) {    
			document.getElementById('partnerErr').innerHTML = ex;
			document.getElementById('partnerErr').style.visibility="visible";
			document.getElementById('partnerErr').style.display="block";
	    }  
	}
	
	function removeRow(td)
	{
		var row= getParent(td,'TR');
		var conf = true;//confirm("Press OK to delete and Cancel to return.");
		if (conf) {
			var tbl = document.getElementById('partnerTbl');
		
			try {
				tbl.deleteRow(row.rowIndex);
				document.getElementById('cntPartners').value = parseInt(document.getElementById('cntPartners').value)-1;
			} 
			catch (ex) {
				document.getElementById('partnerErr').innerHTML = ex;
				document.getElementById('partnerErr').style.visibility="visible";
				document.getElementById('partnerErr').style.display="block";
			}
		}

	}
	
	function paperDetailDiv(){
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
		    ]
		});
	}
	
	function clearWindow()
	{
		document.getElementById('listdivcontainer').innerHTML="<p class='details-info'>"
				+"<?=$this->lang->line('msg_selectpapers')?></p>";
		document.getElementById('detailDivContainer').innerHTML = " <p class='details-info'>"
					+"<?=$this->lang->line('msg_selectpapers')?></p>";
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
							<li><a href='<?=base_url()."index.php/partners"?>'>Partners</a></li>
							<li><span>Papers</span></li>
							<li><a href='<?=base_url()."index.php/products"?>'>Products</a></li>
						</ul>
            		</td>
					<td align='center'>
						<input type='button' value="<?=$this->lang->line('add')?>" onclick="editPaperDetail('add');"/>
						<input type='button' value="<?=$this->lang->line('edit')?>" onclick="editPaperDetail('edit');"/>
						<input type='button' value="<?=$this->lang->line('archive')?>" onclick='deletePaper()'/>
					</td>
                    <td align='right' width='280'>
                        <div id='searchform'>
                            <input id='searchtext' type="text" placeholder="<?=$this->lang->line('search_papers')?>" value="" onkeyup="startSearch(event.which);"/>
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
					<tr onmouseover='ew_MouseOver(this);' onmouseout='ew_MouseOut(this);' class='ewTableRow' onclick='ew_Click(this);loadPapers("<?=$types[$i]?>");'>
						<td><?=$leftmenu[$i]?></td>
						<td align='right'> <span class='counter' id='counter_<?=$i?>'><?=$leftmenu_count[$i]?></span></td>
					</tr>
					<?php } ?>
					<tr class=''>
						<td></td><td align='right'></td>
					</tr>
					<!--<tr onmouseover='ew_MouseOver(this);' onmouseout='ew_MouseOut(this);' class='ewTableRow' onclick='ew_Click(this);'>
						<td><?=$this->lang->line('most_used_papers')?></td>
						<td align='right'></td>
					</tr>
					<tr onmouseover='ew_MouseOver(this);' onmouseout='ew_MouseOut(this);' class='ewTableRow' onclick='ew_Click(this);'>
						<td><?=$this->lang->line('recently_used_papers')?></td>
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
                                <?=$this->lang->line('msg_selectpapers')?>
                            </p>
                        </div>
                    </div>
                </td>
					<td valign='top' width='100%'>
						<div id="flashMessage" style="display:none;"></div>
<!-- Page Detail -->
<div id='detailDivContainer'>
	 <div id="general" class="x-hide-display"></div>
</div>
<!-- Page Detail End -->
					</td>
				</tr>
			</table>
		</td>
	</tr>
</table>
