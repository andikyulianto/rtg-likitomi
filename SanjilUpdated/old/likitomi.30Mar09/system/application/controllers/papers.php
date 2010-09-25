<?php
class Papers extends Controller {
	
	function __construct() 
	{
		parent::Controller();
		$this->freakauth_light->check();
		$this->lang->load('papers',$this->db_session->userdata('language'));
		$this->load->database();
		$this->load->model('Papers_model');
		$this->load->scaffolding('papers');
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
		//$script .= '<script type="text/javascript" src="'.base_url().'static/javascript/AutoSuggestBox.js"></script>';
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
				$this->lang->line('all_papers'),
				$this->lang->line('bygrades'),
				"Archive"
			);
		$data['leftmenu_count'] = array(
				$this->Papers_model->getTotalData(),
				$this->Papers_model->getTotalGrade(),
				$this->Papers_model->getTotalTrash(),			
			);
		$data['types']=array('',"grade","Trash");
		$data['paper_class'] = $this;
		$this->load->view('papers/papers',$data);
	}
	
	function getCounters(){
		$item = array(
				$this->Papers_model->getTotalData(),
				$this->Papers_model->getTotalGrade(),
				$this->Papers_model->getTotalTrash(),			
			);
		$this->load->library('json'); 
		echo json_encode($item);
	}
	
	function getNames()
	{
		$paper_code = ($this->input->post('paper_code'))?$this->input->post('paper_code'):'';
		$data['resultPapers'] = $this->Papers_model->getNames($paper_code);
		$data['action'] = "list";
		$data['paper_class'] = $this;
		$data['code'] = $paper_code;
		$this->load->view('papers/paperlist',$data);
	}

	function getDetails()
	{
		$paper_id = ($this->input->post('paper_id'))?$this->input->post('paper_id'):'0';
		$data['action'] = ($this->input->post('action'))?$this->input->post('action'):'view';;
		if(($paper_id > 0 )||($data['action']=='add'))
		{
			if($data['action'] !='add')
			{
				$data['resultPapers'] = $this->Papers_model->getDetails($paper_id);
			}
			$data['paper_class'] = $this;
			$this->load->view('papers/paperdetail',$data);
		}
		else 
		{
			echo "Invalid Paper ID : ".$paper_id ;
		}
	}
	
	function saveDetail()
	{
		$papers = array();
		$papers['paper_code'] 	= ($this->input->post('paper_code'))?$this->input->post('paper_code'):'';
		$papers['paper_name'] 	= ($this->input->post('paper_name'))?$this->input->post('paper_name'):'';
		$papers['paper_grade'] 	= ($this->input->post('paper_grade'))?$this->input->post('paper_grade'):'';
		$papers['med_liner'] 	= ($this->input->post('med_liner'))?$this->input->post('med_liner'):'';
		$papers['paper_remark'] = ($this->input->post('paper_remark'))?$this->input->post('paper_remark'):'';
		$papers['isdeleted']	= "0";
		$papers['created_on']	= date("Y-m-d G:i:s");
		$papers['created_by']	= $this->db_session->userdata('user_name');
		$papers['modified_on']	= date("Y-m-d G:i:s");
		$papers['modified_by']	= $this->db_session->userdata('user_name');
		
		$partnerids = explode("|",$this->input->post('partnerids'));
		
		$paper_id = $this->Papers_model->insertPaper($papers);
		if($paper_id>0)
		{	
			$this->Papers_model->insertPartners($paper_id,$partnerids,$papers['paper_code']);	
		}
		//never echo here
		echo $paper_id;		
	}
	
	function updateDetail()
	{
		$papers = array();
		$paper_id 	= ($this->input->post('paper_id'))?$this->input->post('paper_id'):'0';
		if($paper_id > 0 )
		{
			$papers['paper_code'] 	= ($this->input->post('paper_code'))?$this->input->post('paper_code'):'';
			$papers['paper_name'] 	= ($this->input->post('paper_name'))?$this->input->post('paper_name'):'';
			$papers['paper_grade'] 	= ($this->input->post('paper_grade'))?$this->input->post('paper_grade'):'';
			$papers['med_liner'] 	= ($this->input->post('med_liner'))?$this->input->post('med_liner'):'';
			$papers['paper_remark'] = ($this->input->post('paper_remark'))?$this->input->post('paper_remark'):'';
			$papers['isdeleted']	= "0";
			$papers['modified_on']	= date("Y-m-d G:i:s");
			$papers['modified_by']	= $this->db_session->userdata('user_name');
			$partnerids = explode("|",$this->input->post('partnerids'));
			$ppids = explode("|",$this->input->post('ppids'));
			
			$this->Papers_model->updatePaper($papers,$paper_id);
			$this->Papers_model->updatePartners($paper_id,$partnerids,$ppids,$papers['paper_code']);
		}
		else 
		{
			echo "Invalid Paper ID : ".$paper_id ;
		}
	}
	
	function getNamesArray($id)
	{
		$firstValue = ($id>0)?$id:0;
		$this->load->model('Partners_model');
		$result = $this->Partners_model->getNames('Supplier');
		echo "<option value='".$firstValue."' ></option>";
		foreach ($result as $row)
		{
			echo "<option value='".$row->partner_id."' ";
			if($row->partner_id==$id) echo " selected='selected' ";
			echo ">".$row->partner_name."</option>";
		}
	}
	
	function deleteDetails()
	{
		$paper_id = ($this->input->post('paper_id'))?$this->input->post('paper_id'):'0';
		if($paper_id > 0)
		{
			$this->Papers_model->deletePaper($paper_id);
		}
		else 
		{
			echo "Invalid Paper ID : ".$paper_id ;
		}
	}
	
	function search()
	{
		$searchkeyword = ($this->input->post('search'))?$this->input->post('search'):'';
		$data['resultPapers'] = $this->Papers_model->search($searchkeyword);
		$data['action'] = "search";
		$data['searchkeyword'] = $searchkeyword;
		$data['paper_class'] = $this;
		$this->load->view('papers/paperlist',$data);
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
}
?>