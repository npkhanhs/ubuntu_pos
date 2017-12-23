#!/usr/bin/env python3
# folder download /etc/updatep/git_download
import os

os.system('cp /etc/updatep/git_download/pos/Update.py /etc/updatep/')
os.system('/etc/updatep/nioc.py')
print("nioc ok")
#os.system('pip3 install -r /etc/updatep/git_download/requirements.txt')
#os.system('pip3 install --upgrade pip3')
