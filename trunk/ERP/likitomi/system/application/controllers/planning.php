<?php
class Planning extends Controller {
	
	function __construct() 
	{
		parent::Controller();
		$this->freakauth_light->check();
		$this->lang->load('planning',$this->db_session->userdata('language'));
		$this->load->database();
		$this->load->model('Planning_model');

	}
	
	function index()
	{
		$data = array(
	      'contentClass' => $this,
	      'title' => $this->lang->line('title'),
		  'scripts' => $this->getScripts(),
		  'styles' => $this->getStyles()
	  	);
 		$this->load->view('template', $data);
	}
	
	function getScripts()
	{
		$script  = '<script type="text/javascript" src="'.base_url().'resources/javascript/ext/ext-base.js"></script>';
		$script .= '<script type="text/javascript" src="'.base_url().'resources/javascript/ext-all.js"></script>';
		$script .= '<script type="text/javascript" src="'.base_url().'static/javascript/common.js"></script>';
		$script .= '<script type="text/javascript" src="'.base_url().'static/javascript/table.js"></script>';
		return $script;
	}
		
	function getStyles()
	{
		$styles	 = '@import "'.base_url().'static/css/planning.css";';
		$styles .=' @import "'.base_url().'static/css/common.css";';
		$styles	.= '@import "'.base_url().'resources/css/ext-all.css";';
		//$styles	.= '@import "'.base_url().'resources/css/xtheme-gray.css";';
		return $styles;
	}
	
	function show()
	{
		$resultAllDelivery	= $this->Planning_model->getAllDelivery();
		$delDateArray 		= array();
		$salesOrderArray	= array();
		$lastmodified 		= array();
		$status				= array();
		
		$cnt=0;
		foreach ($resultAllDelivery->result() as $delivery)
		{
			$delDateArray[$cnt] 	= $delivery->delivery_date;
			$salesOrderArray[$cnt]	= $delivery->sales_order;
			$lastmodified[$cnt]		= substr($delivery->modified_on,0,10);
			$status[$cnt]			= $delivery->status;
			$cnt++;
		}
		
		rsort($delDateArray);
		rsort($salesOrderArray);
		rsort($lastmodified);
		sort($status);
		$data['delDateArray'] 		= array_unique($delDateArray);
		$data['salesOrderArray'] 	= array_unique($salesOrderArray);
		$data['lastmodified']		= array_unique($lastmodified);
		$data['status']				= array_unique($status);
		
		$data['resultAllDelivery'] 	= $resultAllDelivery;
		
		$this->load->view('planning/planning',$data);
	}
	
	function filter()
	{
		$delivery_date_all 	= explode("|",$this->input->post('delivery_date_all'));
		$sales_order_all 	= explode("|",$this->input->post('sales_order_all'));
		$lastmodified_all 	= explode("|",$this->input->post('lastmodified_all'));
		$status_all		 	= explode("|",$this->input->post('status_all'));
		
		$resultDelivery = $this->Planning_model->getFilterResult($delivery_date_all,$sales_order_all,$lastmodified_all,$status_all);
		$deliveryList = array();
		$cnt=0;
		$this->load->model('Salesorder_model');
		foreach($resultDelivery->result() as $delivery)
		{
			$deliveryList[$cnt]['delivery_id']	= $delivery->delivery_id;
			$deliveryList[$cnt]['sales_order']	= $delivery->sales_order;
			
			$salesDetail = $this->Salesorder_model->getSalesDetail($delivery->sales_order);
			$deliveryList[$cnt]['purchase_order_no']	= $salesDetail->purchase_order_no;
			
			$deliveryList[$cnt]['product_code']	= $delivery->product_code;
                        //echo $delivery->product_code;
			$partnerproduct = $this->Planning_model->getProduct_Partner($delivery->product_id);
			
			$deliveryList[$cnt]['product_name'] = $partnerproduct->product_name;
			$deliveryList[$cnt]['partner_name'] = $partnerproduct->partner_name;
			
			$deliveryList[$cnt]['p_width_inch']	= $partnerproduct->p_width_inch;
			$deliveryList[$cnt]['t_length']		= $partnerproduct->t_length;
			
			$productflutes	= $this->Planning_model->getProductFlutes($delivery->product_id,$delivery->product_code);
			if($productflutes->num_rows()>0){
				$deliveryList[$cnt]['flute']		= $productflutes->row()->flute;
				$deliveryList[$cnt]['DF']		= $productflutes->row()->DF;
				$deliveryList[$cnt]['BM']		= $productflutes->row()->BM;
				$deliveryList[$cnt]['BL']		= $productflutes->row()->BL;
				$deliveryList[$cnt]['CM']		= $productflutes->row()->CM;
				$deliveryList[$cnt]['CL']		= $productflutes->row()->CL;
			}else {
				$deliveryList[$cnt]['flute']	= "";
				$deliveryList[$cnt]['DF']		= "";
				$deliveryList[$cnt]['BM']		= "";
				$deliveryList[$cnt]['BL']		= "";
				$deliveryList[$cnt]['CM']		= "";
				$deliveryList[$cnt]['CL']		= "";
			}
			$deliveryList[$cnt]['cut']			= $partnerproduct->cut;
			
			$deliveryList[$cnt]['delivery_date']= $delivery->delivery_date;
			$deliveryList[$cnt]['qty']			= $delivery->qty;
			$deliveryList[$cnt]['modified_on']	= $delivery->modified_on;
			$deliveryList[$cnt]['status']		= $delivery->status;
			$deliveryList[$cnt]['corrugator_date']	= date('Y-m-d');
			$deliveryList[$cnt]['corrugator_time']	= "";
			$deliveryList[$cnt]['converter_date']	= date('Y-m-d');
			$deliveryList[$cnt]['converter_time']	= "";
			$deliveryList[$cnt]['patchpartition_date']	= date('Y-m-d');
			$deliveryList[$cnt]['patchpartition_time']	= "";
			$deliveryList[$cnt]['warehouse_date']	= date('Y-m-d');
			$deliveryList[$cnt]['warehouse_time']	= "";
			//$deliveryList[$cnt]['next_process']	= "";
			$deliveryList[$cnt]['sort']	= $cnt;
			
			$cnt++;
		}
		
		//load JSON lib
		$this->load->library('JSON');	
		echo '{"delivery" :'.$this->json->encode($deliveryList).',"count":"'.$cnt.'"}';
	}
	function formatDate($day)
	{
		$hour  = floor($day*24); 
		$min   = floor((($day*24)-$hour)*60); 
		$time  = ($hour<10)?"0".$hour:$hour;//
		$time .= ":";
		$time .= ($min<10)?"0".$min:$min;
		return $time;
	}
	
//	function getDeliveryHistory()
//	{
//		$delivery_id = ($this->input->post('delivery_id'))?$this->input->post('delivery_id'):'0';
//		$this->load->model('Salesorder_model');
//		$histdata['history'] = $this->Salesorder_model->getDeliveryHistory($delivery_id);
//		$histdata['showheader'] = true;
//		$this->load->view('salesorder/deliveryhistory',$histdata); 
//	}
	
	function savetotalplanjson()
	{
		$jsonData 		= ($this->input->post('data'))?$this->input->post('data'):'';
		$choosendate 	= ($this->input->post('choosendate'))?$this->input->post('choosendate'):date('Y-m-d');		
		if($jsonData == '') return false;
		//load JSON lib
		$this->load->library('JSON');
		$gridData = $this->json->decode($jsonData);	
		$this->Planning_model->deleteAllPlanForToday($choosendate);

		//calculate time
		$time_start_cr = (0.0006949*60)*8;
		$time_start_cv = (0.0006949*60)*9;
		//$time_start_pt = (0.0006949*60)*8;
		//$time_start_wh = (0.0006949*60)*8;
		foreach($gridData as $rowData)
		{
			// start stop time of CR 
			$query = $this->Planning_model->getProduct($rowData->product_code);
			$key = $query->row_array(0);							//get the only one object
			$case 	= $rowData->qty;
			    if(($key['slit'])!=0)
			$cut2 	= $case/$key['slit'];
			$metre	= ($key['t_length']*$cut2)/1000;
			$timeuseCR = 0;
		if((strtoupper($key['flute'])=="B")||(strtoupper($key['flute'])=="C"))
		{
			$timeuseCR = ($metre/120)+4;
		}
		else if((strtoupper($key['flute'])=="BC")||(strtoupper($key['flute'])=="W"))
		{
			$timeuseCR = ($metre/100)+4;
		}
		else $timeuseCR = 0;
		$time_stop_cr = $time_start_cr;
		if($timeuseCR!=0)
		{
			$time_stop_cr = $time_start_cr + $timeuseCR * 0.0006949;
		}
		//start stop time for CV
		//print_r($key);
		if(strpos($key['next_process'],'3CS'))
			$speed = 120;
		else
			$speed = 0;
		$time_stop_cv = $time_start_cv;
		if ($speed > 0)
			$timeuseCV = $rowData->qty / $speed;
		else
			$timeuseCV = 0;
		$time_stop_cv = $time_start_cv+ round($timeuseCV+30) * 0.0006949;
			//print_r($rowData);
			//print_r($key->row_array(0));
			$this->Planning_model->savetotalplan($rowData,$choosendate);
			//Save to fake_table for status tracking
			$this->Planning_model->savetostatustracking($rowData,$this->formatDate($time_start_cr),$this->formatDate($time_stop_cr),$this->formatDate($time_start_cv),$this->formatDate($time_stop_cv));
			$time_start_cr = $time_stop_cr;
		}
		echo "Data Saved as ".$choosendate." Plan.";
	}
	
//	function savetotalplan() 
//	{
//		$delivery_id_list 	= ($this->input->post('deliveryid'))?$this->input->post('deliveryid'):'';
//		$today 				= ($this->input->post('today'))?$this->input->post('today'):'';
//		$corrugator_date 	= ($this->input->post('corrugator_date'))?$this->input->post('corrugator_date'):'';
//		$converter_date 	= ($this->input->post('converter_date'))?$this->input->post('converter_date'):'';
//		
//		$delivery_ids 		= explode("|",$delivery_id_list);	
//		$corrugator_dates 	= explode("|",$corrugator_date);
//		$converter_dates	= explode("|",$converter_date);
//		
//		$this->Planning_model->savetotalplan($delivery_ids,$corrugator_dates,$converter_dates,$today);
//	}
	
	function loadplanbydate()
	{
		$choosendate 	= ($this->input->post('choosendate'))?$this->input->post('choosendate'):'';	
		if($choosendate=='') return 'Error in date';	
		
		$resultDelivery = $this->Planning_model->loadplanbydate($choosendate);
		$deliveryList = array();
		$cnt=0;
		$this->load->model('Salesorder_model');
		foreach($resultDelivery->result() as $delivery)
		{
			$deliveryList[$cnt]['delivery_id']	= $delivery->delivery_id;
			$deliveryList[$cnt]['sales_order']	= $delivery->sales_order;
			
			$salesDetail = $this->Salesorder_model->getSalesDetail($delivery->sales_order);
			$deliveryList[$cnt]['purchase_order_no']	= $salesDetail->purchase_order_no;
			
			$deliveryList[$cnt]['product_code']	= $delivery->product_code;
			$partnerproduct = $this->Planning_model->getProduct_Partner($delivery->product_id);
			
			$deliveryList[$cnt]['product_name'] = $partnerproduct->product_name;
			$deliveryList[$cnt]['partner_name'] = $partnerproduct->partner_name;
			
			$deliveryList[$cnt]['p_width_inch']	= $partnerproduct->p_width_inch;
			$deliveryList[$cnt]['t_length']		= $partnerproduct->t_length;
			
			$productflutes	= $this->Planning_model->getProductFlutes($delivery->product_id,$delivery->product_code);
			if($productflutes->num_rows()>0){
				$deliveryList[$cnt]['flute']		= $productflutes->row()->flute;
			}else {
			$deliveryList[$cnt]['flute']			= "";
			}
			$deliveryList[$cnt]['cut']			= $partnerproduct->cut;
			
			$deliveryList[$cnt]['delivery_date']= $delivery->delivery_date;
			$deliveryList[$cnt]['qty']			= $delivery->qty;
			$deliveryList[$cnt]['modified_on']	= $delivery->modified_on;
			$deliveryList[$cnt]['status']		= $delivery->status;
			$deliveryList[$cnt]['corrugator_date']	= substr($delivery->corrugator_date,0,10);
			$deliveryList[$cnt]['corrugator_time']	= substr($delivery->corrugator_date,11,5);
			$deliveryList[$cnt]['converter_date']	= substr($delivery->converter_date,0,10);
			$deliveryList[$cnt]['converter_time']	= substr($delivery->converter_date,11,5);
			$deliveryList[$cnt]['patchpartition_date']	= substr($delivery->corrugator_date,0,10);
			$deliveryList[$cnt]['patchpartition_time']	= substr($delivery->corrugator_date,11,5);
			$deliveryList[$cnt]['warehouse_date']	= substr($delivery->converter_date,0,10);
			$deliveryList[$cnt]['warehouse_time']	= substr($delivery->converter_date,11,5);
		//	$deliveryList[$cnt]['next_process'] = "";
		/*	$productCat = $this->Planning_model->getProductCat($delivery->product_id,$delivery->product_code);
			if($productCat->num_rows()>0){
				$deliveryList[$cnt]['next_process'] = $productCat->row()->next_process;
			}
			else
			{
				$deliveryList[$cnt]['next_process'] = "";
			}*/
			$cnt++;
		}

		//load JSON lib
		$this->load->library('JSON');	
		echo '{"planned" :'.$this->json->encode($deliveryList).',"count":"'.$cnt.'"}';
	}
	
	function reportplanning()
	{
		$this->load->view('planning/reportplanning');
	}
	
	function barcode($input)
	{



// Including all required classes
require('class/BCGFont.php');
require('class/BCGColor.php');
require('class/BCGDrawing.php'); 

// Including the barcode technology
include('class/BCGcode39.barcode.php'); 

// Loading Font
$font = new BCGFont('class/font/Arial.ttf', 18);
 
// The arguments are R, G, B for color.
$color_black = new BCGColor(0, 0, 0);
$color_white = new BCGColor(255, 255, 255); 

$code = new BCGcode39();
$code->setScale(1); // Resolution
$code->setThickness(30); // Thickness
$code->setForegroundColor($color_black); // Color of bars
$code->setBackgroundColor($color_white); // Color of spaces
$code->setFont($font); // Font (or 0)
//$code->parse($_GET['text']); // Text
$code->parse($input);

/* Here is the list of the arguments
1 - Filename (empty : display on screen)
2 - Background color */
$drawing = new BCGDrawing('', $color_white);
$drawing->setBarcode($code);
$drawing->draw();
// clean the output buffer
ob_clean();
// Header that says it is an image (remove it if you save the barcode to a file)
header('Content-Type: image/png');

// Draw (or save) the image into PNG format.
$drawing->finish(BCGDrawing::IMG_FORMAT_PNG);
//$this->load->view('planning/reportplanning', 'hello');
	}
}
?>