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
    movement_id = models.AutoField(primary_key=True)
    roll_id = models.IntegerField(null=True, blank=True)
    before_wt = models.FloatField(null=True, blank=True)
    actual_wt = models.FloatField(null=True, blank=True)
    from_station = models.CharField(max_length=60, blank=True)
    to_station = models.CharField(max_length=60, blank=True)
    status = models.IntegerField(null=True, blank=True)
    created_by = models.CharField(max_length=60, blank=True)
    created_on = models.DateTimeField(null=True, blank=True)
    xpos = models.CharField(max_length=18, blank=True)
    ypos = models.CharField(max_length=18, blank=True)
    zpos = models.CharField(max_length=18, blank=True)
    class Meta:
        db_table = u'paper_movement'


class PaperRolldetails(models.Model):
    paper_roll_detail_id = models.IntegerField(primary_key=True)
    paper_code = models.CharField(max_length=90, blank=True)
    supplier_id = models.IntegerField(null=True, blank=True)
    supplier_roll_id = models.CharField(max_length=90, blank=True)
    initial_weight = models.IntegerField(null=True, blank=True)
    temp_weight = models.IntegerField(null=True, blank=True)
    remarks = models.CharField(max_length=750, blank=True, unique=True) # Act as Likitomi Roll ID
    notes = models.CharField(max_length=765, blank=True)
    size = models.IntegerField(null=True, blank=True)
    uom = models.CharField(max_length=60, blank=True)
    lane = models.CharField(max_length=3, blank=True)
    position = models.IntegerField(null=True, blank=True)
    rfid_roll_id = models.CharField(max_length=255, blank=True, unique=True)
    invoice_no = models.CharField(max_length=90, blank=True)
    invoice_date = models.DateField(null=True, blank=True)
    isdeleted = models.IntegerField(default=0)
    created_by = models.CharField(max_length=90, blank=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_by = models.CharField(max_length=90, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'paper_rolldetails'


class TblClamplift(models.Model):
    opdate = models.DateField()
    start_time = models.TextField() # This field type is a guess.
    stop_time = models.TextField() # This field type is a guess.
    product_code = models.CharField(max_length=30)
    partner_name = models.CharField(max_length=150)
    product_name = models.CharField(max_length=150)
    sales_order = models.CharField(max_length=30)
    autoid = models.IntegerField()
    flute = models.CharField(max_length=12)
    df = models.CharField(max_length=24, db_column='DF') # Field name made lowercase.
    bl = models.CharField(max_length=24, db_column='BL') # Field name made lowercase.
    cl = models.CharField(max_length=24, db_column='CL') # Field name made lowercase.
    bm = models.CharField(max_length=24, db_column='BM') # Field name made lowercase.
    cm = models.CharField(max_length=24, db_column='CM') # Field name made lowercase.
    p_width_inch = models.IntegerField()
    p_width_mm = models.IntegerField()
    used_df = models.IntegerField()
    used_bl = models.IntegerField()
    used_cl = models.IntegerField()
    used_bm = models.IntegerField()
    used_cm = models.IntegerField()
    used_df_lkg = models.IntegerField()
    used_bl_lkg = models.IntegerField()
    used_cl_lkg = models.IntegerField()
    used_bm_lkg = models.IntegerField()
    used_cm_lkg = models.IntegerField()
    used_df_mkg = models.IntegerField()
    used_bl_mkg = models.IntegerField()
    used_cl_mkg = models.IntegerField()
    used_bm_mkg = models.IntegerField()
    used_cm_mkg = models.IntegerField()
    t_length = models.IntegerField()
    case = models.IntegerField()
    cut = models.IntegerField()
    modified_by = models.CharField(max_length=150)
    modified_on = models.DateTimeField()
    class Meta:
        db_table = u'tbl_clamplift'
