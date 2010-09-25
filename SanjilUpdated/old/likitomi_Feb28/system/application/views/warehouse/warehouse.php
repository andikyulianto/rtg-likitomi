<script type='text/javascript' >
/**
 * @author sanjilshrestha
 */
	var firstrowoffset 	= 0;
	var lastrowoffset 	= 0; 	
	var LOADING_TEXT	= "<?=$this->lang->line('ajax_loading_warehouse')?>";
	var combo_supplier	= null;
	var combo_paper		= null;
	
	window.onload = function() {
		document.getElementById('searchtext').value = '';
		searchWarehouse();
		activatePlaceholders();
		logoutTips();
		window.scrollTo(0,0);
	}
	
	function startSearch(the_key) {	
	    if (!the_key )
	    {
	        if(window.event!==null) the_key = window.event.keyCode;
	    }
		if(( the_key > 64 && the_key < 91)||( the_key > 95 && the_key < 111)){
			searchWarehouse();
		} 
		else if (the_key > 47 && the_key < 58) {
			searchWarehouse();
		} 
		else if(the_key==8){
			searchWarehouse();
		} 
		else if(the_key==13) {
			//document.getElementById('searchtext').value="";
			document.getElementById('searchtext').focus = false;
			var autoSelectId = autoLoadFirstData();
			if (autoSelectId != 0) {
				loadWarehouseDetail(autoSelectId);
			}
		}
	}
	
	function searchWarehouse(){
		var searchkeyword = document.getElementById('searchtext').value;
		Ext.Ajax.request({
			url: BASEURL + 'index.php/warehouse/search/',
			params : { search : searchkeyword},
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
				loadAjax(LOADING_TEXT);
			},
		    'requestcomplete': function(){
				unloadAjax();
			}
		});
	}
	
	function loadWarehouseDetailFromRow(invoice_no,row){
		if(!row.selected)loadWarehouseDetail(invoice_no);
	}
	
	function loadWarehouseDetail(invoice_no){
		document.getElementById('currentselection').value=invoice_no;
		Ext.Ajax.request({
			url: BASEURL + 'index.php/warehouse/getDetails/',
			params : { invoice_no : invoice_no, action : 'view'},
			success: function ( result, request ) { 
				document.getElementById('detailDivContainer').innerHTML = result.responseText;
				unloadAjax();
				window.scrollTo(110,0);
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});
		Ext.Ajax.on({
		    'beforerequest': function(){
				loadAjax(LOADING_TEXT);
			},
		    'requestcomplete': function(){
			}
		});
	}
	
	function editWarehouseDetail(action){
		if (document.getElementById('x_invoice_no') != null) 
			invoice_no = document.getElementById('x_invoice_no').value;
		else (document.getElementById('currentselection') != null) 
			invoice_no = document.getElementById('currentselection').value; 
		if ((invoice_no != 0)||(action =='add')) {
			Ext.Ajax.request({
				url: BASEURL + 'index.php/warehouse/getDetails/',
				params: {
					invoice_no: invoice_no,
					action: action
				},
				success: function(result, request){
					document.getElementById('detailDivContainer').innerHTML = result.responseText;
					Ext.onReady(fnSupplierSelect);
					makePaperCombo();
					window.scrollTo(110, 0);
				},
				failure: function(result, request){
					Ext.MessageBox.alert('Failed', result.responseText);
				}
			});
			Ext.Ajax.on({
				'beforerequest': function(){
					loadAjax(LOADING_TEXT);
				},
				'requestcomplete': function(){
					unloadAjax();
				}
			});
		}
		else {
			document.getElementById('detailDivContainer').innerHTML = " <p class='details-info'>"
					+"<?=$this->lang->line('msg_nothingtoedit')?></p>";
		}
	}
	
	function fnSupplierSelect(){
    	// simple array store
	    var store = new Ext.data.SimpleStore({
		    fields: ['supplier_id', 'supplier_name'],
		    data : [
	        <?=$thisClass->getSuppliers();?>
		]
		});
		combo_supplier = new Ext.form.ComboBox({
			store: store,
		    displayField:'supplier_name',
			valueField:'supplier_id',
		    typeAhead: true,
		    mode: 'local',
		    triggerAction: 'all',
		    emptyText:'Select a Supplier...',
		    selectOnFocus:true,
			applyTo:'x_supplier'
		});
	}
	
	function makePaperCombo()
	{
		var paperStore = new Ext.data.SimpleStore({
		    fields: ['paper_code'],
		    data : [
		         <?=$thisClass->getPapers();?>
			]
		});
		combo_paper = new Ext.form.ComboBox({
			store: paperStore,
	    	displayField:'paper_code',
		    typeAhead: true,
		    mode: 'local',
		    triggerAction: 'all',
		    emptyText:'Select a Paper...',
	    	selectOnFocus:true,
			applyTo:'x_paper_code'
		});
//		var paperCombo=Ext.select("input.combo_papers",true);
//		paperCombo.each(function(el){			
//			var combo  = new Ext.form.ComboBox({
//				store: paperStore,
//		    	displayField:'paper_code',
//			    typeAhead: true,
//			    mode: 'local',
//			    triggerAction: 'all',
//			    emptyText:'Select a Paper...',
//		    	selectOnFocus:true,
//			});
//			combo.applyToMarkup(el);
//		});
	}

	function saveData(action){
		var supplier_roll_id = new Array();
		var size 		= new Array();
		var unit 		= new Array();
		var remarks 	= new Array();
		var weight 		= new Array();
		var rfidtag 	= new Array();
		var invoice_no	= document.getElementById('x_invoice_no').value;
		if((combo_supplier.getValue()=="")){
			alert('Select Supplier');
			window.scrollTo(100,0);
			document.getElementById('x_supplier').focus();
			return false;
		};
		if((combo_paper.getValue()=="")){
			alert('Select Paper Code');
			window.scrollTo(100,0);
			document.getElementById('x_paper_code').focus();
			return false;
		};
		for(var i=1;i<=<?=$thisClass->getLimitInput();?>;i++){
			if ((document.getElementById('x_size_' + i).value != "")) {
				supplier_roll_id[i - 1] = document.getElementById('x_supplier_roll_id_' + i).value;
				size[i - 1] = document.getElementById('x_size_' + i).value;
				unit[i - 1] = document.getElementById('x_unit_' + i).value;
				weight[i - 1] = document.getElementById('x_initial_weight_' + i).value;
				remarks[i - 1] = document.getElementById('x_remarks_' + i).value;
				rfidtag[i - 1] = document.getElementById('x_rfid_roll_id_' + i).value;
			}		
		}
		var jsonArray = new Array(supplier_roll_id,size,unit,weight,remarks,rfidtag);
		var JSONText = JSON.stringify(jsonArray);
		
		Ext.Ajax.request({
			url: BASEURL + 'index.php/warehouse/savestockdata/',
			params : {
				action			: action,
				invoice_no 		: invoice_no,
				invoice_date	: document.getElementById('x_invoice_date').value,
				supplier_id		: combo_supplier.getValue(),
				paper_code 		: combo_paper.getValue(),
				stockjson		: JSONText,
			},
			success: function ( result, request ) {
				timeoutMessage(result.responseText);
				document.getElementById('searchtext').value = '';
				searchWarehouse();
				loadWarehouseDetail(invoice_no);
				unloadAjax();
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});
		Ext.Ajax.on({
		    'beforerequest': function(){
				loadAjax("<?=$this->lang->line('ajax_save_stock')?>");
			},
		});
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
            		<td width='300'>
	            		<ul class="primary-links">
            				<li><a href='<?=base_url()."index.php"?>'>Home</a></li>
							<li><span>Warehouse</span></li>
							<li><a href='<?=base_url()."index.php/stock"?>'>Paper Stock</a></li>
						</ul>
					</td>
					<td align='center'>
						<input type='button' value="<?=$this->lang->line('add')?>" onclick="editWarehouseDetail('add');"/>
						<input type='button' value="<?=$this->lang->line('edit')?>" onclick="editWarehouseDetail('edit');"/>
					</td>
                    <td align='right' width='280'>
                        <div id='searchform'>
                            <input id='searchtext' type="text" placeholder="<?=$this->lang->line('search_invoice')?>" value="" onkeyup="startSearch(event.which);"/>
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
		<td class='leftbar3'>
			<div id='container'>
				<div id='listdivcontainer'>
					<p class="details-info">
						<?=$this->lang->line('msg_searchinvoice')?>
					</p>
				</div>
			</div>
		</td>
		<td valign='top'>
			<div id="flashMessage" style="display:none;"></div>
			<div id='detailDivContainer'>
				<p class="details-info">
                    <?=$this->lang->line('msg_searchinvoice')?>
                </p>
			</div>
		</td>
	</tr>
</table>