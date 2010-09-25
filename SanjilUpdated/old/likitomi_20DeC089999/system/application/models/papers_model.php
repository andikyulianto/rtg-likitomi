<?php

class Papers_model extends Model 
{
	var $tableName = "papers";
	var $tblpartnerpapers = "partners_papers";
	function Papers_model()
	{
		parent::Model();
	}
	
	function getTotalData()
	{
		$this->db->where('isdeleted',0);
		$this->db->from($this->tableName); 
		return $this->db->count_all_results();	
    }
	
	function getTotalGrade()
	{
		$this->db->where('isdeleted',0);
		$this->db->select('paper_grade');
		$this->db->group_by('paper_grade'); 
		$this->db->from($this->tableName); 
		$query = $this->db->get($this->tableName);
		return $query->num_rows();
	}
	
	function getTotalByCodeB($code)
	{
		$this->db->where('isdeleted',0);
		$this->db->like('lower(paper_code)',strtolower($code), 'after'); 
		$this->db->from($this->tableName); 
		return $this->db->count_all_results();
	}
	
	function getTotalTrash(){
		$this->db->where('isdeleted !=',0);
		$this->db->from($this->tableName); 
		return $this->db->count_all_results();
	}
	
	function getNames($code)
	{
		if($code=='Trash') $this->db->where('isdeleted !=',0);
		else {
			$this->db->where('isdeleted',0);
			//if($code!='') $this->db->like('lower(paper_code)',strtolower($code), 'after'); 
			if($code=='grade') $this->db->order_by("paper_grade", "asc"); 
		}
			
		$this->db->select('paper_id,paper_code,paper_name,paper_grade');
		$this->db->order_by("lower(paper_code)", "asc"); 	
		$query = $this->db->get($this->tableName);		
		return $query->result();
	}
	
	function getDetails($id)
	{
		$sql = 	"SELECT tp.*,"
				." partners.partner_name,partners.partner_phone_office,partners.partner_fax,"
				." partners.partner_billing_address,partners.isdeleted AS partnerisdeleted "
				." FROM (SELECT papers.*,partners_papers.tblppid, "
				." partners_papers.partner_id as pid"
				." FROM papers, partners_papers"
				." WHERE papers.paper_id =".$id
				." AND partners_papers.isdeleted =0"
				." AND papers.paper_id = partners_papers.paper_id ) as tp "
				." LEFT JOIN partners ON tp.pid = partners.partner_id;";
		$query = $this->db->query($sql);	
		//echo $this->db->last_query();	
		return $query;
	}
	
	function insertPaper($papers)
	{
		$this->db->trans_start();
		$this->db->insert($this->tableName, $papers); 
		
		$paper_id = $this->db->insert_id();
		
		$this->db->trans_complete();	
		if ($this->db->trans_status() === FALSE)
		{
			log_message('debug', 'Problem Inserting Papers');
			show_error('Please notify support with transaction details');
			return "Failed";		
		}
		return $paper_id;
	}
	
	function updatePaper($papers,$paper_id)
	{
		$this->db->trans_start();
		$this->db->where('paper_id', $paper_id);
		$this->db->update($this->tableName, $papers); 
		
		$this->db->trans_complete();	
		if ($this->db->trans_status() === FALSE)
		{
			log_message('debug', 'Problem Inserting Papers');
			show_error('Please notify support with transaction details');
			return "Failed";		
		}
		return "Success";
	}
	
	function insertPartners($paper_id,$partnerids,$paper_code)
	{
		for($i=0;$i<count($partnerids)-1;$i++)
		{
			if($partnerids[$i] != "")
			{
				$param = array( "paper_id" => $paper_id,
								"partner_id" => $partnerids[$i],
								"paper_code" => $paper_code,
								"isdeleted" => 0);	
				$this->db->insert($this->tblpartnerpapers, $param);
			}
		}
	}
	
	function updatePartners($paper_id,$partnerids,$ppids,$paper_code)
	{
		$this->db->where('paper_id', $paper_id);
		$param = array("isdeleted" => 1);
		$this->db->update($this->tblpartnerpapers, $param);
		for($i=0;$i<count($ppids)-1;$i++)
		{
			if($ppids[$i]>0)
			{
				$param = array("partner_id" => $partnerids[$i],
								"isdeleted" => 0);	
				$this->db->where('paper_id', $paper_id);
				$this->db->where('tblppid',$ppids[$i]);
				$this->db->update($this->tblpartnerpapers, $param);
			}
			else 
			{
				$param = array("partner_id" => $partnerids[$i],
								"isdeleted" => 0,
								"paper_id" => $paper_id,
								"paper_code" => $paper_code);
				$this->db->insert($this->tblpartnerpapers,$param);
			}
			//echo $this->db->last_query();
		}
	}
	
	function deletePaper($paper_id){
		$param = array("isdeleted" => 1);
		$this->db->where('paper_id',$paper_id);
		$this->db->update($this->tableName,$param);
		echo $this->db->last_query();
	}
	
	function search($searchkeyword)
	{
		$this->db->select('paper_id,paper_code,paper_grade,paper_name');
		$this->db->like('lower(paper_code)',strtolower($searchkeyword), 'both'); 
		$this->db->where('isdeleted',0);
		$this->db->order_by("lower(paper_code)", "asc"); 	
		$query = $this->db->get($this->tableName);		
		return $query->result();
	}
	
	function getPapersList()
	{
		$this->db->where('isdeleted',0);
		$this->db->select('paper_id,paper_code');
		$this->db->order_by("lower(paper_code)", "asc"); 	
		$query = $this->db->get($this->tableName);		
		return $query->result();
	}
}

?>
