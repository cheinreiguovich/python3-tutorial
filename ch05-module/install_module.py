#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Test installed module'

__author__ = 'Charles Guo'

import sys
sys.path.append('~/Document/Project/github/python3-tutorial/ch05-module')

import use_module
use_module.test()

from PIL import Image

im = Image.open('python-logo.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')
