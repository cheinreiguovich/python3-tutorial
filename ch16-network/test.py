#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Test'

__author__ = 'Charles Guo'

import subprocess

fpath_srv = 'E:\\Projects\\github\\python3-tutorial\\ch16-network\\srv_program.py'
fpath_tcp = 'E:\\Projects\\github\\python3-tutorial\\ch16-network\\test_app_tcp.py'
fpath_udp = 'E:\\Projects\\github\\python3-tutorial\\ch16-network\\test_app_udp.py'

subprocess.call(['Python.exe', fpath_srv])
