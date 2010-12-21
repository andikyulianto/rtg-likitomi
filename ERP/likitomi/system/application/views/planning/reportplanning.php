<style type="text/css" media="print">
	@page 		{ size: landscape; 	}
	@page :left {
		margin-left: 0cm;
		margin-right:0cm;
	}
	@page:right {
		margin-left: 0cm;
		margin-right:0cm;
	}
</style>
<script type="text/javascript">		

	
	function makeDateField()
	{
		var el = Ext.get('planning_date');
		var df = new Ext.form.DateField({
			"format":'Y-m-d',
			"altFormats":'j|j/n|j/n/y|j/n/Y|j-M|j-M-y|j-M-Y',
			listeners: {
				change: function(o,newVal, oldVal)
				{
					currentSelection = getSelected();
					if(currentSelection!="")
						loadPlanReport(currentSelection);
				},
			}
		});
		df.applyToMarkup(el);
	}
	
	function printPlanning()
	{
		var a = window. open('','','scrollbars=yes,width=800,height=600');
		a.document.open("text/html");
		a.document.write('<html><head><link rel="stylesheet" href="<?=base_url()?>static/css/salesreport.css" /></head><body style="background-image:none;background-color:#FFFFFF;">');
		document.getElementById("wrapper").className="movetotop";
		a.document.write(document.getElementById('wrapper').innerHTML);
		a.document.write('</body></html>');
		a.document.close();
		a.print();
		
		document.getElementById("wrapper").className="movedown";
	}
	
	function clearAllSelected()
	{
		document.getElementById('lnkTotal').className='';
		document.getElementById('lnkClamplift').className='';
		document.getElementById('lnkCorrugator').className='';
		//document.getElementById('lnkKeyIn').className='';
		document.getElementById('lnkConvertor').className='';
		document.getElementById('lnkDelivery').className='';
		document.getElementById('lnkProductStatus').className='';
	}
	
	function getSelected()
	{
		return document.getElementById('currentSelection').value;
	}
	
	function getURL(reportType)
	{
		if(reportType=='lnkTotal') return "totalproductionplan/";
		if(reportType=='lnkClamplift') return "corrugatorclamplift/";
		if(reportType=='lnkCorrugator') return "corrugatordaily/";
		//if(reportType=='lnkKeyIn') return "keyin/";
		if(reportType=='lnkConvertor') return "convertor/";
		if(reportType=='lnkDelivery') return "deliverydaily/";
		if(reportType=='lnkProductStatus') return "productstatus/";
	}
	
	function loadPlanReport(reportType)
	{
		var selected = document.getElementById(reportType);
		clearAllSelected();
		selected.className = 'selectedList';
		document.getElementById('currentSelection').value = reportType;
		var plandate = document.getElementById('planning_date').value;
		newurl = BASEURL + 'index.php/reportplanning/'+getURL(reportType);
		Ext.Ajax.request({
			url: newurl,
			params : { 
				action : reportType,
				plandate  : plandate,
			},
			success: function ( result, request ) 
			{ 
				var container = document.getElementById('wrapper');
				container.innerHTML = result.responseText;
			},
			failure: function ( result, request) { 
				Ext.MessageBox.alert('Failed', result.responseText); 
			} 
		});
	}
	          
	function updateProjectStatusData(deliveryid){
	Ext.Ajax.request({
		url: BASEURL + 'index.php/reportplanning/updateprojectstatusdata/',
		params : {
			delivery_id 		: deliveryid,
			x_delivered_qty	:document.getElementById('x_delivered_qty').value,
			x_damaged_qty	:document.getElementById('x_damaged_qty').value,
			x_total_production_qty:document.getElementById('x_total_production_qty').value,
		},
		success: function ( result, request ) {
			//TODO
			unloadAjax();
		},
		failure: function ( result, request) { 
			Ext.MessageBox.alert('Failed', result.responseText); 
		} 
	});
	Ext.Ajax.on({
	    'beforerequest': function(){
			loadAjax("Updating Project Status Data");
		},
	});
	}
</script>

<input type='hidden' id='currentSelection' value=""/>
<div id="topheader"></div>
<div id="headbar">
            <table width="100%" border="0">
            	<tbody><tr>
            	<td>
            		<ul class="primary-links">
            				<li><a href='<?=base_url()."index.php"?>'>Home</a></li>
							<li><a id='lnkTotal' onclick='loadPlanReport("lnkTotal");' > T.P Plan </a></li>
							<li><a id='lnkClamplift' onclick='loadPlanReport("lnkClamplift");' > Clamplift Plan</a></li>
							<li><a id ='lnkCorrugator' onclick='loadPlanReport("lnkCorrugator");' > Corr. Daily Plan </a></li>
							<!--<li><a id='lnkKeyIn' onclick='loadPlanReport("lnkKeyIn");' > KeyIn </a></li> -->
							<li><a id='lnkConvertor' onclick='loadPlanReport("lnkConvertor");' > Convertor </a></li>
							<li><a id='lnkDelivery' onclick='loadPlanReport("lnkDelivery");' > Delivery Plan </a></li>
							<li><a id='lnkProductStatus' onclick='loadPlanReport("lnkProductStatus");' > Project Status </a></li>
					</ul>
            	</td>
            	<td>
            		<input type='text' id='planning_date' class="date-picker"  value ="<?=date('Y-m-d')?>" size="9" >
            	</td>
            	
            		<td>
						<input type="button" onclick="printPlanning()" value="Print"/>
						<input type="button" onclick="javascript:self.close()" value="Close"/>
					</td>
                    
				</tr>
            </tbody></table>
</div>
<div id='wrapper' class='movedown'>
	<!--Start Edit Here -->
	<table id='container'>
		<tr>
			<td valign='top' height='20px'>
				
			</td>
		</tr>
		<tr>
			<td valign='top'>
				
				 <br/>
				1. Select Date <br/>
				2. Select Type of Report <br/>
				
			</td>
		</tr>
	</table>
	<!--End Edit Here -->
</div>

<script type="text/javascript">
	makeDateField();
</script>