#!/usr/bin/eny python3
# -*- coding: utf-8 -*-

'PIL'

__author__ = 'Charles Guo'

from PIL import Image

im = Image.open('./python-logo.jpg')
w, h = im.size
print('Size = %s x %s' % (w, h))

thumb = im
thumb.thumbnail((w/2, h/2))
thumb.save('thumbnail.jpg', 'jpeg')

from PIL import ImageFilter

blur = im
blur.filter(ImageFilter.BLUR)
blur.save('blur.jpg', 'jpeg')

from PIL import ImageDraw, ImageFont
import random

def rndchar():
	return chr(random.randint(65, 90))
	
def rndcolor1():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
	
def rndcolor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

n = 4
height = 60	
width = height * n
new_im = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('Aquabase.ttf', 36)
draw = ImageDraw.Draw(new_im)

for x in range(width):
	for y in range(height):
		draw.point((x, y), fill = rndcolor1())

for x in range(n):
	draw.text((height * x + 10, 10), rndchar(), font = font, fill = rndcolor2())

new_im.filter(ImageFilter.BLUR)
new_im.save('code.jpg', 'jpeg')


