<?php
class Clampliftmanger extends Controller {
	
	function __construct() 
	{
		parent::Controller();
		$this->freakauth_light->check();
		//$this->lang->load('products', 'english');
		$this->load->database();
		$this->load->model('Clamplift_model');
		$this->load->library('JSON');	
	
	}
	
	function index()
	{
		$data = array(
	      'contentClass' => $this,
	      'title' => "Clamplift Manager | Likitomi ERP",
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
		return $script;
	}	
	
	function getStyles()
	{
		$styles  ='@import "'.base_url().'static/css/common.css";';
		$styles	.='@import "'.base_url().'resources/css/ext-all.css";';
		$styles	.='@import "'.base_url().'static/css/clampliftmanager.css";';
		return $styles;
	}
	
	function show()
	{
		$this->load->view('clamplift/clampliftmanager');
	}
	
	function getclampliftreport()
	{
		$today  	= date('Y-m-d');
		$plandate 	= ($this->input->post('plandate'))?$this->input->post('plandate'):$today;
		$query1 	= $this->Clamplift_model->getLocalData($plandate);
		
		if($query1->num_rows()>0)
		{
			$resultCorrugatorClamplift = $query1;
			$cnt = $resultCorrugatorClamplift->num_rows();
			
			echo '{"clamplift" :'.$this->json->encode($resultCorrugatorClamplift->result()).',"count":"'.$cnt.'"}';
		}
		else {
			$this->getclampliftreport_localdb($plandate);
		}
		
	}
	
	function getclampliftreport_localdb($plandate)
	{
		$this->load->model('Planning_model');
		$resultCorrugatorClamplift = $this->Planning_model->corrugatorclamplift($plandate);
		$clampliftList = array();
		$cnt=0;
		$firstTime = (0.0006949*60)*8+(0.0006949*0);
		$timeStart = $firstTime;
		foreach ($resultCorrugatorClamplift->result() as $key)
		{
			$case 	= $key->qty/($key->cut);
			$cut2 	= $key->qty/($key->cut*$key->slit);
			$used_df = ($key->t_length*$cut2)/1000;
			$used_bl = ($key->BL=="")?"":($key->t_length*$cut2)/1000;
			$used_cl = ($key->CL=="")?"":($key->t_length*$cut2)/1000;
			
			$used_bm = ($key->BM=="")?"":(($key->t_length*$cut2)/1000)*1.44;
			$used_cm = ($key->CM=="")?"":(($key->t_length*$cut2)/1000)*1.48;
			
			$p_width_inch = $key->p_width_mm/25.6 ; //Adopted From Lotus File
			
			$metre	= ($key->t_length*$cut2)/1000;
			$timeuse = 0;
			if((strtoupper($key->flute)=="B")||(strtoupper($key->flute)=="C"))
			{
				$timeuse = ($metre/120)+4;
			}
			else if((strtoupper($key->flute)=="BC")||(strtoupper($key->flute)=="W"))
			{
				$timeuse = ($metre/100)+4;
			}
			else $timeuse = 0;
			
			$timeStop = $timeStart;
			//=IF(AD7=0,0,(A6+(AD7*0.0006949)))
			if($timeuse!=0)
			{
				$timeStop = $timeStart + $timeuse * 0.0006949;
			}
			//IF(A7>=(0.0006949*0*11.5),IF(A7<=(0.0006949*0*12.5),(A7)+(0.0006949*0),A7),A7)
			
			$used_df_lkg = $p_width_inch * 25.4  * $used_df * $this->getGrade($key->DF) / 1000000;
			$used_bl_lkg = $p_width_inch * 25.4  * $used_bl * $this->getGrade($key->BL) / 1000000; 
			$used_cl_lkg = $p_width_inch * 25.4  * $used_cl * $this->getGrade($key->CL) / 1000000; 
			
			$used_bm_lkg = $p_width_inch * 25.4  * $used_bm * $this->getGrade($key->BM) / 1000000; 
			$used_cm_lkg = $p_width_inch * 25.4  * $used_cm * $this->getGrade($key->CM) / 1000000; 
			
			$used_df_mkg = $used_df_lkg * 1.03;
			$used_bl_mkg = $used_bl_lkg * 1.03;
			$used_cl_mkg = $used_cl_lkg * 1.03;
			$used_bm_mkg = $used_bm_lkg * 1.03;
			$used_cm_mkg = $used_cm_lkg * 1.03;
			
			$clampliftList[$cnt]['start_time']		= $this->formatDate($timeStart);
			$clampliftList[$cnt]['stop_time']		= $this->formatDate($timeStop);
			$clampliftList[$cnt]['product_code']	= $key->product_code;
			$clampliftList[$cnt]['product_name']	= $key->product_name;			
			$clampliftList[$cnt]['partner_name']	= $key->partner_name;
			$clampliftList[$cnt]['sales_order']		= $key->sales_order;
			$clampliftList[$cnt]['autoid']			= $key->autoid;
			$clampliftList[$cnt]['flute']			= $key->flute;
			$clampliftList[$cnt]['DF']				= $key->DF;
			$clampliftList[$cnt]['BL']				= $key->BL;
			$clampliftList[$cnt]['CL']				= $key->CL;
			$clampliftList[$cnt]['BM']				= $key->BM;
			$clampliftList[$cnt]['CM']				= $key->CM;
			
			$clampliftList[$cnt]['p_width_mm']		= $key->p_width_mm;
			$clampliftList[$cnt]['p_width_inch']	= $key->p_width_inch;
			
			$clampliftList[$cnt]['used_df']			= round($used_df);
			$clampliftList[$cnt]['used_bl']			= round($used_bl);
			$clampliftList[$cnt]['used_cl']			= round($used_cl);
			$clampliftList[$cnt]['used_bm']			= round($used_bm);
			$clampliftList[$cnt]['used_cm']			= round($used_cm);
			
			$clampliftList[$cnt]['used_df_lkg']		= round($used_df_lkg);
			$clampliftList[$cnt]['used_bl_lkg']		= round($used_bl_lkg);
			$clampliftList[$cnt]['used_cl_lkg']		= round($used_cl_lkg);
			$clampliftList[$cnt]['used_bm_lkg']		= round($used_bm_lkg);
			$clampliftList[$cnt]['used_cm_lkg']		= round($used_cm_lkg);
			
			$clampliftList[$cnt]['used_df_mkg']		= round($used_df_mkg);
			$clampliftList[$cnt]['used_bl_mkg']		= round($used_bl_mkg);
			$clampliftList[$cnt]['used_cl_mkg']		= round($used_cl_mkg);
			$clampliftList[$cnt]['used_bm_mkg']		= round($used_bm_mkg);
			$clampliftList[$cnt]['used_cm_mkg']		= round($used_cm_mkg);
			
			$clampliftList[$cnt]['t_length']		= $key->t_length;
			$clampliftList[$cnt]['case']			= round($case);
			$clampliftList[$cnt]['cut']				= round($cut2);			
			
			$cnt++;
			$timeStart = $timeStop;
		}

		//load JSON lib
		$this->load->library('JSON');	
		echo '{"clamplift" :'.$this->json->encode($clampliftList).',"count":"'.$cnt.'"}';
		
	}
	
	function deletethisday()
	{
		$choosendate 	= ($this->input->post('choosendate'))?$this->input->post('choosendate'):date('Y-m-d');
		$this->Clamplift_model->deleteOnly($choosendate);	
	}
	
	function saveclampliftjson()
	{
		$jsonData 		= ($this->input->post('data'))?$this->input->post('data'):'';
		$choosendate 	= ($this->input->post('choosendate'))?$this->input->post('choosendate'):date('Y-m-d');		
		if($jsonData == '') return false;
		//load JSON lib
		$this->load->library('JSON');
		$gridData = $this->json->decode($jsonData);	
		$this->Clamplift_model->deleteAndAdd($gridData,$choosendate);
	}

	function getGrade($machine)
	{
		$charArray = str_split($machine);
		$grade = "";
		foreach ($charArray as $c)
		{
			if(ctype_digit($c)) 
			{
				$grade .= $c;
			}
		}
		return $this->parseInt($grade);
	}
	
	function parseInt($string) {
		// return intval($string);
		if(preg_match('/(\d+)/', $string, $array)) {
			return $array[1];
		} else {
			return 0;
		}
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
	
	function getStatus()
	{
		$today  	= date('Y-m-d');
		$plandate 	= ($this->input->post('plandate'))?$this->input->post('plandate'):$today;
		$resultCorrugatorClamplift 	= $this->Clamplift_model->getLocalData($plandate);
		if($resultCorrugatorClamplift->num_rows()>0)
		{
			$data['plandate'] = $plandate;
			$data['resultCorrugatorClamplift'] = $resultCorrugatorClamplift;
			$data['getsynctime'] = $this->getSyncTime($plandate);
			$this->load->view('clamplift/clampliftstatus',$data);
		}
		else {
			echo "<br/><br/><h3> NO Records Available for ". $plandate."</h3>";
		}
	}
	
	function getSyncTime($plandate)
	{
		$resultSync 	= $this->Clamplift_model->getSyncTime($plandate);
		if($resultSync->num_rows()>0)
		{
			return "Lasted Saved: ".$resultSync->row()->created_on;
		}
		else 
		{
			return "Never Saved";
		}
	}

	function syncdata()
	{
		$jsonData 		= ($this->input->post('jsondata'))?$this->input->post('jsondata'):'';
		if($jsonData == '') echo "Nothing To Sync";
		
		$this->load->library('JSON');
		$data['gridData'] = $this->json->decode($jsonData);	
		
		$this->load->view('clamplift/syncclampliftdata',$data);
	}
}
?>
