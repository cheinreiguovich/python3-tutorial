#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Use SQLite'

__author__ = 'Charles Guo'

import sqlite3

'''
conn = sqlite3.connect('test_db1.db')    # Access/Create a SQLite database
crsr = conn.cursor()    # Create a cursor
crsr.execute('create table user (id varchar(20) primary key, name varchar(20))')
crsr.execute('insert into user (id, name) values (\'1\', \'Adam\')')

print('# of rows:', crsr.rowcount)
crsr.close()    # Close the cursor
conn.commit()    # Commit
conn.close()    # Close connection
'''

conn = sqlite3.connect('test_db1.db')
crsr = conn.cursor()
crsr.execute('select * from user where id = ?', ('1',))
vals = crsr.fetchall()
print(vals)
crsr.close()
conn.close()
