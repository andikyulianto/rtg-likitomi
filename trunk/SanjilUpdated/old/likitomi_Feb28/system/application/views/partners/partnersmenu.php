<div id='submenubar'>
	<table cellpadding='0' cellspacing='0' >
    <tr align='right'>
        <td onclick='<?php if($tick!=1) echo "loadPartnerDetail(".$partner_id.")"?>'>
            <span <?php if($tick==1) {echo "class='selected'";} else {echo "class='unselected' onmouseover='this.className=\"selected\"' onmouseout='this.className=\"unselected\"'";} ?>>General</span>
        </td>
        <td onclick='<?php if($tick!=2) echo "listproducts()";?>'>
            <span <?php if($tick==2) {echo "class='selected'";} else {echo " class='unselected' onmouseover='this.className=\"selected\"' onmouseout='this.className=\"unselected\"'";} ?>>Products</span>
        </td>
    </tr>
	</table>
</div>