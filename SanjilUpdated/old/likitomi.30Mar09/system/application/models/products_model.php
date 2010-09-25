<?php

class Products_model extends Model 
{
	var $tableName 		= "product_catalog";
	var $tblProducts 	= "products";
	var $tblSalesOrder 	= "sales_order";
	var $tblDelivery 	= "delivery";
	var $tblDHistory	= "delivery_history";

	function Products_model()
	{
		parent::Model();
	}
	
	function getTotalData()
	{
		$this->db->where('isdeleted',0);
		$this->db->from($this->tableName); 
		return $this->db->count_all_results();	
    }
	
	function getTotalDataBy($char)
	{
		$this->db->where('isdeleted',0);
		$this->db->like('lower(product_code)',strtolower($char), 'after'); 
		$this->db->from($this->tableName); 
		return $this->db->count_all_results();	
	}
	
	function getTotalDataByEndZero()
	{
		$this->db->where('isdeleted',0);
		$this->db->like('lower(product_code)','0', 'before'); 
		$this->db->from($this->tableName); 
		return $this->db->count_all_results();	
	}
	
	function getTotalDataByNotEndZero()
	{
		$this->db->where('isdeleted',0);
		$this->db->not_like('lower(product_code)','0', 'before'); 
		$this->db->from($this->tableName); 
		return $this->db->count_all_results();	
	}
	
	function getTotalTrash(){
		$this->db->where('isdeleted !=',0);
		$this->db->from($this->tableName); 
		return $this->db->count_all_results();
	}
	
	function getNames($char)
	{
		$this->db->where('isdeleted',0);
		if($char!='')
			$this->db->like('lower(product_code)',strtolower($char), 'after'); 
		$this->db->select('product_id,product_code,product_name');
		$this->db->order_by("lower(product_code)", "asc"); 	
		$query = $this->db->get($this->tableName);		
		return $query->result();
	}
	
	function getTotalDataByCode($code)
	{
		$this->db->where('isdeleted',0);
		$this->db->like('lower(product_code)',strtolower($code), 'after'); 
		$this->db->from($this->tableName); 
		return $this->db->count_all_results();	
	}
	
	function getLimitedByType($type,$offset,$limit){
		
		if($type=='Trash') $this->db->where('isdeleted !=',0);
		else $this->db->where('isdeleted',0);
		
		$this->db->select('product_id,product_code,product_name');
		if($type=='Outer') $this->db->like('lower(product_code)','0', 'before'); 
		else if($type=='Inner') $this->db->not_like('lower(product_code)','0', 'before'); 
		$this->db->select('product_id,product_code');
		$this->db->order_by("lower(product_code)", "asc"); 	
		$query = $this->db->get($this->tableName,$offset,$limit);
		return $query->result();
		
	}
	function getLimitedNames($code,$limit,$offset)
	{
		$this->db->where('isdeleted',0);
		$this->db->select('product_id,product_code,product_name');
		if($code!='')
			$this->db->like('lower(product_code)',strtolower($code), 'after'); 
		$this->db->select('product_id,product_code');
		$this->db->order_by("lower(product_code)", "asc"); 	
		$query = $this->db->get($this->tableName,$limit,$offset);
		return $query->result();
	}

	function getDetails($product_id)
	{
		$this->db->where('product_id',$product_id);
		$query = $this->db->get($this->tableName);
		return $query->row();
	}
	
	function getProductLine($product_code){
		$this->db->where('isdeleted',0);
		$this->db->where('lower(product_code)',strtolower($product_code));
		$this->db->where('lower(parent_code)',strtolower($product_code));
		$query = $this->db->get($this->tblProducts);
		return $query->row();
	}
	
	function getSalesOrder($sales_order_id)
	{
		$this->db->where('sales_order_id',$sales_order_id);
		$query = $this->db->get($this->tblSalesOrder);
		return $query;
	}
	
	function getProductDetails($parent_code)
	{
		$this->db->where('isdeleted',0);
		$this->db->where('parent_code',$parent_code);
		$query = $this->db->get($this->tblProducts);
		return $query->result();
	}
	
	function getProductDelivey($sales_order_id)
	{
		$this->db->where('sales_order',$sales_order_id);
		$query = $this->db->get($this->tblDelivery);
		return $query;
	}
	
	function getProducts($product_id){
		//$this->db->where('isdeleted',0); //also display deleted products
		$this->db->select('product_id,product_code');
		$this->db->where('product_id',$product_id);
		$query = $this->db->get($this->tableName);
		$row = $query->row();
		$this->db->where('isdeleted',0);
		$this->db->where('parent_code',$row->product_code);
		$query = $this->db->get($this->tblProducts);
		return $query->result();
	}
	
	function insertProduct($products)
	{
		$this->db->trans_start();
		$this->db->insert($this->tableName, $products); 
		
		$product_id = $this->db->insert_id();
		
		$this->db->trans_complete();	
		if ($this->db->trans_status() === FALSE)
		{
			log_message('debug', 'Problem Inserting Products');
			show_error('Please notify support with transaction details');
			return "Failed";		
		}
		return $product_id;
	}
	
	function updateProduct($products,$product_id)
	{
		$this->db->trans_start();
		$this->db->where('product_id', $product_id);
		$this->db->update($this->tableName, $products); 
		
		$this->db->trans_complete();	
		if ($this->db->trans_status() === FALSE)
		{
			log_message('debug', 'Problem Inserting Products');
			show_error('Please notify support with transaction details');
			return "Failed";		
		}
		return "Success";
	}
	
	function updateProductData($products_item,$pid)
	{	
		echo $pid;
		if($products_item['product_code'] != "") 
		{
			if($pid>0)
			{
				$products_item['modified_on'] 	= date("Y-m-d G:i:s");
				$products_item['modified_by']	= $_SERVER['REMOTE_ADDR'];
				$this->db->where('auto_pid', $pid);
				$this->db->update($this->tblProducts, $products_item); 	
				//echo $this->db->last_query();
				return "Success";
			}
			else 
			{
				$products_item['created_on'] 	= date("Y-m-d G:i:s");
				$products_item['created_by']	= $_SERVER['REMOTE_ADDR'];
				$this->db->insert($this->tblProducts, $products_item);	
				//echo $this->db->last_query();
				return "Failure";
			}
		}
		else 
		{
			if($pid>0)
			{
				$param = array(	"isdeleted" => 1,
								"modified_on" => date("Y-m-d G:i:s"),
								"modified_by" => $_SERVER['REMOTE_ADDR'],
							);
				$this->db->where('auto_id', $pid);
				$this->db->update($this->tblProducts, $param); 
				//echo $this->db->last_query();
				return "Success";
			}
		}
	}
	
	function deleteProduct($product_id){
		echo $product_id;
		$param = array("isdeleted" => 1);
		$this->db->where('product_id',$product_id);
		$this->db->update($this->tableName,$param);
		echo $this->db->last_query();
	}
	
	function search($searchkeyword)
	{
		$this->db->where('isdeleted',0);
		$this->db->select('product_id,product_code');
		$this->db->like('lower(product_code)',strtolower($searchkeyword), 'both'); 
		$this->db->order_by("lower(product_code)", "asc"); 	
		$query = $this->db->get($this->tableName);		
		return $query->result();
	}
	
	function insertSalesOrder($sales){
		$this->db->trans_start();
		$this->db->insert($this->tblSalesOrder, $sales); 		
		$sales_order = $this->db->insert_id();
		$this->db->trans_complete();	
		//echo $this->db->last_query(); 
		if ($this->db->trans_status() === FALSE)
		{
			log_message('debug', 'Problem Inserting Sales Order');
			return "0";		
		}
		return $sales_order;
	}
	
	function getSaleDetails($sales_order_id)
	{
		$this->db->where('sales_order_id',$sales_order_id);
		$query = $this->db->get($this->tblSalesOrder);
		return $query->row();
	}
	
	function getAllSaleTotal($product_id)
	{
		$this->db->where('product_id',$product_id);
		$this->db->from($this->tblSalesOrder); 
		return $this->db->count_all_results();	
	}
	
	function getAllSaleDetails($product_id,$offset)
	{
		$limit=1;
		$this->db->where('product_id',$product_id);
		$this->db->order_by('sales_order_id', 'desc'); 	
		$query = $this->db->get($this->tblSalesOrder,$limit,$offset);
		//echo $this->db->last_query(); 
		return $query->row();		
	}
	
	function saveDelivery($delivery)
	{
		$this->db->insert($this->tblDelivery, $delivery); 
		$delivery_id = $this->db->insert_id();
		//never echo here 
		return $delivery_id;
	}
	
	function deleteDelivery($delivery_id)
	{
		$this->db->where('delivery_id',$delivery_id);
		$this->db->delete($this->tblDelivery);
		echo $this->db->last_query(); 
	}
	
	function getDeliveryList($product_id,$sales_order)
	{
		$this->db->where('product_id',$product_id);
		$this->db->where('sales_order',$sales_order);
		$query = $this->db->get($this->tblDelivery);
		return $query;
	}
	
	function inlineEditDelivery($delivery_id,$field,$newvalue,$original)
	{
		$param = array(	"delivery_id" => $delivery_id,
						"field" => $field,
						"from" 	=> $original,
						"to" 	=> $newvalue,
						"state" => 'changed',
						"created_on" => date("Y-m-d G:i:s"),
						"created_by" => $_SERVER['REMOTE_ADDR'],
					);
		$this->db->insert($this->tblDHistory, $param); 
	}
	
	function updateDelivery($delivery_id,$idname,$newvalue,$original)
	{
		$this->db->where('delivery_id',$delivery_id);
		$param = array($idname => $newvalue,"status"=>"updated");
		$this->db->update($this->tblDelivery, $param);
	}
	
	function inlineEditSales($sales_order_id,$field,$newvalue)
	{
		$this->db->where("sales_order_id",$sales_order_id);
		$param = array(	$field => $newvalue,
						"modified_on" => date("Y-m-d G:i:s"),
						"modified_by" => $_SERVER['REMOTE_ADDR'],
					);
		$this->db->update($this->tblSalesOrder, $param); 
		//echo $this->db->last_query();
	}
	
	function productSalesHistory($product_id)
	{
		$sql = 	 "SELECT pc.product_id, so.sales_order_id, d.product_code, d.delivery_date, d.qty, d.delivered_qty,d.total_production_qty, d.damaged_qty, status "
				."FROM product_catalog pc, sales_order so, delivery d "
				."WHERE pc.product_id='".$product_id."'"
				."AND pc.product_id=so.product_id "
				."AND so.product_id=d.product_id "
				."AND so.sales_order_id=d.sales_order "
				."ORDER BY  d.product_code, so.sales_order_id DESC limit 50";
		$query = $this->db->query($sql);
		return $query;
	}
}

?>
