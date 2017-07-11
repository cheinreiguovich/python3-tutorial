#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Simple Mail Transfer Protocal Sending Msg'

__author__ = 'Charles Guo'

from email import encoders
from email.header import Header    # Header(str, coding)
from email.mime.text import MIMEText as MMT
from email.mime.multipart import MIMEMultipart as MMM
from email.mime.base import MIMEBase as MMB
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))

#addr_from = input('Please input your E-mail address: ')
#pswd = input('Please input your password: ')
#addr_to = input('Please input destination E-mail address: ')
#smtp_srv = input('SMTP server: ')
addr_from, pswd = 'g-ch-r@163.com', 'p_r_chaltier'
addr_to = '13811195453@139.com'
smtp_srv = 'smtp.163.com'

# Define Msg
msg = MMT('干嘛呢?', 'plain', 'utf-8')    # MMT(text, subtype, coding)

msg = MMT('<html><body><h1>干嘛呢？</h1>' +
    '<p>send by <a href="https://www.linkedin.com/in/chenruiguo/">Chenrui Guo</a>\'s Python Client</p>' +
    '</body></html>', 'html', 'utf-8')

msg = MMM('alternative')
msg['From'] = _format_addr('Chenrui Guo <%s>' % (addr_from))
msg['To'] = _format_addr('Huixin Li <%s>' % (addr_to))
msg['Subject'] = Header('这是标题', 'utf-8').encode()
msg_txt = MMT('干嘛呢?', 'plain', 'utf-8')
msg_html = MMT('<html><body><h1>干嘛呢？</h1>' + 
	'<p><img src="cid:0"></p>' + 
	'</body></html>', 'html', 'utf-8')
msg.attach(msg_txt)
msg.attach(msg_html)

#import os
#pwd = os.path.abspath('.')
with open(r'C:\Users\guoch\OneDrive\Documents\Project\github\python3-tutorial\ch17-email\avatar.jpg', 'rb') as f:
	mime = MMB('image', 'jpg', filename = 'avatar.jpg')
	# Add header
	mime.add_header('Content-Disposition', 'attachment', filename = 'avatar.jpg')
	mime.add_header('Content-ID', '<0>')
	mime.add_header('X-Attachment-Id', '0')
	# Read attachments and encode with base64
	mime.set_payload(f.read())
	encoders.encode_base64(mime)
	msg.attach(mime)

# Setup server
# <163.com> imap.163.com/smtp.163.com/pop.163.com 993(SSL)/994(SSL)/995(SSL)
# <outlook.com --- POP3> pop3.live.com/smtp.live.com 995(SSL)/587(SSL/TLS)
# <outlook.com --- IMAP> imap-mail.outlook.com/smtp-mail.outlook.com 993(SSL)/587(SSL/TLS)
srv = smtplib.SMTP_SSL(smtp_srv, 994) 
srv.starttls()   
srv.set_debuglevel(1)
srv.login(addr_from, pswd)
srv.sendmail(addr_from, [addr_to], msg.as_string())
srv.quit()

