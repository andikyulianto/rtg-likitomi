<?php
class Planning extends Controller {
	
	function __construct() 
	{
		parent::Controller();
		$this->freakauth_light->check();
		$this->lang->load('planning',$this->db_session->userdata('language'));
		$this->load->database();
		$this->load->model('Planning_model');

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
		$script  = '<script type="text/javascript" src="'.base_url().'resources/javascript/ext/ext-base.js"></script>';
		$script .= '<script type="text/javascript" src="'.base_url().'resources/javascript/ext-all.js"></script>';
		$script .= '<script type="text/javascript" src="'.base_url().'static/javascript/common.js"></script>';
		$script .= '<script type="text/javascript" src="'.base_url().'static/javascript/table.js"></script>';
		return $script;
	}
		
	function getStyles()
	{
		$styles	 = '@import "'.base_url().'static/css/planning.css";';
		$styles .=' @import "'.base_url().'static/css/common.css";';
		$styles	.= '@import "'.base_url().'resources/css/ext-all.css";';
		//$styles	.= '@import "'.base_url().'resources/css/xtheme-gray.css";';
		return $styles;
	}
	
	function show()
	{
		$resultAllDelivery	= $this->Planning_model->getAllDelivery();
		$delDateArray 		= array();
		$salesOrderArray	= array();
		$lastmodified 		= array();
		$status				= array();
		
		$cnt=0;
		foreach ($resultAllDelivery->result() as $delivery)
		{
			$delDateArray[$cnt] 	= $delivery->delivery_date;
			$salesOrderArray[$cnt]	= $delivery->sales_order;
			$lastmodified[$cnt]		= substr($delivery->modified_on,0,10);
			$status[$cnt]			= $delivery->status;
			$cnt++;
		}
		
		rsort($delDateArray);
		rsort($salesOrderArray);
		rsort($lastmodified);
		sort($status);
		$data['delDateArray'] 		= array_unique($delDateArray);
		$data['salesOrderArray'] 	= array_unique($salesOrderArray);
		$data['lastmodified']		= array_unique($lastmodified);
		$data['status']				= array_unique($status);
		
		$data['resultAllDelivery'] 	= $resultAllDelivery;
		
		$this->load->view('planning/planning',$data);
	}
	
	function filter()
	{
		$delivery_date_all 	= explode("|",$this->input->post('delivery_date_all'));
		$sales_order_all 	= explode("|",$this->input->post('sales_order_all'));
		$lastmodified_all 	= explode("|",$this->input->post('lastmodified_all'));
		$status_all		 	= explode("|",$this->input->post('status_all'));
		
		$resultDelivery = $this->Planning_model->getFilterResult($delivery_date_all,$sales_order_all,$lastmodified_all,$status_all);
		$deliveryList = array();
		$cnt=0;
		$this->load->model('Salesorder_model');
		foreach($resultDelivery->result() as $delivery)
		{
			$deliveryList[$cnt]['delivery_id']	= $delivery->delivery_id;
			$deliveryList[$cnt]['sales_order']	= $delivery->sales_order;
			
			$salesDetail = $this->Salesorder_model->getSalesDetail($delivery->sales_order);
			$deliveryList[$cnt]['purchase_order_no']	= $salesDetail->purchase_order_no;
			
			$deliveryList[$cnt]['product_code']	= $delivery->product_code;
                        //echo $delivery->product_code;
			$partnerproduct = $this->Planning_model->getProduct_Partner($delivery->product_id);
			
			$deliveryList[$cnt]['product_name'] = $partnerproduct->product_name;
			$deliveryList[$cnt]['partner_name'] = $partnerproduct->partner_name;
			
			$deliveryList[$cnt]['p_width_inch']	= $partnerproduct->pc_paper_width;
			$deliveryList[$cnt]['t_length']		= $partnerproduct->cr_length;
			
			$productflutes	= $this->Planning_model->getProductFlutes($delivery->product_id,$delivery->product_code);
			if($productflutes->num_rows()>0){

				$deliveryList[$cnt]['flute']		= $productflutes->row()->flute;
				$deliveryList[$cnt]['DF']		= $productflutes->row()->DF;
				$deliveryList[$cnt]['BM']		= $productflutes->row()->BM;
				$deliveryList[$cnt]['BL']		= $productflutes->row()->BL;
				$deliveryList[$cnt]['CM']		= $productflutes->row()->CM;
				$deliveryList[$cnt]['CL']		= $productflutes->row()->CL;
			}else {
				$deliveryList[$cnt]['flute']	= "";
				$deliveryList[$cnt]['DF']		= "";
				$deliveryList[$cnt]['BM']		= "";
				$deliveryList[$cnt]['BL']		= "";
				$deliveryList[$cnt]['CM']		= "";
				$deliveryList[$cnt]['CL']		= "";
			}
			$deliveryList[$cnt]['cut']			= $partnerproduct->cut;
			//echo $partnerproduct->pc_slit;
			$deliveryList[$cnt]['delivery_date']= $delivery->delivery_date;
			$deliveryList[$cnt]['qty']			= $delivery->qty/$partnerproduct->pc_slit;
			$deliveryList[$cnt]['modified_on']	= $delivery->modified_on;
			$deliveryList[$cnt]['status']		= $delivery->status;
			$deliveryList[$cnt]['corrugator_date']	= date('Y-m-d');
			$deliveryList[$cnt]['corrugator_time']	= "";
			$deliveryList[$cnt]['converter_date']	= date('Y-m-d');
			$deliveryList[$cnt]['converter_time']	= "";
			$deliveryList[$cnt]['padpartition_date']	= date('Y-m-d');
			$deliveryList[$cnt]['padpartition_time']	= "";
			$deliveryList[$cnt]['warehouse_date']	= date('Y-m-d');
			$deliveryList[$cnt]['warehouse_time']	= "";
			//$deliveryList[$cnt]['next_process']	= "";
			$deliveryList[$cnt]['sort']	= $cnt;
			

			$cnt++;
		}
		
		//load JSON lib
		$this->load->library('json');	
		echo '{"delivery" :'.$this->json->encode($deliveryList).',"count":"'.$cnt.'"}';
	}
	function formatDate($day)
	{
		$hour  = floor($day*24); 
		$min   = floor((($day*24)-$hour)*60); 
		$time  = ($hour<10)?"0".$hour:$hour;//
		$time .= ":";
		$time .= ($min<10)?"0".$min:$min;
		return $time;
	}
	
//	function getDeliveryHistory()
//	{
//		$delivery_id = ($this->input->post('delivery_id'))?$this->input->post('delivery_id'):'0';
//		$this->load->model('Salesorder_model');
//		$histdata['history'] = $this->Salesorder_model->getDeliveryHistory($delivery_id);
//		$histdata['showheader'] = true;
//		$this->load->view('salesorder/deliveryhistory',$histdata); 
//	}
	
	function savetotalplanjson()
	{
		$jsonData 		= ($this->input->post('data'))?$this->input->post('data'):'';
		$choosendate 	= ($this->input->post('choosendate'))?$this->input->post('choosendate'):date('Y-m-d');		
		if($jsonData == '') return false;
		//load JSON lib
		$this->load->library('JSON');
		$gridData = $this->json->decode($jsonData);	
		$this->Planning_model->deleteAllPlanForToday($choosendate);
		$this->Planning_model->deleteStatusTrackingPlanForToday($choosendate);

		//calculate time
		$time_start_cr = (0.0006949*60)*8.34;
		$time_start_cv = (0.0006949*60)*9.34;
		$time_start_pt = (0.0006949*60)*9.34;
		$time_start_3cs = $time_start_cv;
		$time_start_2cl = $time_start_cv;
		$time_start_3cl = $time_start_cv;
		$time_start_3cm = $time_start_cv;
		$time_start_4cd = $time_start_cv;
		
		$time_start_rd  = $time_start_pt;
		$time_start_ss = $time_start_pt;
		$time_start_remove = $time_start_pt;
		$time_start_foam = $time_start_pt;
		$time_start_tape = $time_start_pt;

		
		$time_stop_cr = $time_start_cr;
		$time_stop_cv = $time_start_cv;
		$time_stop_pt = $time_start_pt;
		$time_stop_2cl=0;
		$time_stop_3cl=0;
		$time_stop_3cm=0;
		$time_stop_3cs=0;
		$time_stop_4cd=0;
		
		$time_stop_rd = 0;
		$time_stop_ss = 0;
		$time_stop_remove = 0;
		$time_stop_foam = 0;
		$time_stope_tape =0;
		
		

		//$time_start_pt = (0.0006949*60)*8;
		//$time_start_wh = (0.0006949*60)*8;


			//count mo
			$mo_cr_count = 0;
			$mo_cv_count = 0;
			
			$date_mo_code = date('dm');

		foreach($gridData as $rowData)
		{
			
		////////////	
		//create MO//
		////////////

			//initialize 
			$mo_cr = "";
			$mo_cv = "";
			$mo_pt = "";
			
			// start stop time of CR 
			$query = $this->Planning_model->getProduct($rowData->product_code);
			$key = $query->row_array(0);							//get the only one object		if($key['req_cr'])
		{
			$mo_cr_count = $mo_cr_count +1;
			$mo_cr_running_process =$mo_cr_count;

			while(strlen($mo_cr_running_process)<3)
			{
				
				$mo_cr_running_process ="0".$mo_cr_running_process;
			}
		}
		if($key['req_2cl']||$key['req_3cm']||$key['req_3cs']||$key['req_4cd']||$key['req_3cl']||$key['req_gh']||$key['req_hs']||$key['req_fg']||
		$key['req_rd']||$key['req_ss']||$key['req_remove']||$key['req_foam']||$key['req_tape'])
		{
			$mo_cv_count = $mo_cv_count +1;
			$mo_cv_running_process =$mo_cv_count;
			while(strlen($mo_cv_running_process)<2)
			{
				
				$mo_cv_running_process ="0".$mo_cv_running_process;
			}
			$cc ="";
			$ccpt="";
			if($key['req_2cl'])
			{
				$cc .= "2L";
			}
			if($key['req_3cm'])
			{
				$cc .= "3M";
			}
			if($key['req_3cs'])
			{
				$cc .= "3S";
			}
			if($key['req_4cd'])
			{
				$cc .= "4D";
			}
			if($key['req_3cl'])
			{
				$cc.="3L";
			}
			if($key['req_gh'])
			{
				$cc.="GH";
			}
			if($key['req_hs'])
			{
				$cc.="HS";
			}
			if($key['req_fg'])
			{
				$cc.="FG";
			}
			if($key['req_rd'])
			{
				$ccpt.="RD";
			}
			if($key['req_ss'])
			{
				$ccpt.="SS";
			}
			if($key['req_remove']||$key['req_foam']||$key['req_tape'])
			{
				$ccpt.="RO";
			}
			//echo $mo_cv_running_process;
		}
		$mo_cr = $date_mo_code."".$mo_cr_running_process;
		if($cc!="")
			$mo_cv = $cc."".$date_mo_code."".$mo_cv_running_process;
		else
			$mo_cv = "";
		if($ccpt!="")
			$mo_pt = $ccpt."".$date_mo_code."".$mo_cv_running_process;
		else
			$mo_pt = "";
		
		//echo $mo_cr."   ".$mo_cv."   ".$mo_pt."<br>";
		
			/// end mo
			///////////////////////////////////
			
			
			
			
			$case 	= $rowData->qty;
			if(($key['pc_slit'])!=0)
			$cut2 	= $case/$key['pc_slit'];
			//echo $key['pc_slit'];
			$metre	= ($key['cr_length']*$cut2)/1000;
			$timeuseCR = 0;
			$realDate = $choosendate;
		/////////////////////////////
		//calculate time use in CR //
		////////////////////////////
		if((strtoupper($key['flute'])=="B")||(strtoupper($key['flute'])=="C"))
		{
			$timeuseCR = ($metre/120)+4;
		}
		else if((strtoupper($key['flute'])=="BC")||(strtoupper($key['flute'])=="W"))
		{
			$timeuseCR = ($metre/100)+4;
		}
		else $timeuseCR = 0;
		///////////////////////////////
		
		
		////////////////////////////
		// Calculate time stop/////
		///////////////////////////
		
		$time_stop_cr = $time_start_cr;
		
		if($timeuseCR!=0)
		{
			$time_stop_cr = $time_start_cr + $timeuseCR * 0.0006949;
		}
		

		// end CR ///
		///////////////////////////////////
		//prepare CV calculation /////
		//////////////////////////
		if($key['req_2cl']||$key['req_3cm']||$key['req_3cs']||$key['req_4cd']||$key['req_3cl']||$key['req_gh']||$key['req_hs']||$key['req_fg'])
		{
			//start stop time for CV
	#		print($key['req_3cm']);
			if($key['req_3cs'])
				$speed = 120;
			elseif($key['req_2cl'])
				$speed = 60;
			elseif($key['req_3cl'])
				$speed = 50;
			elseif($key['req_3cm'])
				$speed = 20;
			elseif($key['req_4cd'])
				$speed = 90;
			elseif($key['req_gh'])
				$speed = 5;
			elseif($key['req_hs'])
				$speed = 15;
			elseif($key['req_fg'])
				$speed = 5;
			else
				$speed = 0;
			//echo $key['next_process']."". $speed ."<br>";
			$time_stop_cv = $time_start_cv;
			if ($speed > 0)
				$timeuseCV = $rowData->qty / $speed;
			else
				$timeuseCV = 0;

			
//////////////////
//calculate CV ///
/////////////////
		
			if($key['req_3cs'])
			{
				if($time_stop_3cs>$time_stop_cr)
					$time_start_3cs = $time_stop_3cs;
				else
					$time_start_3cs = $time_stop_cr;
					
				$time_stop_3cs = $time_start_3cs+ ($timeuseCV+30) * 0.0006949;
				$time_start_cv = $time_start_3cs;
				$time_stop_cv = $time_stop_3cs;
			}
			elseif($key['req_2cl'])
			{
				if($time_stop_2cl>$time_stop_cr)
					$time_start_2cl = $time_stop_2cl;
				else
					$time_start_2cl = $time_stop_cr;

				$time_stop_2cl = $time_start_2cl+ round($timeuseCV+30) * 0.0006949;
				$time_start_cv = $time_start_2cl;
				$time_stop_cv = $time_stop_2cl;
			}
			elseif($key['req_3cl'])
			{
				if($time_stop_3cl>$time_stop_cr)
					$time_start_3cl = $time_stop_3cl;
				else
					$time_start_3cl = $time_stop_cr;		

				$time_stop_3cl = $time_start_3cl+ round($timeuseCV+30) * 0.0006949;
				$time_start_cv = $time_start_3cl;
				$time_stop_cv = $time_stop_3cl;
			}
			elseif($key['req_3cm'])
			{
				if($time_stop_3cm>$time_stop_cr)
					$time_start_3cm = $time_stop_3cm;
				else
					$time_start_3cm = $time_stop_cr;		

				$time_stop_3cm = $time_start_3cm+ round($timeuseCV+30) * 0.0006949;
				$time_start_cv = $time_start_3cm;
				$time_stop_cv = $time_stop_3cm;
			}
			elseif($key['req_4cd'])
			{
				if($time_stop_4cd>$time_stop_cr)
					$time_start_4cd = $time_stop_4cd;
				else
					$time_start_3cs = $time_stop_cr;
				
				$time_stop_4cd = $time_start_4cd+ round($timeuseCV+30) * 0.0006949;
				$time_start_cv = $time_start_4cd;
				$time_stop_cv = $time_stop_4cd;
			}
			else
			{
				$time_stop_cv = $time_start_cv;
			}
			$time_start_wh = $time_stop_cv;
		}
		else{
			$time_stop_cv = NULL;
			$time_start_cv= NULL;
			$time_start_wh = $time_stop_cr;
		}
////////////end CV//////////////////



////////////////////////
///// Start PT /////////
///////////////////////

		if($key['req_rd']||$key['req_ss']||$key['req_remove']||$key['req_foam']||$key['req_tape'])
		{
			if($key['req_rd'])
				$speed = 50;
			elseif($key['req_ss'])
				$speed = 5;
			elseif($key['req_remove'])
				$speed = 1;
			elseif($key['req_foam'])
				$speed = 1;
			elseif($key['req_tape'])
				$speed = 1;
			else
				$speed = 0;
				

			if ($speed > 0)
				$timeusePT = $rowData->qty / $speed;
			else
				$timeusePT = 0;
				
///////////////////////////////
/////////calculate PT Time ////
//////////////////////////////

			if($key['req_2cl']||$key['req_3cm']||$key['req_3cs']||$key['req_4cd']||$key['req_3cl']||$key['req_gh']||$key['req_hs']||$key['req_fg'])
			{
				if($key['req_rd'])
				{
					
					if($time_stop_rd>$time_stop_cv)
						$time_start_rd = $time_stop_rd;
					else
						$time_start_rd = $time_stop_cv;
					
					$time_stop_rd = $time_start_rd+ ($timeusePT+30) * 0.0006949;
					$time_start_pt = $time_start_rd;
					$time_stop_pt = $time_stop_rd;
				}
				if($key['req_ss'])
				{
					
					if($time_stop_ss>$time_stop_cv)
						$time_start_ss = $time_stop_ss;
					else
						$time_start_ss = $time_stop_cv;
					
					$time_stop_ss = $time_start_ss+ ($timeusePT+30) * 0.0006949;
					$time_start_pt = $time_start_ss;
					$time_stop_pt = $time_stop_ss;
				}
				if($key['req_remove'])
				{
					
					if($time_stop_remove>$time_stop_cv)
						$time_start_remove = $time_stop_remove;
					else
						$time_start_remove = $time_stop_cv;
					
					$time_stop_remove = $time_start_remove+ ($timeusePT+30) * 0.0006949;
					$time_start_pt = $time_start_remove;
					$time_stop_pt = $time_stop_remove;
				}
				if($key['req_foam'])
				{
					
					if($time_stop_foam>$time_stop_cv)
						$time_start_foam = $time_stop_foam;
					else
						$time_start_foam = $time_stop_cv;
					
					$time_stop_foam = $time_start_foam+ ($timeusePT+30) * 0.0006949;
					$time_start_pt = $time_start_foam;
					$time_stop_pt = $time_stop_foam;
				}
				if($key['req_tape'])
				{
					
					if($time_stop_tape>$time_stop_cv)
						$time_start_tape = $time_stop_tape;
					else
						$time_start_tape = $time_stop_cv;
					
					$time_stop_tape = $time_start_tape+ ($timeusePT+30) * 0.0006949;
					$time_start_pt = $time_start_tape;
					$time_stop_pt = $time_stop_tape;
				}
				
				
			}
			elseif($key['req_cr']||!($key['req_2cl']||$key['req_3cm']||$key['req_3cs']||$key['req_4cd']||$key['req_3cl']||$key['req_gh']||$key['req_hs']||$key['req_fg'])){
				if($key['req_rd'])
				{
					
					if($time_stop_rd>$time_stop_cr)
						$time_start_rd = $time_stop_rd;
					else
						$time_start_rd = $time_stop_cr;
					
					$time_stop_rd = $time_start_rd+ ($timeusePT+30) * 0.0006949;
					$time_start_pt = $time_start_rd;
					$time_stop_pt = $time_stop_rd;
				}
				if($key['req_ss'])
				{
					
					if($time_stop_ss>$time_stop_cr)
						$time_start_ss = $time_stop_ss;
					else
						$time_start_ss = $time_stop_cr;
					
					$time_stop_ss = $time_start_ss+ ($timeusePT+30) * 0.0006949;
					$time_start_pt = $time_start_ss;
					$time_stop_pt = $time_stop_ss;
				}
				if($key['req_remove'])
				{
					
					if($time_stop_remove>$time_stop_cr)
						$time_start_remove = $time_stop_remove;
					else
						$time_start_remove = $time_stop_cr;
					
					$time_stop_remove = $time_start_remove+ ($timeusePT+30) * 0.0006949;
					$time_start_pt = $time_start_remove;
					$time_stop_pt = $time_stop_remove;
				}
				if($key['req_foam'])
				{
					
					if($time_stop_foam>$time_stop_cr)
						$time_start_foam = $time_stop_foam;
					else
						$time_start_foam = $time_stop_cr;
					
					$time_stop_foam = $time_start_foam+ ($timeusePT+30) * 0.0006949;
					$time_start_pt = $time_start_foam;
					$time_stop_pt = $time_stop_foam;
				}
				if($key['req_tape'])
				{
					
					if($time_stop_tape>$time_stop_cr)
						$time_start_tape = $time_stop_tape;
					else
						$time_start_tape = $time_stop_cr;
					
					$time_stop_tape = $time_start_tape+ ($timeusePT+30) * 0.0006949;
					$time_start_pt = $time_start_tape;
					$time_stop_pt = $time_stop_tape;
				}
			}
			else
			{
				$time_start_pt = NULL;
				$time_stop_pt = NULL;
				
			}
			
			//$time_start_wh = $time_stop_pt +round(10) * 0.0006949;
		}
		else
		{
			$time_start_pt = NULL;
			$time_stop_pt = NULL;
		}
/////////////////////
// find wh time ///
//////////////////
	if($key['req_rd']||$key['req_ss']||$key['req_remove']||$key['req_foam']||$key['req_tape'])
		$time_start_wh = $time_stop_pt;
	elseif($key['req_2cl']||$key['req_3cm']||$key['req_3cs']||$key['req_4cd']||$key['req_3cl']||$key['req_gh']||$key['req_hs']||$key['req_fg'])
		$time_start_wh = $time_stop_cv;
	else
		$time_start_wh = $time_stop_cr;

//////// start to save ////////
				
		//$time_start_cv = $time_stop_cr;
		$this->Planning_model->savetotalplan($rowData,$choosendate,$this->formatDate($time_start_cr),$this->formatDate($time_stop_cr),$this->formatDate($time_start_cv),$this->formatDate($time_stop_cv),$this->formatDate($time_start_pt),$this->formatDate($time_stop_pt),$this->formatDate($time_start_wh),NULL);
		$this->Planning_model->savetostatustracking($rowData,$choosendate,$realDate,$this->formatDate($time_start_cr),$this->formatDate($time_stop_cr),$this->formatDate($time_start_cv),$this->formatDate($time_stop_cv),$this->formatDate($time_start_pt),$this->formatDate($time_stop_pt),$this->formatDate($time_start_wh),$mo_cr,$mo_cv,$mo_pt);
			
			
		//assign for next value
		$time_start_cr = $time_stop_cr;
		$time_start_cv = $time_stop_cv;
		
/**/	}
		
		//save to statusTracking
		echo "Data Saved as 	".$choosendate." Plan.";
	}
	
//	function savetotalplan() 
//	{
//		$delivery_id_list 	= ($this->input->post('deliveryid'))?$this->input->post('deliveryid'):'';
//		$today 				= ($this->input->post('today'))?$this->input->post('today'):'';
//		$corrugator_date 	= ($this->input->post('corrugator_date'))?$this->input->post('corrugator_date'):'';
//		$converter_date 	= ($this->input->post('converter_date'))?$this->input->post('converter_date'):'';
//		
//		$delivery_ids 		= explode("|",$delivery_id_list);	
//		$corrugator_dates 	= explode("|",$corrugator_date);
//		$converter_dates	= explode("|",$converter_date);
//		
//		$this->Planning_model->savetotalplan($delivery_ids,$corrugator_dates,$converter_dates,$today);
//	}
	
	function loadplanbydate()
	{
		$choosendate 	= ($this->input->post('choosendate'))?$this->input->post('choosendate'):'';	
		if($choosendate=='') return 'Error in date';	
		
		$resultDelivery = $this->Planning_model->loadplanbydate($choosendate);
		$deliveryList = array();
		$cnt=0;
		$this->load->model('Salesorder_model');
		foreach($resultDelivery->result() as $delivery)
		{
			$deliveryList[$cnt]['delivery_id']	= $delivery->delivery_id;
			$deliveryList[$cnt]['sales_order']	= $delivery->sales_order;
			
			$salesDetail = $this->Salesorder_model->getSalesDetail($delivery->sales_order);
			$deliveryList[$cnt]['purchase_order_no']	= $salesDetail->purchase_order_no;
			
			$deliveryList[$cnt]['product_code']	= $delivery->product_code;
			$partnerproduct = $this->Planning_model->getProduct_Partner($delivery->product_id);
			
			$deliveryList[$cnt]['product_name'] = $partnerproduct->product_name;
			$deliveryList[$cnt]['partner_name'] = $partnerproduct->partner_name;
			
			$deliveryList[$cnt]['p_width_inch']	= $partnerproduct->pc_paper_width;
			$deliveryList[$cnt]['t_length']		= $partnerproduct->cr_length;
			
			$productflutes	= $this->Planning_model->getProductFlutes($delivery->product_id,$delivery->product_code);
			if($productflutes->num_rows()>0){
				$deliveryList[$cnt]['flute']		= $productflutes->row()->flute;
			}else {
				$deliveryList[$cnt]['flute']			= "";
			}
			$productsTbl = $this->Planning_model->getProduct($delivery->product_code);
			if($productflutes->num_rows()>0){
				$deliveryList[$cnt]['DF']			= $delivery->DF;
				$deliveryList[$cnt]['BM']			= $delivery->BM;
				$deliveryList[$cnt]['BL']			= $delivery->BL;
				$deliveryList[$cnt]['CM']			= $delivery->CM;
				$deliveryList[$cnt]['CL']			= $delivery->CL;
			}else {
				$deliveryList[$cnt]['DF']			= "";
				$deliveryList[$cnt]['BM']			= "";
				$deliveryList[$cnt]['BL']			= "";
				$deliveryList[$cnt]['CM']			= "";
				$deliveryList[$cnt]['CL']			= "";
			}

			$deliveryList[$cnt]['cut']			= $partnerproduct->cut;
			
			$deliveryList[$cnt]['delivery_date']= $delivery->delivery_date;
			$deliveryList[$cnt]['qty']			= $delivery->amount_cr;
			$deliveryList[$cnt]['modified_on']	= $delivery->modified_on;
			$deliveryList[$cnt]['status']		= $delivery->status;
			$deliveryList[$cnt]['corrugator_date']	= substr($delivery->corrugator_date,0,10);
			$deliveryList[$cnt]['corrugator_time']	= substr($delivery->corrugator_date,11,5);
			$deliveryList[$cnt]['converter_date']	= substr($delivery->converter_date,0,10);
			$deliveryList[$cnt]['converter_time']	= substr($delivery->converter_date,11,5);
			$deliveryList[$cnt]['padpartition_date']	= substr($delivery->corrugator_date,0,10);
			$deliveryList[$cnt]['padpartition_time']	= substr($delivery->corrugator_date,11,5);
			$deliveryList[$cnt]['warehouse_date']	= substr($delivery->converter_date,0,10);
			$deliveryList[$cnt]['warehouse_time']	= substr($delivery->converter_date,11,5);
			log_message('info', substr($delivery->corrugator_date,11,5));
		//	$deliveryList[$cnt]['next_process'] = "";
		/*	$productCat = $this->Planning_model->getProductCat($delivery->product_id,$delivery->product_code);
			if($productCat->num_rows()>0){
				$deliveryList[$cnt]['next_process'] = $productCat->row()->next_process;
			}
			else
			{
				$deliveryList[$cnt]['next_process'] = "";
			}*/
			$cnt++;
		}

		//load JSON lib
		$this->load->library('JSON');	
		echo '{"planned" :'.$this->json->encode($deliveryList).',"count":"'.$cnt.'"}';
	}
	
	function reportplanning()
	{
		$this->load->view('planning/reportplanning');
	}
	
	function barcode($input)
	{



// Including all required classes
require('barcodegen/class/BCGFont.php');
require('barcodegen/class/BCGColor.php');
require('barcodegen/class/BCGDrawing.php'); 

// Including the barcode technology
include('barcodegen/class/BCGcode39.barcode.php'); 

// Loading Font
//$font = new BCGFont('barcodegen/class/font/Arial.ttf', 8);
 $font = new BCGFont('barcodegen/class/font/Arial.ttf',-1);
// The arguments are R, G, B for color.
$color_black = new BCGColor(0, 0, 0);
$color_white = new BCGColor(255, 255, 255); 

$code = new BCGcode39();
$code->setScale(1); // Resolution
$code->setThickness(30); // Thickness
$code->setForegroundColor($color_black); // Color of bars
$code->setBackgroundColor($color_white); // Color of spaces
$code->setFont($font); // Font (or 0)
//$code->parse($_GET['text']); // Text
$code->parse($input);

/* Here is the list of the arguments
1 - Filename (empty : display on screen)
2 - Background color */
$drawing = new BCGDrawing('', $color_white);
$drawing->setBarcode($code);
$drawing->draw();
// clean the output buffer
ob_clean();
// Header that says it is an image (remove it if you save the barcode to a file)
header('Content-Type: image/png');

// Draw (or save) the image into PNG format.
$drawing->finish(BCGDrawing::IMG_FORMAT_PNG);
//$this->load->view('planning/reportplanning', 'hello');
	}
}
?>
