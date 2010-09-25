<script type="text/javascript">
/**
 * @author sanjilshrestha
 */
	var firstrowoffset = 0;
	var lastrowoffset = 0; 
	var searchRowIndex= <?=count($leftmenu)?>;
	var LOADING_TEXT	=	"<?=$this->lang->line('ajax_loading_products')?>";
	
	window.onload = function() {
		activatePlaceholders();
		logoutTips();
	}
	
	function updateCounter(){
		Ext.Ajax.request({
			url: BASEURL + 'index.php/products/getCounters/',
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
	
	function loadProducts($product_type){
		window.scrollTo(0,0);
		clearLoads(); 
		Ext.Ajax.request({
			url: BASEURL + 'index.php/products/getNames/',
			params : { product_type : $product_type},
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
				loadAjax("<?=$this->lang->line('ajax_loading_products')?>");
			},
		    'requestcomplete': function(){
				unloadAjax();
			}
		});
	}
	
	function loadProductDetail(product_id){
		document.getElementById('currentselection').value=product_id;
		Ext.Ajax.request({
			url: BASEURL + 'index.php/products/getDetails/',
			params : { product_id : product_id, action : 'view'},
			success: function ( result, request ) { 
				var el = Ext.get('detailDivContainer');
				el.update(result.responseText);
				Ext.onReady(productDetailDiv);
				/*el.fadeIn({
				    endOpacity: 1, 
				    easing: 'easeOut',
				    duration: .1
				});*/
				//el.slideIn('l', { duration: 0.5 });
				unloadAjax();
				window.scrollTo(110,0);
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});
		Ext.Ajax.on({
		    'beforerequest': function(){
				loadAjax("<?=$this->lang->line('ajax_loading_products')?>");
			},
		    'requestcomplete': function(){
				
			}
		});
	}
	
	function editProductDetail(action){
		if (document.getElementById('x_product_id') != null) 
			product_id = document.getElementById('x_product_id').value;
		else (document.getElementById('currentselection') != null) 
			product_id = document.getElementById('currentselection').value; 
		if(action=='add') cw_ClearSelected();
		if(product_id>0 || action=='add')
		{		
			Ext.Ajax.request({
				url: BASEURL + 'index.php/products/getDetails/',
				params: {
					product_id: product_id,
					action: action
				},
				success: function(result, request){
					document.getElementById('detailDivContainer').innerHTML = result.responseText;
					Ext.onReady(productDetailDiv);
					Ext.onReady(fileUploadFunction);
					Ext.onReady(fileUploadFunction_large);
					document.getElementById('productid_file').value=product_id;
					document.getElementById('productid_file_large').value=product_id;
					unloadAjax();
				},
				failure: function(result, request){
					Ext.MessageBox.alert('Failed', result.responseText);
				}
			});
			Ext.Ajax.on({
				'beforerequest': function(){
					loadAjax("<?=$this->lang->line('ajax_loading_products')?>");
				},
				'requestcomplete': function(){}
			});
		} 
		else {
			//To Do
			document.getElementById('detailDivContainer').innerHTML = " <p class='details-info'>"
					+"<?=$this->lang->line('msg_nothingtoedit')?></p>";
		}
	}	
	
	function deleteProductDetail(){
		if (document.getElementById('x_product_id') != null) {
			product_id = document.getElementById('x_product_id').value;
			Ext.Ajax.request({
				url: BASEURL + 'index.php/products/deleteDetails/',
				params: {
					product_id: product_id,
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
					loadAjax("<?=$this->lang->line('ajax_loading_products')?>");
				},
				'requestcomplete': function(){
					unloadAjax();
				}
			});
		} 
		else {
			document.getElementById('detailDivContainer').innerHTML = "<p class='details-info'>"
					+"<?=$this->lang->line('msg_nothingtodelete')?></p>";
		}
	}
	
	function productData(i){
		var productdata =  Ext.get('x_pid_'+i).dom.value+"|"+
			Ext.get('x_code_'+i).dom.value+"|"+
			Ext.get('x_flute_'+i).dom.value+"|"+
			Ext.get('x_DF_'+i).dom.value+"|"+
			Ext.get('x_BM_'+i).dom.value+"|"+
			Ext.get('x_BL_'+i).dom.value+"|"+
			Ext.get('x_CM_'+i).dom.value+"|"+
			Ext.get('x_CL_'+i).dom.value+"|"+
			Ext.get('x_length_'+i).dom.value+"|"+
			Ext.get('x_width_'+i).dom.value+"|"+
			Ext.get('x_height_'+i).dom.value+"|"+
			Ext.get('x_qty_set_'+i).dom.value;
		return productdata;
	}

	function saveData()
	{
		productsall_0 = productData(0);
		productsall_1 = productData(1);
		productsall_2 = productData(2);
		
		Ext.Ajax.request({
		url: BASEURL + 'index.php/products/saveDetail/',
		params : {
			product_code:Ext.get('x_product_code').dom.value,
			product_name:Ext.get('x_product_name').dom.value,
			partner_id:Ext.get('x_partner_id').dom.value,
			product_type:Ext.get('x_product_type').dom.value,
			customer_part_no:Ext.get('x_customer_part_no').dom.value,
			ink_1:Ext.get('x_ink_1').dom.value,
			ink_2:Ext.get('x_ink_2').dom.value,
			ink_3:Ext.get('x_ink_3').dom.value,
			ink_4:Ext.get('x_ink_4').dom.value,
			joint_type:Ext.get('x_joint_type').dom.value,
			joint_details:Ext.get('x_joint_details').dom.value,
			box_style:Ext.get('x_box_style').dom.value,
			rope_color:Ext.get('x_rope_color').dom.value,
			pcs_bundle:Ext.get('x_pcs_bundle').dom.value,
			level:Ext.get('x_level').dom.value,
			p_width_mm:Ext.get('x_p_width_mm').dom.value,
			p_width_inch:Ext.get('x_p_width_inch').dom.value,
			qty_allowance:Ext.get('x_qty_allowance').dom.value,
			scoreline_f:Ext.get('x_scoreline_f').dom.value,
			scoreline_d:Ext.get('x_scoreline_d').dom.value,
			scoreline_f2:Ext.get('x_scoreline_f2').dom.value,
			slit:Ext.get('x_slit').dom.value,
			blank:Ext.get('x_blank').dom.value,
			t_length:Ext.get('x_t_length').dom.value,
			cut:Ext.get('x_cut').dom.value,
			next_process:Ext.get('x_next_process').dom.value,
			code_pd:Ext.get('x_code_pd').dom.value,
			code_rd:Ext.get('x_code_rd').dom.value,
			sketch:Ext.get('x_sketch').dom.value,
			sketch_large:Ext.get('x_sketch_large').dom.value,
			remark:Ext.get('x_remark').dom.value,
			productsall_0:productsall_0,
			productsall_1:productsall_1,
			productsall_2:productsall_2,
		},
		success: function ( result, request ) {
			clearWindow();
			loadProductDetail(result.responseText);
			timeoutMessage("<?=$this->lang->line('msg_successsaved')?>");
			updateCounter();
		},
		failure: function ( result, request) { 
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
	
	function updateData(){
		var product_id=Ext.get('x_product_id').dom.value;
		productsall_0 = productData(0);
		productsall_1 = productData(1);
		productsall_2 = productData(2);
		
		Ext.Ajax.request({
		url: BASEURL + 'index.php/products/updateDetail/',
		params : {
			product_id:product_id,
			product_code:Ext.get('x_product_code').dom.value,
			product_name:Ext.get('x_product_name').dom.value,
			partner_id:Ext.get('x_partner_id').dom.value,
			product_type:Ext.get('x_product_type').dom.value,
			customer_part_no:Ext.get('x_customer_part_no').dom.value,
			ink_1:Ext.get('x_ink_1').dom.value,
			ink_2:Ext.get('x_ink_2').dom.value,
			ink_3:Ext.get('x_ink_3').dom.value,
			ink_4:Ext.get('x_ink_4').dom.value,
			joint_type:Ext.get('x_joint_type').dom.value,
			joint_details:Ext.get('x_joint_details').dom.value,
			box_style:Ext.get('x_box_style').dom.value,
			rope_color:Ext.get('x_rope_color').dom.value,
			pcs_bundle:Ext.get('x_pcs_bundle').dom.value,
			level:Ext.get('x_level').dom.value,
			p_width_mm:Ext.get('x_p_width_mm').dom.value,
			p_width_inch:Ext.get('x_p_width_inch').dom.value,
			qty_allowance:Ext.get('x_qty_allowance').dom.value,
			scoreline_f:Ext.get('x_scoreline_f').dom.value,
			scoreline_d:Ext.get('x_scoreline_d').dom.value,
			scoreline_f2:Ext.get('x_scoreline_f2').dom.value,
			slit:Ext.get('x_slit').dom.value,
			blank:Ext.get('x_blank').dom.value,
			t_length:Ext.get('x_t_length').dom.value,
			cut:Ext.get('x_cut').dom.value,
			next_process:Ext.get('x_next_process').dom.value,
			code_pd:Ext.get('x_code_pd').dom.value,
			code_rd:Ext.get('x_code_rd').dom.value,
			sketch:Ext.get('x_sketch').dom.value,
			sketch_large:Ext.get('x_sketch_large').dom.value,
			remark:Ext.get('x_remark').dom.value,
			productsall_0:productsall_0,
			productsall_1:productsall_1,
			productsall_2:productsall_2,	
		},
		success: function ( result, request ) {
			loadProductDetail(product_id);
			timeoutMessage("<?=$this->lang->line('msg_successsaved')?>");
			updateCounter();
		},
		failure: function ( result, request) { 
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
	
	function cancelData(){
		loadProductDetail(product_id);
	}	
	
	function deleteProduct(){
		if (document.getElementById('x_product_id') != null) {
			Ext.MessageBox.confirm('Confirm', "<?=$this->lang->line('msg_confirmarchive')?>", confirmDelete);
		} else {
			document.getElementById('detailDivContainer').innerHTML = " <p class='details-info'>"
					+"<?=$this->lang->line('msg_nothingtodelete')?></p>";
		}
	}
	function confirmDelete(btn){
        if (btn == 'yes') {
			deleteProductDetail();
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
	
	function productDetailDiv(){
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
		        {contentEl:'sketchdiv', title: ' Sketch '},
				{contentEl :'salesHistory', title: ' Sales '},
				//{autoLoad :'sales', title: ' Sketch Large ', listeners: {activate: handleActivate3}},
		    ]
		});
	}
	
	function handleActivate3(tab){
       prd_AutoSelect();
	   Ext.onReady(salesOrderTips);
	   document.getElementById('x_amount_1').focus();
    }

	function fileUploadFunction()
	{
		Ext.QuickTips.init();
		var fp = new Ext.FormPanel({
	        renderTo: 'fi-form',
	        fileUpload: true,
	        width: 400,
	        frame: false,
			border:false,
	        autoHeight: true,
	        bodyStyle: 'background-color:#fafbfc',
	        labelWidth: 50,
	        defaults: {
	            anchor: '95%',
	            allowBlank: false,
	            msgTarget: 'side'
	        },
	        items: [{
				xtype: 'hidden',
				id: 'productid_file',
				name: 'productid_file',
				hideLabel: true,
			},{
	            xtype: 'fileuploadfield',
	            id: 'form-file',
	            emptyText: 'Select an image',
	            name: 'photo-path',
				hideLabel: true,
	            buttonCfg: {
	                text: '',
	                iconCls: 'upload-icon'
	            }
	        }],
	        buttons: [{
	            text: 'Upload',
	            handler: function()
				{
	                if(fp.getForm().isValid())
					{
		                fp.getForm().submit(
						{
		                    url: '<?=base_url()."index.php/products/fileUpload"?>',
		                    waitMsg: 'Uploading product image...',
		                    success: function(fp, o)
							{
		                        var el = Ext.fly('fi-form');
								el.update('<?=base_url()."files/"?>'+o.result.file);
								document.getElementById('x_sketch').value='<?="files/"?>'+o.result.file;
								document.getElementById('prevSketch').innerHTML='';
								if(!el.isVisible()){
									el.slideIn('t', {
										duration: .2,
										easing: 'easeIn',
										callback: function(){
											el.highlight();
										}
									});
								}else{
									el.highlight();
								}
		                    }
		                });
	                }
	            }
	        },{
	            text: 'Reset',
	            handler: function()
				{
	                fp.getForm().reset();
	            }
        	}]
		});
	}
	
	function fileUploadFunction_large()
	{
		Ext.QuickTips.init();
		var fp = new Ext.FormPanel({
	        renderTo: 'fi-form_large',
	        fileUpload: true,
	        width: 400,
	        frame: false,
			border:false,
	        autoHeight: true,
	        bodyStyle: 'background-color:#fafbfc',
	        labelWidth: 50,
	        defaults: {
	            anchor: '95%',
	            allowBlank: false,
	            msgTarget: 'side'
	        },
	        items: [{
				xtype: 'hidden',
				id: 'productid_file_large',
				name: 'productid_file_large',
				hideLabel: true,
			},{
	            xtype: 'fileuploadfield',
	            id: 'form-file_large',
	            emptyText: 'Select an image',
	            name: 'photo-path_large',
				hideLabel: true,
	            buttonCfg: {
	                text: '',
	                iconCls: 'upload-icon'
	            }
	        }],
	        buttons: [{
	            text: 'Upload',
	            handler: function()
				{
	                if(fp.getForm().isValid())
					{
		                fp.getForm().submit(
						{
		                    url: '<?=base_url()."index.php/products/fileUploadlarge"?>',
		                    waitMsg: 'Uploading product image...',
		                    success: function(fp, o)
							{
		                        var el = Ext.fly('fi-form_large');
								el.update('<?=base_url()."files/"?>'+o.result.file);
								document.getElementById('x_sketch_large').value='<?="files/"?>'+o.result.file;
								document.getElementById('prevSketch_large').innerHTML='';
								if(!el.isVisible()){
									el.slideIn('t', {
										duration: .2,
										easing: 'easeIn',
										callback: function(){
											el.highlight();
										}
									});
								}else{
									el.highlight();
								}
		                    }
		                });
	                }
	            }
	        },{
	            text: 'Reset',
	            handler: function()
				{
	                fp.getForm().reset();
	            }
        	}]
		});
	}
	
	function productLineLoad(obj){
		var product_code = obj.value;
		var allData ='';
		if(product_code!=""){
			var row= getParent(obj,'TR');
			rowIndex = row.rowIndex-1;
			Ext.Ajax.request({
				url: BASEURL + 'index.php/products/getProductLine/',
				params : { 
					product_code: product_code,			
				},
				success: function ( result, request ) { 
					allData = result.responseText;
					if(allData!=""){
						var values = allData.split("|");
						
						if(values.length<11){
							for(i=values.length;i<11;i++) values[i]="";
						}
						document.getElementById('x_code_'+rowIndex).className = "inputUpdated";
						document.getElementById('x_code_'+rowIndex).value = values[0];
						document.getElementById('x_flute_'+rowIndex).className = "inputUpdated";
						document.getElementById('x_flute_'+rowIndex).value = values[1];
						document.getElementById('x_DF_'+rowIndex).className = "inputUpdated";
						document.getElementById('x_DF_'+rowIndex).value = values[2];
						document.getElementById('x_BM_'+rowIndex).className = "inputUpdated";
						document.getElementById('x_BM_'+rowIndex).value = values[3];
						document.getElementById('x_BL_'+rowIndex).className = "inputUpdated";
						document.getElementById('x_BL_'+rowIndex).value = values[4];
						document.getElementById('x_CM_'+rowIndex).className = "inputUpdated";
						document.getElementById('x_CM_'+rowIndex).value = values[5];
						document.getElementById('x_CL_'+rowIndex).className = "inputUpdated";
						document.getElementById('x_CL_'+rowIndex).value = values[6];
						document.getElementById('x_length_'+rowIndex).className = "inputUpdated";
						document.getElementById('x_length_'+rowIndex).value = values[7];
						document.getElementById('x_width_'+rowIndex).className = "inputUpdated";
						document.getElementById('x_width_'+rowIndex).value = values[8];
						document.getElementById('x_height_'+rowIndex).className = "inputUpdated";
						document.getElementById('x_height_'+rowIndex).value = values[9];
						document.getElementById('x_qty_set_'+rowIndex).className = "inputUpdated";
						document.getElementById('x_qty_set_'+rowIndex).value = values[10];
					}
					
				},
				failure: function ( result, request) { 
					Ext.MessageBox.alert('Failed', result.responseText); 
				} 
			});	
		}
	}
	
	function clearWindow()
	{
		document.getElementById('listdivcontainer').innerHTML="<p class='details-info'>"
				+"<?=$this->lang->line('msg_selectproducts')?></p>";
		document.getElementById('detailDivContainer').innerHTML = " <p class='details-info'>"
					+"<?=$this->lang->line('msg_selectproducts')?></p>";
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
							<li><span>Products</span></li>
							<li><a href='<?=base_url()."index.php/salesorder"?>'>Sales Order</a></li>
						</ul>
            		</td>
					<td align='center'>
						<input type='button' value="<?=$this->lang->line('add')?>" onclick="editProductDetail('add');"/>
						<input type='button' value="<?=$this->lang->line('edit')?>" onclick="editProductDetail('edit');"/>
						<input type='button' value="<?=$this->lang->line('archive')?>" onclick='deleteProduct()'/>
					</td>
                    <td align='right' width='280'>
                        <div id='searchform'>
                            <input id='searchtext' type="text" placeholder="<?=$this->lang->line('search_products')?>" value="" onkeyup="startSearch(event.which);"/>
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
					<tr onmouseover='ew_MouseOver(this);' onmouseout='ew_MouseOut(this);' class='ewTableRow' onclick='ew_Click(this);loadProducts("<?=$types[$i]?>");'>
						<td><?=$leftmenu[$i]?></td>
						<td align='right'> <span class='counter' id='counter_<?=$i?>'><?=$leftmenu_count[$i]?></span></td>
					</tr>
					<?php } ?>
					<tr class=''>
						<td></td><td align='right'></td>
					</tr>
					<!--<tr onmouseover='ew_MouseOver(this);' onmouseout='ew_MouseOut(this);' class='ewTableRow' onclick='ew_Click(this);'>
						<td><?=$this->lang->line('most_used_products')?></td>
						<td align='right'></td>
					</tr>
					<tr onmouseover='ew_MouseOver(this);' onmouseout='ew_MouseOut(this);' class='ewTableRow' onclick='ew_Click(this);'>
						<td><?=$this->lang->line('recently_used_products')?></td>
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
                            <?=$this->lang->line('msg_selectproducts')?>
                        </p>
                    </div>
                    </div>
				</td>
					<td valign='top' width='100%'>
						 <div id="flashMessage" style="display:none;"></div>
<!-- Page Detail -->
<div id='detailDivContainer'>
	  <div id="general" class="x-hide-display"></div>
	  <div id="sketchdiv" class="x-hide-display"></div>
	  <div id="salesHistory" class="x-hide-display"></div>
</div>
<!-- Page Detail End -->
					</td>
				</tr>
			</table>
		</td>
	</tr>
</table>