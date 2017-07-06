#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Datetime'

__author__ = 'Charles Guo'

from datetime import datetime

now = datetime.now()
print(now, '\n', type(now))

dt = datetime(2017, 7, 6, 14, 38, 40)
print(dt)
print(dt.timestamp())

t = 1499366320.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t), 'UTC+0:00')

cday = datetime.strptime('2017/07/06 15:01:30', '%Y/%m/%d %H:%M:%S')
print(cday)
print(now.strftime('%a, %b %d %H:%M'))

from datetime import timedelta
print(now + timedelta(hours = 10))
print(now - timedelta(days = 1, hours = 12))

from datetime import timezone
tz_utc_w4 = timezone(timedelta(hours = -4))
print(now.replace(tzinfo = tz_utc_w4))

utc_dt = datetime.utcnow().replace(tzinfo = timezone.utc)
print(utc_dt)
peking_utc_dt = utc_dt.astimezone(timezone(timedelta(hours = 8)))
print(peking_utc_dt)
tokyo_utc_dt = utc_dt.astimezone(timezone(timedelta(hours = 9)))
print(tokyo_utc_dt)
tokyo_peking_dt = peking_utc_dt.astimezone(timezone(timedelta(hours = 9)))
print(tokyo_peking_dt)

# Exercise
import re

def to_timestamp(dt_str, tz_str):
	re_dt = re.compile(r'^(.{4})\-(.)\-(.{1,2})\s(.{2})\:(.{2})\:(.{2})$')
	re_tz = re.compile(r'^(UTC)([+|-])(.{1,2})\:(.{2})$')
	gp_dt = re_dt.match(dt_str).groups()
	gp_tz = re_tz.match(tz_str).groups()
	# print(gp_dt)
	# print(gp_tz)
	if gp_tz[1] == '+':
		tz_hours = int(gp_tz[2])
	else:
		tz_hours = -int(gp_tz[2])
		
	int_dt = []
	for x in gp_dt:
		int_dt.append(int(x))
	dt = datetime(int_dt[0], int_dt[1], int_dt[2], int_dt[3], int_dt[4], int_dt[5])
	utc_dt = dt - timedelta(hours = tz_hours)
	return utc_dt.timestamp()
		
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
#assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
#assert t2 == 1433121030.0, t2
print('%f\n%f\nPass' % (t1, t2))
