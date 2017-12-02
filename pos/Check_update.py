#!/usr/bin/env python3

'''
1 - phai co file "ver.txt" trong /etc/updatep
2 - phai cai git
3 - phai co thu muc /etc/updatep  phan quyen full
4 - phai co thu muc /etc/updatep/git_download  
5 - phai co san file Update.py và Check_update.py trong floder /etc/updatep

'''
import requests
import os


def new_update():
    '''
    Check ver update return new ver
    '''
    curent_ver = requests.get('http://npkhanhs.ddns.net/ver_up.txt').text
    with open('/etc/updatep/ver.txt', 'r') as file_ver:
        ver = file_ver.read()
    if (curent_ver != ver):
        return curent_ver


def update():

    newupdate = new_update()
    if newupdate:
        # xoa thu muc clone
        os.system('rm -rf /etc/updatep/git_download')
        # clone git
        os.system(
            'git clone https://github.com/npkhanhs/ubuntu_pos.git /etc/updatep/git_download')
        # copy file update
        os.system('cp /etc/updatep/git_download/pos/Update.py /etc/updatep/')
        #  cap nhat file ver
        with open('/etc/updatep/ver.txt', 'w') as file_ver:
            file_ver.write(newupdate)

    os.system('/etc/updatep/Update.py')


def main():
    
    time.sleep(600)
    update()


if __name__ == '__main__':
    main()
