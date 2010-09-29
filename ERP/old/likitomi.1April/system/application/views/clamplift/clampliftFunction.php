<?php
	function printItem($id,$data,$class,$pono,$mname)
	{
		$output ="";
		$onclick ="";
		$statuslist = array('queue','inmachine','finished');
		
		switch($statuslist[$class]){
			case "inmachine": 
				$onclick=""; 
				break;
			case "queue": 
				$onclick='paperPick("'.$id.'","'.$mname.'");';
				break;
			case "finished": 
				$onclick="";
				break;
		}	
		if($data !="") 
		{
			$output ="<div id='itemdiv'";
			$output .= " onclick='".$onclick."'";
			$output .= " class='".$statuslist[$class]."'>".$data."<br/>".$pono."<br/>A11</div>";
		}
		return $output;
	}
?>