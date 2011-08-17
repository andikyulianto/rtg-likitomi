<?php
class Planning_model extends Model 
{
	var $tableName 		= "delivery";
	var $tblProducts 	= "products";
	var $tblCatalog		= "product_catalog";
	var $totalPlanning 	= "total_planning";
	var $planning 		= "planning";
	var $status 		= "status";
	var $statustracking 	= "status_tracking";

	function Planning_model()
	{
		parent::Model();
	}
	
	function getAllDelivery()
	{
		//ToDO
		//Data is limited for efficency.
		$this->db->order_by("delivery_id", "desc"); 
		$this->db->limit(130);
		$query = $this->db->get($this->tableName);
		//echo $this->db->last_query();	
		return $query;
	
	}
	function getFilterResult($delivery_date_all,$sales_order_all,$lastmodified_all,$status_all)
	{
		$filterQueryAll ="";
		$filter ="";
		$interColumnConjunction = " OR ";
		$sameColumnConjunction 	= " OR ";
		//Delivery Date
		for($i=0;$i<count($delivery_date_all)-1;$i++)
		{
			if($i>0) $filter .= $sameColumnConjunction;
			$filter .= "delivery_date = '".$delivery_date_all[$i]."'";
		}
		if($filter!=""){
			if($filterQueryAll!="") $filterQueryAll .= $interColumnConjunction;
			$filterQueryAll .= "(".$filter.")";
		}
		//Sales Order
		$filter ="";
		for($i=0;$i<count($sales_order_all)-1;$i++)
		{
			if($i>0) $filter .= $sameColumnConjunction;
			$filter .= "sales_order = '".$sales_order_all[$i]."'";
		}
		if($filter!=""){
			if($filterQueryAll!="") $filterQueryAll .= $interColumnConjunction;
			$filterQueryAll .= "(".$filter.")";
		}
		//Last Modified Date		
		$filter ="";
		for($i=0;$i<count($lastmodified_all)-1;$i++)
		{
			if($i>0) $filter .= $sameColumnConjunction;
			$filter .= "modified_on LIKE '%".$lastmodified_all[$i]."%'";
		}
		if($filter!=""){
			if($filterQueryAll!="") $filterQueryAll .= $interColumnConjunction;
			$filterQueryAll .= "(".$filter.")";
		}
		//Status		
		$filter ="";
		for($i=0;$i<count($status_all)-1;$i++)
		{
			if($i>0) $filter .= $sameColumnConjunction;
			$filter .= "status = '".$status_all[$i]."'";
		}
		if($filter!=""){
			if($filterQueryAll!="") $filterQueryAll .= $interColumnConjunction;
			$filterQueryAll .= "(".$filter.")";
		}
		//Final Query 
		if($filterQueryAll!="") {
			$filterQueryAll = " WHERE ".$filterQueryAll;
		} 
		$filterQueryAll = "SELECT * FROM ".$this->tableName.$filterQueryAll;
				
		$query = $this->db->query($filterQueryAll);
		//echo $this->db->last_query();
		return $query;
	}
	
	function getProduct_Partner($pid)
	{
		$sql = 	"SELECT * FROM ( ".
					"SELECT * FROM `product_catalog` WHERE product_id = ".$pid.
					") AS pr LEFT JOIN partners AS pa ON pa.partner_id = pr.partner_id";
		$query = $this->db->query($sql);
		return $query->row();
	}
	
	function getProductFlutes($pid,$product_code){
		
		$sql = 	 "SELECT p.* FROM ".$this->tblProducts." AS p, ("
				."SELECT product_code FROM ".$this->tblCatalog." WHERE `product_id` = ".$pid
				.") AS pc WHERE pc.product_code = p.parent_code_id "
				." AND p.product_code ='".$product_code."'";
		
		$query = $this->db->query($sql);
		return $query;
	}

	function getProduct($product_code){
		
		$sql = 	 "SELECT * FROM ".$this->tblProducts." as p, ".$this->tblCatalog." as c   WHERE p.product_code ='".$product_code."' and p.product_code=c.product_code";
		
		$query = $this->db->query($sql);
		//echo $sql;
		return $query;
	}
	function getProductCat($pid,$product_code){
		
		$sql = 	 "SELECT pc.* FROM ".$this->tblProducts." AS p, ("
				."SELECT product_code FROM ".$this->tblCatalog." WHERE `product_id` = ".$pid
				.") AS pc WHERE pc.product_code = p.parent_code_id "
				." AND p.product_code ='".$product_code."'";
		
		$query = $this->db->query($sql);
		return $query;
	}
	//Fon 

		function getProductCatProcess($pid){
		
		$sql = 	 "SELECT product_code FROM ".$this->tblCatalog." WHERE `product_id` = ".$pid;
		
		$query = $this->db->query($sql);
		return $query;
	}

	//add save total_plan 
	function savetotalplan($rowData,$choosendate,$time_start_cr,$time_stop_cr,$time_start_cv,$time_stop_cv,$time_start_pt,$time_stop_pt,$time_start_wh)
	{	
		$param = array( "date" => $choosendate,
			"delivery_id" => $rowData->delivery_id,
			"p_width_inch" => $rowData->p_width_inch,
			"t_length" => $rowData->t_length,
			"flute" => $rowData->flute,
			"DF" => $rowData->DF,
			"BM" => $rowData->BM,
			"BL" => $rowData->BL,
			"CM" => $rowData->CM,
			"CL" => $rowData->CL,
 			"corrugator_date" => substr($rowData->corrugator_date,0,10)." ".$time_start_cr,
			"converter_date" => substr($rowData->converter_date,0,10)." ".$time_start_cv,
			//"patchpartition_date" => substr($rowData->patchpartition_date,0,10)." ".$rowData->patchpartition_time.":00",
			//"warehouse_date" => substr($rowData->warehouse_date,0,10)." ".$rowData->warehouse_time.":00",
			//"next_process" => $rowData->next_process
		);

		$this->db->insert($this->totalPlanning, $param);


	}

        function savetostatustracking($rowData,$choosendate,$realDate,$time_start_cr,$time_stop_cr,$time_start_cv,$time_stop_cv,$time_start_pt,$time_stop_pt,$time_start_wh,$mo_cr,$mo_cv,$mo_pt)
        {
        		if($mo_cr=="")
        			$mo_cr=NULL;
        		if($mo_cv=="")
        			$mo_cv=NULL;
        		if($mo_pt=="")
        			$mo_pt=NULL;
			//echo substr($rowData->corrugator_date,0,10)." ".substr($rowData->corrugator_date,11,5).":00";
			//echo substr($rowData->converter_date,0,10)." ".$rowData->converter_time.":00";
			//get amount
			//echo "---".$choosendate;

			$sql = "Select autoid From total_planning Where delivery_id =".$rowData->delivery_id." and date='".$choosendate."'";
			$query = $this->db->query($sql);
			foreach ($query->result() as $row)
			{
				$total_plan_id = $row->autoid;
			}
			
			$sql = "Select product_id,qty,delivery_date,delivery_time,sales_order From delivery Where delivery_id =".$rowData->delivery_id;
			$query = $this->db->query($sql);
			foreach ($query->result() as $row)
			{
				$qty = $row->qty;
				$product_id = $row->product_id;
				$plan_due = $row->delivery_date." ".$row->delivery_time;
				$sale_order = $row->sales_order;
			}
			//sale order
			$sql = "Select product_code_1, product_code_2 From sales_order where sales_order_id=".$sale_order;
			$query = $this->db->query($sql);
			foreach ($query->result() as $row)
			{
				$product_code_1 = $row->product_code_1;
				$product_code_2 = $row->product_code_2;
			}
			if($product_code_2 == "" || $product_code_2 == NULL || $rowData->product_code == $product_code_1)
			{
				//find product id in products
				$sql = "Select auto_id From products where product_code='".$product_code_1."' and parent_code_id='".$product_code_1."'";
				$query = $this->db->query($sql);
				foreach ($query->result() as $row)
				{
					$auto_id = $row->auto_id;
				}
			}
			else
			{
				$sql = "Select auto_id From products where product_code='".$product_code_2."' and parent_code_id='".$product_code_1."'";
				$query = $this->db->query($sql);
				foreach ($query->result() as $row)
				{
					$auto_id = $row->auto_id;
				}
			}
			//echo $auto_id;
			
			$sql = "select * from product_catalog where product_id=".$product_id;
			$query = $this->db->query($sql);
			foreach ($query->result() as $row)
			{
				$amount  = $qty + $row->add_amount;
				$cv_machine = $row->next_process;
				$req_cr = $row->req_cr;
				$req_2cl = $row->req_2cl;
				$req_3cm = $row->req_3cm;
				$req_3cs = $row->req_3cs;
				$req_4cd = $row->req_4cd;
				$req_3cl = $row->req_3cl;
				$req_gh = $row->req_gh;
				$req_hs = $row->req_hs;
				$req_fg = $row->req_fg;
				$req_rd = $row->req_rd;
				$req_ss = $row->req_ss;
				$req_remove = $row->req_remove;
				$req_foam = $row->req_foam;
				$req_tape = $row->req_tape;
				$req_wh = $row->req_wh;
			}

/*			if($cv_machine == 'SHEET')
			{
				$param = array("date" => $choosendate,
						"product_id"=>$rowData->product_code,
						"plan_amount" =>$amount,
						"plan_cr_start" =>substr($rowData->corrugator_date,0,10)." ".$time_start_cr.":00",
						"plan_cr_end" => substr($rowData->corrugator_date,0,10)." ".$time_stop_cr.":00",
						"plan_cv_start" => NULL,
						"plan_cv_end" => NULL,
						"plan_pt_start" => NULL,
						"plan_pt_end" => NULL,
						"plan_wh_start" => substr($rowData->corrugator_date,0,10)." ".$time_stop_cr.":00",
						"plan_due"=>$plan_due,
						"cv_machine" => $cv_machine
				);
			}
*/			//print $time_start_cr.":00"."<br>";
			if($req_cr == 1 and $req_wh == 1 and $req_2cl == 0 and $req_3cm == 0 and $req_3cs == 0 and $req_4cd == 0 and $req_3cl ==0 and $req_gh ==0 and $req_hs == 0 and $req_fg ==0 and $req_rd==0 and $req_ss==0 and $req_remove==0 and $req_foam==0 and $req_tape==0)
			{
				$param = array("date" => $choosendate,
						"delivery_id"=>$rowData->delivery_id,
						"total_plan_id"=>$total_plan_id,
						"product_id"=>$rowData->product_code,
						"product_auto_id"=>$auto_id,
						"sale_order_id" =>$sale_order,
						"plan_amount" =>$amount,
						//"plan_cr_start" =>substr($rowData->corrugator_date,0,10)." ".$time_start_cr.":00",
						//"plan_cr_end" => substr($rowData->corrugator_date,0,10)." ".$time_stop_cr.":00",
						"plan_cr_start" =>substr($realDate,0,10)." ".$time_start_cr.":00",
						"plan_cr_end" => substr($realDate,0,10)." ".$time_stop_cr.":00",
						"plan_cv_start" => NULL,
						"plan_cv_end" => NULL,
						"plan_pt_start" => NULL,
						"plan_pt_end" => NULL,
						//"plan_wh_start" => substr($rowData->converter_date,0,10)." ".$time_start_wh.":00",
						"plan_wh_start" => substr($realDate,0,10)." ".$time_start_wh.":00",
						"plan_due"=>$plan_due,
						"cv_machine" => $cv_machine,
						"mo_cr_code"=>$mo_cr,
						"mo_cv_code"=>$mo_cv,
						"mo_pt_code"=>$mo_pt
				);
			}
			else if($req_cr == 1 and $req_wh == 1 and ($req_2cl == 1 or $req_3cm == 1 or $req_3cs == 1 or $req_4cd == 1 or $req_3cl ==1 or $req_gh ==1 or $req_hs == 1 or $req_fg ==1 or $req_rd==1 or $req_ss==1) and ($req_remove==0 and $req_foam==0 and $req_tape==0))
			{
				$param = array("date" => $choosendate,
						"delivery_id"=>$rowData->delivery_id,
						"total_plan_id"=>$total_plan_id,
						"product_id"=>$rowData->product_code,
						"product_auto_id"=>$auto_id,
						"sale_order_id" =>$sale_order,
						"plan_amount" =>$amount,
/*						"plan_cr_start" =>substr($rowData->corrugator_date,0,10)." ".$time_start_cr.":00",
						"plan_cr_end" => substr($rowData->corrugator_date,0,10)." ".$time_stop_cr.":00",
						"plan_cv_start" => substr($rowData->converter_date,0,10)." ".$time_start_cv.":00",
						"plan_cv_end" => substr($rowData->converter_date,0,10)." ".$time_stop_cv.":00",
*/
						"plan_cr_start" =>substr($realDate,0,10)." ".$time_start_cr.":00",
						"plan_cr_end" => substr($realDate,0,10)." ".$time_stop_cr.":00",
						"plan_cv_start" => substr($realDate,0,10)." ".$time_start_cv.":00",
						"plan_cv_end" => substr($realDate,0,10)." ".$time_stop_cv.":00",
						"plan_pt_start" => NULL,
						"plan_pt_end" => NULL,
						//"plan_wh_start" => substr($rowData->converter_date,0,10)." ".$time_start_wh.":00",
						"plan_wh_start" => substr($realDate,0,10)." ".$time_start_wh.":00",
						"plan_due"=>$plan_due,
						"cv_machine" => $cv_machine,
						"mo_cr_code"=>$mo_cr,
						"mo_cv_code"=>$mo_cv,
						"mo_pt_code"=>$mo_pt
				);
			}
			else if($req_cr == 1 and $req_wh == 1 and ($req_2cl == 0 and $req_3cm == 0 and $req_3cs == 0 and $req_4cd == 0 and $req_3cl ==0 and $req_gh ==0 and $req_hs == 0 and $req_fg ==0 and $req_rd==0 and $req_ss==0) and ($req_remove==1 or $req_foam==1 or $req_tape==1))
			{
				$param = array("date" => $realDate,
						"delivery_id"=>$rowData->delivery_id,
						"total_plan_id"=>$total_plan_id,
						"product_id"=>$rowData->product_code,
						"product_auto_id"=>$auto_id,
						"sale_order_id" =>$sale_order,
						"plan_amount" =>$amount,
						//"plan_cr_start" =>substr($rowData->corrugator_date,0,10)." ".$time_start_cr.":00",
						//"plan_cr_end" => substr($rowData->corrugator_date,0,10)." ".$time_stop_cr.":00",
						"plan_cr_start" =>substr($realDate,0,10)." ".$time_start_cr.":00",
						"plan_cr_end" => substr($realDate,0,10)." ".$time_stop_cr.":00",
						"plan_cv_start" => NULL,
						"plan_cv_end" => NULL,
/*						"plan_pt_start" => substr($rowData->converter_date,0,10)." ".$time_start_pt.":00",
						"plan_pt_end" => substr($rowData->converter_date,0,10)." ".$time_stop_pt.":00",
						"plan_wh_start" => substr($rowData->converter_date,0,10)." ".$time_start_wh.":00",
*/
						"plan_pt_start" => substr($realDate,0,10)." ".$time_start_pt.":00",
						"plan_pt_end" => substr($realDate,0,10)." ".$time_stop_pt.":00",
						"plan_wh_start" => substr($realDate,0,10)." ".$time_start_wh.":00",
						"plan_due"=>$plan_due,
						"cv_machine" => $cv_machine,
						"mo_cr_code"=>$mo_cr,
						"mo_cv_code"=>$mo_cv,
						"mo_pt_code"=>$mo_pt
				);
			}
			else if($req_cr == 1 and $req_wh == 1 and ($req_2cl == 1 or $req_3cm == 1 or $req_3cs == 1 or $req_4cd == 1 or $req_3cl ==1 or $req_gh ==1 or $req_hs == 1 or $req_fg ==1 or $req_rd==1 or $req_ss==1) and ($req_remove==1 or $req_foam==1 or $req_tape==1))
			{
				$param = array("date" => $choosendate,
						"delivery_id"=>$rowData->delivery_id,
						"total_plan_id"=>$total_plan_id,
						"product_id"=>$rowData->product_code,
						"product_auto_id"=>$auto_id,
						"sale_order_id" =>$sale_order,
						"plan_amount" =>$amount,
/*						"plan_cr_start" =>substr($rowData->corrugator_date,0,10)." ".$time_start_cr.":00",
						"plan_cr_end" => substr($rowData->corrugator_date,0,10)." ".$time_stop_cr.":00",
						"plan_cv_start" => substr($rowData->converter_date,0,10)." ".$time_start_cv.":00",
						"plan_cv_end" => substr($rowData->converter_date,0,10)." ".$time_stop_cv.":00",
						"plan_pt_start" => substr($rowData->converter_date,0,10)." ".$time_start_pt.":00",
						"plan_pt_end" => substr($rowData->converter_date,0,10)." ".$time_stop_pt.":00",
						"plan_wh_start" => substr($rowData->converter_date,0,10)." ".$time_start_wh.":00",
*/
						"plan_cr_start" =>substr($realDate,0,10)." ".$time_start_cr.":00",
						"plan_cr_end" => substr($realDate,0,10)." ".$time_stop_cr.":00",
						"plan_cv_start" => substr($realDate,0,10)." ".$time_start_cv.":00",
						"plan_cv_end" => substr($realDate,0,10)." ".$time_stop_cv.":00",
						"plan_pt_start" => substr($realDate,0,10)." ".$time_start_pt.":00",
						"plan_pt_end" => substr($realDate,0,10)." ".$time_stop_pt.":00",
						"plan_wh_start" => substr($realDate,0,10)." ".$time_start_wh.":00",
						"plan_due"=>$plan_due,
						"cv_machine" => $cv_machine,
						"mo_cr_code"=>$mo_cr,
						"mo_cv_code"=>$mo_cv,
						"mo_pt_code"=>$mo_pt
				);
			}
			else
			{
			$param = array("date" => $choosendate,
						"delivery_id"=>$rowData->delivery_id,
						"total_plan_id"=>$total_plan_id,
						"product_id"=>$rowData->product_code,
						"product_auto_id"=>$auto_id,
						"sale_order_id" =>$sale_order,
						"plan_amount" =>$amount,
/*						"plan_cr_start" =>substr($rowData->corrugator_date,0,10)." ".$time_start_cr.":00",
						"plan_cr_end" => substr($rowData->corrugator_date,0,10)." ".$time_stop_cr.":00",
*/
						"plan_cr_start" =>substr($realDate,0,10)." ".$time_start_cr.":00",
						"plan_cr_end" => substr($realDate,0,10)." ".$time_stop_cr.":00",
						"plan_cv_start" => NULL,
						"plan_cv_end" => NULL,
						"plan_pt_start" => NULL,
						"plan_pt_end" => NULL,
//						"plan_wh_start" => substr($rowData->corrugator_date,0,10)." ".$time_stop_cr.":00",
						"plan_wh_start" => substr($realDate,0,10)." ".$time_stop_cr.":00",
						"plan_due"=>$plan_due,
						"cv_machine" => $cv_machine,
						"mo_cr_code"=>$mo_cr,
						"mo_cv_code"=>$mo_cv,
						"mo_pt_code"=>$mo_pt
				);
			}
			//add to status tracking
			$this->db->insert($this->statustracking, $param);
			
			


				
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
	function deleteAllPlanForToday($today)
	{
		//Delete All Records of the day.
		$this->db->where('date',$today); 
		$this->db->delete($this->totalPlanning);
	}
	function deleteStatusTrackingPlanForToday($today)
	{
		//Delete All Records of the day.
		$this->db->where('date',$today); 
		$this->db->delete($this->statustracking);
	}
	
//	function getDeliveryDetails($delivery_id)
//	{
//		$this->db->where("delivery_id",$delivery_id);
//		$query = $this->db->get($this->tableName);
//		return $query->row();
//	}
	
//	function savetotalplan($delivery_ids,$corrugator_dates,$converter_dates,$today)
//	{
//		$this->db->where('date',$today);
//		$this->db->delete($this->totalPlanning);
//		for($i=0;$i<count($delivery_ids);$i++)
//		{
//			//padding
//			if(count($corrugator_dates)<count($delivery_ids)) $corrugator_dates[$i]="";
//			if(count($converter_dates)<count($delivery_ids)) $converter_dates[$i]="";
//			
//			if(($delivery_ids[$i] !="")||($delivery_ids[$i] != 0 ))
//			{
//				$param = array( "date" => $today,
//								"delivery_id" => $delivery_ids[$i],
//								"corrugator_date" => $corrugator_dates[$i],
//								"converter_date" => $converter_dates[$i]);
//				$this->db->insert($this->totalPlanning, $param);
//				
//				//update status
//				$this->db->where("delivery_id",$delivery_ids[$i]);
//				$this->db->update($this->tableName,array('status' => "planned"));
//				//echo $this->db->last_query();
//			}
//		}
//	}
	
	function loadplanbydate($today)
	{
		$this->db->where("date",$today);
		$this->db->join($this->tableName, $this->tableName.'.delivery_id = '.$this->totalPlanning.'.delivery_id', 'left');
		$query = $this->db->get($this->totalPlanning);
		//echo $this->db->last_query();
		return $query;
	}
	
	/*function keyin($plandate)
	{
		$sql = 	 "SELECT * FROM ( SELECT del . * , pcat . * FROM ("
				."SELECT d.product_id AS pid, d.qty, d.delivery_date,d.sales_order, "
				."so.purchase_order_no, so.delivery_at "
				."FROM `delivery` AS d "
				."LEFT JOIN sales_order AS so ON d.sales_order = so.sales_order_id "
				.") AS del LEFT JOIN ("
				."SELECT pc . * FROM product_catalog AS pc WHERE pc.isdeleted =0"
				.") AS pcat ON del.pid = pcat.product_id ) AS prod "
				."LEFT JOIN products ON prod.product_code = products.product_code "
				."LEFT JOIN partners ON prod.partner_id = partners.partner_id ";
				echo "anu".$sql;
		$query = $this->db->query($sql);
		return $query;
	}
	
	//Queries By Anu for Planning Reports
	
	function keyin($plandate)
	{
		$sql = 	 "SELECT tp.autoid, d.sales_order, pd.product_code, pt.partner_name, pc.product_name, d.qty, pd.flute,pc.slit,   "
				."pd.DF, pd.BL,pd.CL, pd.BM, pd.CM,pc.cut,pc.blank, pc.slit, pc.scoreline_f,  "
				."pc.scoreline_d, pc.scoreline_f2, pc.next_process,date_format(d.delivery_date,'%d/%m') as delivery_date, pc.t_length, pc.p_width_inch,  "
				."d.remarks as D_remarks, pc.remark PC_remarks, so.remarks SO_remarks  "
				."FROM total_planning tp, delivery d, products pd, product_catalog pc, partners pt, sales_order so  "
				."WHERE tp.date='".$plandate."'"
				."AND tp.delivery_id = d.delivery_id "
				."AND d.sales_order = so.sales_order_id "
				."AND pc.product_id = d.product_id "
				."AND pt.partner_id = pc.partner_id "
				."AND pc.product_code = pd.parent_code_id "
				."AND pd.product_code = d.product_code "
				."AND pd.isdeleted =0 "
				."ORDER BY tp.autoid";
		$query = $this->db->query($sql);
		return $query;
	}*/
		function convertor($plandate)
	{
		$sql = 	 "SELECT pc.ink_1,pc.ink_2,pc.ink_3,pc.ink_4, d.sales_order,tp.autoid, pd.product_code, pt.partner_name, pc.product_name, ((d.qty*pc.cv_ratio_2) div pc.cv_ratio_1) as qty, pd.flute,"
				."pd.DF, pd.BL,pd.CL, pd.BM, pd.CM,pc.cut,pc.blank, pc.slit, pc.scoreline_f,  "
				."pc.next_process,date_format(d.delivery_date,'%d/%m') as delivery_date "
				."FROM total_planning tp, delivery d, products pd, product_catalog pc, partners pt, sales_order so  "
				."WHERE tp.date='".$plandate."'"
				."AND tp.delivery_id = d.delivery_id "
				."AND d.sales_order = so.sales_order_id "
				."AND pc.product_code = d.product_code "
				."AND pt.partner_id = pc.partner_id "
				."AND pc.product_code = pd.parent_code_id "
				."AND pd.product_code = d.product_code "
				."AND pd.isdeleted =0 "
				."ORDER BY pc.next_process";
				//."AND pc.next_process='2CL'";
		$query = $this->db->query($sql);
		return $query;
	}

		function partition($plandate)
	{
		$sql = 	 "SELECT pc.ink_1,pc.ink_2,pc.ink_3,pc.ink_4, d.sales_order,tp.autoid, pd.product_code, pt.partner_name, pc.product_name, ((d.qty*pc.cv_ratio_2) div pc.cv_ratio_1) as qty, pd.flute, so.purchase_order_no,"
				."pd.DF, pd.BL,pd.CL, pd.BM, pd.CM,pc.cut,pc.blank, pc.slit, pc.scoreline_f,  "
				."pc.next_process,date_format(d.delivery_date,'%d/%m') as delivery_date ,"
				."pc.req_2cl as req_2cl, pc.req_3cm as req_3cm, pc.req_3cs as req_3cs, pc.req_4cd as req_4cd, pc.req_3cl as req_3cl, "
				."pc.req_gh as req_gh, pc.req_hs as req_hs, pc.req_fg as req_fg, pc.req_rd as req_rd, pc.req_ss as req_ss, pc.req_remove as req_remove, pc.req_foam as req_foam, pc.req_tape as req_tape,pc.sketch,pc.scoreline_f,pc.scoreline_d,pc.scoreline_f2,pc.blank,pc.t_length,pd.flute "
				."FROM total_planning tp, delivery d, products pd, product_catalog pc, partners pt, sales_order so  "
				."WHERE tp.date='".$plandate."'"
				."AND tp.delivery_id = d.delivery_id "
				."AND d.sales_order = so.sales_order_id "
				."AND pc.product_code = d.product_code "
				."AND pt.partner_id = pc.partner_id "
				."AND pc.product_code = pd.parent_code_id "
				."AND pd.product_code = d.product_code "
				."AND pd.isdeleted =0 "
				."ORDER BY pc.next_process";
				//."AND pc.next_process='2CL'";
		$query = $this->db->query($sql);
		return $query;
	}
			function machine()
	{
		$sql = 	 "SELECT * FROM machine where machine.is_working=1";
				//."AND pc.next_process='2CL'";
		$query = $this->db->query($sql);
		return $query;
	}
	
	function corrugatorclamplift($plandate)
	{
		$sql = 	 "SELECT tp.autoid, d.sales_order, d.product_code, pt.partner_name, pc.product_name, pd.flute,pc.slit, d.qty as qty,  "
				."pc.cr_ratio_2 / pc.cr_ratio_1 as ratio, pd.DF, pd.BL,pd.CL, pd.BM, pd.CM, pc.p_width_inch,pc.t_length, pc.cut,pc.p_width_mm,  "
				."d.remarks as D_remarks, pc.remark PC_remarks  "
				."FROM total_planning tp, delivery d, products pd, product_catalog pc,partners pt  "
				."WHERE tp.date='".$plandate."'"
				."AND tp.delivery_id = d.delivery_id "
				."AND pc.product_code = d.product_code "
				."AND pt.partner_id = pc.partner_id "
				."AND pc.product_code = pd.parent_code_id "
				."AND pd.product_code = d.product_code "
				."AND pd.isdeleted =0 "
				."ORDER BY tp.autoid";
		$query = $this->db->query($sql);
		return $query;
	}
	
	function corrugatordaily($plandate)
	{
		$sql = 	 "SELECT tp.autoid, d.sales_order, pd.product_code, pt.partner_name, pc.product_name, pd.flute,pc.slit, d.qty as qty, "
				."pd.DF, pd.BL,pd.CL, pd.BM, pd.CM, pc.cut,pc.p_width_inch,pc.t_length,pc.p_width_mm,  "
				."pc.cr_ratio_2 / pc.cr_ratio_1 as ratio, pc.blank, pc.slit, pc.scoreline_f, pc.scoreline_d, pc.scoreline_f2, pc.next_process,  "
				."pc.req_2cl as req_2cl, pc.req_3cm as req_3cm, pc.req_3cs as req_3cs, pc.req_4cd as req_4cd, pc.req_3cl as req_3cl, "
				."pc.req_gh as req_gh, pc.req_hs as req_hs, pc.req_fg as req_fg, pc.req_rd as req_rd, pc.req_ss as req_ss, pc.req_remove as req_remove, pc.req_foam as req_foam, pc.req_tape as req_tape, "
				."date_format(d.delivery_date,'%d/%m') as delivery_date,pc.slit, pc.blank,  "
				."d.remarks as D_remarks, pc.remark PC_remarks  "
				."FROM total_planning tp, delivery d, products pd, product_catalog pc, partners pt  "
				."WHERE tp.date='".$plandate."'"
				."AND tp.delivery_id = d.delivery_id "
				."AND pc.product_code = d.product_code "
				."AND pt.partner_id = pc.partner_id "
				."AND pc.product_code = pd.parent_code_id "
				."AND pd.product_code = d.product_code "
				."AND pd.isdeleted =0 "
				."ORDER BY tp.autoid";
		$query = $this->db->query($sql);
		return $query;
	}
	
	function totalproductionplan($plandate)
	{
		$sql = 	 "SELECT tp.autoid, d.sales_order, so.purchase_order_no, d.product_code, pt.partner_name, pc.product_name, pc.p_width_inch,pc.slit, "  
				."pc.t_length, pd.flute, pc.cut,d.qty as qty,((d.qty*pc.cr_ratio_2) div pc.cr_ratio_1) as qty_cr,((d.qty*pc.cv_ratio_2) div pc.cv_ratio_1) as qty_cv, pc.qty_allowance, date_format(d.delivery_date,'%d/%m') as delivery_date, date_format(tp.corrugator_date,'%d/%m') as corrugator_date, "
				."date_format(tp.corrugator_date,'%H:%i') as corrugator_time,date_format(tp.converter_date,'%d/%m') as converter_date,date_format(tp.converter_date,'%H:%i') as converter_time, "  
				."d.remarks as D_remarks, pc.remark PC_remarks, so.remarks SO_remarks , pc.next_process as machine "
				."FROM total_planning tp, delivery d, product_catalog pc, sales_order so, partners pt, products pd "
				."WHERE tp.date='".$plandate."'"
				."AND tp.delivery_id = d.delivery_id "
				."AND d.sales_order = so.sales_order_id "
				."AND pc.product_code = d.product_code "
				."AND pt.partner_id = pc.partner_id "
				."AND pc.product_code = pd.parent_code_id "
				."AND pd.product_code = d.product_code "
				."AND pd.isdeleted =0 "
				."ORDER BY tp.autoid";
		$query = $this->db->query($sql);
		return $query;
	}
	
	function deliverydaily($plandate)
	{
		$sql = 	"SELECT tp.autoid, d.sales_order, so.purchase_order_no, pd.product_code, pt.partner_name, pc.product_name, pd.flute, pc.cut,d.qty,pc.slit, "
				."pc.qty_allowance, date_format(d.delivery_date,'%d/%m') as delivery_date, d.delivered_qty,pc.p_width_inch,pc.t_length, "
				."d.remarks as D_remarks, pc.remark PC_remarks, so.remarks SO_remarks,d.total_production_qty "
				."FROM total_planning tp, delivery d, products pd, product_catalog pc, partners pt, sales_order so "
				."WHERE tp.date='".$plandate."'"
				."AND tp.delivery_id = d.delivery_id "
				."AND d.sales_order = so.sales_order_id "
				."AND pc.product_code = d.product_code "
				."AND pt.partner_id = pc.partner_id "
				."AND pc.product_code = pd.parent_code_id "
				."AND pd.product_code = d.product_code "
				."AND pd.isdeleted =0 "
				."ORDER BY tp.autoid";
		$query = $this->db->query($sql);
		return $query;
	}
	
	function productstatus($plandate)
	{
		$sql =  "SELECT tp.autoid, d.sales_order, so.purchase_order_no, d.product_code, pt.partner_name, "
				."pc.product_name, d.delivery_id, d.delivery_date, d.qty, d.delivered_qty,d.total_production_qty, d.damaged_qty, status "
				."FROM total_planning tp, delivery d, product_catalog pc, sales_order so, partners pt, products pd  "
				 ."WHERE tp.date='".$plandate."' "
				 ."AND tp.delivery_id = d.delivery_id "  
				 ."AND d.sales_order = so.sales_order_id "  
				 ."AND pc.product_code = d.product_code  "
				 ."AND pt.partner_id = pc.partner_id  "
				 ."AND pc.product_code = pd.parent_code_id "  
				 ."AND pd.product_code = d.product_code  "
				 ."AND pd.isdeleted =0  "
				 ."ORDER BY tp.autoid ";
		$query = $this->db->query($sql);
		return $query;
		
	}
	
	function updateproductstatus($projectdetails,$delivery_id)
	{
		$this->db->where('delivery_id', $delivery_id);
		$this->db->update($this->tableName, $projectdetails);
		$this->db->last_query();
	}
	function getLastCVTime($date,$machine)
	{
//		$sql = 	 "SELECT * FROM ".$this->status." WHERE date ='".$date."'";
//		return $sql;
		$sql = "SELECT * FROM ".$this->statustracking." st, ".$this->tblCatalog." pc WHERE `date` = '".$date."' and  st.`product_id` = pc.product_code and pc.req_".$machine." = 1 ORDER BY plan_cv_end DESC LIMIT 1;";
		
		$query = $this->db->query($sql);
		return $query;
	}
}
?>
