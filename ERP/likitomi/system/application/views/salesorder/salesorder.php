<script type="text/javascript">
/**
 * @author sanjilshrestha
 */
	var firstrowoffset = 0;
	var lastrowoffset = 0; 	
	var LOADING_TEXT	=	"<?=$this->lang->line('ajax_loading_products')?>";
	
	window.onload = function() {
		activatePlaceholders();
		logoutTips();
	}
	
	function displaySearchCnt(){}
	
	function loadProductDetail(product_id){
		document.getElementById('currentselection').value=product_id;
		Ext.Ajax.request({
			url: BASEURL + 'index.php/salesorder/getDetails/',
			params : { product_id : product_id, action : 'view'},
			success: function ( result, request ) { 
				var el = Ext.get('detailDivContainer');
				el.update(result.responseText);
				prd_AutoSelect();
				Ext.onReady(salesOrderTips);
				el.slideIn('l', { duration: 0.1 });		
				unloadAjax();
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
							<li><a href='<?=base_url()."index.php/products"?>'>Products</a></li>
							<li><span>Sales Order</span></li>
						</ul>
            		</td>
					<td align='center'></td>
                    <td align='right' width='280'>
                        <div id='searchform'>
                            <input id='searchtext' type="text" autocomplete="off" placeholder="<?=$this->lang->line('search_products')?>" value="" onkeyup="startSearch(event.which);"/>
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
						<?=$this->lang->line('msg_searchproduct')?>
					</p>
				</div>
			</div>
		</td>
		<td valign='top'>
			<div id='detailDivContainer'>
				<p class="details-info">
                    <?=$this->lang->line('msg_searchproduct')?>
                </p>
			</div>
		</td>
	</tr>
</table>