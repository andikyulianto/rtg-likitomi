<script type="text/javascript">
/**
 * @author sanjilshrestha
 */
	var EXTWIDTH 	= 1030;
	var EXTHEIGHT 	= 600;
	var EXTGRID		= 344;
	var firstrowoffset = 0;
	var lastrowoffset = 0; 
	var alltables = new Array("tblDelDate","tblSalesOrder","tblLastModified","tblStatus");
	var filterbyarray = new Array("delivery_date","sales_order","modified_on","status"); //May not be needed 
	var cardsTotal = 2;
	var chkDuplicateArray = new Array('0');
	Ext.QuickTips.init();
	var loadMask = "";
	var sm = new Ext.grid.CheckboxSelectionModel();
	var cm = new Ext.grid.ColumnModel([
	sm,
		{header: 'ID', 	dataIndex:'delivery_id', width:10, hidden:false},
		{header: 'S.O',	dataIndex: 'sales_order', width:30},
		//{header: 'PO',	dataIndex: 'purchase_order_no',width:100},
		{header: 'P.Code',dataIndex: 'product_code',width:50},
		{header: 'P.Name',dataIndex: 'product_name',width:190},
		{header: 'Customer',dataIndex: 'partner_name',width:190},
		{
			header: 'P.W inch *',
			dataIndex: 'p_width_inch',
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			tooltip: 'Paper width in inch',
			width:50,
		},
		{
			header: 'Length *',
			dataIndex: 't_length',
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width:50,
		},
		{
			header: 'F *',
			dataIndex: 'flute',
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			tooltip: 'Flute type',
			width:20,
		},
	/*	{
			header: 'DF',
			dataIndex: 'DF',
			editor: new Ext.form.TextField({
				allowBlank: true
			}),
			tooltip: 'DF',
			width:50,
		},
		{
			header: 'BM',
			dataIndex: 'BM',
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			tooltip: 'BM',
			width:50,
		},
		{
			header: 'BL',
			dataIndex: 'BL',
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			tooltip: 'BL',
			width:50,
		},
		{
			header: 'CM',
			dataIndex: 'CM',
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			tooltip: 'CM',
			width:50,
		},
		{
			header: 'CL',
			dataIndex: 'CL',
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			tooltip: 'CL',
			width:50,
		},
		{
			header: 'Cut',
			dataIndex: 'cut',
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width:10,
		},*/
		{
			header: 'Amount CR',
			dataIndex: 'qty',
			editor: new Ext.form.TextField({
				allowBlank: true
			}),
			width:50,
		},
		{header: 'Delivery',dataIndex: 'delivery_date',renderer: Ext.util.Format.dateRenderer('d/m'),width:50,},
		{header: 'Status',dataIndex: 'status',width:40,},
		{
			header: 'Corr-Date',
			dataIndex: 'corrugator_date',
			renderer: Ext.util.Format.dateRenderer('Y-m-d'), 
			editor: new Ext.form.DateField({
                format: 'Y-m-d',
                
			}),
			tooltip: 'Corrugator Date',
			width:80,
		},
		{
			header: 'Corr-Time*',
			dataIndex: 'corrugator_time',
			//renderer: Ext.util.Format.dateRenderer('Y-m-d'), 
			editor: new Ext.form.TextField({
                //format: 'Y-m-d',
                
			}),
			tooltip: 'Corrugator Time',
			//renderer: Ext.util.Format.dateRenderer('H:i'),
			width:70,
		},
		{
			header: 'Conv-Date*',
			dataIndex: 'converter_date',
			renderer: Ext.util.Format.dateRenderer('Y-m-d'), 
			editor: new Ext.form.DateField({
                format: 'Y-m-d',
			}),
			tooltip: 'Corrugator Date',
			width:70,
		},
		{
			header: 'Conv-Time*',
			dataIndex: 'converter_time',
			editor:new Ext.form.TimeField({
                    increment:1,
                    allowBlank:false,
                    format:'H:i'
                }),
                renderer: Ext.util.Format.dateRenderer('H:i'),
			width:70,
		},
		{
			header: 'Pad-Date',
			dataIndex: 'padpartition_date',
			renderer: Ext.util.Format.dateRenderer('Y-m-d'), 
			editor: new Ext.form.DateField({
                format: 'Y-m-d',
                
			}),
			tooltip: 'Pad/Partition Date',
			width:70,
		},
		{
			header: 'Pad-Time*',
			dataIndex: 'padpartition_time',
			editor: new Ext.form.TimeField({
                format: 'H:i',
                increment: 1,
			}),
			tooltip: 'Pad/Partition Time',
			//renderer: Ext.util.Format.dateRenderer('H:i'),
			width:70,
		},
		{
			header: 'WH-Date',
			dataIndex: 'warehouse_date',
			renderer: Ext.util.Format.dateRenderer('Y-m-d'), 
			editor: new Ext.form.DateField({
                format: 'Y-m-d',
                
			}),
			tooltip: 'WH Date',
			width:70,
		},
		{
			header: 'WH-Time*',
			dataIndex: 'warehouse_time',
			editor: new Ext.form.TimeField({
                format: 'H:i',
                increment: 1,
			}),
			tooltip: 'WH Time',
			//renderer: Ext.util.Format.dateRenderer('H:i'),
			width:70,
		},
		{
			header: 'Sort*',
			dataIndex: 'sort',
			editor: new Ext.form.TextField({
                allowBlank: false
            }),
			width:70,
		},
		
	]);
	cm.defaultSortable = true;
	
	//For preview
	var smPreview = new Ext.grid.CheckboxSelectionModel();
	var cmPreview = new Ext.grid.ColumnModel([
	smPreview,
		{header: 'ID', 	dataIndex:'delivery_id', width:10, hidden:false},
		{header: 'S.O',	dataIndex: 'sales_order', width:30},
	//	{header: 'PO',	dataIndex: 'purchase_order_no',width:100},
		{header: 'P.Code',dataIndex: 'product_code',width:50},
		{header: 'P.Name',dataIndex: 'product_name',width:190, hidden:true},
		{header: 'Customer',dataIndex: 'partner_name',width:190, hidden:true},
		{
			header: 'P.W inch *',
			dataIndex: 'p_width_inch',
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			tooltip: 'Paper width in inch',
			width:50,
		},
		{
			header: 'Length *',
			dataIndex: 't_length',
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width:50,
		},
		{
			header: 'F *',
			dataIndex: 'flute',
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			tooltip: 'Flute type',
			width:20,
		},
	/*	{
			header: 'DF',
			dataIndex: 'DF',
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			tooltip: 'DF',
			width:50,
		},
		{
			header: 'BM',
			dataIndex: 'BM',
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			tooltip: 'BM',
			width:50,
		},
		{
			header: 'BL',
			dataIndex: 'BL',
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			tooltip: 'BL',
			width:50,
		},
		{
			header: 'CM',
			dataIndex: 'CM',
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			tooltip: 'CM',
			width:50,
		},
		{
			header: 'CL',
			dataIndex: 'CL',
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			tooltip: 'CL',
			width:50,
		},
		{
			header: 'Cut',
			dataIndex: 'cut',
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width:30,
		},*/
		{
			header: 'Amount CR',
			dataIndex: 'qty',
			editor: new Ext.form.TextField({
				allowBlank: true
			}),
			width:50,
		},
		{header: 'Delivery',dataIndex: 'delivery_date',renderer: Ext.util.Format.dateRenderer('d/m'),width:50,},
		{header: 'Status',dataIndex: 'status',width:40,},
		{
			header: 'Corr-Date',
			dataIndex: 'corrugator_date',
			renderer: Ext.util.Format.dateRenderer('Y-m-d'), 
			editor: new Ext.form.DateField({
                format: 'Y-m-d',
			}),
			tooltip: 'Corrugator Date',
			width:70,
		},
		{
			header: 'Corr-Time*',
			dataIndex: 'corrugator_time',
			editor: new Ext.form.TimeField({
                format: 'H:i',
                increment: 1,
			}),
			tooltip: 'Corrugator Time',
			//renderer: Ext.util.Format.dateRenderer('H:i'),
			width:70,
		},
		{
			header: 'Conv-Date*',
			dataIndex: 'converter_date',
			renderer: Ext.util.Format.dateRenderer('Y-m-d'), 
			editor: new Ext.form.DateField({
                format: 'Y-m-d',
			}),
			tooltip: 'Corrugator Date',
			width:70,
		},
		{
			header: 'Conv-Time*',
			dataIndex: 'converter_time',
			editor: new Ext.form.TimeField({
                format:'H:i',
                increment: 1,
            }),
			//renderer: Ext.util.Format.dateRenderer('H:i'),
			width:70,
		},

		{
			header: 'Pad-Date',
			dataIndex: 'padpartition_date',
			renderer: Ext.util.Format.dateRenderer('Y-m-d'), 
			editor: new Ext.form.DateField({
                format: 'Y-m-d',
                
			}),
			tooltip: 'Pad/Partition Date',
			width:70,
		},
		{
			header: 'Pad-Time*',
			dataIndex: 'padpartition_time',
			editor: new Ext.form.TimeField({
                format: 'H:i',
                increment: 1,
			}),
			tooltip: 'Pad/Partition Time',
			//renderer: Ext.util.Format.dateRenderer('H:i'),
			width:80,
		},
		{
			header: 'WH-Date',
			dataIndex: 'warehouse_date',
			renderer: Ext.util.Format.dateRenderer('Y-m-d'), 
			editor: new Ext.form.DateField({
                format: 'Y-m-d',
                
			}),
			tooltip: 'WH Date',
			width:80,
		},
		{
			header: 'WH-Time*',
			dataIndex: 'warehouse_time',
			editor: new Ext.form.TimeField({
                format: 'H:i',
                increment: 1,
			}),
			tooltip: 'WH Time',
			//renderer: Ext.util.Format.dateRenderer('H:i'),
			width:80,
		},
		{
			header: 'Sort*',
			dataIndex: 'sort',
			editor: new Ext.form.TextField({
                allowBlank: false
            }),
			width:80,
		},
		
	]);
	cmPreview.defaultSortable = true;
	
	var loadHandler = function(button, event) {
		var store = Ext.getCmp('gridPlan').getStore();
		store.removeAll();
		store.load({
			params:{choosendate:Ext.getCmp('choosendate').value}
		});
    };

	window.onload = loadHandler;
	
	var planRecord = Ext.data.Record.create([
		{ name: 'delivery_id',type: "int"},
		{ name: 'sales_order',type: "int"},
		{ name: 'purchase_order_no'},
		{ name: 'product_code'},
		{ name: 'product_name'},
		{ name: 'partner_name'},
		{ name: 'p_width_inch',type: "int"},
		{ name: 't_length',type: "int"},
		{ name: 'flute'},
		{ name: 'DF'},
		{ name: 'BM'},
		{ name: 'BL'},
		{ name: 'CM'},
		{ name: 'CL'},
		{ name: 'cut',type: "int"},
		{ name: 'delivery_date',type: 'date', dateFormat: 'Y-m-d'},
		{ name: 'qty',type: "int"},
		{ name: 'modified_on'},
		{ name: 'status'},
		{ name: 'corrugator_date',	type: 'date', dateFormat: 'Y-m-d'},
		{ name: 'corrugator_time',	type: 'date', dateFormat: 'H:i'},
		{ name: 'converter_date',	type: 'date', dateFormat: 'Y-m-d'},
		{ name: 'converter_time', 	type: 'date', dateFormat: 'H:i'},
		{ name: 'padpartition_date',	type: 'date', dateFormat: 'Y-m-d'},
		{ name: 'padpartition_time',	type: 'date', dateFormat: 'H:i'},
		{ name: 'warehouse_date',	type: 'date', dateFormat: 'Y-m-d'},
		{ name: 'warehouse_time', 	type: 'date',dateFormat: 'H:i' },
		//{ name: 'next_process'),
		{ name: 'sort' },
	]);
	var resultStore = new Ext.data.Store({
	    proxy: new Ext.data.HttpProxy({
	        url: BASEURL + 'index.php/planning/filter/',
	    }),
    	reader: new Ext.data.JsonReader({
	        root: 'delivery',
	    	fields : planRecord,
			totalProperty: 'count',
		})
	});
	resultStore.on({
	    'load':{
	        fn: function(store, records, options){
				var selm = Ext.getCmp('resultGrid').getSelectionModel();
				for (i = 0; i < records.length; i++) {
					deliveryid  =  records[i].get('delivery_id');
					if(checkDuplicate(deliveryid))
					{
						selm.selectRow(i,true); // checked status is here!
//						selm.on("beforerowselect", function(){ // added by Patipol
////							alert(selm.getSelections());
//						});
					}
				}
				
				var el = Ext.get('counter_search');
				el.update(resultStore.getCount());
				el.highlight();
				if(loadMask!=null)loadMask.hide();
	        }
		},
	});
	
	var planStore = new Ext.data.Store({
	    proxy: new Ext.data.HttpProxy({
	        url: BASEURL + 'index.php/planning/loadplanbydate/',
			method: 'POST',
	    }),
    	reader: new Ext.data.JsonReader({
	        root: 'planned',
	    	fields : planRecord,
			totalProperty: 'count',
		})
	});
	planStore.on({
		'load':{
			fn: function(store, records, options){
				document.getElementById('counter_plan').innerHTML = store.getCount();
				var cnt=1;
				for(i=0;i<store.getCount();i++) {
					chkDuplicateArray[cnt++] = store.getAt(i).get('delivery_id');
				}
	        }
		},
	});
	
	function sel_SetColor(row) 
	{
		row.className = (row.selected)?"selectedRow":"";
	}
	
	function sel_Click(row) 
	{
        var table = getParent(row, 'TABLE');        
        if (!document.getElementById('chkmultiplecol').checked) {
            clearTableAllExcept(table.id);
        }
        if (!document.getElementById('chkmultiplerow').checked) {
            clearTable(table.id);
        }
		row.selected = !row.selected;
		sel_SetColor(row);
		postTable(table.id);
	}
	
	function clearTable(tblName)
	{
		var table = document.getElementById(tblName);
		for (var i = 0; i < table.rows.length; i++) 
		{
			var thisrow = table.rows[i];
			if (thisrow.selected) 
			{
				thisrow.selected = false;
				sel_SetColor(thisrow);
			}
		}
	}
	
	function clearTableAllExcept(tblName)
	{
		for (i=0;i<alltables.length;i++)
		{ 
            if (tblName != alltables[i]) {
				clearTable(alltables[i]);
            }
		}
	}
	
	function postTable(tblName){
		//alert(inspect(Ext.get('searchContainerDiv')));
		//alert(Ext.get('searchContainerDiv'));
		loadMask = new Ext.LoadMask(Ext.get('searchContainerDiv'), { msg: "Loading..." });
		if(loadMask!=null)loadMask.show();
		var delivery_date_all = "";
		var sales_order_all = "";
		var lastmodified_all = "";
		var status_all = "";
		
		var table = document.getElementById(alltables[0]);
		for (var i = 0; i < table.rows.length; i++) 
		{
			var thisrow = table.rows[i];
			if (thisrow.selected) {
				delivery_date_all += thisrow.cells[0].innerHTML + "|";
			}	
		}
		var table = document.getElementById(alltables[1]);
		for (var i = 0; i < table.rows.length; i++) 
		{
			var thisrow = table.rows[i];
			if (thisrow.selected) {
				sales_order_all += thisrow.cells[0].innerHTML + "|";
			}	
		}
		var table = document.getElementById(alltables[2]);
		for (var i = 0; i < table.rows.length; i++) 
		{
			var thisrow = table.rows[i];
			if (thisrow.selected) {
				lastmodified_all += thisrow.cells[0].innerHTML + "|";
			}	
		}
		var table = document.getElementById(alltables[3]);
		for (var i = 0; i < table.rows.length; i++) 
		{
			var thisrow = table.rows[i];
			if (thisrow.selected) {
				status_all += thisrow.cells[0].innerHTML + "|";
			}	
		}
		
		resultStore.load({
			params : { 
				delivery_date_all 	: delivery_date_all,
				sales_order_all		: sales_order_all,
				lastmodified_all 	: lastmodified_all,
				status_all 			: status_all
			}
		});
		
	}
	
	function checkDuplicate(deliveryid)
	{
		//alert(deliveryid);
		var cnt = chkDuplicateArray.length;
		for(var i=0;i<chkDuplicateArray.length;i++)
		{
			if (deliveryid == chkDuplicateArray[i]) return true;
		}
		return false;
	}
	
	function updateCounterStep2()
	{
		var gridPlan = Ext.getCmp('gridPlan');
		var store = gridPlan.getStore();
		var totaladded =store.getCount();
		var el = Ext.get('counter_plan');
		el.update(totaladded);
		el.highlight();
	}
	
	function clearDuplicateArray()
	{
		for(var i=0;i<chkDuplicateArray.length;i++)
		{
			chkDuplicateArray[i]=0;
		}
	}
	
	//EXT
	var searchPanel = new Ext.Panel({
		id: 'card-0',
		layout:'border',
		width:EXTWIDTH,
		height:EXTHEIGHT,
		contentEl:'planningDivContainer',
		items:[{
			region:'north',
			title:"Search Criteria",
			layout:'fit',
			border:false,
			height:193,
			split:true,
			collapsible:true,
			flotable: true,
			contentEl:'searchContainerDiv'
		},{
			region:'center',
			layout:'fit',
			border:false,
			autoHeight:true,
			contentEl:'searchResultDiv',
			tbar: [
			{
				id: 'addplanning',
				text: 'Add To Planning',
				iconCls: 'add-opt',
				handler: function(){
					//Add To Planing
					var selm = Ext.getCmp('resultGrid').getSelectionModel();
					var gridPlan = Ext.getCmp('gridPlan');
					var store = gridPlan.getStore();
					var records = selm.getSelections(); 
					
					for(i=0;i<records.length;i++)
					{
						deliveryid  =  records[i].get('delivery_id');
						
						if(!checkDuplicate(deliveryid))
						{
							// add here
							var newPlan = new planRecord({
								delivery_id			: deliveryid,
								sales_order			: records[i].get('sales_order'),
								purchase_order_no	: records[i].get('purchase_order_no'),
								product_code		: records[i].get('product_code'),
								product_name		: records[i].get('product_name'),
								partner_name		: records[i].get('partner_name'),
								p_width_inch		: records[i].get('p_width_inch'),
								t_length			: records[i].get('t_length'),
								flute				: records[i].get('flute'),
								DF					: records[i].get('DF'),
								BM					: records[i].get('BM'),
								BL					: records[i].get('BL'),
								CM					: records[i].get('CM'),
								CL					: records[i].get('CL'),
								cut					: records[i].get('cut'),
								delivery_date		: records[i].get('delivery_date'),
								qty					: records[i].get('qty'),
								modified_on			: records[i].get('modified_on'),
								status				: records[i].get('status'),
								corrugator_date		: records[i].get('corrugator_date'),
								corrugator_time		: records[i].get('corrugator_time'),
								converter_date		: records[i].get('converter_date'),
								converter_time		: records[i].get('converter_time'),
								padpartition_date		: records[i].get('padpartition_date'),
								padpartition_time		: records[i].get('padpartition_time'),
								warehouse_date		: records[i].get('warehouse_date'),
								warehouse_time		: records[i].get('warehouse_time'),
								next_process		: records[i].get('next_process'),
								sort				: i,
							});
							//gridPlan.stopEditing();
							store.add(newPlan);
							//gridPlan.startEditing(0, 0);
							chkDuplicateArray[store.getCount()]= deliveryid;
						}
					}
					updateCounterStep2();
					showStep(1);
					
				},
				disabled: false
			},
			'->',
			{
				id:'clearResultSelected',
				text: 'Clear Selected',
				iconCls: 'remove',
				handler: function(){
					var resultGrid = Ext.getCmp('resultGrid');
					var selm = resultGrid.getSelectionModel();
					var store = resultGrid.getStore();
					var records = selm.getSelections();
					for (i = 0; i < records.length; i++) {
						store.remove(records[i]);
					}
				}
			},
			{
				id:'clearResult',
				text: 'Clear All',
				iconCls: 'cancel',
				handler: function(){
					var resultGrid = Ext.getCmp('resultGrid');
					var store = resultGrid.getStore();
					store.removeAll();
					clearTableAllExcept('');
				}
			}
			],
		}]
	});
	
	function showStep(cardnum){
		var cardMain = Ext.getCmp('mainCardContainer');
		var lay = cardMain.getLayout();
		lay.setActiveItem(cardnum);
		Ext.getCmp('move-prev').setDisabled(cardnum==0);
		Ext.getCmp('move-next').setDisabled(cardnum==cardsTotal);
		ew_AutoSelectById(cardnum);
	}
	
	function loadSearchPage() {
		
		var navHandler = function( direction ) {
			var lay = cardMain.getLayout();
			var i = lay.activeItem.id.split('card-')[1];
			var next = parseInt(i) + direction;
			showStep(next);
		};

		var cardMain = new Ext.Panel({
			id:'mainCardContainer',
			layout:'card',
			width:EXTWIDTH,
			height:EXTHEIGHT,
			activeItem: 0, 
			defaults: {
				border:false
			},
			tbar: [
		        {
		            id: 'move-prev',
		            text: 'Back',
		            handler: navHandler.createDelegate(this, [-1]),
		            disabled: true
		        },
		        '->', // greedy spacer so that the buttons are aligned to each side
		        {
		            id: 'move-next',
		            text: 'Next',
		            handler: navHandler.createDelegate(this, [1])
		        }
		    ],

	    	items: [searchPanel,{
		        id: 'card-1',
				title:"Added Plans",
				layout:'fit',
				border:false,
				contentEl:'previewDiv',
				tbar: [
					{
						id: 'addplanning',
						text: 'Save',
						iconCls: 'save',
						handler: function(){
							//TODO
							var store = Ext.getCmp('gridPlan').getStore();
							 jsonData = "[";
							 for(i=0;i<store.getCount();i++) {
							 	record = store.getAt(i);
								jsonData += Ext.util.JSON.encode(record.data) + ",";
							}
							jsonData = jsonData.substring(0,jsonData.length-1) + "]";
							//Ajax Load
							Ext.Ajax.request({
								url: BASEURL + 'index.php/planning/savetotalplanjson/',
								params:{
									data:jsonData,
									choosendate:Ext.get('choosendate').dom.value,								
								},
								success: function ( result, request ) { 
									document.getElementById('planning_msg').style.visibility="visible";
									document.getElementById('planning_msg').style.display="block";
									var el = Ext.get('planning_msg');
									el.update(result.responseText);
									el.slideIn('r', { duration: 0.2 });	
									el.highlight();
									showStep(2);
								},
								failure: function ( result, request) { 
									Ext.MessageBox.show({
										title: 'Failed',
										msg: result.responseText,
										width: 400
									}); 
								} 
							});	
						}
					},  
					{xtype: 'tbspacer'}, {xtype: 'tbspacer'},
					'Choose Date: ', ' ',
					new Ext.form.DateField({
						id		: 'choosendate',
						name	: 'choosendate',
						format	: 'Y-m-d',
						width	: 90,
						value	: '<?=date("Y-m-d")?>',
						allowBlank: false
					}),
					{
						id: 'loadplanning',
						text: 'Load',
						iconCls: 'load',
						handler: loadHandler,
					},
					'->',
					{
						id:'clearResultSelected',
						text: 'Clear Selected',
						iconCls: 'remove',
						handler: function(){
							var gridPlan = Ext.getCmp('gridPlan');
							var selm = gridPlan.getSelectionModel();
							var store = gridPlan.getStore();
							var records = selm.getSelections();
							for (i = 0; i < records.length; i++) {
								store.remove(records[i]);
							}
						}
					},
					{
						id:'clearPlan',
						text: 'Clear All',
						iconCls: 'cancel',
						handler: function(){
							var gridPlan = Ext.getCmp('gridPlan');
							var store = gridPlan.getStore();
							store.removeAll();
							updateCounterStep2();
							clearDuplicateArray();
						}
					}						
				]
		    },{
		        id: 'card-2',
		        contentEl:'genReportDiv',
		    }]
		});		
		cardMain.render('mainDivContainer');	 
	}
	
	function resultGrid()
	{
		var grid = new Ext.grid.EditorGridPanel({
			disableSelection: true, // added by Patipol
			id:'resultGrid',
			store: resultStore,
			cm:cm,
			sm: sm,
			border:false,
			stripeRows: true,
			autoScroll: true,
			height: EXTGRID,
			frame:false,	
			loadMask: true,	
			clicksToEdit:1,
			ddGroup: 'mygridDD1',
            enableDragDrop: true, // enable drag and drop of grid rows
            viewConfig: {
                emptyText: 'No pages found',
                forceFit: true
            },
            listeners: {
                "render": {
                    scope: this,
                    fn: function(grid){
                    
                        // Enable sorting Rows via Drag & Drop
                        // this drop target listens for a row drop
                        //  and handles rearranging the rows
                        
                        var ddrow = new Ext.dd.DropTarget(grid.container, {
                            ddGroup: 'mygridDD1',
                            copy: false,
                            notifyDrop: function(dd, e, data){
                            
                                var ds = grid.store;
                                
                                // NOTE:
                                // you may need to make an ajax call here
                                // to send the new order
                                // and then reload the store
                                
                                
                                // alternatively, you can handle the changes
                                // in the order of the row as demonstrated below
                                
                                // ***************************************
                                
                                var sm = grid.getSelectionModel();
                                var rows = sm.getSelections();
                                if (dd.getDragData(e)) {
                                    var cindex = dd.getDragData(e).rowIndex;
                                    if (typeof(cindex) != "undefined") {
                                        for (i = 0; i < rows.length; i++) {
                                            ds.remove(ds.getById(rows[i].id));
                                        }
                                        ds.insert(cindex, data.selections);
                                        //sm.clearSelections();
                                    }
                                }
                                
                                // ************************************
                            }
                        })
                        
                        // load the grid store
                        //  after the grid has been rendered
                        planStore.load();
                    }
                }
            }
        });
		grid.render('searchResultDiv');
	}
	
    
    ///Preview Pages
    function loadPreviewPage(){
        var gridPlan = new Ext.grid.EditorGridPanel({
            id: 'gridPlan',
            store: planStore,
            cm: cmPreview,
            sm: smPreview,
            border: false,
            stripeRows: true,
            autoScroll: true,
            height: EXTHEIGHT - 80,
            frame: false,
            loadMask: true,
            clicksToEdit: 1,
            ddGroup: 'mygridDD',
            enableDragDrop: true, // enable drag and drop of grid rows
            viewConfig: {
                emptyText: 'No pages found',
                forceFit: true
            },
            listeners: {
                "render": {
                    scope: this,
                    fn: function(grid){
                    
                        // Enable sorting Rows via Drag & Drop
                        // this drop target listens for a row drop
                        //  and handles rearranging the rows
                        
                        var ddrow = new Ext.dd.DropTarget(grid.container, {
                            ddGroup: 'mygridDD',
                            copy: false,
                            notifyDrop: function(dd, e, data){
                            
                                var ds = grid.store;
                                
                                // NOTE:
                                // you may need to make an ajax call here
                                // to send the new order
                                // and then reload the store
                                
                                
                                // alternatively, you can handle the changes
                                // in the order of the row as demonstrated below
                                
                                // ***************************************
                                
                                var sm = grid.getSelectionModel();
                                var rows = sm.getSelections();
                                if (dd.getDragData(e)) {
                                    var cindex = dd.getDragData(e).rowIndex;
                                    if (typeof(cindex) != "undefined") {
                                        for (i = 0; i < rows.length; i++) {
                                            ds.remove(ds.getById(rows[i].id));
                                        }
                                        ds.insert(cindex, data.selections);
                                        sm.clearSelections();
                                    }
                                }
                                
                                // ************************************
                            }
                        })
                        
                        // load the grid store
                        //  after the grid has been rendered
                        planStore.load();
                    }
                }
            }
        });
        gridPlan.render('previewDiv');
    }
Ext.onReady(loadSearchPage);
Ext.onReady(resultGrid);

Ext.onReady(loadPreviewPage);


</script>
<div id="topheader"></div>
<div id="first-background"></div>


<table class='tblcontainer' border='0' width='100%' height='100%' cellspacing="0" cellpadding="0">
	<tr>
    <td colspan=2 class='headertop'>
        <div id='headbar'>
            <table border=0 width=100% >
            	<tr>
            		<td width='320'>
            			<ul class="primary-links">
            				<li><a href='<?=base_url()."index.php"?>'>Home</a></li>
							<li><span>Planning</span></li>
							<li><a href='<?=base_url()."index.php/products"?>'>Products</a></li>
							<li><a href='<?=base_url()."index.php/salesorder"?>'>Sales Order</a></li>
						</ul>
            		</td>
					<td width='40px' align='right'><a href='<?=base_url()."index.php/auth/logout"?>' >
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
					<tr onmouseover='ew_MouseOver(this);' onmouseout='ew_MouseOut(this);' class='ewTableRow' onclick='ew_Click(this);showStep(0);'>
						<td>1. Search and Add</td>
						<td align='right'> <span class='counter' id='counter_search'>0</span></td>
					</tr>
				
					<tr onmouseover='ew_MouseOver(this);' onmouseout='ew_MouseOut(this);' class='ewTableRow' onclick='ew_Click(this);showStep(1);'>
						<td>2. Save/Load Plans </td>
						<td align='right'> <span class='counter' id='counter_plan'>0</span></td>
					</tr>
					<tr onmouseover='ew_MouseOver(this);' onmouseout='ew_MouseOut(this);' class='ewTableRow' onclick='ew_Click(this);showStep(2);'>
						<td>3. Generate Reports</td>
						<td align='right'> </td>
					</tr>
				</table></div></div>
		</td>
		<td valign='top'>
			<table border='0'>
				<tr>
					<td valign='top'><div width='100%' id='planning_msg' class='info_message'></div>
						<div id='mainDivContainer'></div>
<div id='planningDivContainer'></div>
<!--Search Container-->
<div id='searchContainerDiv' class='x-hide-display'>
<table width='100%'>
	<tr><td><center>
		<div id='headerPlanningSearch'> 		
		<table width='100%'>
			<tr>
				<td>
					<table>
						<tr>
							<td></td><td align='center'><span class='spantitle'>Delivery Date</span></td>
							<td></td><td align='center'><span class='spantitle'>Sales Order</span></td>
							<td></td><td align='center'><span class='spantitle'>Modified Date</span></td>
							<td></td><td align='center'><span class='spantitle'>Status</span></td>
						</tr>
						<tr>
							<td class='tblBlank'></td>
							<td>
								<div id='divcheckbox'>						
									<?=tableTemplate("tblDelDate",$delDateArray);?>
								</div>
							</td>
							<td class='tblBlank'></td>
							<td>
								<div id='divcheckbox'>					
									<?=tableTemplate("tblSalesOrder",$salesOrderArray);?>
								</div>
							</td>
							<td class='tblBlank'></td>
							<td>
								<div id='divcheckbox'>					
									<?=tableTemplate("tblLastModified",$lastmodified);?>
								</div>
							</td>
							<td class='tblBlank'></td>
							<td>
								<div id='divcheckbox'>					
									<?=tableTemplate("tblStatus",$status);?>
								</div>
							</td>
							<td class='tblBlank'></td>
						</tr>
					</table>
				</td>	
				<td align='right' style='border-left:1px solid #A0A0A0;'>
					<table>
					<tr>
						<td align='center'><span class='spantitle'>Config</span></td><td></td>
					</tr>
					<tr>
						<td><div id='divcheckbox'>
								<table class='tblcheckbox'>
									<tr><td><input type='checkbox' id='chkmultiplerow' checked/>Multiple Rows</td></tr>
									<tr><td><input type='checkbox' id='chkmultiplecol' checked/>Multiple Columns</td></tr>
								</table>
							</div>
						</td>
						<td class='tblBlank'></td>
					</tr>
					</table>

				</td>
			</tr>
		</table>
	</div></center>
	</td>
	</tr>
</table>

</div>
<!--End Search Container-->
<!--Search Result -->
<div id='searchResultDiv' class='x-hide-display'></div>
<!-- End Search Result -->

<!--Preview Page -->
<div id='previewDiv' class='x-hide-display'></div>
<!--End Preview Page-->
<div id='genReportDiv' class='x-hide-display'>
	Reports are Available at 
	<a href='<?=base_url()."index.php/reportplanning/"?>'> REPORTS</a>
</div>
					</td>
				</tr>
			</table>
		</td>
	</tr>
</table>





<?php
function tableTemplate($tblName, $arrayName)
{
	$printdiff = false;
	if(($tblName=='tblDelDate')||($tblName=='tblLastModified')) {
		$printdiff=true;
	}
	
	$output  = "";
	$output .= "<table id='".$tblName."' class='tblCheckBox' width='100%'>";
	foreach($arrayName as $key=>$value)
	{
		$diffvalue="<td></td>";
		if($printdiff)
		{	$day = get_time_difference(date('Y-m-d'),$value);
			$diffvalue= "<td>".$day."</td>";
		}
		$output .= "<tr onclick='sel_Click(this);' ><td>".$value."</td>".$diffvalue."</tr>";
	}
	$output .= "</table>";
	return $output;	
}

function get_time_difference($start,$end)
{
	$uts['start']      =    strtotime( $start );
    $uts['end']        =    strtotime( $end );
    if( $uts['start']!==-1 && $uts['end']!==-1 )
    {
        if( $uts['end'] >= $uts['start'] )
        {
            $diff    =    $uts['end'] - $uts['start'];
            if( $days=intval((floor($diff/86400))) )
                $diff = $diff % 86400;
            $diff    =    intval( $diff );            
            return "+".$days."d";
        }
        else
        {
            $diff    =  $uts['start'] - $uts['end'];
            if( $days=intval((floor($diff/86400))) )
                $diff = $diff % 86400;
            $diff    =    intval( $diff );            
            return "-".$days."d";
        }
    }
    else
    {
        //trigger_error( "Invalid date/time data detected", E_USER_WARNING );
    }
    return( false );
}
?>
<script>
	ew_AutoSelectById(0);
</script>
