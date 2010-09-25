<?php
class Partners extends Controller {
	
	function __construct() 
	{
		parent::Controller();
		$this->freakauth_light->check();
		$this->lang->load('partners',$this->db_session->userdata('language'));
		$this->load->database();
		$this->load->model('Partners_model');
		$this->load->scaffolding('partners');
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
		$script = '<script type="text/javascript" src="'.base_url().'resources/javascript/ext/ext-base.js"></script>';
		$script .= '<script type="text/javascript" src="'.base_url().'resources/javascript/ext-all.js"></script>';
		$script .= '<script type="text/javascript" src="'.base_url().'static/javascript/common.js"></script>';
		$script .= '<script type="text/javascript" src="'.base_url().'static/javascript/table.js"></script>';
		$script .= '<script type="text/javascript" src="'.base_url().'static/javascript/table2.js"></script>';
		return $script;
	}
		
	function getStyles()
	{
		$styles  ='@import "'.base_url().'static/css/common.css";';
		$styles	.='@import "'.base_url().'resources/css/ext-all.css";';
		$styles .='@import "'.base_url().'resources/css/xtheme-gray.css";';
		return $styles;
	}
	
	function show()
	{
		$data['leftmenu']=array(
				$this->lang->line('all_partners'),
				$this->lang->line('customers'),
				$this->lang->line('suppliers'),
				$this->lang->line('archive'),
			);
		$data['leftmenu_count'] = array(
				$this->Partners_model->getTotalData(),
				$this->Partners_model->getTotalByType('Customer'),
				$this->Partners_model->getTotalByType('Supplier'),
				$this->Partners_model->getTotalTrash(),				
			);
		$data['types']=array('All','Customer','Supplier','Trash');
		
		$this->load->view('partners/partners',$data);
	}
	
	function getCounters(){
		$item = array(
				$this->Partners_model->getTotalData(),
				$this->Partners_model->getTotalByType('Customer'),
				$this->Partners_model->getTotalByType('Supplier'),
				$this->Partners_model->getTotalTrash(),				
			);
		$this->load->library('json'); 
		echo json_encode($item);
	}
	
	function getNames()
	{
		$partner_type = ($this->input->post('partner_type'))?$this->input->post('partner_type'):'all_partners';
		$data['resultPartners'] = $this->Partners_model->getNames($partner_type);
		$data['action'] = "list";
		$data['partner_class'] = $this;
		$this->load->view('partners/partnerlist',$data);
	}
	
	function getDetails()
	{
		$partner_id = ($this->input->post('partner_id'))?$this->input->post('partner_id'):'0';
		$data['action'] = ($this->input->post('action'))?$this->input->post('action'):'view';;
		if(($partner_id > 0) || ($data['action']=='add'))
		{
			if($data['action'] !='add') 
			{
				$data['resultPartner'] = $this->Partners_model->getDetails($partner_id);
				$data['resultPartnerAddresses'] = $this->Partners_model->getPartnerAddresses($partner_id);				
			}
			$this->load->view('partners/partnerdetail',$data);
			$this->listproductsById($partner_id);
		}
		else 
		{
			echo "Invalid Partner ID : ".$partner_id ;
		}
	}
	
	function saveDetail()
	{
		$partners = array();
		$addresses = array();
		$partners['partner_type'] 	= ($this->input->post('partner_type'))?$this->input->post('partner_type'):'';
		$partners['partner_name'] 	= ($this->input->post('partner_name'))?$this->input->post('partner_name'):'';
		$partners['partner_name_thai'] 		= ($this->input->post('partner_name_thai'))?$this->input->post('partner_name_thai'):'';
		$partners['partner_code'] 			= ($this->input->post('partner_code'))?$this->input->post('partner_code'):'';
		$partners['partner_supplier_code'] 	= ($this->input->post('partner_supplier_code'))?$this->input->post('partner_supplier_code'):'';
		$partners['partner_credit_term'] 	= ($this->input->post('partner_credit_term'))?$this->input->post('partner_credit_term'):'';
		$partners['partner_phone_office'] 	= ($this->input->post('partner_phone_office'))?$this->input->post('partner_phone_office'):'';
		$partners['partner_fax'] 			= ($this->input->post('partner_fax'))?$this->input->post('partner_fax'):'';
		$partners['partner_other_phone'] 	= ($this->input->post('partner_other_phone'))?$this->input->post('partner_other_phone'):'';
		$partners['partner_email']	 		= ($this->input->post('partner_email'))?$this->input->post('partner_email'):'';
		$partners['partner_website'] 		= ($this->input->post('partner_website'))?$this->input->post('partner_website'):'';
		$partners['partner_contact_title'] 	= ($this->input->post('partner_contact_title'))?$this->input->post('partner_contact_title'):'';
		$partners['partner_contact_person'] = ($this->input->post('partner_contact_person'))?$this->input->post('partner_contact_person'):'';
		$partners['partner_billing_address'] 	= ($this->input->post('partner_billing_address'))?$this->input->post('partner_billing_address'):'';
		$partners['partner_description'] 	= ($this->input->post('partner_description'))?$this->input->post('partner_description'):'';
		$partners['isdeleted'] 				= '0';
		$partners['created_on'] 			= date("Y-m-d G:i:s");
		$partners['created_by'] 			= $this->db_session->userdata('user_name');
		
		$address_cnt		= $this->input->post('address_cnt');
		$partner_addresses 	= explode("|",$this->input->post('partner_addresses'));
		
		$partner_id = $this->Partners_model->insertPartner($partners);
		if($partner_id>0)
		{	
			$this->Partners_model->insertAddresses($partner_id,$partner_addresses);	
		}
		//never echo here
		echo $partner_id;
	}
	
	function updateDetail()
	{
		$partners = array();
		$addresses = array();
		$partner_id 	= ($this->input->post('partner_id'))?$this->input->post('partner_id'):'0';
		if($partner_id > 0 )
		{
			$partners['partner_type'] 	= ($this->input->post('partner_type'))?$this->input->post('partner_type'):'';
			$partners['partner_name'] 	= ($this->input->post('partner_name'))?$this->input->post('partner_name'):'';
			$partners['partner_name_thai'] 		= ($this->input->post('partner_name_thai'))?$this->input->post('partner_name_thai'):'';
			$partners['partner_code'] 		= ($this->input->post('partner_code'))?$this->input->post('partner_code'):'';
			$partners['partner_supplier_code'] 		= ($this->input->post('partner_supplier_code'))?$this->input->post('partner_supplier_code'):'';
			$partners['partner_credit_term'] 		= ($this->input->post('partner_credit_term'))?$this->input->post('partner_credit_term'):'';
			$partners['partner_phone_office'] 	= ($this->input->post('partner_phone_office'))?$this->input->post('partner_phone_office'):'';
			$partners['partner_fax'] 			= ($this->input->post('partner_fax'))?$this->input->post('partner_fax'):'';
			$partners['partner_other_phone'] 	= ($this->input->post('partner_other_phone'))?$this->input->post('partner_other_phone'):'';
			$partners['partner_email']	 		= ($this->input->post('partner_email'))?$this->input->post('partner_email'):'';
			$partners['partner_website'] 		= ($this->input->post('partner_website'))?$this->input->post('partner_website'):'';
			$partners['partner_contact_title'] 	= ($this->input->post('partner_contact_title'))?$this->input->post('partner_contact_title'):'';
			$partners['partner_contact_person'] 	= ($this->input->post('partner_contact_person'))?$this->input->post('partner_contact_person'):'';
			$partners['partner_billing_address'] 	= ($this->input->post('partner_billing_address'))?$this->input->post('partner_billing_address'):'';
			$partners['partner_description'] 	= ($this->input->post('partner_description'))?$this->input->post('partner_description'):'';
			$partners['isdeleted'] 				= '0';
			$partners['modified_on'] 			= date("Y-m-d G:i:s");
			$partners['modified_by'] 			= $this->db_session->userdata('user_name');
			$this->Partners_model->updatePartner($partners,$partner_id);
			
			$address_cnt		= $this->input->post('address_cnt');
			$partner_addresses 	= explode("|",$this->input->post('partner_addresses'));
			$partner_addresseids = explode("|",$this->input->post('partner_addresseids'));
			
			$this->Partners_model->updateAddresses($partner_id,$partner_addresses,$partner_addresseids);
		}
		else 
		{
			echo "Invalid Partner ID : ".$partner_id ;
		}
		
	}
	
	function deleteDetails()
	{
		$partner_id = ($this->input->post('partner_id'))?$this->input->post('partner_id'):'0';
		if($partner_id > 0)
		{
			$this->Partners_model->deletePartner($partner_id);
		}
		else 
		{
			echo "Invalid Partner ID : ".$partner_id ;
		}
	}
	function search()
	{
		$searchkeyword = ($this->input->post('search'))?$this->input->post('search'):'';
		$data['resultPartners'] = $this->Partners_model->search($searchkeyword);
		$data['action'] = "search";
		$data['searchkeyword'] = $searchkeyword;
		$data['partner_class'] = $this;
		$this->load->view('partners/partnerlist',$data);
		//echo $this->ew_Highlight("Lion Publion Company","lIon");
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
	
	function autoFillPartners(){
		$queryString = ($this->input->post('queryString'))?$this->input->post('queryString'):'';
		$limit = ($this->input->post('limit'))?$this->input->post('limit'):'10';
		$type = ($this->input->post('type'))?$this->input->post('type'):'json';

		if(strlen($queryString) > 0 )
		{
			header ("Expires: Mon, 26 Jul 1997 05:00:00 GMT");
			header ("Last-Modified: " . gmdate("D, d M Y H:i:s") . " GMT");
			header ("Cache-Control: no-cache, must-revalidate");
			header ("Pragma: no-cache");
			$items = array();
			$items = $this->Partners_model->getAutoFillNamesArray('Supplier',$limit,$queryString);
			//print_r($items);
			if($type=='json')
			{
				//header("Content-Type: application/json");		
				$this->load->library('JSON');
				echo "JSON:".$this->json->encode($items);
			}
			if($type == 'xml')
			{
				header("Content-Type: text/xml");
				echo '<?xml version="1.0" encoding="utf-8" ?>';
				echo "<results>";
				for ($i=0;$i<count($items);$i++){
					echo '<rs id="'.$items[$i]['partner_id'].'" name="'.$items[$i]['partner_name'].'"></rs>';
				}
				echo "</results>";
			}
		}
	}
	
	function getNamesArray()
	{
		$result = $this->Partners_model->getNames('Supplier');
		foreach ($result as $row)
		{
			echo '"'.$row->partner_id.'='.$row->partner_name.'",';
		}		
	}
	
	function listproducts(){
		$partner_id = ($this->input->post('partner_id'))?$this->input->post('partner_id'):'0';
		if($partner_id > 0 )
		{
			$data['resultPartner'] = $this->Partners_model->getDetails($partner_id);
			$data['resultProduct'] = $this->Partners_model->listProducts($partner_id);	
			$data['productcnt']	=	$this->Partners_model->listProductscnt($partner_id);
			$this->load->view('partners/partnerproduct',$data);
		}
		else 
		{
			echo "Invalid Partner ID : ".$partner_id ;
		}
	}
	function listproductsById($partner_id){
		if($partner_id > 0 )
		{
			$data['resultPartner'] = $this->Partners_model->getDetails($partner_id);
			$data['resultProduct'] = $this->Partners_model->listProducts($partner_id);	
			$data['productcnt']	=	$this->Partners_model->listProductscnt($partner_id);
			$this->load->view('partners/partnerproduct',$data);
		}
	}
}
?>