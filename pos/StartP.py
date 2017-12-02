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
    file_info = open('/etc/pos/info', 'w')
    file_info.write(CN + '\n')
    file_info.close()

    os.system('dmidecode -s system-serial-number >> /etc/pos/info')
    os.system('dmidecode -s system-product-name >> /etc/pos/info')

    return '/etc/pos/info'


def cconfig_anydesk():
    # clean config anydesk
    os.system('rm -rf /home/fepos/.anydesk/*')
    os.system('rm -rf /home/ccpos/.anydesk/*')


def make_swap():
    if os.path.isfile('/swapfile'):
        print('swapfile Exist')
    else:
        os.system('dd if=/dev/zero of=/swapfile bs=1M count=4000')
        os.system('chmod 600 /swapfile')
        os.system('mkswap /swapfile')
        os.system('swapon /swapfile')
        os.system('echo "/swapfile none swap sw 0 0" | sudo tee -a /etc/fstab')
        print('make swap ok')


def main():

    hostname = change_hostname()
    get_info(hostname)
    cconfig_anydesk()
    make_swap()


if __name__ == '__main__':
    main()
