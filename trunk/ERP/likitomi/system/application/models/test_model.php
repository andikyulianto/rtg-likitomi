<?php
class Test_model extends Model 
{

	var $status 	= "status_tracking";

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

}
?>
