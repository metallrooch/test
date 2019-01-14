import yagmail

receiver = "your@gmail.com"
body = "Hello there from Yagmail"

yag = yagmail.SMTP(user=None, password=None, 
	host='smtp.gmail.com', port=None, 
	smtp_starttls=None, smtp_ssl=True, 
	smtp_set_debuglevel=0, smtp_skip_login=False, 
	encoding='utf-8', oauth2_file=None, 
	soft_email_validation=True)
