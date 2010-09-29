<?php
class Clamplift_model extends Model 
{
	var $tableName = 'tbl_clamplift';
	var $tblSync	= 'sync_clamplift';
	var $DB1;
	function Clamplift_model()
	{
		parent::Model();
		$this->load->database();
		//$this->DB1 = $this->load->database('driver1', TRUE); 
	} 
	
	function getTaskByDate($filterdate)
	{
		$this->db->where('opdate', $filterdate);
		$query = $this->db->get($this->tableName);
		return $query;
	}
	
	function getNextTask($id,$date,$limit){	
		$this->db->where('date', $date); 
		$query = $this->db->get($this->tableName);
		$offset=0;
		$boolflag=1;
		foreach ($query->result() as $row){
			if($row->id==$id){
				$boolflag=0;
			}else {
				if($boolflag==1) $offset++;
			}
		}
		
		$this->db->like('opdate', $date, "both");  
		$query = $this->db->get($this->tableName,$limit,$offset);
		//echo $this->db->last_query(); 
		return $query;
	}
	
	function getNextUse($id,$code,$date,$limit){	
		$this->db->where('date', $date); 
		$this->db->where("(DF = '$code' OR BM = '$code' OR BL = '$code' OR CM = '$code' OR CL = '$code')");
		$query = $this->db->get($this->tableName);
		$offset=0;
		$boolflag=1;
		foreach ($query->result() as $row){
			if($row->id==$id){
				$boolflag=0;
			}else {
				if($boolflag==1) $offset++;
			}
		}
		
		$this->db->where('date', $date); 
		$this->db->where("(DF = '$code' OR BM = '$code' OR BL = '$code' OR CM = '$code' OR CL = '$code')");	
		 
		$query = $this->db->get($this->tableName,$limit,$offset);
		//echo $this->db->last_query(); 
		return $query;
	}
	
	function getPaperByStatus($date,$statusid)
	{
		$this->db->where('date', $date); 
		$this->db->where('status !=','00000');
		$query = $this->db->get($this->tableName);
		$RowCnt=0;
		$taskTable = array();
		foreach ($query->result() as $row)
		{
			if((substr($row->status,0,1)==$statusid) || 
				(substr($row->status,1,1)==$statusid) || 
				(substr($row->status,2,1)==$statusid) || 
				(substr($row->status,3,1)==$statusid) || 
				(substr($row->status,4,1)==$statusid)) 
			{
				$status = $row->status;
			
				$taskTable[$RowCnt]= array();
				$taskTable[$RowCnt]['time']  = substr($row->start,0,5);
				$taskTable[$RowCnt]['rowDF'] = $row->id.'|'.$row->DF.'|'.$status.'|'.$row->pono;
				$taskTable[$RowCnt]['rowBM'] = $row->id.'|'.$row->BM.'|'.$status.'|'.$row->pono;
				$taskTable[$RowCnt]['rowBL'] = $row->id.'|'.$row->BL.'|'.$status.'|'.$row->pono;
				$taskTable[$RowCnt]['rowCM'] = $row->id.'|'.$row->CM.'|'.$status.'|'.$row->pono;
				$taskTable[$RowCnt]['rowCL'] = $row->id.'|'.$row->CL.'|'.$status.'|'.$row->pono;	
				$RowCnt++;
			}
		}
		return $taskTable;
		
	}
	
	function paperPick($id){
		$this->db->where('id', $id); 
		$query = $this->db->get($this->tableName);
		return $query->row();
	}
	
	//Manager Portion
	/*
	function getRemoteData($today)
	{
		$this->DB1->where('opdate',$today); 
		$query = $this->DB1->get($this->tableName);
		//echo $this->DB1->last_query();
		return $query;
	}
	*/
	
	function getLocalData($today)
	{
		$this->db->where('opdate',$today); 
		$query = $this->db->get($this->tableName);
		return $query;
	}
	
	function deleteOnly($today)
	{
		$this->db->where('opdate',$today); 
		$this->db->delete($this->tableName);
		echo "Deleted Successfully";
	}
	
	function deleteAndAdd($gridData,$today)
	{
		$this->db->trans_start();
		$this->db->where('opdate',$today); 
		$this->db->delete($this->tableName);

		foreach($gridData as $rowData)
		{
			if($rowData->product_code!="")
			{
				$prod = $this->getProductForClamplift($rowData->product_code);
			} else {
				$prod = $rowData;	
			}
			//$prod = $rowData; //Why I need this ?
			$param = array( "opdate" => $today,
					"start_time" => $rowData->start_time,
					"stop_time" => $rowData->stop_time,
					"product_code" => $prod->product_code,
					"product_name" => $prod->product_name,			
					"partner_name" => $prod->partner_name,
					"sales_order" => $rowData->sales_order,
					"autoid" => $rowData->autoid,
					"flute" => $rowData->flute,
					"DF" => $rowData->DF,
					"BL" => $rowData->BL,
					"CL" => $rowData->CL,
					"BM" => $rowData->BM,
					"CM" => $rowData->CM,
					
					"p_width_mm" => $rowData->p_width_mm,
					"p_width_inch" => $rowData->p_width_inch,
					"used_df" => $rowData->used_df,
					"used_bl" => $rowData->used_bl,
					"used_cl" => $rowData->used_cl,
					"used_bm" => $rowData->used_bm,
					"used_cm" => $rowData->used_cm,
					
					"used_df_lkg" => $rowData->used_df_lkg,
					"used_bl_lkg" => $rowData->used_bl_lkg,
					"used_cl_lkg" => $rowData->used_cl_lkg,
					"used_bm_lkg" => $rowData->used_bm_lkg,
					"used_cm_lkg" => $rowData->used_cm_lkg,
					
					"used_df_mkg" => $rowData->used_df_mkg,
					"used_bl_mkg" => $rowData->used_bl_mkg,
					"used_cl_mkg" => $rowData->used_cl_mkg,
					"used_bm_mkg" => $rowData->used_bm_mkg,
					"used_cm_mkg" => $rowData->used_cm_mkg,
					
					
					"t_length" => $rowData->t_length,
					"case" => $rowData->case,
					"cut" => $rowData->cut,
				);
					
			$this->db->insert($this->tableName, $param);
		}
		$this->db->trans_complete();	
		if ($this->db->trans_status() === FALSE)
		{
			echo " ERROR: COULDN'T SAVE DATA ";	
		}
		echo "Data Saved for".$today;
	}
	
	function getProductForClamplift($product_code)
	{
		$sql = 	 "SELECT pc.product_id, pc.product_code, pc.product_name, p.partner_name "
				."FROM ( "
				."SELECT * FROM `product_catalog` WHERE product_code = '".$product_code."' "
				." ) AS pc "
				."LEFT JOIN partners p ON pc.partner_id = p.partner_id";
		$query = $this->db->query($sql);
		return $query->row();
	}
	
	function getSyncTime($opdate)
	{
		$this->db->where('opdate', $opdate);
		$this->db->order_by("id", "desc"); 
		$query = $this->db->get($this->tblSync);
		return $query;
	}
/*	function saveData($rowData,$choosendate)
	{	
		$param = array( "opdate" => $choosendate,
			"delivery_id" => $rowData->delivery_id,
			"corrugator_date" => substr($rowData->corrugator_date,0,10)." ".$rowData->corrugator_time.":00",
			"converter_date" => substr($rowData->converter_date,0,10)." ".$rowData->converter_time.":00");
		$this->db->insert($this->totalPlanning, $param);
		echo $this->db->last_query();
	}
*/
}

?>
