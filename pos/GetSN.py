#!/usr/bin/env python3

import time
import requests


def UpSN():
    time.sleep(2)
    time_login = time.asctime(time.localtime(time.time()))
    file_info = open('/etc/pos/info', 'r')
    info_machine = file_info.read().replace('\n', ';')
    file_info.close()
    print(info_machine)
    requests.post('http://npkhanhs.ddns.net/logging.php',
                  {"value": info_machine + time_login})


def main():
    UpSN()


if __name__ == '__main__':
    main()
