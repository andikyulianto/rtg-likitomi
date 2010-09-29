<?php
class SalesOrder extends Controller {
	
	function __construct() 
	{
		parent::Controller();
		$this->freakauth_light->check();
		$this->lang->load('products', 'english');
		$this->load->database();
		$this->load->model('Products_model');
	}
		
	function index()
	{
		$data = array(
	      'contentClass' => $this,
	      'title' => "Sales Order",
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
		$script .= '<script type="text/javascript" src="'.base_url().'static/javascript/products.js"></script>';
		return $script;
	}
	
	function getStyles()
	{
		$styles  ='@import "'.base_url().'static/css/common.css";';
		$styles	.='@import "'.base_url().'resources/css/ext-all.css";';		
		$styles .='@import "'.base_url().'resources/css/xtheme-gray.css";';
		$styles	.='@import "'.base_url().'static/css/salesorder.css";';
		return $styles;
	}
	
	function show()
	{
		$this->load->view('salesorder/salesorder');
	}
	
	function getDetails()
	{
		$product_id = ($this->input->post('product_id'))?$this->input->post('product_id'):'0';
		$data['action'] = ($this->input->post('action'))?$this->input->post('action'):'view';
		if($product_id > 0 )
		{
			$data['resultProductCatalog'] 	= $this->Products_model->getDetails($product_id);
			$this->load->model('Partners_model');
			$customerInfo 			= $this->Partners_model->getCustomerInfo($data['resultProductCatalog']->partner_id);
			$data['customer_name']			= $customerInfo->partner_name;
			$data['billing_address']		= $customerInfo->partner_billing_address;	
			$data['partner_isdeleted']		= $customerInfo->isdeleted;
			$data['resultProducts'] 		= $this->Products_model->getProducts($product_id);
			$data['deliveryAddresses']		= $this->Partners_model->getAddresses($data['resultProductCatalog']->partner_id);
			$data['resultParnters']=$this->Partners_model->getNames('Customer');
			$data['thisClass']		= $this;
			$data['product_id']		= $product_id;
			$this->load->view('salesorder/salesorderdiv', $data);
		}
		else 
		{
			echo "Invalid Product ID : ".$product_id ;
		}
	}
	
	function getCumulativeStock($product_id,$product_code)
	{
		$this->load->model('Salesorder_model');
		$data['stockDetails']	= $this->Salesorder_model->getStock($product_id,$product_code);
		$cumulativeStock=0;
		foreach ($data['stockDetails']->result() as $resultStock )
		{
			$stock = $resultStock->total_production_qty -($resultStock->delivered_qty +$resultStock->damaged_qty);
			$cumulativeStock +=$stock;
		}
		return $cumulativeStock;		
	}
	function reportCatalog($product_id)
	{
		$data['resultProductCatalog'] 	= $this->Products_model->getDetails($product_id);
		$product_code = $data['resultProductCatalog']->product_code;
		$this->load->model('Partners_model');
		$customerInfo = $this->Partners_model->getCustomerInfo($data['resultProductCatalog']->partner_id);
		$data['customer_name']		= $customerInfo->partner_name;
		$data['numSales'] = 0;
		$data['productDetails'] = $this->Products_model->getProductDetails($product_code);
		$data['numDelivery'] =0;
		
		$this->load->view('salesorder/reportsalesorder',$data);
	}
	
	function reportSalesOrder($sales_order_id)
	{
		$data['resultSalesOrder'] 	= $this->Products_model->getSalesOrder($sales_order_id);
		$data['numSales']			= $data['resultSalesOrder']->num_rows();
		$product_id 				= $data['resultSalesOrder']->row()->product_id;
		
		$data['resultProductCatalog'] 	= $this->Products_model->getDetails($product_id);
		$product_code 				= $data['resultProductCatalog']->product_code;
		
		$this->load->model('Partners_model');
		$customerInfo = $this->Partners_model->getCustomerInfo($data['resultProductCatalog']->partner_id);
		$data['customer_name']		= $customerInfo->partner_name;

		$data['productDetails'] = $this->Products_model->getProductDetails($product_code);
		$data['productDelivery']= $this->Products_model->getProductDelivey($sales_order_id);
		$data['numDelivery'] 	= $data['productDelivery']->num_rows();
		
		$this->load->view('salesorder/reportsalesorder',$data);
	}
	
	function createSalesOrderPage()
	{
		$product_id = ($this->input->post('product_id'))?$this->input->post('product_id'):'0';
		$data['action'] = ($this->input->post('action'))?$this->input->post('action'):'view';
		if($product_id > 0 )
		{
			$data['resultProductCatalog'] 	= $this->Products_model->getDetails($product_id);
			$this->load->model('Partners_model');
			$customerInfo 			= $this->Partners_model->getCustomerInfo($data['resultProductCatalog']->partner_id);
			$data['customer_name']			= $customerInfo->partner_name;
			$data['billing_address']		= $customerInfo->partner_billing_address;	
			$data['partner_isdeleted']		= $customerInfo->isdeleted;
			$data['resultProducts'] 		= $this->Products_model->getProducts($product_id);
			$data['deliveryAddresses']		= $this->Partners_model->getAddresses($data['resultProductCatalog']->partner_id);
			$data['resultParnters']=$this->Partners_model->getNames('Customer');
			$data['thisClass']		= $this;
			$data['product_id']		= $product_id;
			$this->load->view('salesorder/createsalesorder',$data);
		}
		else 
		{
			echo "Invalid Product ID : ".$product_id ;
		}
		
	}
	
	function addSalesOrder()
	{
		$sales['product_id'] 		= ($this->input->post('product_id'))?$this->input->post('product_id'):'0';
		$sales['delivery_at'] 		= ($this->input->post('delivery_at'))?$this->input->post('delivery_at'):'';
		$sales['purchase_order_no']	= ($this->input->post('purchase_order_no'))?$this->input->post('purchase_order_no'):'';
		$sales['remarks']			= ($this->input->post('remarks'))?$this->input->post('remarks'):'';
		$productAll = explode("|",$this->input->post('productCodes'));
		$cnt=1;
		for($i=0;$i<(count($productAll)-1);$i+=2){
			$sales['product_code_'.$cnt]  = $productAll[$i];
			$sales['amount_'.$cnt] = $productAll[$i+1];
			$cnt=($cnt>4)?$cnt=4:$cnt+1;
		}
		$sales['sales_order_date']	= date("Y-m-d");
		$sales['created_on'] 		= date("Y-m-d G:i:s");
		$sales['created_by'] 		= $_SERVER['REMOTE_ADDR'];
		//print_r($sales);
		$sales_order_id = $this->Products_model->insertSalesOrder($sales);
		$this->loadSalesOrder();
	}
	
	function editSalesOrder()
	{
		$sales['sales_order_id'] 	= ($this->input->post('sales_order_id'))?$this->input->post('sales_order_id'):'0';
		$sales['action'] 			= ($this->input->post('action'))?$this->input->post('action'):'edit';;
		$salesOrder					= $this->Products_model->getSalesOrder($sales['sales_order_id']);
		if($salesOrder->num_rows()>0) 
		{
			$sales['resultSalesOrder'] = $salesOrder->row();
			$product_id	= $salesOrder->row()->product_id;
			$sales['resultProductCatalog'] 	= $this->Products_model->getDetails($product_id);
			$this->load->model('Partners_model');
			$customerInfo 			= $this->Partners_model->getCustomerInfo($sales['resultProductCatalog']->partner_id);
			$sales['customer_name']			= $customerInfo->partner_name;
			$sales['billing_address']		= $customerInfo->partner_billing_address;	
			$sales['resultProducts'] 		= $this->Products_model->getProducts($product_id);
			$sales['deliveryAddresses']		= $this->Partners_model->getAddresses($sales['resultProductCatalog']->partner_id);
				
			$this->load->view('products/salesordercontent',$sales);	
		}
		else {
			echo "Invalid sales order id : ".$sales_order_id;
		}
	}
	
	function loadSalesOrder()
	{
		$product_id	= ($this->input->post('product_id'))?$this->input->post('product_id'):'0';
		$page=($this->input->post('page'))?$this->input->post('page'):'0';
		
		$data['resultSales'] = $this->Products_model->getAllSaleDetails($product_id,$page);
		$data['page']		= $page;
		$data['totalRec']	= $this->Products_model->getAllSaleTotal($product_id);
		if($data['totalRec']>0)
		{
			$data['deliveryLists'] 		= $this->Products_model->getDeliveryList($product_id,$data['resultSales']->sales_order_id);
			$data['totalRecDelivery']	= $data['deliveryLists']->num_rows();
			$this->load->model('Salesorder_model');
			$data['salesClass']			= $this->Salesorder_model;
			$this->load->view('salesorder/reviewsalesorder',$data);		
		} else 
		{
			$this->load->view('salesorder/nullsalesorder');	
		}
		
	}
	
	function saveDelivery()
	{	
		$delivery['product_id']	= ($this->input->post('product_id'))?$this->input->post('product_id'):'0';
		$delivery['product_code']	= ($this->input->post('product_code'))?$this->input->post('product_code'):'';
		$delivery['delivery_time']	= ($this->input->post('delivery_time'))?$this->input->post('delivery_time'):'';
		$delivery['delivery_date']	= ($this->input->post('delivery_date'))?date("Y-m-d",strtotime($this->input->post('delivery_date'))):'';
		$delivery['qty']			= ($this->input->post('qty'))?$this->input->post('qty'):'';
		$delivery['sales_order']	= ($this->input->post('sales_order'))?$this->input->post('sales_order'):'';
		$delivery['status']			= "new";
		$delivery['created_on'] 	= date("Y-m-d G:i:s");
		$delivery['created_by'] 	= $_SERVER['REMOTE_ADDR'];
		$delivery['modified_on'] 	= date("Y-m-d G:i:s");
		$delivery['modified_by'] 	= $_SERVER['REMOTE_ADDR'];
		$delivery_id = $this->Products_model->saveDelivery($delivery);
		echo $delivery_id;
		//never echo here
	}
	
	function deleteDelivery()
	{
		$delivery_id	= ($this->input->post('delivery_id'))?$this->input->post('delivery_id'):'0';
		$this->Products_model->deleteDelivery($delivery_id);
	}
	
	function inlineedit()
	{
		$delivery_id	= ($this->input->post('delivery_id'))?$this->input->post('delivery_id'):'0';
		$id				= ($this->input->post('id'))?$this->input->post('id'):'0';
		$original		= ($this->input->post('original'))?$this->input->post('original'):'';
		$newvalue		= ($this->input->post('newvalue'))?$this->input->post('newvalue'):'';
		$idname = ""; $field ="";
		switch($id)
		{
			case 3: $idname="delivery_date"; 
					$field="Date"; 
					$original =date("Y-m-d",strtotime($original));
					$newvalue =date("Y-m-d",strtotime($newvalue));
					break;
			case 4: $idname="delivery_time"; 
					$field="Time"; 
					break;
			case 5: $idname="qty"; $field="Quantity"; break;
		}
		
		$this->Products_model->inlineEditDelivery($delivery_id,$field,$newvalue,$original);
		$this->Products_model->updateDelivery($delivery_id,$idname,$newvalue,$original);
		echo 'Today: '.date("G:i").' - <span style="color:blue">'.$field.
			'</span> changed from <span style="color:red">'.date("d-m-Y",strtotime($original)).
			'</span> to <span style="color:green">'.date("d-m-Y",strtotime($newvalue)).
			'</span> ';	
	}
	
	function inlineeditsales()
	{
		$sales_order_id	= ($this->input->post('sales_order_id'))?$this->input->post('sales_order_id'):'0';
		$field			= ($this->input->post('field'))?$this->input->post('field'):'';
		$newvalue		= ($this->input->post('newvalue'))?$this->input->post('newvalue'):'';
		$this->Products_model->inlineEditSales($sales_order_id,$field,$newvalue);	
	}
}
?>