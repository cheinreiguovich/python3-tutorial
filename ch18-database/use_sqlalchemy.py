#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Use SQLAlchemy'

__author__ = 'Charles Guo'

from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql

# Create Class
Base = declarative_base()
class User(Base):
	
	__tablename__ = 'user'
	
	id = Column(String(20), primary_key = True)
	name = Column(String(20))

class Book(Base):
	
	__tablename__ = 'book'
	
	id = Column(String(20), primary_key = True)
	name = Column(String(20))
	usr_id = Column(String(20), ForeignKey('user.id'))

# Create DBSession

db_type, db_driver = 'mysql', 'pymysql'
username, password = 'root', 'Inuyasha0411$'
host, port = 'localhost', 3306
db_name = 'test'
eng = create_engine('%s+%s://%s:%s@%s:%s/%s' % (db_type, db_driver, username, password, host, port, db_name))
DBSession = sessionmaker(bind = eng)
ss = DBSession()

'''
# Access database
conn = pymysql.connect(
	host = 'localhost', 
	user = 'root', 
	password = 'Inuyasha0411$', 
	database = "test"
)
crsr = conn.cursor()
crsr.execute('create table user (id varchar(20) primary key, ' + 
	'name varchar(20))')
crsr.execute('create table book (id varchar(20) primary key, ' + 
	'name varchar(20), usr_id varchar(20))')
'''

'''
# Insert data

usr_1 = User(id = '1', name = 'Adam')
usr_2 = User(id = '2', name = 'Bob')
ss.add(usr_1)
ss.add(usr_2)
book_1 = Book(id = 'sn-01', name = 'Chapter-A', usr_id = '1')
book_2 = Book(id = 'sn-02', name = 'Chapter-B', usr_id = '1')
ss.add(book_1)
ss.add(book_2)
ss.commit()
ss.close()
'''


# Search data

users = ss.query(User).filter(User.id == '1').one()
print('Type:', type(users))
print('Name:', users.name)
ss.close()

