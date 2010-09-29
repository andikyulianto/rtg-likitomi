<?php
class Home extends Controller {
	
	function __construct() 
	{
		parent::Controller();
		$this->freakauth_light->check();
		if($this->db_session->userdata('language')=="") $language ='english';
		else $language = $this->db_session->userdata('language');
		$this->lang->load('home',$language);
		$this->_container = $this->config->item('FAL_template_dir').'template/container';
	}
	
	function index()
	{
		$data['heading'] = 'Likitomi ERP';
        $data['page'] = $this->config->item('FAL_template_dir').'content/home';
        $this->load->vars($data);
        $this->load->view($this->_container);
	}
	
	function setlang($lang){
		if($lang =='th') $language = 'thai';
		else if($lang =='en') $language = 'english';
		else  $language = 'english';
		$userdata =$this->db_session->userdata();
		$userdata['language'] = $language;
		$this->db_session->set_userdata($userdata);
		$this->db_session->set_flashdata('flashMessage',"Language changed to ".$language);
		$this->index();
	}
}

?>