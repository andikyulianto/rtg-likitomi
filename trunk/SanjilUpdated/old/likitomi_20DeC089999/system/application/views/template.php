<?php
header("Expires: Mon, 26 Jul 1997 05:00:00 GMT"); // Date in the past
header("Last-Modified: " . gmdate("D, d M Y H:i:s") . " GMT"); // Always modified
header("Cache-Control: private, no-store, no-cache, must-revalidate"); // HTTP/1.1 
header("Cache-Control: post-check=0, pre-check=0", false);
header("Pragma: no-cache"); // HTTP/1.0
?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<title><?=$title?></title>
		<?=link_tag('static/images/favicon.ico', 'shortcut icon', 'image/x-icon');?>
		<?=link_tag('static/images/favicon.ico', 'icon', 'image/x-icon');?>
		
		<script type="text/javascript">
			var BASEURL= "<?=base_url()?>";
			var FIXWIDTH = "630";
		</script>
		
		<?=$scripts?>
		
		<script type="text/javascript">
			var mask = new Ext.LoadMask(Ext.getBody(), { msg: "Loading..." });
			function loadAjax(msg){
				document.getElementById('ajax_loading').style.visibility="visible";
				document.getElementById('ajax_loading').style.display="block";
				document.getElementById('ajax_loading').innerHTML=msg;
				//if(mask!=null)mask.show();
			}
			function unloadAjax(){
				document.getElementById('ajax_loading').innerHTML="";
				document.getElementById('ajax_loading').style.display="none";
				document.getElementById('ajax_loading').style.visibility="hidden";
				//if(mask!=null)mask.hide();
			}
		</script>
		
		<style type="text/css">
			@import "<?=base_url()?>static/css/styles.css";	
			<?=$styles?>
		</style>	
		<style type="text/css">			
			#container {
			    height: 640px; /* Fixed Height */
				/*position:absolute;*/
			}
		</style>	
	</head>
	<body>
		 <div id='ajax_loading'>Loading..</div>
		<?php $contentClass->show(); ?>
	</body>
</html>
