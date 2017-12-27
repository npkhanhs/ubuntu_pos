#!/usr/bin/env python3

'''
	- Install pyvirtualdisplay:
		sudo apt-get install xvfb 
		echo 256487 | sudo -S apt-get install xvfb 
		pip3 install pyvirtualdisplay
'''

try:
    from pyvirtualdisplay import Display
except:
    import os
    os.system("pip3 install pyvirtualdisplay")
    from pyvirtualdisplay import Display
from selenium import webdriver
display = Display(visible=0)
display.start()
driver = webdriver.Firefox()
driver.get('http://nioc.ddns.net/niocweb.html')
