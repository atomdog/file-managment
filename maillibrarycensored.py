import imaplib
import smtplib
import logLibrary
import datetime

def checkmail():
	inbox = imaplib.IMAP4_SSL("imap.gmail.com")
	inbox.login("insertemailhere", "insertemailpasshere")
	inbox.select('inbox')
	iv, maillist = inbox.search(None, "UNSEEN")
	for iteration in maillist[0].split():
		scutvariable = 0
		ecutvariable = 0
		iv, maillist = inbox.fetch(iteration, '(RFC822)')
		rawSMTPDATA = iteration, maillist[0][1]
		rawSMTPDATA = rawSMTPDATA[1]
		scutvariable = rawSMTPDATA.find('From: ') +6
		ecutvariable = rawSMTPDATA.find('Date: ') - 1
		sender = rawSMTPDATA[scutvariable:ecutvariable]
		#scutvariable = rawSMTPDATA.find('Date: ') +6
		#ecutvariable = rawSMTPDATA.find('X-Mms-Sender-Visibility: Show') -1
		#date = rawSMTPDATA[scutvariable:ecutvariable]
		scutvariable = rawSMTPDATA.find('<td>') + 30
		ecutvariable = rawSMTPDATA.find('</td>') -22
		body = rawSMTPDATA[scutvariable:ecutvariable]
		date = datetime.datetime.now()
		body.lower()
		print(sender)
		print(date)
		print(body)
		#logLibrary.dbappend("inlog.csv", sender, date, body)
	inbox.close()
	inbox.logout()

def sendmail(target, msg):
	smtpgateway= smtplib.SMTP('smtp.gmail.com', 587)
	smtpgateway.starttls()
	smtpgateway.login("insertemailhere", "insertemailpasshere")
	smtpgateway.sendmail("insertemailhere", target, msg)
	smtpgateway.quit()

#sendmail("8438197750@txt.att.net", "hello")
#checkmail()
