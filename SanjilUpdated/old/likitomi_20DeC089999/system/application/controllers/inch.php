<?php
class Inch extends Controller {
	
	function __construct() 
	{
		parent::Controller();
		$this->freakauth_light->check();
		$this->load->scaffolding('inch_mm');
	}
	
	function index()
	{
		
	}
}