<?php
header("Expires: Mon, 26 Jul 1997 05:00:00 GMT"); // Date in the past
header("Last-Modified: " . gmdate("D, d M Y H:i:s") . " GMT"); // Always modified
header("Cache-Control: private, no-store, no-cache, must-revalidate"); // HTTP/1.1 
header("Cache-Control: post-check=0, pre-check=0", false);
header("Pragma: no-cache"); // HTTP/1.0
?>
<html>
<head>
	<link type="text/css" rel="stylesheet" href="<?=base_url().'static/css/salesreport.css'?>" />
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
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
		function printSalesOrder()
		{
			document.getElementById("topheader").className="hidden";
			document.getElementById("headbar").className="hidden";
			document.getElementById("wrapper").className="movetotop";
			document.body.offsetWidth;document.body.offsetHeight;
			window.print();
		}
	</script>
</head>
<body>
<div id="topheader"></div>
<div id="headbar">
            <table width="100%" border="0">
            	<tbody><tr>
            		<td align="center">
						<input type="button" onclick="printSalesOrder()" value="Print"/>
						<input type="button" onclick="javascript:self.close()" value="Close"/>
					</td>
                    
				</tr>
            </tbody></table>
 </div>
<div id='wrapper' class='movedown'>
	<table id='container'>
		<tr>
			<td valign='top' height='40px'>
				<div class='title'>SALES ORDER</div>
				<table id=header>
					<tr>
						<td style='padding:0px' >PRODUCT CODE :<span class='dotted'>&nbsp; <b><?=$resultProductCatalog->product_code?></b>&nbsp;</span></td>
						<td style='padding:0px' >NO :<span class='dotted'>&nbsp;<b><?php echo ($numSales>0)?$resultSalesOrder->row()->sales_order_id:""?></b>&nbsp;</span></td>
					</tr>
				</table>
			</td>
		</tr>
		<tr>
			<td style='padding:0px' valign='top'>
				<table height='100%'>
					<tr>
						<td style='padding:0px' class='leftbar'>
							<table  border="1" height='100%'>
								<tr >
								    <td colspan="5" height='40'>CUSTOMER &nbsp;<b><?=$customer_name?></b></td>
									<td colspan="6">PRODUCT  &nbsp;<b><?=$resultProductCatalog->product_name?></b></td>
								</tr>
								<tr>
								    <td rowspan="2" width="70" class='subtitle'>PRODUCT CODE </td>
								    <td rowspan="2" width="40" class='subtitle'>FLUTE</td>
								    <td colspan="5" class='subtitle'>BROAD COMBINATION </td>
								    <td colspan="3" class='subtitle'>INNER DIMENSION (m.m) </td>
								    <td rowspan="2" width="40" class='subtitle'>QTY / SET</td>
								</tr>
								<tr align='center'>
								    <td width="70">D-F</td>
								    <td width="70">BM</td>
								    <td width="70">B-L</td>
								    <td width="70">CM</td>
								    <td width="70">C-L</td>
								    <td width="46">L</td>
								    <td width="46">W</td>
								    <td width="46">H</td>
								</tr>
<?php 
$cnt=0;
foreach ($productDetails as $prod) {
	$cnt++;
?> 
 <tr>
	<td height='25'><b><?=$prod->product_code?></b></td>
    <td><b><?=$prod->flute?></b></td>
    <td><b><?=$prod->DF?></b></td>
    <td><b><?=$prod->BM?></b></td>
    <td><b><?=$prod->BL?></b></td>
    <td><b><?=$prod->CM?></b></td>
    <td><b><?=$prod->CL?></b></td> 
    <td><b><?=$prod->Length_mm?></b></td>
    <td><b><?=$prod->Width_mm?></b></td>
    <td><b><?=$prod->Height_mm?></b></td>
    <td><b><?=$prod->qty_set?></b></td>
</tr>
<?php }
for($i=$cnt;$i<5;$i++){
?>
<tr>
	<td height='25'>&nbsp;</td>
	<td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td>
	<td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td>
	<td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td>
	<td>&nbsp;</td>
</tr>
<?php } ?>
<?php
$inkCnt =0;
if($resultProductCatalog->ink_1!="")$inkCnt++;
if($resultProductCatalog->ink_2!="")$inkCnt++;
if($resultProductCatalog->ink_3!="")$inkCnt++;
?>
								<tr>
								    <td colspan="3" class='subtitle'>INK ( <b><?=$inkCnt?></b> ) COLOR</td>
								    <td rowspan="2" colspan="2" class='subtitle'>JOINT TYPE : <b><?=$resultProductCatalog->joint_type?></b> <br/>
										<br/><b><?=$resultProductCatalog->joint_details?></b></td>
								    <td rowspan="2" class='subtitle'>BOX :<br/><br/><b><?=$resultProductCatalog->box_style?></b></td>
								    <td rowspan="2" colspan="2" class='subtitle'>ROPE COLOR :<span class='dotted'>&nbsp;&nbsp;<b><?=$resultProductCatalog->rope_color?></b>&nbsp;&nbsp;</span> <br/><br/>
									<span class='dotted'>&nbsp;&nbsp;&nbsp;<b><?=$resultProductCatalog->pcs_bundle?></b>&nbsp;&nbsp;&nbsp;</span>PCS/ BUNDLE</td>
								    <td rowspan="2" class='subtitle'>LEVEL<br/><br/><b><?=$resultProductCatalog->level?></b></td>
								    <td colspan="2" rowspan="2" class='subtitle'>PAPER WIDTH <br/><br/>
									<b><?=$resultProductCatalog->p_width_inch?>" / <?=$resultProductCatalog->slit?></b></td>
								</tr>	
								<tr>
								    <td><b><?=$resultProductCatalog->ink_1?></b></td>
								    <td><b><?=$resultProductCatalog->ink_2?></b></td>
								    <td><b><?=$resultProductCatalog->ink_3?></b></td>
							 	</tr>
								<tr>
								    <td colspan="11" class='image'>
								    <?php if($resultProductCatalog->sketch!="") echo "<img src='".base_url().$resultProductCatalog->sketch."'>"?>
									</td>
								</tr>
							</table>
						</td>
						<td class='centerbar'></td>
						<td class='rightbar' style='padding:0px'>
							<table border='1'>
								<tr>
									<td colspan="2" class='subtitleleft'>DATE : <br/> <b><?php echo ($numSales>0)?$resultSalesOrder->row()->sales_order_date:""?></b></td>
								    <td class='subtitleleft'>SALESMAN : <br/> <b><?php echo ($numSales>0)?$resultSalesOrder->row()->salesman:""?></b></td>
								    <td colspan="2" class='subtitleleft'>PROCESS<br/>
									<?=$resultProductCatalog->next_process?></td>
								</tr>
								<tr>
									<td colspan="3" class='subtitleleft'>Product Name : <?=$resultProductCatalog->product_name?> <br/><br/> For: Sales & Account <br/></td>
									<td class='subtitle' width='70px'>CODE RD : <b><?=$resultProductCatalog->code_rd?></b></td>
									<td class='subtitle' width='70px'>CODE PD : <b><?=$resultProductCatalog->code_pd?></b></td>								  
								</tr>
								<tr>
									<td class='subtitle' width="70">P.CODE</td>
									<td class='subtitle' width="70">AMOUNT</td>
									<td class='subtitleleft' colspan="2" rowspan="3">DELIVERY AT : <br/><?php echo ($numSales>0)?$resultSalesOrder->row()->delivery_at:""?> </td>
									<td class='subtitleleft' rowspan="3">QTY ALLOWANCE: <br/><br/><b><?=$resultProductCatalog->qty_allowance?></b></td>									
								</tr>
								<tr>
									<td><b><?php echo ($numSales>0)?$resultSalesOrder->row()->product_code_1:""?>&nbsp;</b></td>
									<td><b><?php echo ($numSales>0)?$resultSalesOrder->row()->amount_1:""?>&nbsp;</b></td>
								</tr>
								<tr>
									<td><b><?php echo ($numSales>0)?$resultSalesOrder->row()->product_code_2:""?>&nbsp;</b></td>
									<td><b><?php echo ($numSales>0)?$resultSalesOrder->row()->amount_2:""?>&nbsp;</b></td>
								</tr>
								<tr>
									<td><b><?php echo ($numSales>0)?$resultSalesOrder->row()->product_code_3:""?>&nbsp;</b></td>
									<td><b><?php echo ($numSales>0)?$resultSalesOrder->row()->amount_3:""?>&nbsp;</b></td>
									<td class='subtitleleft' colspan="2" rowspan="3">PURCHASE ORDER NO :</br></br><b><?php echo ($numSales>0)?$resultSalesOrder->row()->purchase_order_no:""?></b> </td>
									<td class='subtitleleft' colspan="2" rowspan="3">STOCK : </td>
								</tr>
								<tr>
									<td><b><?php echo ($numSales>0)?$resultSalesOrder->row()->product_code_4:""?>&nbsp;</b></td>
									<td><b><?php echo ($numSales>0)?$resultSalesOrder->row()->amount_4:""?>&nbsp;</b></td>
								</tr>
								<tr>
									<td>&nbsp;</td>
									<td>&nbsp;</td>
								</tr>
							</table>
							<div style="height:4px;"> 	</div>
							<table border='1'>
								<tr>
									<td class='subtitleleft' >REMARKS : <?=$resultProductCatalog->remark?></td>
								</tr>
							</table>
							<div style="height:4px;"> 	</div>
							<table border='1'>
								<tr>
									<td class='subtitle' width='30px'>NO.</td>
									<td class='subtitle' >DOC REF </td>
								    <td class='subtitle'>DELIVERY DATE </td>
								    <td class='subtitle'>P.CODE </td>  
									<td class='subtitle'>QTY. </td>  
								</tr>
<?php 
$cnt=0;
if($numDelivery>0){
foreach ($productDelivery->result() as $prod) {
	$cnt++;
?>
  <tr>
    <td><b><?=$cnt?></b></td>
	<td><b><?=$prod->doc_ref?></b></td>
	<td><b><?=$prod->delivery_date?></b></td>
    <td><b><?=$prod->product_code?></b></td>
	<td><b><?=$prod->qty?></b></td>
  </tr>
<?php }}?>
<?php 
for($i=$cnt;$i<12;$i++){
?>
<tr>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
	<td>&nbsp;</td>
  </tr>
<?php }?></table>
<div style="height:4px;"> 	</div>
<table border='1'>
	<tr>
	    <td class='subtitlebottom' width='40%'>SALES COORDINATOR </td>
	    <td class='subtitlebottom' width='30%'> SALE </td>
	    <td class='subtitlebottom' width='30%'>APPROVED</td>
  	</tr>
</table>
						</td>
					</tr>
				</table>
			</td>
		</tr>
	</table>
</div>
	