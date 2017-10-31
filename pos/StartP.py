#!/usr/bin/env python3


import os
# import requests


def change_hostname():
    CN = input("nhap CN: ")

    with open('/etc/hostname', 'w') as file_hostname:
        file_hostname.write(CN)

    with open('/etc/hosts', 'r+') as file_hosts:
        list_file_hosts = file_hosts.read().split('\n')
        file_hosts.seek(0)
        list_file_hosts[1] = '127.0.0.1\t' + CN
        file_hosts.write('\n'.join(list_file_hosts))

    return CN


def get_info(CN):
    with open('/etc/pos/info', 'w') as file_info:
        file_info.write(CN + '\n')

    os.system('dmidecode -s system-serial-number >> info')
    os.system('dmidecode -s system-product-name >> info')

    return '/etc/pos/info'


def main():
    hostname = change_hostname()
    get_info(hostname)


if __name__ == '__main__':
    main()
