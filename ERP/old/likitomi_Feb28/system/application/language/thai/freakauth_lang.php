<?php  if (!defined('BASEPATH')) exit('No direct script access allowed');
/**
 * Language file needed by the FreakAuth library
 * @package     FreakAuth_light
 * @subpackage  Languages
 * @category    Authentication
 * @author      Daniel Vecchiato (danfreak)
 * @copyright   Copyright (c) 2007, 4webby.com
 * @license		http://www.gnu.org/licenses/lgpl.html
 * @link 		http://4webby.com/freakauth
 * @version 	1.1
 */

//------------------------------------------------------------------
//WEBSITE STUFF
//------------------------------------------------------------------
$lang['FAL_turned_off_message'] = 'The website %s is actually down for maintenance.';
$lang['FAL_welcome'] = 'ยินดีต้อนรับสู่ลิคิโทมิ  :: ';
$lang['FAL_email_halo_message'] = 'Dear';
$lang['FAL_user_name_label'] = 'ชื่อผู้ใช้';
$lang['FAL_user_password_label'] = 'รหัสผ่าน';
$lang['FAL_user_password_confirm_label'] = 'ยืนยันรหัสผ่าน';
$lang['FAL_user_email_label'] = 'อีเมล์';
$lang['FAL_user_autologin_label'] = 'จำรหัส';
$lang['FAL_user_country_label'] = 'ประเทศ';

$lang['FAL_login_label'] = 'เข้าสู้ระบบ';
$lang['FAL_logout_label'] = 'ออกจากระบบ';

$lang['FAL_cancel_label'] = 'ยกเลิ';
$lang['FAL_agree_label'] = 'I Agree';
$lang['FAL_continue_label'] = 'ทำต่อ';
$lang['FAL_donotagree_label'] = 'I Do Not Agree';
$lang['FAL_forgotten_password_label'] = 'ลืมรหัสผ่าน';
$lang['FAL_register_label'] = 'ลงทะเบียน';
$lang['FAL_registration_label'] = 'การลงทะเบียน';
$lang['FAL_change_password_label'] = 'เปลี่ยนรหัสผ่าน';
$lang['FAL_activation_label'] = 'ยืนยันผู้ใช้งาน';

$lang['FAL_citation_message'] = 'Thank You!';
$lang['FAL_already_logged_in_msg'] = 'เข้าใช้งานระบบเรียบร้อยแล้ว!';

$lang['FAL_unknown_user'] = 'ไม่ทราบชื่อผู้ใช้งาน';

$lang['FAL_no_credentials_guest'] = 'You do not have the credentials to access this reserved area, please login and retry.';
$lang['FAL_no_credentials_user'] = 'You do not have the credentials to access this reserved area.';

//------------------------------------------------------------------
//CAPTCHA
//------------------------------------------------------------------
$lang['FAL_captcha_label'] = 'รหัสป้องกันความปลอดภัย';
$lang['FAL_captcha_message'] = 'กรุณากรอกรหัสตามช่องด้านล่าง';

//------------------------------------------------------------------
//REGISTRATION
//------------------------------------------------------------------
$lang['FAL_register_cancel_confirm'] = 'คุณแน่ใจหรือไม่ ว่าต้องการยกเลิกการใช้งานระบบ?\\n\\nกรุณาคลิกที่ ยกเลิก เพื่อไปสู่ขั้นตอนการลงทะเบียน';

$lang['FAL_register_success_message'] = 'Thank You!<br />การลงเบียนของคุณเสร็จสมบูรณ์แล้วครับ!<br /><br />You have just been sent an email containing membership activation instructions.<br />';

$lang['FAL_invalid_register_message'] = 'Invalid registration attempt.';

$lang['FAL_terms_of_service_message'] = 'Terms of Agreement';

//------------------------------------------------------------------
//ACTIVATION
//------------------------------------------------------------------
$lang['FAL_activation_email_subject'] = 'รายละเอียดการยืนยันผู้ใช้งาน';
$lang['FAL_activation_email_body_message'] = 'ขอบคุณสำหรับการละเบียนสมาชิกใหม่\n ยืนยันสมาชิกใหม่, please visit the following URL in the next 24 hours:';

$lang['FAL_activation_login_instruction'] ='After activating your accout you can login as:';
$lang['FAL_activation_keep_data'] ='กรุณาเก็บอีเมล์นี้ไว้เพื่ออ้างอิงในภายหลัง!';

$lang['FAL_activation_failed_message'] = 'ขอโทษด้วยครับ, เนื่องจากการยืนยันสมาชิกล้มเหลว.  กรุณาติดต่อผู้ดูแลระบบ.';
$lang['FAL_activation_success_message'] = 'ยินดีด้วยครับ การยืนยันสมาชิกของคุณสำเร็จแล้ว.  กรุณาเข้าสู่ระบบ.';




//------------------------------------------------------------------
//VALIDATION ERROR MESSAGES
//------------------------------------------------------------------
$lang['FAL_invalid_user_message'] = 'ไม่มีผู้ใช้งาน';
$lang['FAL_invalid_username_password_message'] = 'ไม่มีชื่อผู้ใช้งาน และรหัสผ่านนี้';
$lang['FAL_invalid_username_message'] = 'ไม่มีชื่อผู้ใช้งาน';
$lang['FAL_invalid_password_message'] = 'ไม่มีรหัสผ่าน';
$lang['FAL_username_first_password_message'] = 'กรุณากรอกชื่อผู้ใช้งานของท่าน และรหัสผ่าน';
$lang['FAL_banned_user_message'] = 'Go away man!';
$lang['FAL_login_message'] = 'คุณเข้าสู่ระบบแล้ว';
$lang['FAL_logout_message'] = 'คุณออกจากระบบแล้ว';
$lang['FAL_length_validation_message'] = 'ต้องกรอกระหว่าง %s และ/หรือ %s ตามจำนวนตัวอักษร';
$lang['FAL_allowed_characters_validation_message'] = 'อนุญาตเฉพาะอักขระ, เลขหลัก, ขีดเส้นใต้ หรือ ขีด (-) ตัวอักษร';
$lang['FAL_invalid_validation_message'] = ' %s ไม่ทราบ: ';
$lang['FAL_in_use_validation_message'] = ' %s มีการเรียกใช้อยู่';
$lang['FAL_country_validation_message'] = 'กรุณากรอกประเทศ';
$lang['FAL_user_email_duplicate'] = 'A user with this e-mail has already registered. If you have forgotten your login details you can get them here.';
$lang['FAL_usertemp_email_duplicate'] = 'A user with this e-mail has already registered and is waiting for activation. If this is your e-mail address please check your e-mail inbox and activate your account.';
 
//------------------------------------------------------------------
//CHANGE PASSWORD
//------------------------------------------------------------------
$lang['FAL_change_password_success'] = 'Your password has been successfully changed';
$lang['FAL_old_password_label'] = 'Old Password';
$lang['FAL_new_password_label'] = 'New Password';
$lang['FAL_retype_new_password_label'] = 'Confirm';
$lang['FAL_submit'] = 'Submit';
$lang['FAL_reset'] = 'Reset';
$lang['FAL_change_password_failed_message'] = 'Invalid information';

//------------------------------------------------------------------
//FORGOTTEN PASSWORD
//------------------------------------------------------------------
//->email
$lang['FAL_forgotten_password_email_subject'] = 'Forgotten password reminder';
$lang['FAL_forgotten_password_email_reset_subject'] = 'New login information';
$lang['FAL_forgotten_password_email_header_message'] = 'To reset your password, please go to the following page:';
$lang['FAL_forgotten_password_email_body_message'] = ' You or somebody else requested a password remind about your account. If You do not remember your password and want to change it, please click on the following link:';

$lang['FAL_forgotten_password_email_body_message2'] ='If You did not do any request please ignore this e-mail.';

$lang['FAL_forgotten_password_reset_email_body_message'] = 'Here is your new login information:';
$lang['FAL_forgotten_password_reset_email_user_label'] = 'Username';
$lang['FAL_forgotten_password_reset_email_password_label'] = 'Password';

$lang['FAL_forgotten_password_email_change_message'] = 'To change this ugly password, please go to the following page:';

//->messages
$lang['FAL_forgotten_password_success_message'] = 'Instructions for resetting your password have just been emailed to you. ';
$lang['FAL_forgotten_password_user_not_found_message'] = 'We are sorry, but no user was found with the email address you provided';
$lang['FAL_forgotten_password_reset_failed_message'] = 'We are sorry, but your forgotten password reset has failed.  Contact the site administrator for assistance.';
$lang['FAL_forgotten_password_reset_success_message'] = 'Your password has been reset and emailed to you.';

//------------------------------------------------------------------
//FLASH MESSAGES
//------------------------------------------------------------------
$lang['FAL_user_added'] = ' new user successfully added!';
$lang['FAL_user_edited'] = ' user edited successfully!';
$lang['FAL_user_deleted'] = ' user successfully deleted!';
$lang['FAL_no_permissions'] = 'You don\'t have the credentials to access this area';

//------------------------------------------------------------------
//OTHER MESSAGES
//------------------------------------------------------------------
$lang['FAL_no_DB_data'] = 'No data in DB: please add them!';
$lang['FAL_confirm_delete'] = 'Are you SURE you want to delete this record?';
$lang['download_firefox'] = 'Please use Firefox Browser for this application.';


?>
