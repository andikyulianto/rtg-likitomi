<?php

class Partners_model extends Model 
{
	var $tableName = "partners";
	var $tblAddress = "addresses";
	var $tblProductCatalog = "product_catalog";
	
	function Partners_model()
	{
		parent::Model();
	}
	
	function getTotalData()
	{
		$this->db->where('isdeleted',0);
		//return $this->db->count_all($this->tableName);
		$this->db->from($this->tableName); 
		return $this->db->count_all_results();	
    }
	
	function getTotalByType($type)
	{
		$this->db->where('isdeleted',0);
		$this->db->where('partner_type',$type);
		$this->db->from($this->tableName); 
		return $this->db->count_all_results();	
	}
	
	function getTotalTrash(){
		$this->db->where('isdeleted !=',0);
		$this->db->from($this->tableName); 
		return $this->db->count_all_results();
	}
	
	function getNames($type)
	{
		if($type=='Trash') $this->db->where('isdeleted !=',0);
		else $this->db->where('isdeleted',0);
		if(($type=='Customer') || ($type=='Supplier'))
			$this->db->where('partner_type',$type);
		$this->db->select('partner_id,partner_name');
		$this->db->order_by("lower(partner_name)", "asc"); 	
		$query = $this->db->get($this->tableName);		
		return $query->result();
	}

	function getDetails($id)
	{
		$this->db->where('partner_id',$id);
		$query = $this->db->get($this->tableName);		
		return $query->row();
	}
	
	function insertPartner($partners)
	{
		$this->db->trans_start();
		$this->db->insert($this->tableName, $partners); 
		
		$partner_id = $this->db->insert_id();
		
		$this->db->trans_complete();	
		if ($this->db->trans_status() === FALSE)
		{
			log_message('debug', 'Problem Inserting Partners');
			show_error('Please notify support with transaction details');
			return "Failed";		
		}
		return $partner_id;
	}
	
	function updatePartner($partners,$partner_id)
	{
		$this->db->trans_start();
		$this->db->where('partner_id', $partner_id);
		$this->db->update($this->tableName, $partners); 
		
		$this->db->trans_complete();	
		if ($this->db->trans_status() === FALSE)
		{
			log_message('debug', 'Problem Inserting Partners');
			show_error('Please notify support with transaction details');
			return "Failed";		
		}
		return "Success";
	}
	
	function getPartnerAddresses($id)
	{
		$this->db->where('partner_id',$id);
		$this->db->where('isdeleted',0);
		$query = $this->db->get($this->tblAddress);		
		return $query->result();
	}
	
	function insertAddresses($partner_id,$addresses)
	{
		$now = date("Y-m-d G:i:s"); 
		for($i=0;$i<count($addresses)-1;$i++)
		{
			if($addresses[$i] != "")
			{
				$param = array("partner_id"=>$partner_id,
							"address" => $addresses[$i],
							"isdeleted" => 0, 
							"created_on" => $now,
							"modified_on" => $now,
							"created_by" => $_SERVER['REMOTE_ADDR']);	
				$this->db->insert($this->tblAddress,$param);
			}
		}
	}
	
	function updateAddresses($partner_id,$addresses,$addresseids)
	{
		$now = date("Y-m-d G:i:s");
		$this->db->where('partner_id',$partner_id);
		$param = array("isdeleted" => 1);
		$this->db->update($this->tblAddress,$param);
		for($i=0;$i<count($addresseids)-1;$i++)
		{
			if($addresseids[$i]>0)
			{
				$param = array("address" => $addresses[$i],
								"isdeleted" => 0, 
								"modified_on" => $now,
								"modified_by" => $_SERVER['REMOTE_ADDR']);	
				$this->db->where('partner_id',$partner_id);
				$this->db->where('address_id',$addresseids[$i]);
				$this->db->update($this->tblAddress,$param);
			}
			else 
			{
				$param = array("partner_id"=>$partner_id,
							"address" => $addresses[$i],
							"isdeleted" => 0, 
							"created_on" => $now,
							"modified_on" => $now,
							"created_by" => $_SERVER['REMOTE_ADDR']);	
				$this->db->insert($this->tblAddress,$param);
			}
			echo $this->db->last_query();
		}
	}
	
	function deletePartner($partner_id){
		$param = array("isdeleted" => 1);
		$this->db->where('partner_id',$partner_id);
		$this->db->update($this->tableName,$param);
	}
	
	function search($searchkeyword)
	{
		$this->db->select('partner_id,partner_name');
		$this->db->where('isdeleted',0);
		$this->db->like('lower(partner_name)',strtolower($searchkeyword), 'both'); 
		$this->db->order_by("lower(partner_name)", "asc"); 	
		$query = $this->db->get($this->tableName);		
		return $query->result();
	}
	
	function getAutoFillNamesArray($type,$limit,$queryString){
		$items = array();
		$this->db->select('partner_id,partner_name');	
		$this->db->where('partner_type',$type);
		$this->db->like('lower(partner_name)',strtolower($queryString), 'after');
		$this->db->limit($limit); 
		$res = $this->db->get($this->tableName);
		
		if ($res->num_rows() > 0) 
		{	
			$count = 0;
			foreach ($res->result() as $item) {		
				foreach ($item as $key => $value) {
					$items[$count][$key] = $value;
				}
				$count++;
			}
		} 		
		return $items;
	}
	
	function listProducts($partner_id){
		$this->db->select('product_id,partner_id,product_code,product_name');
		$this->db->where('partner_id',$partner_id);
		$query = $this->db->get($this->tblProductCatalog);		
		return $query->result();
	}
	
	function listProductscnt($partner_id){
		$this->db->select('product_id');
		$this->db->where('partner_id',$partner_id);
		$this->db->from($this->tblProductCatalog); 
		return $this->db->count_all_results();	
	}
	
	function getCustomerInfo($partner_id)
	{
		$this->db->select('partner_name,partner_billing_address,isdeleted');
		//$this->db->where('isdeleted',0);
		$this->db->where('partner_id',$partner_id);
		$query = $this->db->get($this->tableName);
		return $query->row();
	}
	
	function getAddresses($partner_id)
	{
		$this->db->where('isdeleted',0);
		$this->db->where('partner_id',$partner_id);
		$query = $this->db->get($this->tblAddress);
		return $query;
	}

	function getNamesById($partner_id)
	{
		$this->db->where('partner_id',$partner_id);
		$this->db->select('partner_id,partner_name');
		$query = $this->db->get($this->tableName);		
		//echo $this->db->last_query();
		return $query->row();
	}

}

?>
