#!/usr/bin/env python3


import os
# import requests


def change_hostname():
    CN = input("nhap CN: ")

    file_hostname_open = open('/etc/hostname', 'w')
    file_hostname_open.write(CN)
    file_hostname_open.close()

    file_hosts_open = open('/etc/hosts', 'r+')
    file_hosts = file_hosts_open.read()
    list_file_hosts = file_hosts.split('\n')
    list_file_hosts[1] = '127.0.0.1\t' + CN
    file_hosts = '\n'.join(list_file_hosts)
    file_hosts_open.seek(0)
    file_hosts_open.write(file_hosts)
    file_hosts_open.close()

    file_info = open('/etc/pos/info', 'w')
    file_info.write(CN + '\n')
    file_info.seek(1)
    file_info.close()

    os.system('dmidecode -s system-serial-number >> info')
    os.system('dmidecode -s system-product-name >> info')

    os.system('rm')


def main():
    change_hostname()


if __name__ == '__main__':
    main()
