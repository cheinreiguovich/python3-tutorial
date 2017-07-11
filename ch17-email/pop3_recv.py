#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'POP3 receiving msg'

__author__ = 'Charles Guo'

import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

email, pswd = 'g-ch-r@163.com', 'p_r_chaltier'
srv_pop3 = 'pop.163.com'

srv = poplib.POP3(srv_pop3)
srv.set_debuglevel(1)
print(srv.getwelcome().decode('utf-8'))

srv.user(email)
srv.pass_(pswd)


print('Message: %s. Size: %s' % (srv.stat()))
resp, mails, octets = srv.list()
print(mails)


idx_latest = len(mails)
resp, lines, octets = srv.retr(idx_latest-2)    # Retrieve an email

msg_content = b'\r\n'.join(lines).decode('utf-8')
msg = Parser().parsestr(msg_content)

def decode_str(s):
	val, charset = decode_header(s)[0]
	if charset:
		val = val.decode(charset)
	return val

def guess_charset(msg):
	charset = msg.get_charset()
	if charset is None:
		content_type = msg.get('Content-Type', '').lower()
		pos = content_type.find('charset=')
		if pos >= 0:
			charset = content_type[pos + 8:].strip()
	return charset

def print_msg(msg, indent = 0):
	if indent == 0:
		for header in ['From', 'To', 'Subject']:
			val = msg.get(header, '')
			if val:
				if header == 'Subject':
					val = decode_str(val)
				else:
					hdr, addr = parseaddr(val)
					name = decode_str(hdr)
					val = u'%s <%s>' % (name, addr)
			print('%s%s: %s' % ('  ' * indent, header, val))
	if (msg.is_multipart()):
		parts = msg.get_payload()
		for n, part in enumerate(parts):
			print('%spart %s' % ('  ' * indent, n))
			print('%s----------------' % ('  ' * indent))
			print_msg(part, indent + 1)
	else:
		content_type = msg.get_content_type()
		if content_type == 'text/plain' or content_type == 'text/html':
			content = msg.get_payload(decode = True)
			charset = guess_charset(msg)
			if charset:
				content = content.decode(charset)
			print('%sText: %s' % ('  ' * indent, content + '...'))
		else:
			print('%sAttachment: %s' % ('   ' * indent, content_type))
			
print_msg(msg)