#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'SQLite exercise'

__author__ = 'Charles Guo'

import os, sqlite3

db_file = os.path.join(os.path.abspath('.'), 'test.db')
'''
# Initialize database

if os.path.isfile(db_file):
	os.remove(db_file)

conn = sqlite3.connect(db_file)
crsr = conn.cursor()
crsr.execute('create table user (id varchar(20) primary key, ' + 
	'name varchar(20), score int)')
crsr.execute(r"insert into user values ('A-001', 'Adam', 95)")
crsr.execute(r"insert into user values ('A-002', 'Bart', 62)")
crsr.execute(r"insert into user values ('A-003', 'Lisa', 78)")
crsr.close()
conn.commit()
conn.close()
'''

def get_score_in(low, high):
	conn = sqlite3.connect(db_file)
	crsr = conn.cursor()
	crsr.execute('select name from user where score >= ? and score <= ? order by score', (low, high,))
	vals = crsr.fetchall()
	crsr.close()
	conn.close()
	return list(x[0] for x in vals)

assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)
print('Pass')

