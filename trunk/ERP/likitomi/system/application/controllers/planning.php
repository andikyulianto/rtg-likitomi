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
		$time_start_3cs = $time_start_cv;
		$time_start_2cl = $time_start_cv;
		$time_start_3cl = $time_start_cv;
		$time_start_3cm = $time_start_cv;
		$time_start_4cd = $time_start_cv;
		
		

		$time_stop_2cl=0;
		$time_stop_3cl=0;
		$time_stop_3cm=0;
		$time_stop_4cd=0;

		//$time_start_pt = (0.0006949*60)*8;
		//$time_start_wh = (0.0006949*60)*8;


			//count mo
			$mo_cr_count = 0;
			$mo_cv_count = 0;
			
			$date_mo_code = date('dm');

		foreach($gridData as $rowData)
		{
			//initialize 
			$mo_cr = "";
			$mo_cv = "";
			$mo_pt = "";
			
			// start stop time of CR 
			$query = $this->Planning_model->getProduct($rowData->product_code);
			$key = $query->row_array(0);							//get the only one object
		////////////	
		//create MO//
		////////////
		if($key['req_cr'])
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
			
			
			
			
			$case 	= $rowData->qty;
			if(($key['slit'])!=0)
			$cut2 	= $case/$key['slit'];
			$metre	= ($key['t_length']*$cut2)/1000;
			$timeuseCR = 0;
			$realDate = $choosendate;
		if((strtoupper($key['flute'])=="B")||(strtoupper($key['flute'])=="C"))
		{
			$timeuseCR = ($metre/120)+4;
		}
		else if((strtoupper($key['flute'])=="BC")||(strtoupper($key['flute'])=="W"))
		{
			$timeuseCR = ($metre/100)+4;
		}
		else $timeuseCR = 0;
		$time_stop_cr = $time_start_cr;
		if($timeuseCR!=0)
		{
			$time_stop_cr = $time_start_cr + $timeuseCR * 0.0006949;
		}
		if($key['req_3cs']||$key['req_2cl']||$key['req_3cl']||$key['req_3cm']||$key['req_4cd'])
		{
			//start stop time for CV
	#		print($key['req_3cm']);
			if($key['req_3cs'])
				$speed = 120;
			elseif($key['req_2cl'])
				$speed = 60;
			elseif($key['req_3cl'])
				$speed = 60;
			elseif($key['req_3cm'])
				$speed = 60;
			elseif($key['req_4cd'])
				$speed = 60;
			else
				$speed = 0;
			//echo $key['next_process']."". $speed ."<br>";
			//$time_stop_cv = $time_start_cv;
			if ($speed > 0)
				$timeuseCV = $rowData->qty / $speed;
			else
				$timeuseCV = 0;

			


		
			if($key['req_3cs'])
			{
				$time_start_3cs = $time_stop_cr;
				$time_stop_3cs = $time_start_3cs+ round($timeuseCV+30) * 0.0006949;
				$time_stop_cv = $time_stop_3cs;
			}
			elseif($key['req_2cl'])
			{
/*
				if((double)$time_stop_cr<(double)$time_stop_2cl)
				{
					$time_start_2cl = $time_stop_2cl;
//					print $rowData->product_code."--2CL "." $time_stop_cr $time_stop_2cl  $time_start_2cl "." --- $time_stop_2cl<br>";
				}
				else
				{
					$time_start_2cl = $time_stop_cr;
//					print $rowData->product_code."--CR"." $time_stop_cr $time_stop_2cl  $time_start_2cl "." --- $time_stop_cr <br>";
				}
*/				$time_start_2cl = $time_stop_cr;
				$time_stop_2cl = $time_start_2cl+ round($timeuseCV+30) * 0.0006949;
				$time_stop_cv = $time_stop_2cl;
			}
			elseif($key['req_3cl'])
			{
				$time_start_3cl = $time_stop_cr;
				$time_stop_3cl = $time_start_3cl+ round($timeuseCV+30) * 0.0006949;
				$time_stop_cv = $time_stop_3cl;
			}
			elseif($key['req_3cm'])
			{
/*				if($time_stop_cr<$time_stop_3cm)
				{
					$time_start_3cm = $time_stop_3cm;
					print $rowData->product_code."--3CM "." $time_stop_cr $time_stop_3cm  $time_start_3cm "." --- $time_stop_3cm<br>";
				}
				else
				{
					$time_start_3cm = $time_stop_cr;
					print $rowData->product_code."--3CM"." $time_stop_cr $time_stop_3cm  $time_start_3cm "." --- $time_stop_cr <br>";
				}
*/				$time_start_3cm = $time_stop_cr;
				$time_stop_3cm = $time_start_3cm+ round($timeuseCV+30) * 0.0006949;
				$time_stop_cv = $time_stop_3cm;
			}
			elseif($key['req_4cd'])
			{
				$time_start_4cd = $time_stop_cr;
				$time_stop_4cd = $time_start_4cd+ round($timeuseCV+30) * 0.0006949;
				$time_stop_cv = $time_stop_4cd;
			}
			else
				$time_stop_cv = $time_start_cv;
			$time_start_wh = $time_stop_cv;
		}
		else{
			$time_stop_cv = NULL;
			$time_start_cv= NULL;
			$time_start_wh = $time_stop_cr;
		}
		if($key['req_rd']||$key['req_ss']||$key['req_remove']||$key['req_foam']||$key['req_tape'])
		{
			
			if($key['req_3cs']||$key['req_2cl']||$key['req_3cl']||$key['req_3cm']||$key['req_4cd']){
				$time_start_pt = $time_stop_cv + round(10) * 0.0006949;
			}
			elseif($key['req_cr']){
				$time_start_pt = $time_stop_cr + round(10) * 0.0006949;
			}
			else
				$time_start_pt = NULL;
			$time_stop_pt = $time_start_pt +round(($key['req_rd']+ $key['req_ss']+$key['req_remove']+$key['req_foam']+$key['req_tape'])* 30) * 0.0006949;
			$time_start_wh = $time_stop_pt +round(10) * 0.0006949;
		}
		else
		{
			$time_start_pt = NULL;
			$time_stop_pt = NULL;
		}
 		log_message('info','product code:'.$rowData->product_code);
 		log_message('info', 'CR Start :'.$time_start_cr.'CR Stop :'.$time_stop_cr);

		
		//echo $rowData;
		//$rowData['time_start_cr'] = $time_start_cr;
			//print_r($rowData);
			//print_r($key->row_array(0));
			
			
#			$this->Planning_model->savetotalplan($rowData,$choosendate,$this->formatDate($time_start_cr),$this->formatDate($time_stop_cr),$this->formatDate($time_start_cv),$this->formatDate($time_stop_cv),$this->formatDate($time_start_pt),$this->formatDate($time_stop_pt),$this->formatDate($time_start_wh),$key);
#			//Save to  status tracking
#			$this->Planning_model->savetostatustracking($rowData,$choosendate,$this->formatDate($time_start_cr),$this->formatDate($time_stop_cr),$this->formatDate($time_start_cv),$this->formatDate($time_stop_cv),$this->formatDate($time_start_pt),$this->formatDate($time_stop_pt),$this->formatDate($time_start_wh));


#					echo $key['next_process'];

			
		if($key['req_3cs'])
		{
			$time_stop_3cs = $time_start_3cs+ round($timeuseCV+30) * 0.0006949;
			
						//$choosendate,$realDate
			$tempCRStart = $time_start_cr;
			$tempCRStop = $time_stop_cr;
//			echo "print 3cs==".$time_start_3cs."----";
			log_message('info', 'CR Start (3cs b):'.$time_start_cr.'CR Stop :'.$time_stop_cr);
			log_message('info', '3CS Start (3cs b):'.$time_start_3cs.'3CS Stop :'.$time_stop_3cs);
			log_message('info', 'PT Start (3cs b):'.$time_start_pt.'PT Stop :'.$time_stop_pt);
			log_message('info', 'WH Start (3cs b):'.$time_start_wh);			
			if((double)$time_start_cr >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				(double)$time_start_cr-=1;
				(double)$time_stop_cr-=1;
			
			}
			elseif ((double)$time_stop_cr >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				(double)$time_stop_cr-=1;
			}

			//check cv
			if((double)$time_start_3cs >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				//(double)$time_start_cv-=1;
				(double)$time_stop_cv-=1;
				(double)$time_start_3cs-=1;
				(double)$time_stop_3cs-=1;
			
			}
			elseif ((double)$time_stop_3cs >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				(double)$time_stop_cv-=1;
				(double)$time_stop_3cs-=1;
			}
			//check wh
			if((double)$time_start_wh >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				(double)$time_start_wh-=1;
				//(double)$time_stop_cr-=1;
			
			}
			log_message('info', 'CR Start (3cs a):'.$time_start_cr.'CR Stop :'.$time_stop_cr.' choose date:'.$choosendate.' real date:'.$realDate);
			log_message('info', '3CS Start (3cs a):'.$time_start_3cs.'3CS Stop :'.$time_stop_3cs.' choose date:'.$choosendate.' real date:'.$realDate);
			log_message('info', 'PT Start (3cs a):'.$time_start_pt.'PT Stop :'.$time_stop_pt.' choose date:'.$choosendate.' real date:'.$realDate);
			log_message('info', 'WH Start (3cs a):'.$time_start_wh);	
//			echo $rowData->product_code."req_3cs ".$time_stop_cv." ".$choosendate."<br>";
			
			$this->Planning_model->savetotalplan($rowData,$choosendate,$this->formatDate($time_start_cr),$this->formatDate($time_stop_cr),$this->formatDate($time_start_3cs),$this->formatDate($time_stop_3cs),$this->formatDate($time_start_pt),$this->formatDate($time_stop_pt),$this->formatDate($time_start_wh),$key);
			//Save to  status tracking
			$this->Planning_model->savetostatustracking($rowData,$choosendate,$realDate,$this->formatDate($time_start_cr),$this->formatDate($time_stop_cr),$this->formatDate($time_start_3cs),$this->formatDate($time_stop_3cs),$this->formatDate($time_start_pt),$this->formatDate($time_stop_pt),$this->formatDate($time_start_wh),$mo_cr,$mo_cv,$mo_pt);
			$time_start_cr = $tempCRStart ;
			$time_stop_cr= $tempCRStop;

			$time_stop_cv = $time_stop_3cs;
		}
		elseif($key['req_2cl'])
		{
			if((double)$time_stop_cr<(double)$time_stop_2cl)
				$time_start_2cl = $time_stop_2cl;
			else
				$time_start_2cl = $time_stop_cr;
			$time_stop_2cl = $time_start_2cl+ round($timeuseCV+30) * 0.0006949;
			$tempCRStart = $time_start_cr;
			$tempCRStop = $time_stop_cr;
			log_message('info', 'CR Start (2cl b):'.$time_start_cr.'CR Stop :'.$time_stop_cr);
			log_message('info', '2CL Start (2cl b):'.$time_start_2cl.'2CL Stop :'.$time_stop_2cl);
			log_message('info', 'PT Start (2cl b):'.$time_start_pt.'PT Stop :'.$time_stop_pt);
			log_message('info', 'WH Start (2cl b):'.$time_start_wh);	
//			echo "print CV==".$time_stop_cv."----";
			if((double)$time_start_cr >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				(double)$time_start_cr-=1;
				(double)$time_stop_cr-=1;
			
			}
			elseif ((double)$time_stop_cr >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				(double)$time_stop_cr-=1;
			}
			//check cv
			if((double)$time_start_2cl >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				(double)$time_stop_cv-=1;
				(double)$time_start_2cl-=1;
				(double)$time_stop_2cl-=1;
			
			}
			elseif ((double)$time_stop_2cl >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				(double)$time_stop_cv-=1;
				(double)$time_stop_2cl-=1;
			}
			//check wh
			if((double)$time_start_wh >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				(double)$time_start_wh-=1;
				//(double)$time_stop_cr-=1;
			
			}
			log_message('info', 'CR Start (2cl a):'.$time_start_cr.'CR Stop :'.$time_stop_cr.' choose date:'.$choosendate.' real date:'.$realDate);
			log_message('info', '2CL Start (2cl a):'.$time_start_2cl.'2CL Stop :'.$time_stop_2cl.' choose date:'.$choosendate.' real date:'.$realDate);
			log_message('info', 'PT Start (2cl a):'.$time_start_pt.'PT Stop :'.$time_stop_pt.' choose date:'.$choosendate.' real date:'.$realDate);
			log_message('info', 'WH Start (2cl a):'.$time_start_wh.' choose date:'.$choosendate.' real date:'.$realDate);	
//			echo $rowData->product_code."req_2cl ".$time_stop_cv." ".$choosendate."<br>";
			
			
			
			$this->Planning_model->savetotalplan($rowData,$choosendate,$this->formatDate($time_start_cr),$this->formatDate($time_stop_cr),$this->formatDate($time_start_2cl),$this->formatDate($time_stop_2cl),$this->formatDate($time_start_pt),$this->formatDate($time_stop_pt),$this->formatDate($time_start_wh),$key);
			//Save to  status tracking
			$this->Planning_model->savetostatustracking($rowData,$choosendate,$realDate,$this->formatDate($time_start_cr),$this->formatDate($time_stop_cr),$this->formatDate($time_start_2cl),$this->formatDate($time_stop_2cl),$this->formatDate($time_start_pt),$this->formatDate($time_stop_pt),$this->formatDate($time_start_wh),$mo_cr,$mo_cv,$mo_pt);
			
//			$choosendate = $tempDate;
			$time_start_cr = $tempCRStart ;
			$time_stop_cr= $tempCRStop;
			$time_stop_cv = $time_stop_2cl;
		}
		elseif($key['req_3cl'])
		{

			$time_stop_3cl = $time_start_3cl+ round($timeuseCV+30) * 0.0006949;
			
						//$choosendate,$realDate
			$tempCRStart = $time_start_cr;
			$tempCRStop = $time_stop_cr;
			log_message('info', 'CR Start (3CL b):'.$time_start_cr.'CR Stop :'.$time_stop_cr);
			log_message('info', '3CL Start (3CL b):'.$time_start_3cl.'3CL Stop :'.$time_stop_3cl);
			log_message('info', 'PT Start (3CL b):'.$time_start_pt.'PT Stop :'.$time_stop_pt);
			log_message('info', 'WH Start(3CL b):'.$time_start_wh);	
//			echo "print CV==".$time_stop_cv."----";
			if((double)$time_start_cr >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				(double)$time_start_cr-=1;
				(double)$time_stop_cr-=1;
			
			}
			elseif ((double)$time_stop_cr >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				(double)$time_stop_cr-=1;
			}
			//check cv
			if((double)$time_start_3cl >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				//(double)$time_start_cv-=1;
				(double)$time_stop_cv-=1;
				(double)$time_start_3cl-=1;
				(double)$time_stop_3cl-=1;
			
			}
			elseif ((double)$time_stop_3cl >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				(double)$time_stop_cv-=1;
				(double)$time_stop_3cl-=1;
			}
			//check wh
			if((double)$time_start_wh >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				(double)$time_start_wh-=1;
				//(double)$time_stop_cr-=1;
			
			}
			log_message('info', 'CR Start (3CL a):'.$time_start_cr.'CR Stop :'.$time_stop_cr.' choose date:'.$choosendate.' real date:'.$realDate);
			log_message('info', '3CL Start (3CL a):'.$time_start_3cl.'3CL Stop :'.$time_stop_3cl.' choose date:'.$choosendate.' real date:'.$realDate);
			log_message('info', 'PT Start (3CL a):'.$time_start_pt.'PT Stop :'.$time_stop_pt.' choose date:'.$choosendate.' real date:'.$realDate);
			log_message('info', 'WH Start (3CL a):'.$time_start_wh);
//			echo $rowData->product_code."-3cl".$time_stop_cv." <br>";
			$this->Planning_model->savetotalplan($rowData,$choosendate,$this->formatDate($time_start_cr),$this->formatDate($time_stop_cr),$this->formatDate($time_start_3cl),$this->formatDate($time_stop_3cl),$this->formatDate($time_start_pt),$this->formatDate($time_stop_pt),$this->formatDate($time_start_wh),$key);
			//Save to  status tracking
			$this->Planning_model->savetostatustracking($rowData,$choosendate,$realDate,$this->formatDate($time_start_cr),$this->formatDate($time_stop_cr),$this->formatDate($time_start_3cl),$this->formatDate($time_stop_3cl),$this->formatDate($time_start_pt),$this->formatDate($time_stop_pt),$this->formatDate($time_start_wh),$mo_cr,$mo_cv,$mo_pt);

			$time_start_cr = $tempCRStart ;
			$time_stop_cr= $tempCRStop;
			$time_stop_cv = $time_stop_3cl;
		}
		elseif($key['req_3cm'])
		{
			if((double)$time_stop_cr<(double)$time_stop_3cm)
				$time_start_3cm = $time_stop_3cm;
			else
				$time_start_3cm = $time_stop_cr;
			$time_stop_3cm = $time_start_3cm+ round($timeuseCV+30) * 0.0006949;
			
						//$choosendate,$realDate
			$tempCRStart = $time_start_cr;
			$tempCRStop = $time_stop_cr;
			log_message('info', 'CR Start (3CM b):'.$time_start_cr.'CR Stop :'.$time_stop_cr);
			log_message('info', '3CM Start (3CM b):'.$time_start_3cm.'3CM Stop :'.$time_stop_3cm);
			log_message('info', 'PT Start (3CM b):'.$time_start_pt.'PT Stop :'.$time_stop_pt);
			log_message('info', 'WH Start (3CM b):'.$time_start_wh);
//			echo "print 3CM==".$time_start_3cm."----";
			if((double)$time_start_cr >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				(double)$time_start_cr-=1;
				(double)$time_stop_cr-=1;
			
			}
			elseif ((double)$time_stop_cr >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				(double)$time_stop_cr-=1;
			}
			//check cv
			if((double)$time_start_3cm >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				//(double)$time_start_cv-=1;
				(double)$time_stop_cv-=1;
				(double)$time_start_3cm-=1;
				(double)$time_stop_3cm-=1;
			
			}
			elseif ((double)$time_stop_3cm >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				(double)$time_stop_cv-=1;
				(double)$time_stop_3cm-=1;
			}
			//check wh
			if((double)$time_start_wh >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				(double)$time_start_wh-=1;
				//(double)$time_stop_cr-=1;
			
			}
			log_message('info', 'CR Start (3CM a):'.$time_start_cr.'CR Stop :'.$time_stop_cr.' choose date:'.$choosendate.' real date:'.$realDate);
			log_message('info', '3CM Start (3CM a):'.$time_start_3cm.'3CM Stop :'.$time_stop_3cm.' choose date:'.$choosendate.' real date:'.$realDate);
			log_message('info', 'PT Start (3CM a):'.$time_start_pt.'PT Stop :'.$time_stop_pt.' choose date:'.$choosendate.' real date:'.$realDate);
			log_message('info', 'WH Start (3CM a):'.$time_start_wh);
//				echo $rowData->product_code."-3cm ".$time_stop_cr."<br>";
			$this->Planning_model->savetotalplan($rowData,$choosendate,$this->formatDate($time_start_cr),$this->formatDate($time_stop_cr),$this->formatDate($time_start_3cm),$this->formatDate($time_stop_3cm),$this->formatDate($time_start_pt),$this->formatDate($time_stop_pt),$this->formatDate($time_start_wh),$key);
			//Save to  status tracking
			$this->Planning_model->savetostatustracking($rowData,$choosendate,$realDate,$this->formatDate($time_start_cr),$this->formatDate($time_stop_cr),$this->formatDate($time_start_3cm),$this->formatDate($time_stop_3cm),$this->formatDate($time_start_pt),$this->formatDate($time_stop_pt),$this->formatDate($time_start_wh),$mo_cr,$mo_cv,$mo_pt);

			$time_start_cr = $tempCRStart ;
			$time_stop_cr= $tempCRStop;
			$time_stop_cv = $time_stop_3cm;
		}
		elseif($key['req_4cd'])
		{
	
			$time_stop_4cd = $time_start_4cd+ round($timeuseCV+30) * 0.0006949;
			
			//$choosendate,$realDate
			$tempCRStart = $time_start_cr;
			$tempCRStop = $time_stop_cr;
			log_message('info', 'CR Start (4CD b):'.$time_start_cr.'CR Stop :'.$time_stop_cr);
			log_message('info', '4CD Start (4CD b):'.$time_start_4cd.'4CD Stop :'.$time_stop_4cd);
			log_message('info', 'PT Start (4CD b):'.$time_start_pt.'PT Stop :'.$time_stop_pt);
			log_message('info', 'WH Start (4CD b):'.$time_start_wh);
//			echo "print wh==".$time_start_wh."----";
			if((double)$time_start_cr >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				(double)$time_start_cr-=1;
				(double)$time_stop_cr-=1;
			
			}
			elseif ((double)$time_stop_cr >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				(double)$time_stop_cr-=1;
			}
			//check cv
			if((double)$time_start_4cd >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				//(double)$time_start_cv-=1;
				(double)$time_stop_cv-=1;
				(double)$time_start_4cd-=1;
				(double)$time_stop_4cd-=1;
			
			}
			elseif ((double)$time_stop_4cd >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				(double)$time_stop_cv-=1;
				(double)$time_stop_4cd-=1;
			}
			//check wh
			if((double)$time_start_wh >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				(double)$time_start_wh-=1;
				//(double)$time_stop_cr-=1;
			
			}
			log_message('info', 'CR Start (4CD a):'.$time_start_cr.'CR Stop :'.$time_stop_cr.' choose date:'.$choosendate.' real date:'.$realDate);
			log_message('info', '4CD Start (4CD a):'.$time_start_4cd.'4CD Stop :'.$time_stop_4cd.' choose date:'.$choosendate.' real date:'.$realDate);
			log_message('info', 'PT Start (4CD a):'.$time_start_pt.'PT Stop :'.$time_stop_pt.' choose date:'.$choosendate.' real date:'.$realDate);
			log_message('info', 'WH Start (4CD a):'.$time_start_wh);
//			echo $rowData->product_code."-4cd time start wh".$time_start_wh."<br>";
			$this->Planning_model->savetotalplan($rowData,$choosendate,$this->formatDate($time_start_cr),$this->formatDate($time_stop_cr),$this->formatDate($time_start_4cd),$this->formatDate($time_stop_4cd),$this->formatDate($time_start_pt),$this->formatDate($time_stop_pt),$this->formatDate($time_start_wh),$key);
			//Save to  status tracking
			$this->Planning_model->savetostatustracking($rowData,$choosendate,$realDate,$this->formatDate($time_start_cr),$this->formatDate($time_stop_cr),$this->formatDate($time_start_4cd),$this->formatDate($time_stop_4cd),$this->formatDate($time_start_pt),$this->formatDate($time_stop_pt),$this->formatDate($time_start_wh),$mo_cr,$mo_cv,$mo_pt);

			$time_start_cr = $tempCRStart ;
			$time_stop_cr= $tempCRStop;
			$time_stop_cv = $time_stop_4cd;
		}
		elseif($key['req_rd']||$key['req_ss']||$key['req_remove']||$key['req_foam']||$key['req_tape']){
			log_message('info', 'CR Start (In PT):'.$time_start_cr.'CR Stop :'.$time_stop_cr.' choose date:'.$choosendate.' real date:'.$realDate);
			log_message('info', 'PT Start (In PT):'.$time_start_pt.'PT Stop :'.$time_stop_pt.' choose date:'.$choosendate.' real date:'.$realDate);
			log_message('info', 'WH Start (In PT):'.$time_start_wh.' choose date:'.$choosendate.' real date:'.$realDate);
//	echo $rowData->product_code."-pt".$time_start_cr."<br>";
	

			$this->Planning_model->savetotalplan($rowData,$choosendate,$this->formatDate($time_start_cr),$this->formatDate($time_stop_cr),NULL,NULL,$this->formatDate($time_start_pt),$this->formatDate($time_stop_pt),$this->formatDate($time_start_wh),$key);
			//Save to  status tracking
			$this->Planning_model->savetostatustracking($rowData,$choosendate,$realDate,$this->formatDate($time_start_cr),$this->formatDate($time_stop_cr),NULL,NULL,$this->formatDate($time_start_pt),$this->formatDate($time_stop_pt),$this->formatDate($time_start_wh),$mo_cr,$mo_cv,$mo_pt);

		}
		elseif(!($key['req_3cs']||$key['req_2cl']||$key['req_3cl']||$key['req_3cm']||$key['req_4cd']))
		{
			$tempCRStart = $time_start_cr;
			$tempCRStop = $time_stop_cr;
			log_message('info', 'CR Start (Not in CV b):'.$time_start_cr.'CR Stop :'.$time_stop_cr);
			log_message('info', 'PT Start (Not in CV b):'.$time_start_pt.'PT Stop :'.$time_stop_pt);
			log_message('info', 'WH Start (Not in CV b):'.$time_start_wh);
//	echo $rowData->product_code."-not cv ".$time_stop_cr."<br>";
			
			if((double)$time_start_cr >=1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				(double)$time_start_cr-=1;
				(double)$time_stop_cr-=1;
			
			}
			elseif ((double)$time_stop_cr >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				(double)$time_stop_cr-=1;
			}
			if((double)$time_start_wh >= 1)
			{
				$realDate = date("Y-m-d",strtotime("+1 day",strtotime($choosendate)));
				(double)$time_start_wh-=1;
				//(double)$time_stop_cr-=1;
			
			}
			log_message('info', 'CR Start (Not in CV a):'.$time_start_cr.'CR Stop :'.$time_stop_cr.' choose date:'.$choosendate.' real date:'.$realDate);
			log_message('info', 'PT Start (Not in CV a):'.$time_start_pt.'PT Stop :'.$time_stop_pt.' choose date:'.$choosendate.' real date:'.$realDate);
			log_message('info', 'WH Start (Not in CV a):'.$time_start_wh.' choose date:'.$choosendate.' real date:'.$realDate);
			$this->Planning_model->savetotalplan($rowData,$choosendate,$this->formatDate($time_start_cr),$this->formatDate($time_stop_cr),NULL,NULL,$this->formatDate($time_start_pt),$this->formatDate($time_stop_pt),$this->formatDate($time_start_wh),$key);
			//Save to  status tracking
			$this->Planning_model->savetostatustracking($rowData,$choosendate,$realDate,$this->formatDate($time_start_cr),$this->formatDate($time_stop_cr),NULL,NULL,$this->formatDate($time_start_pt),$this->formatDate($time_stop_pt),$this->formatDate($time_start_wh),$mo_cr,$mo_cv,$mo_pt);
			
			
			
			$time_start_cr = $tempCRStart ;
			$time_stop_cr= $tempCRStop;
			
		}
		elseif(!($key['req_rd']||$key['req_ss']||$key['req_remove']||$key['req_foam']||$key['req_tape']||$key['req_3cs']||$key['req_2cl']||$key['req_3cl']||$key['req_3cm']||$key['req_4cd']))
		{
			log_message('info', 'CR Start (Not in CV/PT):'.$time_start_cr.'CR Stop :'.$time_stop_cr.' choose date:'.$choosendate.' real date:'.$realDate);
			log_message('info', 'PT Start (Not in CV/PT):'.$time_start_pt.'PT Stop :'.$time_stop_pt.' choose date:'.$choosendate.' real date:'.$realDate);
			log_message('info', 'WH Start (Not in CV/PT):'.$time_start_wh.' choose date:'.$choosendate.' choose date:'.$realDate);
//	echo $rowData->product_code."-not pt not cv ".$time_start_cr."<br>";
			$this->Planning_model->savetotalplan($rowData,$choosendate,$this->formatDate($time_start_cr),$this->formatDate($time_stop_cr),NULL,NULL,NULL,NULL,$this->formatDate($time_start_wh),$key);
			//Save to  status tracking
			$this->Planning_model->savetostatustracking($rowData,$choosendate,$realDate,$this->formatDate($time_start_cr),$this->formatDate($time_stop_cr),NULL,NULL,NULL,NULL,$this->formatDate($time_start_wh),$mo_cr,$mo_cv,$mo_pt);
			
			
			$time_start_cr = $tempCRStart ;
			$time_stop_cr= $tempCRStop;
		}
		else
		
		$time_stop_cv = $time_stop_cv;
		if($time_stop_cr<$time_stop_2cl)
			$time_start_2cl = $time_stop_2cl;
		else
			$time_start_2cl = $time_stop_cr;
		$time_start_3cl = $time_stop_3cl;
		$time_start_3cm = $time_stop_3cm;
		$time_start_4cd = $time_stop_4cd;
		
		$time_start_cr = $time_stop_cr;
			log_message('info', '-----------------');
			


/**/		}
		
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
