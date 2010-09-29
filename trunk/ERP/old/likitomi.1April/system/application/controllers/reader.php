<?php
class Reader extends Controller {
	
	function __construct() 
	{
		parent::Controller();
		$this->load->scaffolding('reader');
	}
	
	function index()
	{
		$data = array(
	      'contentClass' => $this,
	      'title' => "Reader Management",
		  'scripts' => $this->getScripts(),
		  'styles' => $this->getStyles()
	  	);
 		$this->load->view('template', $data);
	}
	
	function getScripts()
	{
		$script = '<script type="text/javascript" src="'.base_url().'resources/javascript/ext/ext-base.js"></script>';
		$script .= '<script type="text/javascript" src="'.base_url().'resources/javascript/ext-all.js"></script>';
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
		$this->load->view('reader/reader');
	}
	
	function lab($filecnt=1,$ant=5)
	{
		if($filecnt <=0)$filecnt =1;
		$file = "http://localhost/data/".$filecnt;
		$buffer= "";
		$handle = @fopen($file, "r");
		if ($handle) {
		    while (!feof($handle)) {
		        $buffer = fgets($handle, 4096);
		        //echo $buffer;
		    }
		    fclose($handle);
		}
		
		if($buffer!="") {
			$data['datetime'] = substr($buffer,0,strpos($buffer,"["));
			$start = strlen($data['datetime']);
			
			$data['antenna1'] = substr($buffer,$start+1,strpos($buffer,"][")-$start-1);
			$start = $start+strlen($data['antenna1'])+3;
			
			$data['antenna4'] = substr($buffer,$start);
			$data['antenna4'] = substr($data['antenna4'],0,strlen($data['antenna4'])-1);
			
			$data['filecnt'] = $filecnt;
			$data['ant'] = $ant;
			
			$this->load->view('reader/lab',$data);
		}
		else  {
			$data['datetime'] = "";
			$data['antenna1'] = "0";
			$data['antenna4'] = "0";
			for($i=1;$i<100;$i++)
				$data['antenna1'] .= ",0";
				$data['antenna4'] .= ",0";
			
			$data['filecnt'] = $filecnt-1;
			$data['ant'] = $ant;
			
			$this->load->view('reader/lab',$data);
		}
		
	}
}