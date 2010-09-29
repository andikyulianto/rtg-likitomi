<?php
 
class Salesorder_model extends Model 
{
	var $tblDHistory	= "delivery_history";
	var $tblSales		= "sales_order";

	function Products_model()
	{
		parent::Model();
	}
	
	function getDeliveryHistory($delivery_id)
	{
		$this->db->where('delivery_id',$delivery_id);
		$this->db->order_by("created_on", "desc"); 	
		$query = $this->db->get($this->tblDHistory);
		return $query;
	}
	
	function getSalesDetail($sales_order_id)
	{
		$this->db->where('sales_order_id',$sales_order_id);
		$query = $this->db->get($this->tblSales);
		return $query->row();	
	}
	
	function getStock($product_id, $product_code)
	{
		$sql =	"SELECT pc.product_id, so.sales_order_id, d.product_code, d.qty, d.delivered_qty,d.total_production_qty, d.damaged_qty " 
     			."FROM product_catalog pc, sales_order so, delivery d " 
     			."WHERE pc.product_id='".$product_id."' "
     			."AND pc.product_code='".$product_code."' "
     			."AND pc.product_id=so.product_id "
     			."AND so.product_id=d.product_id "
     			."AND so.sales_order_id=d.sales_order " 
     			."ORDER BY  d.product_code, so.sales_order_id DESC";
     $query = $this->db->query($sql);
     //echo $this->db->last_query();
	return $query;
	}
}
?>
