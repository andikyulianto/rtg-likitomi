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
			$deliveryList[$cnt]['corrugator_date']	= date('Y-m-d');
			$deliveryList[$cnt]['corrugator_time']	= "";
			$deliveryList[$cnt]['converter_date']	= date('Y-m-d');
			$deliveryList[$cnt]['converter_time']	= "";
			
			$cnt++;
		}
		
		//load JSON lib
		$this->load->library('JSON');	
		echo '{"delivery" :'.$this->json->encode($deliveryList).',"count":"'.$cnt.'"}';
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
		foreach($gridData as $rowData)
		{
			$this->Planning_model->savetotalplan($rowData,$choosendate);
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
	
	
}
?>