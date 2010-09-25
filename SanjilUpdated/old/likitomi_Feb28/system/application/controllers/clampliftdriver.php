<?php

class Clampliftdriver extends Controller {
	
	function __construct()
	{
		parent::Controller();	
		$this->lang->load('clamplift', 'english');
		$this->load->model('Clamplift_model');	
	}
	
	function index()
	{
		$data = array(
			'title' => $this->lang->line('title'),
	  	);
		$this->load->view('clamplift/clamplifthome', $data);
	}
	
	function locatebytext()
	{
		$data = array(
			'title' => $this->lang->line('title'),
	  	);
		$this->load->view('clamplift/vehicle/locatebytext', $data);
	}


	function track()
	{	
		$data = array(
			'title' => $this->lang->line('title'),
	  	);
		$this->load->view('clamplift/vehicle/track', $data);
	}
	function testxml()
	{	
		$data = array(
			'title' => $this->lang->line('title'),
	  	);
		$this->load->view('clamplift/testxml', $data);
	}
	function scan()
	{	
		$data = array(
			'title' => $this->lang->line('title'),
	  	);
		$this->load->view('clamplift/vehicle/scan', $data);
	}
	
	function scanonly()
	{	
		$data = array(
			'title' => $this->lang->line('title'),
	  	);
		$this->load->view('clamplift/vehicle/scanonly', $data);
	}
}
?>