<script type="text/javascript">
/**
 * @author sanjilshrestha
 */
	var EXTWIDTH 	= 1060;
	var EXTHEIGHT 	= 600;
	window.onload = function() {
		logoutTips();
		makeDateField();
		loadClampliftStatus();
	}
	
	function deletethisday(thisday)
	{
		var mask2 = new Ext.LoadMask(Ext.get('syncdatadiv'), { msg: "Loading..." });
		if(mask2!=null)mask2.show();
		Ext.Ajax.request({
			url: BASEURL + 'index.php/clampliftmanger/deletethisday/',
			params : { thisday : thisday},
			success: function ( result, request ) { 
				if(mask2!=null)mask2.hide();
				alert(result.responseText);
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});	
		loadClampliftData();
	}
	
	function syncplandata()
	{
		var mask2 = new Ext.LoadMask(Ext.get('syncdatadiv'), { msg: "Loading..." });
		if(mask2!=null)mask2.show();
		Ext.Ajax.request({
			url: BASEURL + 'index.php/clampliftmanger/syncdata/',
			params : { jsondata : document.getElementById('jsondata').innerHTML},
			success: function ( result, request ) { 
				if(mask2!=null)mask2.hide();
				alert(result.responseText);
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});
	}
	function makeDateField()
	{
		var el = Ext.get('clamplift_date');
		var df = new Ext.form.DateField({
			"format":'Y-m-d',
			"altFormats":'j|j/n|j/n/y|j/n/Y|j-M|j-M-y|j-M-Y',
		});
		df.applyToMarkup(el);
	}
	
	function loadClampliftData()
	{
		document.getElementById('statusDiv').className = "x-hide-display";
		document.getElementById('containerDiv').className = '';
		var plandate = document.getElementById('clamplift_date').value;
					
		store.removeAll();
		store.load({params : { 
				plandate:plandate }
		});
		Ext.getCmp('mainPanel'). setTitle("Table for "+plandate);
		document.getElementById('choosendate').value = document.getElementById('clamplift_date').value;
		window.scrollTo(0,0); 
	}
	
	function loadClampliftStatus()
	{
		document.getElementById('containerDiv').className = "x-hide-display";
		document.getElementById('statusDiv').className = '';
		var plandate = document.getElementById('clamplift_date').value;
		Ext.Ajax.request({
			url: BASEURL + 'index.php/clampliftmanger/getStatus/',
			params : { plandate : plandate},
			success: function ( result, request ) { 
				document.getElementById('statusDiv').innerHTML=result.responseText;
				
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});
	}
	var planRecord = Ext.data.Record.create([
		{ name: 'start_time'},
		{ name: 'stop_time'},
		{ name: 'product_code'},
		{ name: 'product_name'},
		{ name: 'partner_name'},
		{ name: 'sales_order'},
		{ name: 'autoid'},
		{ name: 'flute'},
		{ name: 'DF'},
		{ name: 'BL'},
		{ name: 'CL'},
		{ name: 'BM'},
		{ name: 'CM'},
		{ name: 'p_width_mm',type: "int"},
		{ name: 'p_width_inch',type: "int"},
		{ name: 'used_df',type: "int"},
		{ name: 'used_bl',type: "int"},
		{ name: 'used_cl',type: "int"},
		{ name: 'used_bm',type: "int"},
		{ name: 'used_cm',type: "int"},
		
		{ name: 'used_df_lkg',type: "int"},
		{ name: 'used_bl_lkg',type: "int"},
		{ name: 'used_cl_lkg',type: "int"},
		{ name: 'used_bm_lkg',type: "int"},
		{ name: 'used_cm_lkg',type: "int"},
		
		{ name: 'used_df_mkg',type: "int"},
		{ name: 'used_bl_mkg',type: "int"},
		{ name: 'used_cl_mkg',type: "int"},
		{ name: 'used_bm_mkg',type: "int"},
		{ name: 'used_cm_mkg',type: "int"},
		
		{ name: 't_length',type: "int"},
		{ name: 'case',type: "int"},
		{ name: 'cut',type: "int"},
	]);
	
	var store = new Ext.data.Store({
	    proxy: new Ext.data.HttpProxy({
	        url: BASEURL  + 'index.php/clampliftmanger/getclampliftreport/',
	    }),
    	reader: new Ext.data.JsonReader({
	        root: 'clamplift',
	    	fields : planRecord,
			totalProperty: 'count',
		})
	});
	
	var sm = new Ext.grid.CheckboxSelectionModel();
	var cm = new Ext.grid.ColumnModel([
	sm,
		{
			header: 'Start Time', 	
			dataIndex:'start_time',
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 60
		},
		{
			header: 'Start Time', 
			dataIndex:'stop_time',
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 60
		},
		{
			header: 'Code', 
			dataIndex:'product_code', 
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 60
		},
		{header: 'Product Name', 	dataIndex:'product_name', width: 150},
		{header: 'Partner Name', 	dataIndex:'partner_name', width: 150},
		{
			header: 'SO', 
			dataIndex:'sales_order',
			editor: new Ext.form.TextField({
				allowBlank: false
			}), 
			width: 40
		},
		{
			header: 'ORD.NO', 
			dataIndex:'autoid', 
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 50
		},
		{
			header: 'F', 
			dataIndex:'flute', 
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 30
		},
		{
			header: 'DF', 
			dataIndex:'DF', 
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 60
		},
		{
			header: 'BL', 
			dataIndex:'BL', 
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 60
		},
		{
			header: 'CL', 
			dataIndex:'CL', 
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 60
		},
		{
			header: 'BM',
			dataIndex:'BM',
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 60
		},
		{
			header: 'CM', 
			dataIndex:'CM', 
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 60
		},
		{
			header: 'P.W.(mm)', 
			dataIndex:'p_width_mm', 
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 60
		},
		{
			header: 'P.W.(inch)', 
			dataIndex:'p_width_inch', 
			width: 60
		},
		{
			header: 'DF', 
			dataIndex:'used_df', 
			width: 40
		},
		{
			header: 'BL', 
			dataIndex:'used_bl', 
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 40},
		{
			header: 'CL', 
			dataIndex:'used_cl', 
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 40
		},
		{
			header: 'BM', 
			dataIndex:'used_bm', 
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 40
		},
		{
			header: 'CM', 
			dataIndex:'used_cm', 
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 40
		},
		{
			header: 'DF', 
			dataIndex:'used_df_lkg', 
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 40
		},
		{
			header: 'BL', 
			dataIndex:'used_bl_lkg', 
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 40
		},
		{
			header: 'CL', 
			dataIndex:'used_cl_lkg', 
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 40
		},
		{
			header: 'BM', 
			dataIndex:'used_bm_lkg', 
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 40
		},
		{
			header: 'CM', 
			dataIndex:'used_cm_lkg', 
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 40
		},
		{
			header: 'DF', 
			dataIndex:'used_df_mkg', 
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 40
		},
		{
			header: 'BL', 
			dataIndex:'used_bl_mkg', 
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 40
		},
		{
			header: 'CL', 
			dataIndex:'used_cl_mkg', 
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 40
		},
		{
			header: 'BM', dataIndex:'used_bm_mkg', editor: new Ext.form.TextField({
				allowBlank: false
			}),width: 40
		},
		{
			header: 'CM', dataIndex:'used_cm_mkg', editor: new Ext.form.TextField({
				allowBlank: false
			}),width: 40
		},		
		{
			header: 'Length', 
			dataIndex:'t_length', 
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 60
		},
		{
			header: 'Case', 
			dataIndex:'case', 
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 50
		},
		{
			header: 'Cut', 
			dataIndex:'cut', 
			editor: new Ext.form.TextField({
				allowBlank: false
			}),
			width: 50
		},
		
	]);
	cm.defaultSortable = true;
	
	function clampliftGrid()
	{
		var grid = new Ext.grid.EditorGridPanel({
			id:'clampliftGrid',
			store: store,
			cm: cm,
			sm: sm,
			border:true,
			stripeRows: true,
			autoScroll: false,
			height:EXTHEIGHT-20,
			width: EXTWIDTH,
			frame:false,	
			loadMask: true,	
			clicksToEdit:1,
		});
		grid.render('clampliftdiv');
	}
	
	function mainFrame(){
		var mainPanel = new Ext.Panel({
		id: 'mainPanel',
		layout:'border',
		width:EXTWIDTH+2,
		height:EXTHEIGHT+33,
		title:'not saved',
		items:[{
			region:'center',
			layout:'fit',
			border:false,
			autoHeight:true,
			contentEl:'clampliftdiv',
			tbar: [
			{
				id: 'addrecord',
				text: 'Add New',
				iconCls: 'add-opt',
				handler: function(){
					var clampliftGrid = Ext.getCmp('clampliftGrid');
					var selm = clampliftGrid.getSelectionModel();
					var storetmp = clampliftGrid.getStore();
					
					var newRecord = new planRecord({
						start_time:'',	stop_time:'',	product_code: '',
						product_name: '(Auto Gen)',
						partner_name: '(Auto Gen)',
						sales_order: '',
						autoid:	'',	flute: '',	DF: '',
						BL: '',
						CL: '',
						BM: '',
						CM: '',
						p_width_mm: '',
						p_width_inch: '',
						used_df: '',
						used_bl: '',
						used_cl: '',
						used_bm: '',
						used_cm: '',
						
						used_df_lkg: '',
						used_bl_lkg: '',
						used_cl_lkg: '',
						used_bm_lkg: '',
						used_cm_lkg: '',
						
						used_df_mkg: '',
						used_bl_mkg: '',
						used_cl_mkg: '',
						used_bm_mkg: '',
						used_cm_mkg: '',
						
						t_length: '',
						case: '',
						cut: '',
						
						
					});
					//gridPlan.stopEditing();
					storetmp.add(newRecord);
					//gridPlan.startEditing(0, 0);
					
				}
			},{
				id: 'saverecord',
				text: 'Save',
				iconCls: 'save',
				handler: function(){
					//TODO
					var clampliftGrid = Ext.getCmp('clampliftGrid');
					var selm = clampliftGrid.getSelectionModel();
					var storetmp = clampliftGrid.getStore();
					
					jsonData = "[";
					 for(i=0;i<storetmp.getCount();i++) {
					 	record = storetmp.getAt(i);
						jsonData += Ext.util.JSON.encode(record.data) + ",";
					}
					jsonData = jsonData.substring(0,jsonData.length-1) + "]";
					//Ajax Load
					Ext.Ajax.request({
						url: BASEURL + 'index.php/clampliftmanger/saveclampliftjson/',
						params:{
							data:jsonData,
							choosendate:Ext.get('choosendate').dom.value,								
						},
						success: function ( result, request ) { 
							document.getElementById('flashMessage').style.visibility="visible";
							document.getElementById('flashMessage').style.display="block";
							var el = Ext.get('flashMessage');
							el.update(result.responseText);
							el.highlight("",{ duration: 6 });    
						    el.switchOff({
						        easing: 'easeIn',
						        duration: 0.3,
						        remove: false,
						        useDisplay: false
						    });
							document.getElementById('clamplift_date').value=Ext.get('choosendate').dom.value;
							loadClampliftStatus();
						},
						failure: function ( result, request) { 
							Ext.MessageBox.alert('Failed', result.responseText); 
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
			})
			,'->',
			{
				id:'clearResultSelected',
				text: 'Clear Selected',
				iconCls: 'remove',
				handler: function(){
					var clampliftGrid = Ext.getCmp('clampliftGrid');
					var selm = clampliftGrid.getSelectionModel();
					var storetmp = clampliftGrid.getStore();
					var records = selm.getSelections();
					for (i = 0; i < records.length; i++) {
						storetmp.remove(records[i]);
					}
				}
			},
			{
				id:'clearResult',
				text: 'Clear All',
				iconCls: 'cancel',
				handler: function(){
					var clampliftGrid = Ext.getCmp('clampliftGrid');
					var storetmp = clampliftGrid.getStore();
					storetmp.removeAll();
				}
			}
			],
		}]
		});mainPanel.render('maindiv');	
	}

Ext.onReady(mainFrame);
Ext.onReady(clampliftGrid);
</script>


<div id="topheader"></div>
<table class='tblcontainer' border='0' width='100%' height='100%' cellspacing="0" cellpadding="0">
	<tr>
    <td class='headertop'>
		<div id="headbar">
		    <table width="100%" border="0">
		    	<tbody><tr>
		        	<td>
			    		<ul class="primary-links">
			    				<li><a href='<?=base_url()."index.php"?>'>Home</a></li>
								<li><span> Clamplift Plan </span></li>
								<li><a href='<?=base_url()."index.php/reportplanning/"?>'> Report Planning </a></li>	
						</ul>
		        	</td>
		        	<td align='right'>
			            <table>
			                <tr>
			                    <td>
			                        <input type='text' id='clamplift_date' class="date-picker" value ="<?=date('Y-m-d')?>" size="9">
			                    </td>
			                    <td>
			                        <input type='button' value ="Load " onClick='loadClampliftData();'/>
									<input type='button' value ="Status " onClick='loadClampliftStatus();'/>
			                    </td>
			                </tr>
			            </table>
		        	</td>
		            <td width='40px'><a href='<?=base_url()."index.php/auth/logout"?>' id='tip-logout'>
							<img src='<?=base_url()."static/images/logout.png"?>' />
						</a></td>    
					</tr>
		        </tbody>
			</table>
		</div>
	</td>
	</tr>
	<tr>
		<td>
			<div id="flashMessage" style="display:none"> </div>
			<div id='containerDiv' class="x-hide-display"> 
				<div id='maindiv'> </div>
				<div id='clampliftdiv'> </div>
			</div>
			<div id='statusDiv' class="x-hide-display"></div>
		</td>
	</tr>
</table>
