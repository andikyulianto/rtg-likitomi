<?php
class Products extends Controller {
	
	function __construct() 
	{
		parent::Controller();
		$this->freakauth_light->check();
		$this->lang->load('products', $this->db_session->userdata('language'));
		$this->load->database();
		$this->load->model('Products_model');
		$this->load->scaffolding('product_catalog');
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
		$script .= '<script type="text/javascript" src="'.base_url().'static/javascript/table2.js"></script>';
		$script .= '<script type="text/javascript" src="'.base_url().'static/javascript/FileUploadField.js"></script>';
		$script .= '<script type="text/javascript" src="'.base_url().'static/javascript/products.js"></script>';
		return $script;
	}	
	function getStyles()
	{
		$styles  ='@import "'.base_url().'static/css/common.css";';
		$styles	.='@import "'.base_url().'resources/css/ext-all.css";';
		$styles	.='@import "'.base_url().'static/css/file-upload.css";';
		$styles .='@import "'.base_url().'resources/css/xtheme-gray.css";';
		return $styles;
	}
	
	function show()
	{
		$data['leftmenu']=array(
				$this->lang->line('all_products'),
				"Outer Boxes",
				"Inner Boxes",
				"Archive",
			);
		$data['leftmenu_count'] = array(
				$this->Products_model->getTotalData(),
				$this->Products_model->getTotalDataByEndZero(),
				$this->Products_model->getTotalDataByNotEndZero(),
				$this->Products_model->getTotalTrash(),
			);
		$data['types']=array('All','Outer','Inner',"Trash");
		$this->load->view('products/products',$data);
	}
	
	function getCounters(){
		$item = array(
				$this->Products_model->getTotalData(),
				$this->Products_model->getTotalDataByEndZero(),
				$this->Products_model->getTotalDataByNotEndZero(),
				$this->Products_model->getTotalTrash(),
			);
		$this->load->library('json'); 
		echo json_encode($item);
	}
	
	function getNames()
	{
		$product_type = ($this->input->post('product_type'))?$this->input->post('product_type'):'All';
		$page=($this->input->post('page'))?$this->input->post('page'):'0';
		$data['resultProducts'] = $this->Products_model->getLimitedByType($product_type,$this->perPage(),$page);
		if($product_type=='All') $data['totalRec'] = $this->Products_model->getTotalData();
		else if($product_type=='Outer') $data['totalRec'] = $this->Products_model->getTotalDataByEndZero();
		else if($product_type=='Inner') $data['totalRec'] = $this->Products_model->getTotalDataByNotEndZero();
		else if($product_type=='Trash') $data['totalRec'] = $this->Products_model->getTotalTrash();
		$data['perPage'] = $this->perPage();
		$data['page'] = $page;
		$data['action'] = "list";
		$data['product_type'] =$product_type;
		$this->load->view('products/productlist',$data);
	}
	
	function perPage(){
		return 30;
	}
	
	function getDetails()
	{
		$product_id = ($this->input->post('product_id'))?$this->input->post('product_id'):'0';
		$data['action'] = ($this->input->post('action'))?$this->input->post('action'):'view';
		if(($product_id > 0 )||($data['action']=='add'))
		{
			$this->load->model('Partners_model');
			if($data['action'] !='add'){
				$data['resultProductCatalog'] 	= $this->Products_model->getDetails($product_id);		
				$customerInfo 			= $this->Partners_model->getCustomerInfo($data['resultProductCatalog']->partner_id);
				$data['customer_name']			= $customerInfo->partner_name;
				$data['billing_address']		= $customerInfo->partner_billing_address;	
				$data['partner_isdeleted']		= $customerInfo->isdeleted;
				$data['resultProducts'] 		= $this->Products_model->getProducts($product_id);
				$data['deliveryAddresses']		= $this->Partners_model->getAddresses($data['resultProductCatalog']->partner_id);
			}
			$data['resultParnters']=$this->Partners_model->getNames('Customer');
			
			$data['resultProductSalesHistory'] = $this->Products_model->productSalesHistory($product_id);
			$data['salesCount'] = $data['resultProductSalesHistory']->num_rows();
			
			$this->load->view('products/productdetail',$data);
			$this->load->view('products/productsaleshistory',$data);
				
		}
		else 
		{
			echo "Invalid Product ID : ".$product_id ;
		}
	}
	
	function getProductLine(){
		$product_code= ($this->input->post('product_code'))?$this->input->post('product_code'):'';
		if($product_code!=""){
			$resultProduct 	= $this->Products_model->getProductLine($product_code);
			if($resultProduct){
				echo $resultProduct->product_code."|"
				.$resultProduct->flute."|"
				.$resultProduct->DF."|"
				.$resultProduct->BM."|"
				.$resultProduct->BL."|"
				.$resultProduct->CM."|"
				.$resultProduct->CL."|"
				.$resultProduct->Length_mm."|"
				.$resultProduct->Width_mm."|"
				.$resultProduct->Height_mm."|"
				.$resultProduct->qty_set;				
			}
			else { echo "";}			
		}	
	}

	function productData($productsall)
	{
		$product_data =  array();
		$product_data['product_code']=$productsall[1];
		$product_data['flute']=$productsall[2];
		$product_data['DF']=$productsall[3];
		$product_data['BM']=$productsall[4];
		$product_data['BL']=$productsall[5];
		$product_data['CM']=$productsall[6];
		$product_data['CL']=$productsall[7];
		$product_data['Length_mm']=$productsall[8];
		$product_data['Width_mm']=$productsall[9];
		$product_data['Height_mm']=$productsall[10];
		$product_data['qty_set']=$productsall[11];
		return $product_data;
	}
	function saveDetail()
	{
		$products = array();
		$products['product_code'] = ($this->input->post('product_code'))?$this->input->post('product_code'):'';
		$products['product_name'] = ($this->input->post('product_name'))?$this->input->post('product_name'):'';
		$products['partner_id'] = ($this->input->post('partner_id'))?$this->input->post('partner_id'):'';
		$products['product_type'] = ($this->input->post('product_type'))?$this->input->post('product_type'):'';
		$products['customer_part_no'] = ($this->input->post('customer_part_no'))?$this->input->post('customer_part_no'):'';
		$products['ink_1'] = ($this->input->post('ink_1'))?$this->input->post('ink_1'):'';
		$products['ink_2'] = ($this->input->post('ink_2'))?$this->input->post('ink_2'):'';
		$products['ink_3'] = ($this->input->post('ink_3'))?$this->input->post('ink_3'):'';
		$products['ink_4'] = ($this->input->post('ink_4'))?$this->input->post('ink_4'):'';
		$products['joint_type'] = ($this->input->post('joint_type'))?$this->input->post('joint_type'):'';
		$products['joint_details'] = ($this->input->post('joint_details'))?$this->input->post('joint_details'):'';
		$products['box_style'] = ($this->input->post('box_style'))?$this->input->post('box_style'):'';
		$products['rope_color'] = ($this->input->post('rope_color'))?$this->input->post('rope_color'):'';
		$products['pcs_bundle'] = ($this->input->post('pcs_bundle'))?$this->input->post('pcs_bundle'):'';
		$products['level'] = ($this->input->post('level'))?$this->input->post('level'):'';
		$products['p_width_mm'] = ($this->input->post('p_width_mm'))?$this->input->post('p_width_mm'):'';
		$products['p_width_inch'] = ($this->input->post('p_width_inch'))?$this->input->post('p_width_inch'):'';
		$products['qty_allowance'] = ($this->input->post('qty_allowance'))?$this->input->post('qty_allowance'):'';
		$products['scoreline_f'] = ($this->input->post('scoreline_f'))?$this->input->post('scoreline_f'):'';
		$products['scoreline_d'] = ($this->input->post('scoreline_d'))?$this->input->post('scoreline_d'):'';
		$products['scoreline_f2'] = ($this->input->post('scoreline_f2'))?$this->input->post('scoreline_f2'):'';
		$products['slit'] = ($this->input->post('slit'))?$this->input->post('slit'):'';
		$products['blank'] = ($this->input->post('blank'))?$this->input->post('blank'):'';
		$products['t_length'] = ($this->input->post('t_length'))?$this->input->post('t_length'):'';
		$products['cut'] = ($this->input->post('cut'))?$this->input->post('cut'):'';
		$products['next_process'] = ($this->input->post('next_process'))?$this->input->post('next_process'):'';
		$products['code_pd'] = ($this->input->post('code_pd'))?$this->input->post('code_pd'):'';
		$products['code_rd'] = ($this->input->post('code_rd'))?$this->input->post('code_rd'):'';
		$products['sketch'] = ($this->input->post('sketch'))?$this->input->post('sketch'):'';
		$products['sketch_large'] = ($this->input->post('sketch_large'))?$this->input->post('sketch_large'):'';
		$products['remark'] = ($this->input->post('remark'))?$this->input->post('remark'):'';
		$products['isdeleted'] 				= '0';
		$products['created_on'] 			= date("Y-m-d G:i:s");
		$products['created_by'] 			= $_SERVER['REMOTE_ADDR'];
		
		$productsall_0 = explode("|",$this->input->post('productsall_0'));
		$productsall_1 = explode("|",$this->input->post('productsall_1'));
		$productsall_2 = explode("|",$this->input->post('productsall_2'));
		
		$product_id = $this->Products_model->insertProduct($products);
		
		$product_data =  array();
		$pid =$productsall_0[0];
		$product_data = $this->productData($productsall_0);
		$product_data['parent_code'] = $products['product_code'];
		$this->Products_model->updateProductData($product_data,$pid);
		
		$pid =$productsall_1[0];
		$product_data = $this->productData($productsall_1);
		$product_data['parent_code'] = $products['product_code'];
		$this->Products_model->updateProductData($product_data,$pid);
		
		$pid =$productsall_2[0];
		$product_data = $this->productData($productsall_2);
		$product_data['parent_code'] = $products['product_code'];
		$this->Products_model->updateProductData($product_data,$pid);
		//never echo here 
		echo $product_id;
	}
	
	function updateDetail()
	{
		$products = array();
		$product_id 	= ($this->input->post('product_id'))?$this->input->post('product_id'):'0';
		if($product_id > 0 )
		{
			$products['product_code'] = ($this->input->post('product_code'))?$this->input->post('product_code'):'';
			$products['product_name'] = ($this->input->post('product_name'))?$this->input->post('product_name'):'';
			$products['partner_id'] = ($this->input->post('partner_id'))?$this->input->post('partner_id'):'';
			$products['product_type'] = ($this->input->post('product_type'))?$this->input->post('product_type'):'';
			$products['customer_part_no'] = ($this->input->post('customer_part_no'))?$this->input->post('customer_part_no'):'';
			$products['ink_1'] = ($this->input->post('ink_1'))?$this->input->post('ink_1'):'';
			$products['ink_2'] = ($this->input->post('ink_2'))?$this->input->post('ink_2'):'';
			$products['ink_3'] = ($this->input->post('ink_3'))?$this->input->post('ink_3'):'';
			$products['ink_4'] = ($this->input->post('ink_4'))?$this->input->post('ink_4'):'';
			$products['joint_type'] = ($this->input->post('joint_type'))?$this->input->post('joint_type'):'';
			$products['joint_details'] = ($this->input->post('joint_details'))?$this->input->post('joint_details'):'';
			$products['box_style'] = ($this->input->post('box_style'))?$this->input->post('box_style'):'';
			$products['rope_color'] = ($this->input->post('rope_color'))?$this->input->post('rope_color'):'';
			$products['pcs_bundle'] = ($this->input->post('pcs_bundle'))?$this->input->post('pcs_bundle'):'';
			$products['level'] = ($this->input->post('level'))?$this->input->post('level'):'';
			$products['p_width_mm'] = ($this->input->post('p_width_mm'))?$this->input->post('p_width_mm'):'';
			$products['p_width_inch'] = ($this->input->post('p_width_inch'))?$this->input->post('p_width_inch'):'';
			$products['qty_allowance'] = ($this->input->post('qty_allowance'))?$this->input->post('qty_allowance'):'';
			$products['scoreline_f'] = ($this->input->post('scoreline_f'))?$this->input->post('scoreline_f'):'';
			$products['scoreline_d'] = ($this->input->post('scoreline_d'))?$this->input->post('scoreline_d'):'';
			$products['scoreline_f2'] = ($this->input->post('scoreline_f2'))?$this->input->post('scoreline_f2'):'';
			$products['slit'] = ($this->input->post('slit'))?$this->input->post('slit'):'';
			$products['blank'] = ($this->input->post('blank'))?$this->input->post('blank'):'';
			$products['t_length'] = ($this->input->post('t_length'))?$this->input->post('t_length'):'';
			$products['cut'] = ($this->input->post('cut'))?$this->input->post('cut'):'';
			$products['next_process'] = ($this->input->post('next_process'))?$this->input->post('next_process'):'';
			$products['code_pd'] = ($this->input->post('code_pd'))?$this->input->post('code_pd'):'';
			$products['code_rd'] = ($this->input->post('code_rd'))?$this->input->post('code_rd'):'';
			$products['sketch'] = ($this->input->post('sketch'))?$this->input->post('sketch'):'';
			$products['sketch_large'] = ($this->input->post('sketch_large'))?$this->input->post('sketch_large'):'';
			$products['remark'] = ($this->input->post('remark'))?$this->input->post('remark'):'';
			$products['isdeleted'] 				= '0';
			$products['modified_on'] 			= date("Y-m-d G:i:s");
			$products['modified_by'] 			= $_SERVER['REMOTE_ADDR'];
			
			$productsall_0 = explode("|",$this->input->post('productsall_0'));
			$productsall_1 = explode("|",$this->input->post('productsall_1'));
			$productsall_2 = explode("|",$this->input->post('productsall_2'));
			
			$this->Products_model->updateProduct($products,$product_id);
			
			$product_data =  array();
			$pid =$productsall_0[0];
			$product_data = $this->productData($productsall_0);
			$product_data['parent_code'] = $products['product_code'];
			$this->Products_model->updateProductData($product_data,$pid);
			
			$pid =$productsall_1[0];
			$product_data = $this->productData($productsall_1);
			$product_data['parent_code'] = $products['product_code'];
			$this->Products_model->updateProductData($product_data,$pid);
			
			$pid =$productsall_2[0];
			$product_data = $this->productData($productsall_2);
			$product_data['parent_code'] = $products['product_code'];
			$this->Products_model->updateProductData($product_data,$pid);

		}
		else 
		{
			echo "Invalid Product ID : ".$product_id ;
		}
		
	}
	
	function deleteDetails()
	{
		$product_id = ($this->input->post('product_id'))?$this->input->post('product_id'):'0';
		if($product_id > 0)
		{
			$this->Products_model->deleteProduct($product_id);
		}
		else 
		{
			echo "Invalid Product ID : ".$product_id ;
		}
	}
	
	function search()
	{
		$searchkeyword = ($this->input->post('search'))?$this->input->post('search'):'';
		
		$data['searchkeyword'] = $searchkeyword;
		$page=($this->input->post('page'))?$this->input->post('page'):'0';
		$data['resultProducts'] = $this->Products_model->getLimitedNames($searchkeyword,$this->perPage(),$page);
		$data['totalRec'] = $this->Products_model->getTotalDataByCode($searchkeyword);
		$data['perPage'] = $this->perPage();
		$data['page'] = $page;
		$data['action'] = "search";
		$data['product_class'] = $this;
		$data['product_type'] =$searchkeyword;
		$this->load->view('products/productlist',$data);
	}
		
		
	// Highlight value based on basic search keywords
	function ew_Highlight($src, $bkw) {
		$outstr = "";
		if (strlen($src) > 0 && (strlen($bkw) > 0)) {
			$x=0;
			$wrky = stripos($src, $bkw);
			if ($wrky !== FALSE) {
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
	
	function fileUpload()
	{
		$productid_file=($this->input->post('productid_file'))?$this->input->post('productid_file'):'0';
		$fileName = $_FILES["photo-path"]["name"];
		$ext = substr($fileName, strrpos($fileName, '.') + 1);
		move_uploaded_file($_FILES["photo-path"]["tmp_name"], "files/" . $productid_file.".".$ext);
	    echo '{success:true, file:'.json_encode($productid_file.".".$ext).'}';
	}
	
	function fileUploadlarge()
	{
		$productid_file=($this->input->post('productid_file_large'))?$this->input->post('productid_file_large'):'0';
		$fileName = $_FILES["photo-path_large"]["name"];
		$ext = substr($fileName, strrpos($fileName, '.') + 1);
		move_uploaded_file($_FILES["photo-path_large"]["tmp_name"], "files/" . $productid_file."_Large.".$ext);
	    echo '{success:true, file:'.json_encode($productid_file."_Large.".$ext).'}';
	}
	
	function productSalesHistory($product_id)
	{
		
	}
}
?>