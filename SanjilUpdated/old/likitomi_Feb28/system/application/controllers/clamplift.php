<?php

class Clamplift extends Controller {
	
	function Clamplift()
	{
		parent::Controller();	
		$this->lang->load('clamplift', 'english');
		$this->load->model('Clamplift_model');	
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
		$script='';
		$script .= '<script type="text/javascript" src="'.base_url().'resources/javascript/ext/ext-base.js"></script>';
		$script .= '<script type="text/javascript" src="'.base_url().'resources/javascript/ext-all.js"></script>';
		$script .= '<script type="text/javascript" src="'.base_url().'resources/javascript/mootools/mootools-smoothscroll.js"></script>';
		$script .= '<script type="text/javascript" src="'.base_url().'static/javascript/table.js"></script>';
		return $script;
	}	
	function getStyles()
	{
		$styles  ='@import "'.base_url().'static/css/clamplift.css";';
		$styles	.='@import "'.base_url().'resources/css/ext-all.css";';
		$styles .='@import "'.base_url().'resources/css/xtheme-gray.css";';
		return $styles;
	}
	
	function show()
	{		
		$data['results'] = $this->Clamplift_model->getTaskByDate(date('Y-m-d'));
		$data['totalRec'] = $data['results']->num_rows();	
	
		$taskTable = array();
		$RowCnt=0;
		$lastTime='00:00';
		$changeRow =0;
		
		$currentTime = date('H:i'); 
		$minDiffTime = (60*60*24); $diffTime =0;
		$now =0;
		foreach ($data['results']->result() as $row)
		{
			$thisTime = substr($row->start,0,5);
			$diffTime = $this->timeDiff($lastTime,$thisTime);
			$changeRow = ($diffTime>=900)?1:0;
			$status = $row->status; 
			$diffTime = $this->timeDiff($currentTime,$thisTime);
			if($minDiffTime>$diffTime){
				$minDiffTime= $diffTime;
				$now = $RowCnt;
			}			
			if($changeRow) 
			{
				$RowCnt++;
				$lastTime = $thisTime;
				$taskTable[$RowCnt]= array();
				$taskTable[$RowCnt]['time'] =$thisTime;	
				$taskTable[$RowCnt]['rowDF'] = $row->id.'|'.$row->DF.'|'.$status.'|'.$row->pono;
				$taskTable[$RowCnt]['rowBM'] = $row->id.'|'.$row->BM.'|'.$status.'|'.$row->pono;
				$taskTable[$RowCnt]['rowBL'] = $row->id.'|'.$row->BL.'|'.$status.'|'.$row->pono;
				$taskTable[$RowCnt]['rowCM'] = $row->id.'|'.$row->CM.'|'.$status.'|'.$row->pono;
				$taskTable[$RowCnt]['rowCL'] = $row->id.'|'.$row->CL.'|'.$status.'|'.$row->pono;	
			}
			else 
			{
				$taskTable[$RowCnt]['rowDF'] .= '|'.$row->id.'|'.$row->DF.'|'.$status.'|'.$row->pono;
				$taskTable[$RowCnt]['rowBM'] .= '|'.$row->id.'|'.$row->BM.'|'.$status.'|'.$row->pono;
				$taskTable[$RowCnt]['rowBL'] .= '|'.$row->id.'|'.$row->BL.'|'.$status.'|'.$row->pono;
				$taskTable[$RowCnt]['rowCM'] .= '|'.$row->id.'|'.$row->CM.'|'.$status.'|'.$row->pono;
				$taskTable[$RowCnt]['rowCL'] .= '|'.$row->id.'|'.$row->CL.'|'.$status.'|'.$row->pono;				
			}
		}
		
		//$data['interval'] 	= $this->getInterval();
		//$data['totalSec'] = ceil($RowCnt/$data['interval']) - 1; 
		
		$data['totalSec'] = 4;
		$data['interval'] 	= round(($RowCnt/$data['totalSec']),0); // interval
		
		$data['taskTable'] 	= $taskTable;
		$data['now']= $now;

		$this->load->view('clamplift/clamplift',$data);
	}
	
	function workingdate(){
		return '3';
	}
	function limit(){
		return 5;
	}
	
	function getPaperByStatus()
	{
		$statusid=1;
		$date=$this->workingdate();
		$data['taskTable'] 	= $this->Clamplift_model->getPaperByStatus($date,$statusid);
		$this->load->view('clamplift/clampliftlist.php',$data);
	}
	
	function getNextUse($id,$code)
	{	
		$date=$this->workingdate();
		$limit=$this->limit();
		
		$data['results'] = $this->Clamplift_model->getNextUse($id,$code,$date,$limit);
		$data['totalRec'] = $data['results']->num_rows();	
		//$taskTable = array();
		$RowCnt=0;
		foreach ($data['results']->result() as $row)
		{
			$thisTime = substr($row->start,0,5);
			$status = $row->status; 
			
			$RowCnt++;
			$lastTime = $thisTime;
			$taskTable[$RowCnt]= array();
			$taskTable[$RowCnt]['time'] =$thisTime;	
			$taskTable[$RowCnt]['rowDF'] = $row->id.'|'.$row->DF.'|'.$status.'|'.$row->pono;
			$taskTable[$RowCnt]['rowBM'] = $row->id.'|'.$row->BM.'|'.$status.'|'.$row->pono;
			$taskTable[$RowCnt]['rowBL'] = $row->id.'|'.$row->BL.'|'.$status.'|'.$row->pono;
			$taskTable[$RowCnt]['rowCM'] = $row->id.'|'.$row->CM.'|'.$status.'|'.$row->pono;
			$taskTable[$RowCnt]['rowCL'] = $row->id.'|'.$row->CL.'|'.$status.'|'.$row->pono;	
		}
		$data['taskTable'] 	= $taskTable;
		$this->load->view('clamplift/clampliftlist.php',$data);
	}
	
	function getNextTask($id)
	{	
		$date=$this->workingdate();
		$limit=$this->limit();
		
		$data['results'] = $this->Clamplift_model->getNextTask($id,$date,$limit);
		$data['totalRec'] = $data['results']->num_rows();	
		$taskTable = array();
		$RowCnt=0;
		foreach ($data['results']->result() as $row)
		{
			$thisTime = substr($row->start,0,5);
			$status = $row->status; 
			
			$RowCnt++;
			$lastTime = $thisTime;
			$taskTable[$RowCnt]= array();
			$taskTable[$RowCnt]['time'] =$thisTime;	
			$taskTable[$RowCnt]['rowDF'] = $row->id.'|'.$row->DF.'|'.$status.'|'.$row->pono;
			$taskTable[$RowCnt]['rowBM'] = $row->id.'|'.$row->BM.'|'.$status.'|'.$row->pono;
			$taskTable[$RowCnt]['rowBL'] = $row->id.'|'.$row->BL.'|'.$status.'|'.$row->pono;
			$taskTable[$RowCnt]['rowCM'] = $row->id.'|'.$row->CM.'|'.$status.'|'.$row->pono;
			$taskTable[$RowCnt]['rowCL'] = $row->id.'|'.$row->CL.'|'.$status.'|'.$row->pono;	
		}
		$data['taskTable'] 	= $taskTable;
		$this->load->view('clamplift/clampliftlist.php',$data);
	}
	
	function paperPick() //paperPick
	{
		$id = ($this->input->post('id'))?$this->input->post('id'):'47';
		$mname = ($this->input->post('mname'))?$this->input->post('mname'):'DF';
		$row = $this->Clamplift_model->paperPick($id);
		$code = "";
		switch($mname){
			case 'DF': $code = $row->DF; break;
			case 'BM': $code = $row->BM; break;
			case 'BL': $code = $row->BL; break;
			case 'CM': $code = $row->CM; break;
			case 'CL': $code = $row->CL; break; 
		}
		$data['clamplift']=$this;
		$data['code']	=$code;
		$data['id']		=$id;
		$data['mname']	=$mname;
	
		$this->load->view('clamplift/clampliftpick.php',$data);
	}
	
	/* 
	 * Check if time difference 
	 * Returns $timeDiff 
	 */
	function timeDiff($start,$end) 
	{
		$firstTime=strtotime($start);
		$lastTime=strtotime($end);
		$timeDiff=($lastTime>$firstTime)?($lastTime-$firstTime):($firstTime-$lastTime);
		//return ($timeDiff>=900)?1:0;		
		return $timeDiff;
	}

}
?>
