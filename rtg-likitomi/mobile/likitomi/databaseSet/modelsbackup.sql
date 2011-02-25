BEGIN;CREATE TABLE `addresses` (
    `address_id` integer NOT NULL PRIMARY KEY,
    `partner_id` integer NOT NULL,
    `address` varchar(750) NOT NULL,
    `isdeleted` integer,
    `created_on` datetime,
    `created_by` varchar(90) NOT NULL,
    `modified_on` datetime,
    `modified_by` varchar(90) NOT NULL
)
;
CREATE TABLE `ci_sessions` (
    `session_id` varchar(120) NOT NULL PRIMARY KEY,
    `ip_address` varchar(48) NOT NULL,
    `user_agent` varchar(150) NOT NULL,
    `last_activity` integer NOT NULL,
    `session_data` longtext NOT NULL
)
;
CREATE TABLE `delivery` (
    `delivery_id` integer NOT NULL PRIMARY KEY,
    `sales_order` integer NOT NULL,
    `product_id` integer,
    `product_code` varchar(60) NOT NULL,
    `doc_ref` varchar(90) NOT NULL,
    `delivery_date` date,
    `delivery_time` longtext NOT NULL,
    `qty` integer,
    `delivered_qty` integer,
    `total_production_qty` integer,
    `damaged_qty` integer,
    `status` varchar(90) NOT NULL,
    `remarks` longtext NOT NULL,
    `created_on` datetime,
    `created_by` varchar(90) NOT NULL,
    `modified_on` datetime,
    `modified_by` varchar(90) NOT NULL
)
;
CREATE TABLE `delivery_history` (
    `histid` integer NOT NULL PRIMARY KEY,
    `delivery_id` integer NOT NULL,
    `field` varchar(90) NOT NULL,
    `from` varchar(90) NOT NULL,
    `to` varchar(90) NOT NULL,
    `state` varchar(90) NOT NULL,
    `created_on` datetime,
    `created_by` varchar(90) NOT NULL
)
;
CREATE TABLE `Employee` (
    `eID` varchar(12) NOT NULL PRIMARY KEY,
    `firstname` varchar(765) NOT NULL,
    `lastname` varchar(765) NOT NULL,
    `task` varchar(45) NOT NULL,
    `picture` longtext NOT NULL
)
;
CREATE TABLE `Machine` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY
)
;
CREATE TABLE `fa_country` (
    `id` integer NOT NULL PRIMARY KEY,
    `iso` varchar(6) NOT NULL,
    `name` varchar(240) NOT NULL,
    `iso3` varchar(9) NOT NULL,
    `numcode` integer
)
;
CREATE TABLE `fa_user` (
    `id` integer NOT NULL PRIMARY KEY,
    `user_name` varchar(135) NOT NULL,
    `country_id` integer,
    `password` varchar(150) NOT NULL,
    `email` varchar(360) NOT NULL,
    `role` varchar(150) NOT NULL,
    `banned` integer NOT NULL,
    `forgotten_password_code` varchar(150) NOT NULL,
    `last_visit` datetime,
    `created` datetime NOT NULL,
    `modified` datetime NOT NULL
)
;
CREATE TABLE `fa_user_profile` (
    `id` integer NOT NULL PRIMARY KEY,
    `name` varchar(150) NOT NULL,
    `surname` varchar(150) NOT NULL,
    `phone` varchar(150) NOT NULL
)
;
CREATE TABLE `fa_user_temp` (
    `id` integer NOT NULL PRIMARY KEY,
    `user_name` varchar(135) NOT NULL,
    `country_id` integer,
    `password` varchar(150) NOT NULL,
    `email` varchar(360) NOT NULL,
    `activation_code` varchar(150) NOT NULL,
    `created` datetime NOT NULL
)
;
CREATE TABLE `fake_status_tracking` (
    `plan_id` integer NOT NULL PRIMARY KEY,
    `product_id` varchar(30) NOT NULL,
    `plan_amount` integer,
    `plan_cr_start` datetime,
    `plan_cr_end` datetime,
    `plan_cv_start` datetime,
    `plan_cv_end` datetime,
    `plan_pt_start` datetime,
    `plan_pt_end` datetime,
    `plan_wh_start` datetime,
    `plan_wh_end` datetime,
    `current_status` varchar(33) NOT NULL,
    `actual_amount_cr` integer,
    `actual_cr_start` datetime,
    `actual_cr_end` datetime,
    `actual_amount_cv` integer,
    `actual_cv_start` datetime,
    `actual_cv_end` datetime,
    `actual_amount_pt` integer,
    `actual_pt_start` datetime,
    `actual_pt_end` datetime,
    `actual_amount_wh` integer,
    `actual_wh_start` datetime,
    `actual_wh_end` datetime,
    `previous_section` varchar(15) NOT NULL,
    `cv_machine` varchar(15) NOT NULL
)
;
CREATE TABLE `inch_mm` (
    `inch` integer NOT NULL PRIMARY KEY,
    `mm` integer NOT NULL
)
;
CREATE TABLE `paper_movement` (
    `movement_id` integer NOT NULL PRIMARY KEY,
    `roll_id` integer,
    `before_wt` double precision,
    `actual_wt` double precision,
    `from_station` varchar(60) NOT NULL,
    `to_station` varchar(60) NOT NULL,
    `status` integer,
    `created_by` varchar(60) NOT NULL,
    `created_on` datetime,
    `xpos` varchar(18) NOT NULL,
    `ypos` varchar(18) NOT NULL,
    `zpos` varchar(18) NOT NULL
)
;
CREATE TABLE `paper_rolldetails` (
    `paper_roll_detail_id` integer NOT NULL PRIMARY KEY,
    `paper_code` varchar(90) NOT NULL,
    `supplier_id` integer,
    `supplier_roll_id` varchar(90) NOT NULL,
    `initial_weight` integer,
    `remarks` varchar(750) NOT NULL,
    `notes` varchar(765) NOT NULL,
    `size` integer,
    `uom` varchar(60) NOT NULL,
    `rfid_roll_id` varchar(765) NOT NULL,
    `invoice_no` varchar(90) NOT NULL,
    `invoice_date` date,
    `isdeleted` integer NOT NULL,
    `created_by` varchar(90) NOT NULL,
    `created_on` datetime,
    `modified_by` varchar(90) NOT NULL,
    `modified_on` datetime
)
;
CREATE TABLE `papers` (
    `paper_id` integer NOT NULL PRIMARY KEY,
    `paper_code` varchar(30) NOT NULL UNIQUE,
    `paper_name` varchar(765) NOT NULL,
    `paper_grade` varchar(765) NOT NULL,
    `med_liner` varchar(765) NOT NULL,
    `partner_id_old` integer,
    `partner_sn_old` varchar(30) NOT NULL,
    `paper_remark` varchar(765) NOT NULL,
    `created_on` datetime,
    `created_by` varchar(90) NOT NULL,
    `modified_on` datetime,
    `modified_by` varchar(90) NOT NULL,
    `isdeleted` integer NOT NULL
)
;
CREATE TABLE `partners` (
    `partner_id` integer NOT NULL PRIMARY KEY,
    `partner_code` varchar(60) NOT NULL,
    `partner_supplier_code` varchar(150) NOT NULL,
    `partner_name` varchar(765) NOT NULL,
    `partner_name_thai` varchar(765) NOT NULL,
    `partner_type` varchar(36) NOT NULL,
    `partner_credit_term` varchar(90) NOT NULL,
    `partner_phone_office` varchar(90) NOT NULL,
    `partner_fax` varchar(90) NOT NULL,
    `partner_other_phone` varchar(90) NOT NULL,
    `partner_email` varchar(150) NOT NULL,
    `partner_website` varchar(90) NOT NULL,
    `partner_contact_person` varchar(150) NOT NULL,
    `partner_contact_title` varchar(60) NOT NULL,
    `logo` varchar(765) NOT NULL,
    `created_by` varchar(90) NOT NULL,
    `created_on` datetime,
    `modified_by` varchar(90) NOT NULL,
    `modified_on` datetime,
    `partner_description` longtext NOT NULL,
    `partner_billing_address` longtext NOT NULL,
    `isdeleted` integer NOT NULL
)
;
CREATE TABLE `partners_papers` (
    `tblppid` integer NOT NULL PRIMARY KEY,
    `partner_id` integer NOT NULL,
    `paper_id` integer NOT NULL,
    `paper_code` varchar(30) NOT NULL,
    `isdeleted` integer NOT NULL
)
;
CREATE TABLE `planning` (
    `planning_id` integer NOT NULL PRIMARY KEY,
    `product_code` varchar(30) NOT NULL,
    `mo` varchar(30) NOT NULL,
    `sales_order_id` varchar(30) NOT NULL
)
;
CREATE TABLE `product_catalog` (
    `product_id` integer NOT NULL PRIMARY KEY,
    `product_code` varchar(60) NOT NULL UNIQUE,
    `product_name` varchar(765) NOT NULL,
    `partner_id` varchar(765) NOT NULL,
    `cname` varchar(765) NOT NULL,
    `product_type` varchar(60) NOT NULL,
    `customer_part_no` varchar(60) NOT NULL,
    `ink_1` varchar(60) NOT NULL,
    `ink_2` varchar(60) NOT NULL,
    `ink_3` varchar(60) NOT NULL,
    `ink_4` varchar(60) NOT NULL,
    `joint_type` varchar(60) NOT NULL,
    `joint_details` varchar(150) NOT NULL,
    `box_style` varchar(150) NOT NULL,
    `rope_color` varchar(765) NOT NULL,
    `pcs_bundle` integer,
    `level` varchar(30) NOT NULL,
    `p_width_mm` integer,
    `p_width_inch` integer,
    `qty_allowance` varchar(60) NOT NULL,
    `scoreline_f` integer,
    `scoreline_d` integer,
    `scoreline_f2` integer,
    `slit` integer,
    `blank` integer,
    `t_length` integer,
    `cut` integer,
    `next_process` varchar(300) NOT NULL,
    `code_pd` varchar(300) NOT NULL,
    `code_rd` varchar(300) NOT NULL,
    `sketch` varchar(765) NOT NULL,
    `sketch_large` varchar(765) NOT NULL,
    `remark` varchar(765) NOT NULL,
    `isdeleted` integer NOT NULL,
    `created_on` datetime,
    `created_by` varchar(90) NOT NULL,
    `modified_on` datetime,
    `modified_by` varchar(90) NOT NULL,
    `code` integer
)
;
CREATE TABLE `products` (
    `auto_pid` integer NOT NULL PRIMARY KEY,
    `parent_code` varchar(60) NOT NULL,
    `product_code` varchar(60) NOT NULL,
    `flute` varchar(12) NOT NULL,
    `DF` varchar(30) NOT NULL,
    `BM` varchar(30) NOT NULL,
    `BL` varchar(30) NOT NULL,
    `CM` varchar(30) NOT NULL,
    `CL` varchar(30) NOT NULL,
    `Length_mm` integer,
    `Width_mm` integer,
    `Height_mm` integer,
    `qty_set` integer,
    `square_mp_box` integer,
    `isdeleted` integer NOT NULL,
    `created_on` datetime,
    `created_by` varchar(90) NOT NULL,
    `modified_on` datetime,
    `modified_by` varchar(90) NOT NULL
)
;
CREATE TABLE `reader` (
    `id` integer NOT NULL PRIMARY KEY,
    `tagid` varchar(765) NOT NULL,
    `eventid` varchar(24) NOT NULL
)
;
CREATE TABLE `sales_order` (
    `sales_order_id` integer NOT NULL PRIMARY KEY,
    `sales_order_no` integer,
    `product_id` integer,
    `sales_order_date` date,
    `product_code_1` varchar(60) NOT NULL,
    `amount_1` integer,
    `product_code_2` varchar(60) NOT NULL,
    `amount_2` integer,
    `product_code_3` varchar(60) NOT NULL,
    `amount_3` integer,
    `product_code_4` varchar(60) NOT NULL,
    `amount_4` integer,
    `delivery_at` longtext NOT NULL,
    `purchase_order_no` varchar(150) NOT NULL,
    `salesman` varchar(60) NOT NULL,
    `remarks` longtext NOT NULL,
    `created_on` datetime,
    `created_by` varchar(90) NOT NULL,
    `modified_on` datetime,
    `modified_by` varchar(90) NOT NULL
)
;
CREATE TABLE `stock_planning` (
    `stock_planning_id` integer NOT NULL PRIMARY KEY,
    `delivery_id` integer,
    `DF` varchar(30) NOT NULL,
    `BM` varchar(30) NOT NULL,
    `BL` varchar(30) NOT NULL,
    `CM` varchar(30) NOT NULL,
    `DF_roll_id` integer,
    `BM_roll_id` integer,
    `BL_roll_id` integer,
    `CM_roll_id` integer,
    `created_on` datetime
)
;
CREATE TABLE `sync_clamplift` (
    `id` integer NOT NULL PRIMARY KEY,
    `opdate` date NOT NULL,
    `sync` integer NOT NULL,
    `created_on` datetime NOT NULL
)
;
CREATE TABLE `tagmap` (
    `tagid` integer NOT NULL PRIMARY KEY,
    `eventid` integer NOT NULL
)
;
CREATE TABLE `total_planning` (
    `autoid` integer NOT NULL PRIMARY KEY,
    `date` date NOT NULL,
    `delivery_id` integer NOT NULL,
    `p_width_mm` integer,
    `t_length` integer,
    `flute` varchar(12) NOT NULL,
    `cut` integer,
    `corrugator_date` datetime,
    `converter_date` datetime,
    `patchpartition_date` datetime,
    `warehouse_date` datetime,
    `DF` varchar(21) NOT NULL,
    `BM` varchar(21) NOT NULL,
    `BL` varchar(21) NOT NULL,
    `CM` varchar(21) NOT NULL,
    `CL` varchar(21) NOT NULL,
    `p_width_inch` integer,
    `next_process` varchar(33) NOT NULL
)
;COMMIT;
