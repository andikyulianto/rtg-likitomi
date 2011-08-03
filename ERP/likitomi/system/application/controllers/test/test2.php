<?php
require_once(APPPATH . '/controllers/test/Toast.php');

class Test2 extends Toast
{
	function Test2()
	{
		parent::Toast(__FILE__);
		$this->load->database();
		$this->load->model('Test_model');
		$this->load->model('Planning_model');
		// Load any models, libraries etc. you need here
	}

	/**
	 * OPTIONAL; Anything in this function will be run before each test
	 * Good for doing cleanup: resetting sessions, renewing objects, etc.
	 */
	function _pre() {}

	/**
	 * OPTIONAL; Anything in this function will be run after each test
	 * I use it for setting $this->message = $this->My_model->getError();
	 */
	function _post() {}


	/* TESTS BELOW */
	function test_CRStartDateZero()
	{
	$date =date("Y-m-d").' 00:00:00';
	$result = $this->Test_model->getTime($date);
		for($i=0;$i<$result->num_rows;$i++)
		{
			$array=$result->_fetch_assoc();
			//print_r($array);
			$test = $array['plan_cr_start'];
			$expect = '0000-00-00 00:00:00';
			$this->_assert_not_equals($test,$expect);
			if(!$this->_assert_not_equals($test,$expect))
				print "CRStartDateZero: ".$test." ".$array['product_id']."<br>";
		}
	}
	function test_CRStopDateZero()
	{
	$date =date("Y-m-d").' 00:00:00';
	$result = $this->Test_model->getTime($date);
		for($i=0;$i<$result->num_rows;$i++)
		{
			$array=$result->_fetch_assoc();
			//print_r($array);
			$test = $array['plan_cr_end'];
			$expect = '0000-00-00 00:00:00';
			$this->_assert_not_equals($test,$expect);
			if(!$this->_assert_not_equals($test,$expect))
				print "CRStopDateZero: ".$test." ".$array['product_id']."<br>";
		}
	}
	function test_CVStartDateZero()
	{
	$date =date("Y-m-d").' 00:00:00';
	$result = $this->Test_model->getTime($date);
		for($i=0;$i<$result->num_rows;$i++)
		{
			$array=$result->_fetch_assoc();
			//print_r($array);
			$test = $array['plan_cv_start'];
			$expect = '0000-00-00 00:00:00';
			$this->_assert_not_equals($test,$expect);
			if(!$this->_assert_not_equals($test,$expect))
				print "CVStartDateZero: ".$test." ".$array['product_id']."<br>";
		}
	}
	function test_CVStopDateZero()
	{
	$date =date("Y-m-d").' 00:00:00';
	$result = $this->Test_model->getTime($date);
		for($i=0;$i<$result->num_rows;$i++)
		{
			$array=$result->_fetch_assoc();
			//print_r($array);
			$test = $array['plan_cv_end'];
			$expect = '0000-00-00 00:00:00';
			$this->_assert_not_equals($test,$expect);
			if(!$this->_assert_not_equals($test,$expect))
				print "CVStopDateZero: ".$test." ".$array['product_id']."<br>";
		}
	}
	function test_PTStartDateZero()
	{
	$date =date("Y-m-d").' 00:00:00';
	$result = $this->Test_model->getTime($date);
		for($i=0;$i<$result->num_rows;$i++)
		{
			$array=$result->_fetch_assoc();
			//print_r($array);
			$test = $array['plan_pt_start'];
			$expect = '0000-00-00 00:00:00';
			$this->_assert_not_equals($test,$expect);
			if(!$this->_assert_not_equals($test,$expect))
				print "PTStartDateZero: ".$test." ".$array['product_id']."<br>";
		}
	}
	function test_PTStopDateZero()
	{
	$date =date("Y-m-d").' 00:00:00';
	$result = $this->Test_model->getTime($date);
		for($i=0;$i<$result->num_rows;$i++)
		{
			$array=$result->_fetch_assoc();
			//print_r($array);
			$test = $array['plan_pt_end'];
			$expect = '0000-00-00 00:00:00';
			$this->_assert_not_equals($test,$expect);
			if(!$this->_assert_not_equals($test,$expect))
				print "CVStopDateZero: ".$test." ".$array['product_id']."<br>";
		}
	}
	function test_WHStartDateZero()
	{
	$date =date("Y-m-d").' 00:00:00';
	$result = $this->Test_model->getTime($date);
		for($i=0;$i<$result->num_rows;$i++)
		{
			$array=$result->_fetch_assoc();
			//print_r($array);
			$test = $array['plan_wh_start'];
			$expect = '0000-00-00 00:00:00';
			$this->_assert_not_equals($test,$expect);
			if(!$this->_assert_not_equals($test,$expect))
				print "WHStartDateZero: ".$test." ".$array['product_id']."<br>";
		}
	}
// only time zero
	function test_CRStartTimeZero()
	{
	$date =date("Y-m-d").' 00:00:00';
	$result = $this->Test_model->getTime($date);
		for($i=0;$i<$result->num_rows;$i++)
		{
			$array=$result->_fetch_assoc();
			//print_r($array);
			$test = $array['plan_cr_start'];
			$expect = $date.' 00:00:00';
			$this->_assert_not_equals($test,$expect);
			if(!$this->_assert_not_equals($test,$expect))
				print "CRStartTimeZero: ".$test." ".$array['product_id']."<br>";
			$expect = date("Y-m-d",strtotime("+1 day",strtotime($date))).' 00:00:00';
			$this->_assert_not_equals($test,$expect);
			if(!$this->_assert_not_equals($test,$expect))
				print "CRStartTimeZero: ".$test." ".$array['product_id']."<br>";
		}
	}
	function test_CRStopTimeZero()
	{
	$date =date("Y-m-d").' 00:00:00';
	$result = $this->Test_model->getTime($date);
		for($i=0;$i<$result->num_rows;$i++)
		{
			$array=$result->_fetch_assoc();
			//print_r($array);
			$test = $array['plan_cr_end'];
			$expect = '0000-00-00 00:00:00';
			$this->_assert_not_equals($test,$expect);
			if(!$this->_assert_not_equals($test,$expect))
				print "CRStopTimeZero: ".$test." ".$array['product_id']."<br>";
			$expect = date("Y-m-d",strtotime("+1 day",strtotime($date))).' 00:00:00';
			$this->_assert_not_equals($test,$expect);
			if(!$this->_assert_not_equals($test,$expect))
				print "CRStopTimeZero: ".$test." ".$array['product_id']."<br>";
		}
	}
	function test_CVStartTimeZero()
	{
	$date =date("Y-m-d").' 00:00:00';
	$result = $this->Test_model->getTime($date);
		for($i=0;$i<$result->num_rows;$i++)
		{
			$array=$result->_fetch_assoc();
			//print_r($array);
			$test = $array['plan_cv_start'];
			$expect = $date.' 00:00:00';
			$this->_assert_not_equals($test,$expect);
			if(!$this->_assert_not_equals($test,$expect))
				print "CVStartTimeZero: ".$test." ".$array['product_id']."<br>";
			$expect = date("Y-m-d",strtotime("+1 day",strtotime($date))).' 00:00:00';
			$this->_assert_not_equals($test,$expect);
			if(!$this->_assert_not_equals($test,$expect))
				print "CVStartTimeZero: ".$test." ".$array['product_id']."<br>";
		}
	}
	function test_CVStopTimeZero()
	{
	$date =date("Y-m-d").' 00:00:00';
	$result = $this->Test_model->getTime($date);
		for($i=0;$i<$result->num_rows;$i++)
		{
			$array=$result->_fetch_assoc();
			//print_r($array);
			$test = $array['plan_cv_end'];
			$expect = $date.' 00:00:00';
			$this->_assert_not_equals($test,$expect);
			if(!$this->_assert_not_equals($test,$expect))
				print "CVStopTimeZero: ".$test." ".$array['product_id']."<br>";
			$expect = date("Y-m-d",strtotime("+1 day",strtotime($date))).' 00:00:00';
			$this->_assert_not_equals($test,$expect);
			if(!$this->_assert_not_equals($test,$expect))
				print "CVStopTimeZero: ".$test." ".$array['product_id']."<br>";
		}
	}
	function test_PTStartTimeZero()
	{
	$date =date("Y-m-d").' 00:00:00';
	$result = $this->Test_model->getTime($date);
		for($i=0;$i<$result->num_rows;$i++)
		{
			$array=$result->_fetch_assoc();
			//print_r($array);
			$test = $array['plan_pt_start'];
			$expect = $date.' 00:00:00';
			$this->_assert_not_equals($test,$expect);
			if(!$this->_assert_not_equals($test,$expect))
				print "PTStartTimeZero: ".$test." ".$array['product_id']."<br>";
			$expect = date("Y-m-d",strtotime("+1 day",strtotime($date))).' 00:00:00';
			$this->_assert_not_equals($test,$expect);
			if(!$this->_assert_not_equals($test,$expect))
				print "PTStartTimeZero: ".$test." ".$array['product_id']."<br>";
		}
	}
	function test_PTStopTimeZero()
	{
	$date =date("Y-m-d").' 00:00:00';
	$result = $this->Test_model->getTime($date);
		for($i=0;$i<$result->num_rows;$i++)
		{
			$array=$result->_fetch_assoc();
			//print_r($array);
			$test = $array['plan_pt_end'];
			$expect = $date.' 00:00:00';
			$this->_assert_not_equals($test,$expect);
			if(!$this->_assert_not_equals($test,$expect))
				print "PTStopTimeZero: ".$test." ".$array['product_id']."<br>";
			$expect = date("Y-m-d",strtotime("+1 day",strtotime($date))).' 00:00:00';
			$this->_assert_not_equals($test,$expect);
			if(!$this->_assert_not_equals($test,$expect))
				print "PTStopTimeZero: ".$test." ".$array['product_id']."<br>";
		}
	}
	function test_WHStartTimeZero()
	{
	$date =date("Y-m-d").' 00:00:00';
	$result = $this->Test_model->getTime($date);
		for($i=0;$i<$result->num_rows;$i++)
		{
			$array=$result->_fetch_assoc();
			//print_r($array);
			$test = $array['plan_wh_start'];
			$expect = $date.' 00:00:00';
			$this->_assert_not_equals($test,$expect);
			if(!$this->_assert_not_equals($test,$expect))
				print "WHStartTimeZero: ".$test." ".$array['product_id']."<br>";
			$expect = date("Y-m-d",strtotime("+1 day",strtotime($date))).' 00:00:00';
			$this->_assert_not_equals($test,$expect);
			if(!$this->_assert_not_equals($test,$expect))
				print "WHStartTimeZero: ".$test." ".$array['product_id']."<br>";
		}
	}
	function test_CRStartTimeBeforeEight()
	{
	
	$date =date("Y-m-d").' 00:00:00';
	$result = $this->Test_model->getTime($date);
		for($i=0;$i<$result->num_rows;$i++)
		{
			$array=$result->_fetch_assoc();
			//print_r($array);
			$test =  strtotime(date($array['plan_cr_start']));
			$expect =  strtotime(date(date("Y-m-d").' 08:20:00'));

		//	$this->_assert_not_equals($test,$expect);
			$this->_assert_true($test>=$expect);
//			print $expect;
			if(!$this->_assert_true($test>=$expect))
//			print date('M d, Y G:i:s',$expect)." > ".date('M d, Y G:i:s',$test)."<br>";
				print "CRStartTimeBeforeEight: ".date('M d, Y G:i:s',$test)." ".$array['product_id']."<br>";

		}
	}
	function test_CRStopTimeBeforeEight()
	{
	
	$date =date("Y-m-d").' 00:00:00';
	$result = $this->Test_model->getTime($date);
		for($i=0;$i<$result->num_rows;$i++)
		{
			$array=$result->_fetch_assoc();
			//print_r($array);
			$test =  strtotime(date($array['plan_cr_end']));
			$expect =  strtotime(date(date("Y-m-d").' 08:20:00'));

		//	$this->_assert_not_equals($test,$expect);
			$this->_assert_true($test>=$expect);
//			print $expect;
			if(!$this->_assert_true($test>=$expect))
//			print date('M d, Y G:i:s',$expect)." > ".date('M d, Y G:i:s',$test)."<br>";
				print "CRStopTimeBeforeEight: ".date('M d, Y G:i:s',$test)." ".$array['product_id']."<br>";

		}
	}
	function test_CVStartTimeBeforeEight()
	{
	
	$date =date("Y-m-d").' 00:00:00';
	$result = $this->Test_model->getTime($date);
		for($i=0;$i<$result->num_rows;$i++)
		{
			$array=$result->_fetch_assoc();
			if ($array['plan_cv_end']!=null)
		{
			$test =  strtotime(date($array['plan_cv_start']));
			$expect =  strtotime(date(date("Y-m-d").' 08:20:00'));

		//	$this->_assert_not_equals($test,$expect);
			$this->_assert_true($test>=$expect);
//			print $expect;
			if(!$this->_assert_true($test>=$expect))
//			print date('M d, Y G:i:s',$expect)." > ".date('M d, Y G:i:s',$test)."<br>";
				print "CVStartTimeBeforeEight: ".date('M d, Y G:i:s',$test)." ".$array['product_id']."<br>";
		}
		}
	}
	function test_CVStopTimeBeforeEight()
	{
	
	$date =date("Y-m-d").' 00:00:00';
	$result = $this->Test_model->getTime($date);
		for($i=0;$i<$result->num_rows;$i++)
		{

			$array=$result->_fetch_assoc();
			//print_r($array);
			if ($array['plan_cv_end']!=null)
		{
			$test =  strtotime(date($array['plan_cv_end']));
			$expect =  strtotime(date(date("Y-m-d").' 08:20:00'));

		//	$this->_assert_not_equals($test,$expect);
			$this->_assert_true($test>=$expect);
//			print $expect;
			if(!$this->_assert_true($test>=$expect))
//			print date('M d, Y G:i:s',$expect)." > ".date('M d, Y G:i:s',$test)."<br>";
				print "CVStopTimeBeforeEight: ".date('M d, Y G:i:s',$test)." ".$array['product_id']."<br>";
		}

		}
	}
	function test_PTStartTimeBeforeEight()
	{
	
	$date =date("Y-m-d").' 00:00:00';
	$result = $this->Test_model->getTime($date);
		for($i=0;$i<$result->num_rows;$i++)
		{
			$array=$result->_fetch_assoc();
			if ($array['plan_pt_start']!=null)
		{
			$test =  strtotime(date($array['plan_pt_start']));
			$expect =  strtotime(date(date("Y-m-d").' 08:20:00'));

		//	$this->_assert_not_equals($test,$expect);
			$this->_assert_true($test>=$expect);
//			print $expect;
			if(!$this->_assert_true($test>=$expect))
//			print date('M d, Y G:i:s',$expect)." > ".date('M d, Y G:i:s',$test)."<br>";
				print "PTStartTimeBeforeEight: ".date('M d, Y G:i:s',$test)." ".$array['product_id']."<br>";
		}
		}
	}
	function test_PTStopTimeBeforeEight()
	{
	
	$date =date("Y-m-d").' 00:00:00';
	$result = $this->Test_model->getTime($date);
		for($i=0;$i<$result->num_rows;$i++)
		{
			$array=$result->_fetch_assoc();
			if ($array['plan_pt_end']!=null)
		{
			$test =  strtotime(date($array['plan_pt_end']));
			$expect =  strtotime(date(date("Y-m-d").' 08:20:00'));

		//	$this->_assert_not_equals($test,$expect);
			$this->_assert_true($test>=$expect);
//			print $expect;
			if(!$this->_assert_true($test>=$expect))
//			print date('M d, Y G:i:s',$expect)." > ".date('M d, Y G:i:s',$test)."<br>";
				print "PTStopTimeBeforeEight: ".date('M d, Y G:i:s',$test)." ".$array['product_id']."<br>";
		}
		}
	}
	function test_WHStartTimeBeforeEight()
	{
	
	$date =date("Y-m-d").' 00:00:00';
	$result = $this->Test_model->getTime($date);
		for($i=0;$i<$result->num_rows;$i++)
		{
			$array=$result->_fetch_assoc();
			//print_r($array);
			$test =  strtotime(date($array['plan_wh_start']));
			$expect =  strtotime(date(date("Y-m-d").' 08:20:00'));

		//	$this->_assert_not_equals($test,$expect);
			$this->_assert_true($test>=$expect);
//			print $expect;
			if(!$this->_assert_true($test>=$expect))
//			print date('M d, Y G:i:s',$expect)." > ".date('M d, Y G:i:s',$test)."<br>";
				print "WHStartTimeBeforeEight: ".date('M d, Y G:i:s',$test)." ".$array['product_id']."<br>";

		}
	}

	

}

// End of file example_test.php */
// Location: ./system/application/controllers/test/example_test.php */
