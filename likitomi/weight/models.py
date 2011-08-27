# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class PaperMovement(models.Model):
    """
    Stores movement of paper rolls, related to :model:`weight.PaperRolldetails`.

    """
    movement_id = models.AutoField(primary_key=True, help_text="Movement identifier.")
    roll_id = models.CharField(max_length=255, help_text="ID of paper roll that moved which is used as foreign key to join with 'paper_roll_detail_id' in :model:`weight.PaperRolldetails`.")
    before_wt = models.FloatField(null=True, blank=True, help_text="The weight of paper roll before movement.")
    actual_wt = models.FloatField(null=True, blank=True, help_text="The weight of paper roll after movement, latest weight.")
    from_station = models.CharField(max_length=60, blank=True)
    to_station = models.CharField(max_length=60, blank=True)
    status = models.IntegerField(null=True, blank=True)
    created_by = models.CharField(max_length=60, blank=True, help_text="The person who made the movement.")
    created_on = models.DateTimeField(null=True, blank=True, help_text="Timestamp for the movement.")
    xpos = models.CharField(max_length=18, blank=True)
    ypos = models.CharField(max_length=18, blank=True)
    zpos = models.CharField(max_length=18, blank=True)
    class Meta:
        """Real table name is 'paper_movement'."""
        db_table = u'paper_movement'


class PaperRolldetails(models.Model):
    """
    Stores detail of paper rolls, related to :model:`weight.PaperMovement`.

    """
    paper_roll_detail_id = models.IntegerField(primary_key=True, help_text="Paper roll identifier.")
    paper_code = models.CharField(max_length=90, blank=True, help_text="Paper code.")
    supplier_id = models.IntegerField(null=True, blank=True, help_text="ID of supplier.")
    supplier_roll_id = models.CharField(max_length=90, blank=True, help_text="Paper roll ID of supplier.")
    initial_weight = models.IntegerField(null=True, blank=True, help_text="Initial weight of paper roll.")
    temp_weight = models.IntegerField(null=True, blank=True, help_text="Temporary weight which is supposed to be updated to retrieving from weighing indicator.")
    remarks = models.CharField(max_length=750, blank=True, help_text="Some remarks.")
    notes = models.CharField(max_length=765, blank=True, help_text="Some notes.")
    size = models.IntegerField(null=True, blank=True, help_text="Paper size")
    uom = models.CharField(max_length=60, blank=True, help_text="Unit of paper size, inch or millimeter (mm.)")
    lane = models.CharField(max_length=3, blank=True, help_text="Th current lane of paper roll, y-axis.")
    position = models.IntegerField(null=True, blank=True, help_text="The current position of paper roll, x-axis.")
    rfid_roll_id = models.CharField(max_length=255, blank=True, unique=True, help_text="RFID of paper code, the same number as 'likitomi roll ID'.")
    likitomi_roll_id = models.CharField(max_length=255, blank=True, unique=True, help_text="Likitomi roll ID.")
    invoice_no = models.CharField(max_length=90, blank=True, help_text="Invoice number.")
    invoice_date = models.DateField(null=True, blank=True, help_text="Date of invoice.")
    isdeleted = models.IntegerField(default=0, help_text="Status of paper (0 is not deleted, 1 is deleted), deleted paper will not display in the system.")
    created_by = models.CharField(max_length=90, blank=True, help_text="The person who created the paper roll.")
    created_on = models.DateTimeField(null=True, blank=True, help_text="Timestamp of creating the paper roll.")
    modified_by = models.CharField(max_length=90, blank=True, help_text="The person who modified any data on the paper roll.")
    modified_on = models.DateTimeField(null=True, blank=True, help_text="Timestamp of modifying the data on the paper roll.")
    class Meta:
        """Real table name is 'paper_rolldetails'."""
        db_table = u'paper_rolldetails'


class TblClamplift(models.Model):
    """
    Stores corrugator plan for clamp-lift (clamp-lift plan) retrieving from planning.

    """
    opdate = models.DateField(help_text="Date of the plan.")
    start_time = models.TextField(help_text="Start time of producing a product in plan.") # This field type is a guess.
    stop_time = models.TextField(help_text="Stop time of producing a product in plan.") # This field type is a guess.
    product_code = models.CharField(max_length=30, help_text="Product code.")
    partner_name = models.CharField(max_length=150, help_text="Partner name who is the customer.")
    product_name = models.CharField(max_length=150, help_text="Name of product.")
    sales_order = models.CharField(max_length=30, help_text="Sales order number of the product.")
    autoid = models.IntegerField(help_text="Order number of producing a product in plan.")
    flute = models.CharField(max_length=12, help_text="Flute of product.")
    df = models.CharField(max_length=24, db_column='DF', help_text="Paper code used for DF machine.") # Field name made lowercase.
    bl = models.CharField(max_length=24, db_column='BL', help_text="Paper code used for BL machine.") # Field name made lowercase.
    cl = models.CharField(max_length=24, db_column='CL', help_text="Paper code used for CL machine.") # Field name made lowercase.
    bm = models.CharField(max_length=24, db_column='BM', help_text="Paper code used for BM machine.") # Field name made lowercase.
    cm = models.CharField(max_length=24, db_column='CM', help_text="Paper code used for CM machine.") # Field name made lowercase.
    p_width_inch = models.IntegerField(help_text="Paper width in inch.")
    p_width_mm = models.IntegerField(help_text="Paper width in millimeter (mm.).")
    used_df = models.IntegerField(help_text="Length used of paper for DF machine.")
    used_bl = models.IntegerField(help_text="Length used of paper for BL machine.")
    used_cl = models.IntegerField(help_text="Length used of paper for CL machine.")
    used_bm = models.IntegerField(help_text="Length used of paper for BM machine.")
    used_cm = models.IntegerField(help_text="Length used of paper for CM machine.")
    used_df_lkg = models.IntegerField(help_text="Weight used of paper in kgs. for DF machine.")
    used_bl_lkg = models.IntegerField(help_text="Weight used of paper in kgs. for BL machine.")
    used_cl_lkg = models.IntegerField(help_text="Weight used of paper in kgs. for CL machine.")
    used_bm_lkg = models.IntegerField(help_text="Weight used of paper in kgs. for BM machine.")
    used_cm_lkg = models.IntegerField(help_text="Weight used of paper in kgs. for CM machine.")
    used_df_mkg = models.IntegerField(help_text="+Loss weight used of paper in kgs. for DF machine.")
    used_bl_mkg = models.IntegerField(help_text="+Loss weight used of paper in kgs. for BL machine.")
    used_cl_mkg = models.IntegerField(help_text="+Loss weight used of paper in kgs. for CL machine.")
    used_bm_mkg = models.IntegerField(help_text="+Loss weight used of paper in kgs. for BM machine.")
    used_cm_mkg = models.IntegerField(help_text="+Loss weight used of paper in kgs. for CM machine.")
    t_length = models.IntegerField(help_text="Total length of piece of product at corrugator.")
    case = models.IntegerField(help_text="The number in pieces of product after cut and slit, 'case = cut x slit'")
    cut = models.IntegerField(help_text="The number in pieces of product after cut before slit, 'case = cut x slit'")
    modified_by = models.CharField(max_length=150, help_text="The person who modified the product in plan.")
    modified_on = models.DateTimeField(help_text="Timestamp for nodifying the product in plan.")
    class Meta:
        """Real table name is 'tbl_clamplift'."""
        db_table = u'tbl_clamplift'
