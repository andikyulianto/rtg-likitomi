<?php 
class Stock extends Controller {
	
	function __construct() 
	{
		parent::Controller();
		//$this->freakauth_light->check();
		$this->lang->load('warehouse',$this->db_session->userdata('language'));
		$this->load->database();
		$this->load->model('Warehouse_model');
		$this->load->scaffolding('paper_rolldetails');
	}
	
	function index()
	{
		$this->freakauth_light->check();
		$data = array(
	      'contentClass' => $this,
	      'title' => $this->lang->line('stocktitle'),
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
		$script .= '<script type="text/javascript" src="'.base_url().'static/javascript/table2.js"></script>';
		$script .= '<script type="text/javascript" src="'.base_url().'static/javascript/json2.js"></script>';
		return $script;
	}
		
	function getStyles()
	{
		$styles  ='@import "'.base_url().'static/css/common.css";';
		$styles	.='@import "'.base_url().'resources/css/ext-all.css";';
		$styles .='@import "'.base_url().'static/css/warehouse.css";';
		
		return $styles;
	}
	
	function show()
	{
		$invoiceArray 		= array();
		$paperCodeArray		= array();
		$suppliersArray		= array();
		$invoiceDateArray	= array();
		$movementDateArray	= array();
		
		$supplierNameArray	= array();
		
		$resultAllWarehouse	= $this->Warehouse_model->getAll();
		$cnt=0;
		foreach ($resultAllWarehouse->result() as $stock)
		{
			$invoiceArray[$cnt]			= $stock->invoice_no;
			$paperCodeArray[$cnt]		= $stock->paper_code;
			$suppliersArray[$cnt]		= $stock->supplier_id;
			$invoiceDateArray[$cnt]		= $stock->invoice_date;
			
			$cnt++;
		}
		
		$cnt=0;
		$resultAllDates	= $this->Warehouse_model->getAll_PaperMovementDate();
		foreach ($resultAllDates->result() as $stockDate)
		{
			$movementDateArray[$cnt++]	= $stockDate->movement_date;
		}
		
		$invoiceArrayUnique 		= array_unique($invoiceArray);
		$paperCodeArrayUnique		= array_unique($paperCodeArray);
		$suppliersArrayUnique		= array_unique($suppliersArray);
		$invoiceDateArrayUnique		= array_unique($invoiceDateArray);
		$movementDateArrayUnique	= array_unique($movementDateArray);
		
		//Sort Array
		rsort($invoiceArrayUnique);
		sort($paperCodeArrayUnique);
		rsort($suppliersArrayUnique);
		rsort($invoiceDateArrayUnique);
		rsort($movementDateArrayUnique);		
		
		foreach($suppliersArrayUnique as $sup){
			$supplierNameArray[$sup] = $this->getSupplierById($sup);
		}
		
		$stockFilter =  array();
		$stockFilter['invoiceArray']		= $invoiceArrayUnique;
		$stockFilter['paperCodeArray']		= $paperCodeArrayUnique;
		$stockFilter['suppliersArray']		= $supplierNameArray;
		$stockFilter['invoiceDateArray']	= $invoiceDateArrayUnique;
		$stockFilter['movementDateArray']	= $movementDateArrayUnique;
		
		$this->load->view('warehouse/stock',$stockFilter);
	}
	
	function filter()
	{
		//load JSON lib
		$this->load->library('JSON');
		$invoice_all 		= $this->json->decode($this->input->post('invoice_all'));
		$papercode_all 		= $this->json->decode($this->input->post('papercode_all'));
		$supplier_all 		= $this->json->decode($this->input->post('supplier_all'));
		$invoicedate_all	= $this->json->decode($this->input->post('invoicedate_all'));
		$movement_all		= $this->json->decode($this->input->post('movement_all'));
		$query_mode 		= $this->input->post('query_mode');	
		$data['resultStock'] = $this->Warehouse_model->getFilterResult($invoice_all,$papercode_all,$supplier_all,$invoicedate_all,$movement_all, $query_mode);
		$data['thisClass'] = $this;
		$this->load->view('warehouse/stockResult',$data);
	}
	
	function getSupplierById($supplierid)
	{
		$this->load->model('Partners_model');
		$row = $this->Partners_model->getNamesById($supplierid);
		return $row->partner_name;
	}
	
	function getLatestWeight($rollid)
	{
		$row = $this->Warehouse_model->getLatestWeight($rollid);
		if($row->num_rows()>0)
		{
			$item = $row->row();
			return $item->actual_wt;
		}
		else return 0;
	}
	
	function getLatestMovement($rollid)
	{
		$query = $this->Warehouse_model->getLatestWeight($rollid);
		return $query;
	}
	
	function getClampLiftFilter($paper_code)
	{
		$data = array(
	      'contentClass' => $this,
	      'title' => $this->lang->line('stocktitle'),
		  'scripts' => $this->getScripts(),
		  'styles' => $this->getStyles()
	  	);
		header("Expires: Mon, 26 Jul 1997 05:00:00 GMT"); // Date in the past
		header("Last-Modified: " . gmdate("D, d M Y H:i:s") . " GMT"); // Always modified
		header("Cache-Control: private, no-store, no-cache, must-revalidate"); // HTTP/1.1 
		header("Cache-Control: post-check=0, pre-check=0", false);
		header("Pragma: no-cache"); // HTTP/1.0

		
		//$paper_code = ($this->input->post('paper_code'))?$this->input->post('paper_code'):'0';
		$sql = "SELECT * FROM paper_rolldetails WHERE (paper_code = '".$paper_code."')";
		//echo $sql;
		$query = $this->db->query($sql);
		$data['resultStock'] = $query;
		$data['thisClass'] = $this;
		$this->load->view('warehouse/stockbycode',$data);
		
	}
	

}