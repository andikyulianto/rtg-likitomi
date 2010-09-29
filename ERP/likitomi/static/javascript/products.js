/**
 * @author Sanjil Shrestha 
 */
function prd_selAddress(row){
	prd_ClearSelected();
	row.className='highlightAddress';
	document.getElementById('x_delivery').value =row.innerHTML;
}

function prd_ClearSelected() {
	var table = document.getElementById('tblDeliveryAddressDiv');
	for (var i = 1; i < table.rows.length; i++) {
		var thisrow = table.rows[i];
		thisrow.cells[0].className="tblProdViewWrap";
	}
}

function prd_AutoSelect() {
	var table = document.getElementById('tblDeliveryAddressDiv');
	var thisrow = table.rows[1];
	thisrow.cells[0].className='highlightAddress';
}

function previewCatalog(url){
	window.open(url,"Sales",'width=400,height=200');
}

//Product Function Used In Sales Order as well
	function startSearch(the_key) {	
		if (document.getElementById('searchtext').value.length <3) return;
	    if (!the_key )
	    {
	        if(window.event!==null) the_key = window.event.keyCode;
	    }
		if(( the_key > 64 && the_key < 91)||( the_key > 95 && the_key < 111)){
			searchProducts();
		}
		else if (the_key > 47 && the_key < 58) {
			searchProducts();
		}
		else if (the_key == 8) { //backspace
			searchProducts();
		}
		else if(the_key==13) {
			//document.getElementById('searchtext').value="";
			document.getElementById('searchtext').focus = false;
			var autoSelectId = autoLoadFirstData();
			if (autoSelectId != 0) {
				loadProductDetail(autoSelectId);
			}
		}	
	}
	
	function searchProducts(){
		var searchkeyword = document.getElementById('searchtext').value;
		Ext.Ajax.request({
			url: BASEURL + 'index.php/products/search/',
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
				loadAjax(LOADING_TEXT);
			},
		    'requestcomplete': function(){
				unloadAjax();
			}
		});
	}
	
	
	function ajax_pagination(dir,page,perpage,product_type){
		if(dir=="next") page = page + perpage;
		if(dir=="prev") page = page - perpage;
		Ext.Ajax.request({
			url: BASEURL + 'index.php/products/getNames/',
			params : { page : page, product_type:product_type},
			success: function ( result, request ) { 
				var el = Ext.get('ajaxpagination');
				el.update(result.responseText);
				if(dir=='next')el.slideIn('l', { duration: 0.2 });
				else el.slideIn('r', { duration: 0.2 });
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});
	}

	function ajax_pagination_search(dir,page,perpage,product_type){
		if(dir=="next") page = page + perpage;
		if(dir=="prev") page = page - perpage;
		var searchkeyword = document.getElementById('searchtext').value;
		Ext.Ajax.request({
			url: BASEURL + 'index.php/products/search/',
			params : { page : page, search : searchkeyword},
			success: function ( result, request ) { 
				var el = Ext.get('ajaxpagination');
				el.update(result.responseText);
				if(dir=='next')el.slideIn('l', { duration: 0.2 });
				else el.slideIn('r', { duration: 0.2 });
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});
	}
	
	function loadProductDetailFromRow(product_id,row){
		if(!row.selected)loadProductDetail(product_id);
	}
	
	function loadSalesOrder(page){
		var product_id=Ext.get('x_product_id').dom.value;
		Ext.Ajax.request({
			url: BASEURL + 'index.php/salesorder/loadSalesOrder/',
			params : { 
				product_id	:product_id,
				page		:page,
			},
			success: function ( result, request ) { 
				document.getElementById('salesOrderContainer').innerHTML = result.responseText;
				/*var el = Ext.get('salesOrderContainer');
				el.update(result.responseText);
				el.slideIn('l', { duration: 0.1});*/
				Ext.onReady(makeDateFields2);
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});		
	}
	
	function createSalesOrderPage()
	{
		var product_id=Ext.get('x_product_id').dom.value;
		Ext.Ajax.request({
			url: BASEURL + 'index.php/salesorder/createSalesOrderPage/',
			params : { 
				product_id	: product_id,
				action	: "view"
			},
			success: function ( result, request ) { 
				document.getElementById('salesOrderContainer').innerHTML = result.responseText;
				prd_AutoSelect();
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});
	}
	
	function addSalesOrder(){
		var validation = validateText(document.getElementById('x_amount_1'));
		if(!validation) return false;
		var product_id=Ext.get('x_product_id').dom.value;
		if(product_id>0){
			var loop = document.getElementById('cntProducts').value;
			var productCodes="";
			for(i=1;i<=loop;i++){
				productCodes += Ext.get('x_product_code_'+i).dom.value+"|"+Ext.get('x_amount_'+i).dom.value+"|";
			}
			Ext.Ajax.request({
				url: BASEURL + 'index.php/salesorder/addSalesOrder/',
				params : { 
					product_id	:product_id,
					productCodes:productCodes,
					delivery_at	:Ext.get('x_delivery').dom.value,
					purchase_order_no	:Ext.get('x_purchase_order').dom.value,
					remarks			:Ext.get('x_remarks').dom.value,
				},
				success: function ( result, request ) { 
					document.getElementById('salesOrderContainer').innerHTML = result.responseText;
					Ext.onReady(makeDateFields);
				},
				failure: function ( result, request) { 
					Ext.MessageBox.alert('Failed', result.responseText); 
				} 
			});	
		}
		else {
			Ext.MessageBox.alert('Failed', "Invalid Product ID"+product_id); 
		}
	}
	
	function editSalesOrder(sales_order_id){
		Ext.Ajax.request({
			url: BASEURL + 'index.php/salesorder/editSalesOrder/',
			params : { 
				sales_order_id	:sales_order_id,
				action			:"edit",
			},
			success: function ( result, request ) { 
				document.getElementById('salesOrderContainer').innerHTML = result.responseText;
				prd_AutoSelect();
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});	
	}
	
	function saveDelivery(rowtd)
	{
		var row= getParent(rowtd,'TR');
		Ext.Ajax.request({
			url: BASEURL + 'index.php/salesorder/saveDelivery/',
			params : { 
				product_id		:Ext.get('x_product_id').dom.value,
				product_code	:Ext.get('x_sel_product_code').dom.value,
				sales_order		:Ext.get('x_sales_order').dom.value,
				delivery_date	:Ext.get('x_delivery_date').dom.value,
				delivery_time	:Ext.get('x_delivery_time').dom.value,
				qty				:Ext.get('x_qty').dom.value,
			},
			success: function ( result, request ) { 
				var delivery_id = parseInt(result.responseText);
				var tbl = document.getElementById('tblDelivery');
				var lastRow = tbl.rows.length;
				var mydate = Ext.get('x_delivery_date').dom.value.split('-');
				var printdate = mydate[0] + '-' + mydate[1] + '-' + mydate[2];
				try {
				 	var row = tbl.insertRow(lastRow-1);
					cell	= row.insertCell(0);
					cell.className	= 'tblProdView';
					cell.innerHTML	= delivery_id+"<input type='hidden' id='x_delivery_id_"+row.rowIndex+"' value='"+delivery_id+"' />";
					cell 	= row.insertCell(1);
					cell.className	= 'tblProdView';
					cell.innerHTML	= Ext.get('x_sel_product_code').dom.value;
					cell 	= row.insertCell(2);
					cell.className	= 'tblProdView';
					cell.innerHTML 	= "<span onclick='inlinedit(this,3)'>"+printdate+"</span>";
					cell 	= row.insertCell(3);
					cell.className	= 'tblProdView';
					cell.innerHTML 	= "<span onclick='inlinedit(this,4)'>"+Ext.get('x_delivery_time').dom.value+"</span>";
					cell 	= row.insertCell(4);
					cell.className	= 'tblProdView';
					cell.innerHTML 	= "<span onclick='inlinedit(this,5)'>"+Ext.get('x_qty').dom.value+"</span>";
					cell 	= row.insertCell(5);
					cell.className	= 'tblProdView';
					cell.innerHTML 	= 'new';
					cell 	= row.insertCell(6);
					cell.className	= 'tblProdView';
					cell.innerHTML = 'Today';
					cell 	= row.insertCell(7);
					cell.className	= 'tblProdView';
					cell.innerHTML = "<img src='"+BASEURL+"static/images/extjs/delete.gif' />";
					cell.setAttribute('onclick','deleteDelivery(this,\''+Ext.get('x_qty').dom.value+'\');');
					
					//
					var row = tbl.insertRow(lastRow);
					row.setAttribute("class","dodd");
					cell	= row.insertCell(0);
					cell.setAttribute("colspan",'2');	
					cell	= row.insertCell(1);
					cell.setAttribute("colspan",'6');				
				} 
			    catch (ex) {}
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});	
	}
	
	function deleteDelivery(rowtd, value)
	{
		Ext.MessageBox.confirm('Confirm', 'Are you sure you want to delete?', 
			function(btn)
            {
                if (btn == 'yes') confirmdeleteDelivery(rowtd);
            }
		);
		document.getElementById('remaining_amt').value = parseInt(document.getElementById('remaining_amt').value) + parseInt(value);
	}
	
	function confirmdeleteDelivery(rowtd)
	{
		var row= getParent(rowtd,'TR');
		Ext.Ajax.request({
			url: BASEURL + 'index.php/salesorder/deleteDelivery/',
			params : { 
				product_id		:Ext.get('x_product_id').dom.value,
				delivery_id		:Ext.get('x_delivery_id_'+row.rowIndex).dom.value,
			},
			success: function ( result, request ) { 
				row.className = 'highlightDeletedDelivery';
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});	
		
	}
	
	function inlinedit(obj,id)
	{
		var ori_value = obj.innerHTML;
		var rowtd= getParent(obj,'TD');
		var row= getParent(rowtd,'TR');
		var rowIndex = row.rowIndex;
		rowtd.innerHTML  = "<input type='text' value='"+ori_value+"' size='10' id='x_row"+rowIndex+"' /> <br/>";
		rowtd.innerHTML += "<input type='button' value='Save'   onclick=\"saverow('"+ori_value+"',this,"+rowIndex+","+id+");\" />";
		rowtd.innerHTML += "<input type='button' value='Cancel' onclick=\"clearrow('"+ori_value+"',this,"+id+");\" />";
	}
	
	function clearrow(ori,obj,id)
	{
		var rowtd= getParent(obj,'TD');
		rowtd.innerHTML = "<span onclick='inlinedit(this,"+id+")'>"+ori+"</span>";
	}
	
	function saverow(ori,obj,rowIndex,id)
	{
		var rowtd		= getParent(obj,'TD');
		var newvalue	= document.getElementById('x_row'+rowIndex).value;
		var delivery_id	= Ext.get('x_delivery_id_'+rowIndex).dom.value;
		rowtd.innerHTML = "<span onclick='inlinedit(this,"+id+")'>"+newvalue+"</span>";
		
		if(newvalue==ori) {
			return false;
		}
		
		Ext.Ajax.request({
			url: BASEURL + 'index.php/salesorder/inlineedit/',
			params : { 
				delivery_id		:delivery_id,
				id				:id,
				original		:ori,
				newvalue		:newvalue,
			},
			success: function ( result, request ) { 
				var table = document.getElementById('tblDelivery');
				destrow = rowIndex+1;
				var newrow = table.rows[destrow];
				cell	= newrow.cells[1];
				cell.innerHTML = "<br/> * "+result.responseText+"<br/>"+cell.innerHTML;
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});	
	}
	
	function inlineEditSales(obj,id)
	{
		var ori_value = obj.innerHTML;
		var rowtd= getParent(obj,'TD');
		rowtd.innerHTML  = "<input type='text' value='"+ori_value+"' size='10' id='x_"+id+"' /> <br/>";
		rowtd.innerHTML += "<input type='button' value='Save'   onclick=\"saveInline('"+ori_value+"',this,'"+id+"');\" />";
		rowtd.innerHTML += "<input type='button' value='Cancel' onclick=\"clearInline('"+ori_value+"',this,'"+id+"');\" />";
	}
	
	function saveInline(ori,obj,id)
	{
		var rowtd		= getParent(obj,'TD');
		var newvalue	= document.getElementById('x_'+id).value;
		rowtd.innerHTML = "<span onclick='inlineEditSales(this,\""+id+"\")'>"+newvalue+"</span>";
		
		if(newvalue==ori) {
			return false;
		}
		Ext.Ajax.request({
			url: BASEURL + 'index.php/salesorder/inlineeditsales/',
			params : { 
				sales_order_id	: Ext.get('x_sales_order').dom.value,
				field			: id,
				newvalue		: newvalue,
			},
			success: function ( result, request ) { 
			
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});	
	}
	
	function clearInline(ori,obj,id)
	{
		var rowtd= getParent(obj,'TD');
		rowtd.innerHTML = "<span onclick='inlineEditSales(this,\""+id+"\")'>"+ori+"</span>";
	}
	
//Tooltips

function salesOrderTips(){
	new Ext.ToolTip({
		target: 'tip-choosedelivery',
		html: 'Click One of the Delivery Addresses',
		trackMouse:true
	});
	Ext.QuickTips.init();
}

	function sumAmount(obj){
		var remaining_amt = parseInt(document.getElementById('remaining_amt').value);
		var current = parseInt(document.getElementById('x_qty').value);
		
		if(current>remaining_amt)
		{
			alert ('Delivery ('+current+') is More than planned');
			return false;
		}
		else 
		{
			saveDelivery(obj);
			document.getElementById('remaining_amt').value= remaining_amt - current;
		}
		return true;
	}
