<?php

//Connect to Clamplift Database
$con = mysql_connect("192.168.1.100","likitomidb","likitomidb");
if (!$con)
{
	die('Could not connect: ' . mysql_error());
}
mysql_select_db("likitomidb", $con);

$data = $gridData->clamplift;
$opdate = $gridData->opdate;

$cnt=0;
$msg = "NULL";
//Seting up transaction

$null = mysql_query("START TRANSACTION", $con);
mysql_query("BEGIN", $con);

$sql  = " DELETE FROM `tbl_clamplift` WHERE `tbl_clamplift`.`opdate` LIKE '".$opdate."'";  
mysql_query($sql);

foreach ($data as $row)
{	$sql  = "INSERT INTO `tbl_clamplift` VALUES(NULL,'$opdate','$row->start_time','$row->stop_time','$row->product_code','$row->partner_name','$row->product_name','$row->sales_order','$row->autoid','$row->flute','$row->DF','$row->BL','$row->CL','$row->BM','$row->CM','$row->p_width_inch','$row->p_width_mm','$row->used_df','$row->used_bl','$row->used_cl','$row->used_bm','$row->used_cm','$row->used_df_lkg','$row->used_bl_lkg','$row->used_cl_lkg','$row->used_bm_lkg','$row->used_cm_lkg','$row->used_df_mkg','$row->used_bl_mkg','$row->used_cl_mkg','$row->used_bm_mkg','$row->used_cm_mkg','$row->t_length','$row->case','$row->cut','system','".date('Y-m-d H:m:s')."','00000');";
	mysql_query($sql);
	//echo $sql;
	$cnt++;
}

if (!mysql_error())
{
	mysql_query("COMMIT",$con);
	$msg = $cnt." records inserted"; 
	$this->db->insert('sync_clamplift',array("opdate"=>$opdate,"created_on"=>date('Y-m-d H:m:s')));
}
else
{
	mysql_query("ROLLBACK",$con);
	$msg = "Nothing is inserted (rollbacked)";
}

echo $msg;

mysql_close($con);
?>
