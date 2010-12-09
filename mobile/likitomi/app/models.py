# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=240)
    #class Meta:
    #    db_table = u'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()
    #class Meta:
     #   db_table = u'auth_group_permissions'

class AuthMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    message = models.TextField()
    #class Meta:
    #    db_table = u'auth_message'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    content_type_id = models.IntegerField()
    codename = models.CharField(unique=True, max_length=255)
    #class Meta:
     #   db_table = u'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=90)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=384)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    #class Meta:
    #    db_table = u'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()
    #class Meta:
    #    db_table = u'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()
    #class Meta:
     #   db_table = u'auth_user_user_permissions'

class CiSessions(models.Model):
    session_id = models.CharField(max_length=120, primary_key=True)
    ip_address = models.CharField(max_length=48)
    user_agent = models.CharField(max_length=150)
    last_activity = models.IntegerField()
    session_data = models.TextField(blank=True)
    #class Meta:
    #    db_table = u'ci_sessions'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user_id = models.IntegerField()
    content_type_id = models.IntegerField(null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=600)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    #class Meta:
     #   db_table = u'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    app_label = models.CharField(unique=True, max_length=255)
    model = models.CharField(unique=True, max_length=255)
    #class Meta:
    #    db_table = u'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=120, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    #class Meta:
     #   db_table = u'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=300)
    name = models.CharField(max_length=150)
    #class Meta:
     #   db_table = u'django_site'

class Employee(models.Model):
    eid = models.CharField(max_length=12, primary_key=True, db_column='eID') # Field name made lowercase.
    firstname = models.CharField(max_length=765, blank=True)
    lastname = models.CharField(max_length=765, blank=True)
    task = models.CharField(max_length=45, blank=True)
    picture = models.TextField(blank=True)
    class Meta:
        db_table = u'employee'

class FaCountry(models.Model):
    id = models.IntegerField(primary_key=True)
    iso = models.CharField(max_length=6)
    name = models.CharField(max_length=240)
    iso3 = models.CharField(max_length=9, blank=True)
    numcode = models.IntegerField(null=True, blank=True)
    #class Meta:
     #   db_table = u'fa_country'

class FaUser(models.Model):
    faid = models.IntegerField(primary_key=True)
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
    #class Meta:
     #   db_table = u'fa_user'

class FaUserProfile(models.Model):
    faid = models.IntegerField(unique=True)
    name = models.CharField(max_length=150, blank=True)
    surname = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=150, blank=True)
    #class Meta:
    #    db_table = u'fa_user_profile'

class FaUserTemp(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=135)
    country_id = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=150)
    email = models.CharField(max_length=360)
    activation_code = models.CharField(max_length=150)
    created = models.DateTimeField()
    #class Meta:
    #    db_table = u'fa_user_temp'

class FakeStatusTracking(models.Model):
    plan_id = models.IntegerField(primary_key=True, db_column='plan_id')
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
    current_status = models.CharField(max_length=33)
    actual_id = models.IntegerField()
    actual_amount_cr = models.IntegerField()
    actual_cr_start = models.DateTimeField(null=True, blank=True)
    actual_cr_end = models.DateTimeField(null=True, blank=True)
    actual_amount_cv = models.IntegerField()
    actual_cv_start = models.DateTimeField(null=True, blank=True)
    actual_cv_end = models.DateTimeField(null=True, blank=True)
    actual_amount_pt = models.IntegerField()
    actual_pt_start = models.DateTimeField(null=True, blank=True)
    actual_pt_end = models.DateTimeField(null=True, blank=True)
    actual_amount_wh = models.IntegerField()
    actual_wh_start = models.DateTimeField(null=True, blank=True)
    actual_wh_end = models.DateTimeField(null=True, blank=True)
    previous_section = models.CharField(max_length=15, blank=True)
    cv_machine = models.CharField(max_length=15, blank=True)
    class Meta:
        db_table = u'fake_status_tracking'

class FakeTotalActual(models.Model):
    actual_id = models.IntegerField(primary_key=True)
    actual_amount_cr = models.IntegerField()
    actual_cr_start = models.DateTimeField(null=True, blank=True)
    actual_cr_end = models.DateTimeField(null=True, blank=True)
    actual_amount_cv = models.IntegerField()
    actual_cv_start = models.DateTimeField(null=True, blank=True)
    actual_cv_end = models.DateTimeField(null=True, blank=True)
    actual_amount_pt = models.IntegerField()
    actual_pt_start = models.DateTimeField(null=True, blank=True)
    actual_pt_end = models.DateTimeField(null=True, blank=True)
    actual_amount_wh = models.IntegerField()
    actual_wh_start = models.DateTimeField(null=True, blank=True)
    actual_wh_end = models.DateTimeField(null=True, blank=True)
    #class Meta:
    #    db_table = u'fake_total_actual'

class FakeTotalPlanning(models.Model):
    plan_id = models.IntegerField(primary_key=True)
    product_id = models.CharField(max_length=30, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    cr_start = models.DateTimeField(null=True, blank=True)
    cr_end = models.DateTimeField(null=True, blank=True)
    cv_start = models.DateTimeField(null=True, blank=True)
    cv_end = models.DateTimeField(null=True, blank=True)
    pt_start = models.DateTimeField(null=True, blank=True)
    pt_end = models.DateTimeField(null=True, blank=True)
    wh_start = models.DateTimeField(null=True, blank=True)
    wh_end = models.DateTimeField(null=True, blank=True)
    current_status = models.CharField(max_length=33)
    #class Meta:
     #   db_table = u'fake_total_planning'

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
    #class Meta:
    #    db_table = u'product_catalog'

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
    #class Meta:
    #    db_table = u'products'
