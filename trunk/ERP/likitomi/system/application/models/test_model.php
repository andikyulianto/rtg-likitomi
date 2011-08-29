<?php
class Test_model extends Model 
{

	var $status 	= "status_tracking";
	var $product 	= "product_catalog";

	function Test_model()
	{
		parent::Model();
	}
	
	function getAllStatus()
	{
		//ToDO
		//Data is limited for efficency.
		$this->db->order_by("plan_id", "desc"); 
		$this->db->limit(130);
		$query = $this->db->get($this->status);
		//echo $this->db->last_query();	
		return $query;
	
	}
	function getTime($date)
	{
		$sql = 	 "SELECT * FROM ".$this->status." WHERE date ='".$date."'";
		
		$query = $this->db->query($sql);
		return $query;
	}

	function getMachineTime($date,$machine)
	{
//		$sql = 	 "SELECT * FROM ".$this->status." WHERE date ='".$date."'";
//		return $sql;
		$sql = "SELECT plan_cv_start,plan_cv_end,st.product_id FROM ".$this->status." as st, ".$this->product." as pc WHERE  st.`product_id` = pc.product_code and pc.req_".$machine." = 1 and date ='".$date."' ORDER BY plan_cv_start ASC;";
//		$sql = "SELECT plan_cv_start,plan_cv_end,st.product_id FROM ".$this->status." as st, ".$this->product." as pc WHERE `date` = '".$date."' and  st.`product_id` = pc.product_code and pc.req_".$machine." = 1 ORDER BY plan_cv_start ASC;";
		
		$query = $this->db->query($sql);
		return $query;
	}

}
?>
