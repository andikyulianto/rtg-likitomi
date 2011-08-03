<?php

class Test extends Controller {
	
	function test() 
	{
		parent::Controller();
		$this->load->library('unit_test');
		$this->load->database();
		$this->load->model('Test_model');
		$this->load->model('Planning_model');

	}
	
	function index()
	{
		$this->all();
	}
	function all(){
		$this->test1();
	}
	function test1(){
		$test = 1 + 1;
		$expected_result = 2;
		$test_name = 'Adds one plus one';
		$this->unit->run($test, $expected_result, $test_name);
		echo $this->unit->report();
		$result = $this->Test_model->getAllStatus();
		for($i=0;$i<$result->num_rows;$i++)
		{
			$array=$result->_fetch_assoc();
			//print_r($array);
			print $array['plan_cr_start']."<br>";
		}
//		print_r($result);

	}
	
}

