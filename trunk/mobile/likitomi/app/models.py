## This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models


class Addresses(models.Model):
    address_id = models.IntegerField(primary_key=True)
    partner_id = models.IntegerField()
    address = models.CharField(max_length=750, blank=True)
    isdeleted = models.IntegerField(null=True, blank=True)
    created_on = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=90, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    modified_by = models.CharField(max_length=90, blank=True)
    class Meta:
        db_table = u'addresses'

    


class CiSessions(models.Model):
    session_id = models.CharField(max_length=120, primary_key=True)
    ip_address = models.CharField(max_length=48)
    user_agent = models.CharField(max_length=150)
    last_activity = models.IntegerField()
    session_data = models.TextField(blank=True)
    class Meta:
        db_table = u'ci_sessions'

class Delivery(models.Model):
    delivery_id = models.IntegerField(primary_key=True)
    sales_order = models.IntegerField()
    product_id = models.IntegerField(null=True, blank=True)
    product_code = models.CharField(max_length=60, blank=True)
    doc_ref = models.CharField(max_length=90, blank=True)
    delivery_date = models.DateField(null=True, blank=True)
    delivery_time = models.TextField() # This field type is a guess.
    qty = models.IntegerField(null=True, blank=True)
    delivered_qty = models.IntegerField(null=True, blank=True)
    total_production_qty = models.IntegerField(null=True, blank=True)
    damaged_qty = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=90, blank=True)
    remarks = models.TextField(blank=True)
    created_on = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=90, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    modified_by = models.CharField(max_length=90, blank=True)
    class Meta:
        db_table = u'delivery'

class DeliveryHistory(models.Model):
    histid = models.IntegerField(primary_key=True)
    delivery_id = models.IntegerField()
    field = models.CharField(max_length=90, blank=True)
    from_field = models.CharField(max_length=90, db_column='from', blank=True) # Field renamed because it was a Python reserved word. Field name made lowercase.
    to = models.CharField(max_length=90, blank=True)
    state = models.CharField(max_length=90, blank=True)
    created_on = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=90, blank=True)
    class Meta:
        db_table = u'delivery_history'

class Employee(models.Model):
    eid = models.CharField(max_length=12, primary_key=True, db_column='eID') # Field name made lowercase.
    firstname = models.CharField(max_length=765, blank=True)
    lastname = models.CharField(max_length=765, blank=True)
    task = models.CharField(max_length=45, blank=True)
    picture = models.TextField(blank=True)
    class Admin:
        pass
    class Meta:
        db_table = u'employee'

class FaCountry(models.Model):
    id = models.IntegerField(primary_key=True)
    iso = models.CharField(max_length=6)
    name = models.CharField(max_length=240)
    iso3 = models.CharField(max_length=9, blank=True)
    numcode = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'fa_country'

class FaUser(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=135)
    country_id = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=150)
    email = models.CharField(max_length=360)
    role = models.CharField(max_length=150)
    banned = models.IntegerField()
    forgotten_password_code = models.CharField(max_length=150, blank=True)
    last_visit = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    class Meta:
        db_table = u'fa_user'

class FaUserProfile(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, blank=True)
    surname = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = u'fa_user_profile'

class FaUserTemp(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=135)
    country_id = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=150)
    email = models.CharField(max_length=360)
    activation_code = models.CharField(max_length=150)
    created = models.DateTimeField()
    class Meta:
        db_table = u'fa_user_temp'

class FakeStatusTracking(models.Model):
    plan_id = models.IntegerField(primary_key=True)
    product_id = models.CharField(max_length=30, blank=True)
    plan_amount = models.IntegerField(null=True, blank=True)
    plan_cr_start = models.DateTimeField(null=True, blank=True)
    plan_cr_end = models.DateTimeField(null=True, blank=True)
    plan_cv_start = models.DateTimeField(null=True, blank=True)
    plan_cv_end = models.DateTimeField(null=True, blank=True)
    plan_pt_start = models.DateTimeField(null=True, blank=True)
    plan_pt_end = models.DateTimeField(null=True, blank=True)
    plan_wh_start = models.DateTimeField(null=True, blank=True)
    plan_wh_end = models.DateTimeField(null=True, blank=True)
    plan_due = models.DateTimeField(null=True, blank = True)
    current_status = models.CharField(max_length=33, blank=True)
    actual_amount_cr = models.IntegerField(null=True, blank=True)
    actual_cr_start = models.DateTimeField(null=True, blank=True)
    actual_cr_end = models.DateTimeField(null=True, blank=True)
    actual_amount_cv = models.IntegerField(null=True, blank=True)
    actual_cv_start = models.DateTimeField(null=True, blank=True)
    actual_cv_end = models.DateTimeField(null=True, blank=True)
    actual_amount_pt = models.IntegerField(null=True, blank=True)
    actual_pt_start = models.DateTimeField(null=True, blank=True)
    actual_pt_end = models.DateTimeField(null=True, blank=True)
    actual_amount_wh = models.IntegerField(null=True, blank=True)
    actual_wh_start = models.DateTimeField(null=True, blank=True)
    actual_wh_end = models.DateTimeField(null=True, blank=True)
    actual_due = models.DateTimeField(null=True, blank=True)
    process1 = models.CharField(max_length=5, blank=True)
    process2 = models.CharField(max_length=5, blank=True)
    process3 = models.CharField(max_length=5, blank=True)
    process4 = models.CharField(max_length=5, blank=True)
    cv_machine = models.CharField(max_length=15, blank=True)
    days_left = models.IntegerField(null=True, blank=True)

    class Admin: pass

    class Meta:
        db_table = u'fake_status_tracking'
    def calculate_date(self):
        import datetime
        return 8
        #return int((datetime.datetime.now() - self.plan_due))
    #days_left = property(calculate_date)


class InchMm(models.Model):
    inch = models.IntegerField(primary_key=True)
    mm = models.IntegerField()
    class Meta:
        db_table = u'inch_mm'

class PaperMovement(models.Model):
    movement_id = models.IntegerField(primary_key=True)
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
    remarks = models.CharField(max_length=750, blank=True)
    notes = models.CharField(max_length=765, blank=True)
    size = models.IntegerField(null=True, blank=True)
    uom = models.CharField(max_length=60, blank=True)
    rfid_roll_id = models.CharField(max_length=765, blank=True)
    invoice_no = models.CharField(max_length=90, blank=True)
    invoice_date = models.DateField(null=True, blank=True)
    isdeleted = models.IntegerField()
    created_by = models.CharField(max_length=90, blank=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_by = models.CharField(max_length=90, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'paper_rolldetails'

class Papers(models.Model):
    paper_id = models.IntegerField(primary_key=True)
    paper_code = models.CharField(unique=True, max_length=30)
    paper_name = models.CharField(max_length=765, blank=True)
    paper_grade = models.CharField(max_length=765, blank=True)
    med_liner = models.CharField(max_length=765, blank=True)
    partner_id_old = models.IntegerField(null=True, blank=True)
    partner_sn_old = models.CharField(max_length=30)
    paper_remark = models.CharField(max_length=765, blank=True)
    created_on = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=90, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    modified_by = models.CharField(max_length=90, blank=True)
    isdeleted = models.IntegerField()
    class Meta:
        db_table = u'papers'

class Partners(models.Model):
    partner_id = models.IntegerField(primary_key=True)
    partner_code = models.CharField(max_length=60, blank=True)
    partner_supplier_code = models.CharField(max_length=150, blank=True)
    partner_name = models.CharField(max_length=765)
    partner_name_thai = models.CharField(max_length=765, blank=True)
    partner_type = models.CharField(max_length=36, blank=True)
    partner_credit_term = models.CharField(max_length=90)
    partner_phone_office = models.CharField(max_length=90, blank=True)
    partner_fax = models.CharField(max_length=90, blank=True)
    partner_other_phone = models.CharField(max_length=90, blank=True)
    partner_email = models.CharField(max_length=150, blank=True)
    partner_website = models.CharField(max_length=90, blank=True)
    partner_contact_person = models.CharField(max_length=150, blank=True)
    partner_contact_title = models.CharField(max_length=60, blank=True)
    logo = models.CharField(max_length=765, blank=True)
    created_by = models.CharField(max_length=90, blank=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_by = models.CharField(max_length=90)
    modified_on = models.DateTimeField(null=True, blank=True)
    partner_description = models.TextField(blank=True)
    partner_billing_address = models.TextField(blank=True)
    isdeleted = models.IntegerField()
    class Meta:
        db_table = u'partners'

class PartnersPapers(models.Model):
    tblppid = models.IntegerField(primary_key=True)
    partner_id = models.IntegerField()
    paper_id = models.IntegerField()
    paper_code = models.CharField(max_length=30)
    isdeleted = models.IntegerField()
    class Meta:
        db_table = u'partners_papers'

class Planning(models.Model):
    planning_id = models.IntegerField(primary_key=True)
    product_code = models.CharField(max_length=30, blank=True)
    mo = models.CharField(max_length=30, blank=True)
    sales_order_id = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = u'planning'

class ProductCatalog(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_code = models.CharField(unique=True, max_length=60, blank=True)
    product_name = models.CharField(max_length=765, blank=True)
    partner_id = models.CharField(max_length=765, blank=True)
    cname = models.CharField(max_length=765, blank=True)
    product_type = models.CharField(max_length=60, blank=True)
    customer_part_no = models.CharField(max_length=60, blank=True)
    ink_1 = models.CharField(max_length=60, blank=True)
    ink_2 = models.CharField(max_length=60, blank=True)
    ink_3 = models.CharField(max_length=60, blank=True)
    ink_4 = models.CharField(max_length=60, blank=True)
    joint_type = models.CharField(max_length=60, blank=True)
    joint_details = models.CharField(max_length=150, blank=True)
    box_style = models.CharField(max_length=150, blank=True)
    rope_color = models.CharField(max_length=765, blank=True)
    pcs_bundle = models.IntegerField(null=True, blank=True)
    level = models.CharField(max_length=30, blank=True)
    p_width_mm = models.IntegerField(null=True, blank=True)
    p_width_inch = models.IntegerField(null=True, blank=True)
    qty_allowance = models.CharField(max_length=60, blank=True)
    scoreline_f = models.IntegerField(null=True, blank=True)
    scoreline_d = models.IntegerField(null=True, blank=True)
    scoreline_f2 = models.IntegerField(null=True, blank=True)
    slit = models.IntegerField(null=True, blank=True)
    blank = models.IntegerField(null=True, blank=True)
    t_length = models.IntegerField(null=True, blank=True)
    cut = models.IntegerField(null=True, blank=True)
    next_process = models.CharField(max_length=300, blank=True)
    code_pd = models.CharField(max_length=300, blank=True)
    code_rd = models.CharField(max_length=300, blank=True)
    sketch = models.CharField(max_length=765, blank=True)
    sketch_large = models.CharField(max_length=765, blank=True)
    remark = models.CharField(max_length=765, blank=True)
    isdeleted = models.IntegerField()
    created_on = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=90, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    modified_by = models.CharField(max_length=90, blank=True)
    code = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'product_catalog'

class Products(models.Model):
    auto_pid = models.IntegerField(primary_key=True)
    parent_code = models.CharField(max_length=60, blank=True)
    product_code = models.CharField(max_length=60, blank=True)
    flute = models.CharField(max_length=12, blank=True)
    df = models.CharField(max_length=30, db_column='DF', blank=True) # Field name made lowercase.
    bm = models.CharField(max_length=30, db_column='BM', blank=True) # Field name made lowercase.
    bl = models.CharField(max_length=30, db_column='BL', blank=True) # Field name made lowercase.
    cm = models.CharField(max_length=30, db_column='CM', blank=True) # Field name made lowercase.
    cl = models.CharField(max_length=30, db_column='CL', blank=True) # Field name made lowercase.
    length_mm = models.IntegerField(null=True, db_column='Length_mm', blank=True) # Field name made lowercase.
    width_mm = models.IntegerField(null=True, db_column='Width_mm', blank=True) # Field name made lowercase.
    height_mm = models.IntegerField(null=True, db_column='Height_mm', blank=True) # Field name made lowercase.
    qty_set = models.IntegerField(null=True, blank=True)
    square_mp_box = models.IntegerField(null=True, blank=True)
    isdeleted = models.IntegerField()
    created_on = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=90, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    modified_by = models.CharField(max_length=90, blank=True)
    class Meta:
        db_table = u'products'


class Reader(models.Model):
    id = models.IntegerField(primary_key=True)
    tagid = models.CharField(max_length=765)
    eventid = models.CharField(max_length=24, blank=True)
    class Meta:
        db_table = u'reader'

class SalesOrder(models.Model):
    sales_order_id = models.IntegerField(primary_key=True)
    sales_order_no = models.IntegerField(null=True, blank=True)
    product_id = models.IntegerField(null=True, blank=True)
    sales_order_date = models.DateField(null=True, blank=True)
    product_code_1 = models.CharField(max_length=60, blank=True)
    amount_1 = models.IntegerField(null=True, blank=True)
    product_code_2 = models.CharField(max_length=60, blank=True)
    amount_2 = models.IntegerField(null=True, blank=True)
    product_code_3 = models.CharField(max_length=60, blank=True)
    amount_3 = models.IntegerField(null=True, blank=True)
    product_code_4 = models.CharField(max_length=60, blank=True)
    amount_4 = models.IntegerField(null=True, blank=True)
    delivery_at = models.TextField(blank=True)
    purchase_order_no = models.CharField(max_length=150, blank=True)
    salesman = models.CharField(max_length=60, blank=True)
    remarks = models.TextField(blank=True)
    created_on = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=90, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    modified_by = models.CharField(max_length=90, blank=True)
    class Meta:
        db_table = u'sales_order'

class StockPlanning(models.Model):
    stock_planning_id = models.IntegerField(primary_key=True)
    delivery_id = models.IntegerField(null=True, blank=True)
    df = models.CharField(max_length=30, db_column='DF', blank=True) # Field name made lowercase.
    bm = models.CharField(max_length=30, db_column='BM', blank=True) # Field name made lowercase.
    bl = models.CharField(max_length=30, db_column='BL', blank=True) # Field name made lowercase.
    cm = models.CharField(max_length=30, db_column='CM', blank=True) # Field name made lowercase.
    df_roll_id = models.IntegerField(null=True, db_column='DF_roll_id', blank=True) # Field name made lowercase.
    bm_roll_id = models.IntegerField(null=True, db_column='BM_roll_id', blank=True) # Field name made lowercase.
    bl_roll_id = models.IntegerField(null=True, db_column='BL_roll_id', blank=True) # Field name made lowercase.
    cm_roll_id = models.IntegerField(null=True, db_column='CM_roll_id', blank=True) # Field name made lowercase.
    created_on = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'stock_planning'

class SyncClamplift(models.Model):
    id = models.IntegerField(primary_key=True)
    opdate = models.DateField()
    sync = models.IntegerField()
    created_on = models.DateTimeField()
    class Meta:
        db_table = u'sync_clamplift'

class Tagmap(models.Model):
    tagid = models.IntegerField(primary_key=True)
    eventid = models.IntegerField()
    class Meta:
        db_table = u'tagmap'

class TotalPlanning(models.Model):
    autoid = models.IntegerField(primary_key=True)
    date = models.DateField()
    delivery_id = models.IntegerField()
    p_width_mm = models.IntegerField(null=True, blank=True)
    t_length = models.IntegerField(null=True, blank=True)
    flute = models.CharField(max_length=12, blank=True)
    cut = models.IntegerField(null=True, blank=True)
    corrugator_date = models.DateTimeField(null=True, blank=True)
    converter_date = models.DateTimeField(null=True, blank=True)
    patchpartition_date = models.DateTimeField(null=True, blank=True)
    warehouse_date = models.DateTimeField(null=True, blank=True)
    df = models.CharField(max_length=21, db_column='DF', blank=True) # Field name made lowercase.
    bm = models.CharField(max_length=21, db_column='BM', blank=True) # Field name made lowercase.
    bl = models.CharField(max_length=21, db_column='BL', blank=True) # Field name made lowercase.
    cm = models.CharField(max_length=21, db_column='CM', blank=True) # Field name made lowercase.
    cl = models.CharField(max_length=21, db_column='CL', blank=True) # Field name made lowercase.
    p_width_inch = models.IntegerField(null=True, blank=True)
    next_process = models.CharField(max_length=33, blank=True)
    class Meta:
        db_table = u'total_planning'
