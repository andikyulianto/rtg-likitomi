<?php
class Reportplanning extends Controller {
	
	function __construct() 
	{
		parent::Controller();
		$this->freakauth_light->check();
		//$this->lang->load('products', 'english');
		$this->load->database();
		$this->load->model('Planning_model');
	}
	
	function index()
	{
		$data = array(
	      'contentClass' => $this,
	      'title' => "Report Planning | Likitomi ERP",
		  'scripts' => $this->getScripts(),
		  'styles' => $this->getStyles()
	  	);
	  	$this->load->view('template', $data);
	}
	
	function getScripts()
	{
		$script  = '<script type="text/javascript" src="'.base_url().'resources/javascript/ext/ext-base.js"></script>';
		$script .= '<script type="text/javascript" src="'.base_url().'resources/javascript/ext-all.js"></script>';
		return $script;
	}	
	
	function getStyles()
	{
		$styles  ='@import "'.base_url().'static/css/salesreport.css";';
		$styles	.='@import "'.base_url().'resources/css/ext-all.css";';
		return $styles;
	}
	
	function show()
	{
		$this->load->view('planning/reportplanning');
	}	
	
	function totalproductionplan()
	{
		$today  	= date('Y-m-d');
		$plandate 	= ($this->input->post('plandate'))?$this->input->post('plandate'):$today;
		
		$data['resultTotalProductionPlan'] = $this->Planning_model->totalproductionplan($plandate);
		$data['plandate'] = $plandate;
		$this->load->view('planning/totalproductionplan',$data);
	}
	
	function keyin()
	{
		$today  	= date('Y-m-d');
		$plandate 	= ($this->input->post('plandate'))?$this->input->post('plandate'):$today;
		$data['resultKeyin'] = $this->Planning_model->keyin($plandate);
		$data['plandate'] = $plandate;
		$this->load->view('planning/keyin',$data);
	}
	function convertor()
	{
		$today  	= date('Y-m-d');
		$plandate 	= ($this->input->post('plandate'))?$this->input->post('plandate'):$today;
		$data['resultConvertor'] = $this->Planning_model->convertor($plandate);
		$data['plandate'] = $plandate;
		$this->load->view('planning/convertor',$data);
	}
	
	function corrugatorclamplift()
	{
		$today  	= date('Y-m-d');
		$plandate 	= ($this->input->post('plandate'))?$this->input->post('plandate'):$today;
		$data['resultCorrugatorClamplift'] = $this->Planning_model->corrugatorclamplift($plandate);
		$data['plandate'] = $plandate;
		$this->load->view('planning/corrugatorclamplift',$data);
	}
	
	function corrugatordaily()
	{
		$today  	= date('Y-m-d');
		$plandate 	= ($this->input->post('plandate'))?$this->input->post('plandate'):$today;
		$data['resultCorrugatorDaily'] = $this->Planning_model->corrugatordaily($plandate);
		$data['plandate'] = $plandate;
		$this->load->view('planning/corrugatordaily',$data);
	}
	
	function deliverydaily()
	{
		$today  	= date('Y-m-d');
		$plandate 	= ($this->input->post('plandate'))?$this->input->post('plandate'):$today;
		$data['resultDeliveryDaily'] = $this->Planning_model->deliverydaily($plandate);
		$data['plandate'] = $plandate;
		$this->load->view('planning/deliverydaily',$data);
	}
	
	function productstatus()
	{
		$today  	= date('Y-m-d');
		$plandate 	= ($this->input->post('plandate'))?$this->input->post('plandate'):$today;
		$data['resultProductStatus'] = $this->Planning_model->productstatus($plandate);
		$data['plandate'] = $plandate;
		$this->load->view('planning/productstatus',$data);	
	}
	
	function updateprojectstatusdata()
	{
		$projectdetails = array();
		$delivery_id 	= ($this->input->post('delivery_id'))?$this->input->post('delivery_id'):'0';
		
		if($delivery_id>0){
			$projectdetails['delivered_qty'] 			= ($this->input->post('x_delivered_qty'))?$this->input->post('x_delivered_qty'):'0';
			$projectdetails['total_production_qty'] 	= ($this->input->post('x_total_production_qty'))?$this->input->post('x_total_production_qty'):'0';
			$projectdetails ['damaged_qty']				= ($this->input->post('x_damaged_qty'))?$this->input->post('x_damaged_qty'):'0';
			$projectdetails ['status']					= "produced";
			$this->Planning_model->updateproductstatus($projectdetails,$delivery_id);
		}
		else{
			echo "Invalid ID : ".$delivery_id;
		}
		
	}
}
?>