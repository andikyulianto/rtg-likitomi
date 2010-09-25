<?php 
class Warehouse extends Controller {
	
	function __construct() 
	{
		parent::Controller();
		$this->freakauth_light->check();
		$this->lang->load('warehouse',$this->db_session->userdata('language'));
		$this->load->database();
		$this->load->model('Warehouse_model');
		$this->load->scaffolding('paper_rolldetails');
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
		$data['thisClass'] = $this;
		$this->load->view('warehouse/warehouse',$data);
	}
	
	function getLimitInput()
	{
		return 30;
	}

	function getDetails()
	{
		$invoice_no = ($this->input->post('invoice_no'))?$this->input->post('invoice_no'):'0';
		$data['action'] = ($this->input->post('action'))?$this->input->post('action'):'view';;
		$data['limit'] = $this->getLimitInput();
		if($data['action'] !='add') 
		{
			$data['resultInvoiceDetail'] = $this->Warehouse_model->getDetails($invoice_no);	
			$data['thisClass'] = $this;		
		}
		$this->load->view('warehouse/warehousedetail',$data);
	}
	
	function getSuppliers()
	{
		$this->load->model('Partners_model');
		$result = $this->Partners_model->getNames('Supplier');
		foreach ($result as $row)
		{
			echo "['".$row->partner_id."','".$row->partner_name."'],";
		}
	}
	
	function getPapers()
	{
		$this->load->model('Papers_model');
		$result = $this->Papers_model->getPapersList('Supplier');
		foreach ($result as $row)
		{
			echo "['".$row->paper_code."'],";
		}
	}
	
	function getSupplierById($supplierid)
	{
		$this->load->model('Partners_model');
		$row = $this->Partners_model->getNamesById($supplierid);
		return $row->partner_name;
	}

	function search()
	{
		$searchkeyword = ($this->input->post('search'))?$this->input->post('search'):'';
		$data['resultWarehouse'] = $this->Warehouse_model->search($searchkeyword);
		$data['action'] = "search";
		$data['searchkeyword'] = $searchkeyword;
		$data['warehouse_class'] = $this;
		$this->load->view('warehouse/warehouselist',$data);
	}
	
	// Highlight value based on basic search keywords
	function ew_Highlight($src, $bkw) {
		$outstr = "";
		if (strlen($src) > 0 && (strlen($bkw) > 0)) 
		{
			$x=0;
			$wrky = stripos($src, $bkw);
			if ($wrky !== FALSE) 
			{
				$outstr .= substr($src, $x, $wrky) .
					"<span class=\"ewHighlightSearch\">" .
					substr($src, $wrky, strlen($bkw)) . "</span>";
				$x = $wrky + strlen($bkw);
				$outstr .= substr($src, $x, strlen($src));
			}			
		} else {
			$outstr = $src;
		}
		return $outstr;
	}
	
	function savestockdata()
	{
		$action			= ($this->input->post('action'))?$this->input->post('action'):'save';
		$supplier_id	= ($this->input->post('supplier_id'))?$this->input->post('supplier_id'):'0';
		$invoice_date	= ($this->input->post('invoice_date'))?$this->input->post('invoice_date'):date('Y-m-d');
		$invoice_no		= ($this->input->post('invoice_no'))?$this->input->post('invoice_no'):'0';
		$paper_code		= ($this->input->post('paper_code'))?$this->input->post('paper_code'):'0';

		//load JSON lib
		$this->load->library('JSON');
		$warehouse = $this->json->decode($this->input->post('stockjson'));
		if($action == 'update') {
			$cnt = $this->Warehouse_model->deleteWarehouseStock($invoice_no);
		}
		
		$cnt = $this->Warehouse_model->insertWarehouseStock($supplier_id,$invoice_date,$invoice_no,$paper_code,$warehouse);
		echo $cnt ." Record";
		echo ($cnt>1)?"s":"";
		echo ($action == 'update')?" Updated":" Added";	
	}	
}
?>