#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Use MySQL/PyMySQL'

__author__ = 'Charles Guo'

import pymysql

'''
# Initialize database

$ mysql -u root -p
$ password
$ create database xxx;
$ use xxx;
'''

# Access database
conn = pymysql.connect(
	host = 'localhost', 
	user = 'root', 
	password = 'Inuyasha0411$', 
	database = "test"
)
crsr = conn.cursor()

'''
# Insert values
crsr.execute('create table user (id varchar(20) primary key, ' + 
	'name varchar(20))')
#crsr.execute('insert into user (id, name) values (%s, %s)', ['A-001','Adam'])
#crsr.execute('insert into user (id, name) values (%s, %s)', ['A-002','Bob'])
#crsr.execute('insert into user (id, name) values (%s, %s)', ['A-003','Carl'])
print('# of rows:', crsr.rowcount)
conn.commit()
crsr.close()
conn.close()
'''


'''
# Search

crsr.execute('select name from user where id = %s', ('A-002',))
vals = crsr.fetchall()
print(vals)
crsr.close()
conn.close()
'''
