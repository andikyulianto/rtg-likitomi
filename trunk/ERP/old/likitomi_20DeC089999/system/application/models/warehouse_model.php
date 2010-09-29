<?php
class Warehouse_model extends Model 
{
	var $tableName 			= 'paper_rolldetails';
	var $tblPaperMovement 	= 'paper_movement';
	function Warehouse_model()
	{
		parent::Model();
	}
	
	function getAll()
	{
		//ToDO
		$this->db->limit(100);
		$query = $this->db->get($this->tableName);
		//echo $this->db->last_query();
		return $query;
	}
	
	function getAll_PaperMovementDate()
	{
		$sql= "SELECT DISTINCT date_format(created_on,'%Y-%m-%d') as movement_date FROM ".$this->tblPaperMovement;
		$query = $this->db->query($sql);
		return $query;
	}
	
	function getFilterResult($invoice_all,$papercode_all,$supplier_all,$invoicedate_all,$movement_all, $query_mode)
	{
		$filterQueryAll ="";
		$filter ="";
		$interColumnConjunction = " AND ";
		$sameColumnConjunction 	= " OR ";
		
		//Invoice
		for($i=0;$i<count($invoice_all);$i++)
		{
			if($i>0) $filter .= $sameColumnConjunction;
			$filter .= "invoice_no = '".$invoice_all[$i]."'";
		}
		if($filter!=""){
			if($filterQueryAll!="") $filterQueryAll .= $interColumnConjunction;
			$filterQueryAll .= "(".$filter.")";
		}
		
		//Paper Code
		$filter ="";
		for($i=0;$i<count($papercode_all);$i++)
		{
			if($i>0) $filter .= $sameColumnConjunction;
			$filter .= "paper_code = '".$papercode_all[$i]."'";
		}
		if($filter!=""){
			if($filterQueryAll!="") $filterQueryAll .= $interColumnConjunction;
			$filterQueryAll .= "(".$filter.")";
		}
		
		//Supplier
		$filter ="";
		for($i=0;$i<count($supplier_all);$i++)
		{
			if($i>0) $filter .= $sameColumnConjunction;
			$filter .= "supplier_id = '".$supplier_all[$i]."'";
		}
		if($filter!=""){
			if($filterQueryAll!="") $filterQueryAll .= $interColumnConjunction;
			$filterQueryAll .= "(".$filter.")";
		}
		
		//Invoice Date
		$filter ="";
		for($i=0;$i<count($invoicedate_all);$i++)
		{
			if($i>0) $filter .= $sameColumnConjunction;
			$filter .= "invoice_date = '".$invoicedate_all[$i]."'";
		}
		if($filter!=""){
			if($filterQueryAll!="") $filterQueryAll .= $interColumnConjunction;
			$filterQueryAll .= "(".$filter.")";
		}
		
		//Movement Date
		$filter ="";
		for($i=0;$i<count($movement_all);$i++)
		{
			if($i>0) $filter .= $sameColumnConjunction;
			$filter .= "date_format(created_on,'%Y-%m-%d') = '".$movement_all[$i]."'";
		}
		if($filter!=""){
			if($filterQueryAll!="") $filterQueryAll .= $interColumnConjunction;
			$filterQueryAll .= "(".$filter.")";
		}
		 
		//Final Query 
		if($filterQueryAll!="") {
			$filterQueryAll = " WHERE ".$filterQueryAll."";
		} 
		
		$sql = "SELECT * FROM ".$this->tableName.$filterQueryAll;
		
		/*Show History			
		if ($query_mode==0){
			$sql = "SELECT * FROM ".$this->tableName." AS pr LEFT JOIN "
			."(SELECT ".$this->tblPaperMovement.". *, max(created_on) as max_date from ".$this->tblPaperMovement."  GROUP BY roll_id) as pm "
			."ON pr.paper_roll_detail_id=pm.roll_id "
			.$filterQueryAll." ORDER BY pr.paper_code";
		}
		//Show No History
		else if($query_mode==1){
			$sql = "SELECT * FROM (SELECT * FROM ".$this->tableName.$filterQueryAll.") AS pr LEFT JOIN "
			."( SELECT * FROM ".$this->tblPaperMovement." ORDER BY `created_on` DESC ) AS pm "
			."ON pr.paper_roll_detail_id=pm.roll_id ORDER BY pr.paper_code";
		}
		*/
		
		$query = $this->db->query($sql);
		//echo $this->db->last_query();
		return $query;
	}
	
	function search($searchkeyword)
	{
		$this->db->select('paper_roll_detail_id,invoice_no,invoice_date');
		$this->db->where('isdeleted',0);
		if($searchkeyword!="")$this->db->like('invoice_no',$searchkeyword, 'both'); 
		$this->db->group_by('invoice_no');
		$this->db->order_by("invoice_date", "desc"); 	
		$this->db->limit(30);
		$query = $this->db->get($this->tableName);	
		//echo $this->db->last_query();	
		return $query->result();
	}
	
	function getDetails($invoice_no)
	{
		$this->db->where('invoice_no',$invoice_no);
		$query = $this->db->get($this->tableName);		
		return $query->result();
	}
	
	function insertWarehouseStock($supplier_id,$invoice_date,$invoice_no,$paper_code,$warehouse)
	{
		$supplier_roll_id 	= $warehouse[0];
		$size				= $warehouse[1];
		$unit				= $warehouse[2];
		$weight				= $warehouse[3];
		$remarks			= $warehouse[4];
		$rfidtagid			= $warehouse[5];
		
		for($i=0;$i<count($size);$i++){
			$data = array(
	               'paper_code' 		=> $paper_code,
				   'supplier_id'		=> $supplier_id,
				   'supplier_roll_id' 	=> $supplier_roll_id[$i],
				   'initial_weight'		=> $weight[$i],
				   'remarks'			=> $remarks[$i],
				   'size'				=> $size[$i],
				   'uom'				=> $unit[$i],
				   'rfid_roll_id'		=> $rfidtagid[$i],
				   'invoice_no'			=> $invoice_no,
				   'invoice_date'		=> $invoice_date,
				   'isdeleted'			=> '0',
				   'created_by'			=> $this->db_session->userdata('user_name'),
				   'created_on'			=> date("Y-m-d G:i:s"),
	            );
			$this->db->insert($this->tableName, $data); 
			//echo $this->db->last_query();
		}
		return count($size);
	}
	
	function deleteWarehouseStock($invoice_no)
	{
		$this->db->where('invoice_no', $invoice_no);
		$this->db->delete($this->tableName);
	}
	
	function getLatestWeight($rollid)
	{
		$sql =   " SELECT * FROM ".$this->tblPaperMovement." AS pm WHERE `movement_id` IN ( "
				." SELECT max( `movement_id` ) FROM ".$this->tblPaperMovement
				." WHERE `roll_id` = ".$rollid." )";
		$query = $this->db->query($sql);
		return $query;
	}
}
?>