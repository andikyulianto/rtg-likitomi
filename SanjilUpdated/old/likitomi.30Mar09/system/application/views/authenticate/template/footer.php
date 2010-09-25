
<div class="clear"></div>

</div> 
	<div id="footer">
    <hr/>
	Page requested at <?=date('H:m:s',$_SERVER['REQUEST_TIME'])?> from <?=$_SERVER['SERVER_NAME']?> and rendered in {elapsed_time} seconds.Memory Usuage: {memory_usage}.<br />
	This application is developed as part of RTG-Budget Joint Industrial Research Project Fiscal Year, 2007-2008<br/>
	at <a href="http://www.ait.asia" target="_blank" >Asian Institute of Technology</a> for 
	<a href="http://www.likitomi.co.th/" target="_blank">Likitomi (Thailand) Company Limited</a>. 
	<div style="margin-top:5px">
		<a href="http://aptana.com/" target="_blank" ><img src="<?=base_url()?>static/images/built_with_aptana.gif" 
			alt="built with aptana" title="Aptana" border="0" /></a>							
		<a href="http://codeigniter.com/" target='_blank'><img src="<?=base_url()?>static/images/codeigniter.gif" title="Codeigniter" border="0" /></a>
	</div>	
    </div>
</body>
</html>