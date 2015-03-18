Project Name: **"Enhancement of Efficiency in Process Traceability and Inventory Management of Corrugated Paper Carton Manufacturer Using Barcode and RFID Technology"**

---

### Part 1: Process Traceability (Status Tracking Application) ###

**Status:** Testing

Status Tracking Process targets on employee who works in the factory. Currently, this system separates the users into 5 roles are: Planner and Manager, Corrugator, Convertor, Pad and Partition, and Warehouse.


<table border='1'>
<tr><th align='center'><h3>Features</h3></th><th align='center'><h3>Description</h3></th></tr>
<tr><td width='30%'><b>1. Planner and Manager</b></td></tr>
<tr><td>--- 1.1 The 4 subsections display </td><td>Display today plans for each section</td></tr>
<tr><td>--- 1.2 The pointer, ">", displays current process  </td><td>Display the expect process that is running now.</td></tr>
<tr><td>--- 1.3 Showing expected starting time </td><td>Display starting time for today plan</td></tr>
<tr><td>--- 1.4 waiting cell for actual time </td><td>The below cell of the expected starting time is the actual time that records after user selects the expected starting time. If starting time is recorded, it will appear in this cell.</td></tr>
<tr><td>--- 1.5 Display product code </td><td>The product codes that post orderly according to starting time. Use is able to click on the product code in order to view more information about this process</td></tr>
<tr><td>--- 1.6 Showing previous section </td><td>In CV, PT, and WH, these sections are derived from previous section. This version support the name of previous section</td></tr>
<tr><td>--- 1.7 Showing parallel process </td><td>This version supports the display showing multi-running process in the CV, PT and WH</td></tr>
<tr><td>--- 1.8 Limitation for only one glance </td><td>Up to the users screen, the initial value for limits the items for each plan is "3" but the users can change this value directly from the config.py file.</td></tr>
<tr><td>--- 1.9 Showing the whole plan for selected section</td><td>After clicking on the header of section, it will show the today-plan for particular section</td></tr>

<tr><td width='30%'><b>2. Corrugator</b></td></tr>
<tr><td>--- 2.1 Home for CR</td><td>This page show the overall plan for Corrugator section only.</td></tr>
<tr><td>--- 2.2 Starting time</td><td>The plan of CR is exactly the same as the in the PC but this users are able to edit the actual starting time and ending time for machines.</td></tr>
<tr><td>--- 2.3 Updating actual time</td><td>Users are able to record the actual of the starting time. From this page, users are able to see the expected amount and other information for configuring the machine</td></tr>
<tr><td>--- 2.4 Updating ending time</td><td>Users are able to record the actual of the ending time. Moreover, this page allows users to report the number of finished product back to Planning</td></tr>
<tr><td width='30%'><b>3. Convertor</b></td></tr>
<tr><td>--- 3.1 Home for CV</td><td>This page show the overall plan for Convertor section only.</td></tr>
<tr><td>--- 3.2 Starting time</td><td>The plan of CV is exactly the same as the in the PC but this users are able to edit the actual starting time and ending time for machines.</td></tr>
<tr><td>--- 3.3 Updating actual time</td><td>Users are able to record the actual of the starting time. From this page, users are able to see the expected amount and other information for configuring the machine</td></tr>
<tr><td>--- 3.4 Updating ending time</td><td>Users are able to record the actual of the ending time. Moreover, this page allows users to report the number of finished product back to Planning</td></tr>
<tr><td width='30%'><b>4. Pad and Partition</b></td></tr>
<tr><td>--- 4.1 Home for PT</td><td>This page show the overall plan for Pad and Partition section only.</td></tr>
<tr><td>--- 4.2 Starting time</td><td>The plan of PT is exactly the same as the in the PC but this users are able to edit the actual starting time and ending time for machines.</td></tr>
<tr><td>--- 4.3 Updating actual time</td><td>Users are able to record the actual of the starting time. From this page, users are able to see the expected amount and other information for configuring the machine</td></tr>
<tr><td>--- 4.4 Updating ending time</td><td>Users are able to record the actual of the ending time. Moreover, this page allows users to report the number of finished product back to Planning</td></tr>
<tr><td width='30%'><b>5. Warehouse</b></td></tr>
<<tr><td>--- 5.1 Home for WH</td><td>This page show the overall plan for Warehouse section only.</td></tr>
<tr><td>--- 5.2 Starting time</td><td>The plan of WH is exactly the same as the in the PC but this users are able to edit the actual starting time that products are coming into warehouse.</td></tr>
<tr><td>--- 5.3 Updating actual time</td><td>Users are able to record the actual of the starting time. From this page, users are able to see the expected amount and other information for configuring the machine</td></tr>
</table>
### Part 2: Inventory Management (Clamp-lift Application) ###

**Status:** Ready for testing

Clamp-lift application consist of 3 components: 1. Clamp-lift Plan, 2. Stock List and Map, and 3. Current Paper Roll.

<table border='1'>
<tr><th align='center'><h3>Features</h3></th><th align='center'><h3>Description</h3></th></tr>
<tr><td width='30%'><b>1. Clamp-lift Plan</b></td></tr>
<tr><td>--- 1.1 Real-time date and time</td><td>Current date and time always shown above the plan.</td></tr>
<tr><td>--- 1.2 Minimal clamp-lift plan</td><td>Clamp-lift plan which displays only required information to clamp-lift drivers for finishing their tasks including start time, sheet code, paper size, and spec with weight to be used.</td></tr>
<tr><td>--- 1.3 Use again?</td><td>Paper rolls with same paper code and size will be hi-lighted at the same time after clicked to inform that this particular kind of paper roll is going to be used again or not in the day which could help clamp-lift driver to decide that the paper roll should be kept in buffer area or paper roll stock.</td></tr>
<tr><td>--- 1.4 Clamp-lift plan in detail</td><td>The whole clamp-lift plan also provided optionally.</td></tr>
<tr><td><b>2. Stock List and Map</b></td></tr>
<tr><td>--- 2.1 List of paper roll</td><td>List of paper rolls which is looking for will be displayed with its weight and class of weight. Class of weight could help clamp-lift driver to prioritize paper roll to use.</td></tr>
<tr><td>--- 2.2 Location on map</td><td>Paper roll which is looking for will be displayed on the factory layout map informing location with the number of paper rolls in each class of weight for each block.</td></tr>
<tr><td>--- 2.3 Vehicle tracking</td><td>Clamp-lift vehicle in the paper roll stock area can be tracked as well.</td></tr>
<tr><td>--- 2.4 Updating location directly on the map</td><td>Location of paper rolls can be updated according to the current location of clamp-lift vehicle by clicking the block(s) next the to vehicle on the map.</td></tr>
<tr><td>--- 2.5 Paper roll search</td><td>Paper rolls in stock can be searched by paper code and size. The result will be the same as clicking any paper spec in clamp-lift plan.</td></tr>
<tr><td><b>3. Current Paper Roll</b></td></tr>
<tr><td>--- 3.1 Current paper roll</td><td>Paper roll data can be retrieved from RFID tag which includes paper roll ID, paper code, paper size, previous location, previous weight.</td></tr>
<tr><td>--- 3.2 Update weight function</td><td>Function to update weight of paper rolls after used will be available at scale. The weight will be retrieved from scale.</td></tr>
<tr><td>--- 3.3 Undo updating weight function</td><td>Updated weight can be rolled back with undo function.</td></tr>
<tr><td>--- 3.4 More options to update weight and location</td><td>Optionally, weight of paper roll can be updated manually and location can be updated according to previous location, current location, and manually.</td></tr>
</table>