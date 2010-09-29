<?php
class Planning_model extends Model 
{
	var $tableName 		= "delivery";
	var $tblProducts 	= "products";
	var $tblCatalog		= "product_catalog";
	var $totalPlanning 	= "total_planning";

	function Planning_model()
	{
		parent::Model();
	}
	
	function getAllDelivery()
	{
		//ToDO
		//Data is limited for efficency.
		$this->db->order_by("delivery_id", "desc"); 
		$this->db->limit(100);
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
					") AS pr LEFT JOIN Partners AS pa ON pa.partner_id = pr.partner_id";
		$query = $this->db->query($sql);
		return $query->row();
	}
	
	function getProductFlutes($pid,$product_code){
		
		$sql = 	 "SELECT p.* FROM ".$this->tblProducts." AS p, ("
				."SELECT product_code FROM ".$this->tblCatalog." WHERE `product_id` = ".$pid
				.") AS pc WHERE pc.product_code = p.parent_code "
				." AND p.product_code ='".$product_code."'";
		
		$query = $this->db->query($sql);
		return $query;
	}
	
	function savetotalplan($rowData,$choosendate)
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
 			"corrugator_date" => substr($rowData->corrugator_date,0,10)." ".$rowData->corrugator_time.":00",
			"converter_date" => substr($rowData->converter_date,0,10)." ".$rowData->converter_time.":00");
		$this->db->insert($this->totalPlanning, $param);
		//echo $this->db->last_query();
	}
	
	function deleteAllPlanForToday($today)
	{
		//Delete All Records of the day.
		$this->db->where('date',$today); 
		$this->db->delete($this->totalPlanning);
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
	}*/
	
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
				."AND pc.product_code = pd.parent_code "
				."AND pd.product_code = d.product_code "
				."AND pd.isdeleted =0 "
				."ORDER BY tp.autoid";
		$query = $this->db->query($sql);
		return $query;
	}
	
	function corrugatorclamplift($plandate)
	{
		$sql = 	 "SELECT tp.autoid, d.sales_order, d.product_code, pt.partner_name, pc.product_name, pd.flute,pc.slit,  d.qty,  "
				."pd.DF, pd.BL,pd.CL, pd.BM, pd.CM, pc.p_width_inch,pc.t_length, pc.cut,pc.p_width_mm,  "
				."d.remarks as D_remarks, pc.remark PC_remarks  "
				."FROM total_planning tp, delivery d, products pd, product_catalog pc,partners pt  "
				."WHERE tp.date='".$plandate."'"
				."AND tp.delivery_id = d.delivery_id "
				."AND pc.product_id = d.product_id "
				."AND pt.partner_id = pc.partner_id "
				."AND pc.product_code = pd.parent_code "
				."AND pd.product_code = d.product_code "
				."AND pd.isdeleted =0 "
				."ORDER BY tp.autoid";
		$query = $this->db->query($sql);
		return $query;
	}
	
	function corrugatordaily($plandate)
	{
		$sql = 	 "SELECT tp.autoid, d.sales_order, pd.product_code, pt.partner_name, pc.product_name, pd.flute,pc.slit, d.qty, "
				."pd.DF, pd.BL,pd.CL, pd.BM, pd.CM, pc.cut,pc.p_width_inch,pc.t_length,pc.p_width_mm,  "
				."pc.blank, pc.slit, pc.scoreline_f, pc.scoreline_d, pc.scoreline_f2, pc.next_process,  "
				."date_format(d.delivery_date,'%d/%m') as delivery_date,pc.slit, pc.blank,  "
				."d.remarks as D_remarks, pc.remark PC_remarks  "
				."FROM total_planning tp, delivery d, products pd, product_catalog pc, partners pt  "
				."WHERE tp.date='".$plandate."'"
				."AND tp.delivery_id = d.delivery_id "
				."AND pc.product_id = d.product_id "
				."AND pt.partner_id = pc.partner_id "
				."AND pc.product_code = pd.parent_code "
				."AND pd.product_code = d.product_code "
				."AND pd.isdeleted =0 "
				."ORDER BY tp.autoid";
		$query = $this->db->query($sql);
		return $query;
	}
	
	function totalproductionplan($plandate)
	{
		$sql = 	 "SELECT tp.autoid, d.sales_order, so.purchase_order_no, d.product_code, pt.partner_name, pc.product_name, pc.p_width_inch,pc.slit, "  
				."pc.t_length, pd.flute, pc.cut,d.qty, pc.qty_allowance, date_format(d.delivery_date,'%d/%m') as delivery_date, date_format(tp.corrugator_date,'%d/%m') as corrugator_date, "
				."date_format(tp.corrugator_date,'%H:%i') as corrugator_time,date_format(tp.converter_date,'%d/%m') as converter_date,date_format(tp.converter_date,'%H:%i') as converter_time, "  
				."d.remarks as D_remarks, pc.remark PC_remarks, so.remarks SO_remarks  "
				."FROM total_planning tp, delivery d, product_catalog pc, sales_order so, partners pt, products pd "
				."WHERE tp.date='".$plandate."'"
				."AND tp.delivery_id = d.delivery_id "
				."AND d.sales_order = so.sales_order_id "
				."AND pc.product_id = d.product_id "
				."AND pt.partner_id = pc.partner_id "
				."AND pc.product_code = pd.parent_code "
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
				."d.remarks as D_remarks, pc.remark PC_remarks, so.remarks SO_remarks "
				."FROM total_planning tp, delivery d, products pd, product_catalog pc, partners pt, sales_order so "
				."WHERE tp.date='".$plandate."'"
				."AND tp.delivery_id = d.delivery_id "
				."AND d.sales_order = so.sales_order_id "
				."AND pc.product_id = d.product_id "
				."AND pt.partner_id = pc.partner_id "
				."AND pc.product_code = pd.parent_code "
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
				 ."AND pc.product_id = d.product_id  "
				 ."AND pt.partner_id = pc.partner_id  "
				 ."AND pc.product_code = pd.parent_code "  
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
}
?>