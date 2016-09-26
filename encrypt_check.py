#!/usr/bin/python

import subprocess
import os
import time


def main():
    HOST_DB = '172.16.4.106'
    _ECRYPT_DIR = '/home/cdrone/secret-cdrone'
    _ECRYPT_MOUNT_POINT = '/home/cdrone/secret-cdrone'
    try:
        # while True:
            ###Check HUB connection
        if check_ping(HOST_DB) is True:
            print "OK"
           #Mac =  arp_get_mac(HOST_DB)
            _ecrypt_mount(_ECRYPT_DIR, _ECRYPT_MOUNT_POINT)

        else:
            print "Ping fail"
            # time.sleep(3)
    except:
        print "Error"


def arp_get_mac(ip_address):
    try:
        result_text = subprocess.Popen(("arp -n | grep %s | awk {'print $3'}" % ip_address), stdout=subprocess.PIPE, shell=True).communicate()[0]
        result_text2 = result_text.split('\n')
        return result_text2[0]
    except:
        return "Error"


def _ecrypt_mount(self, edir, mnt):
        """Mount the eCrypt File System
        @param ddir: directory where encrypted file system is stored
        @param mnt: mount point for encrypted file system
        """
        options = ('-o'
                   ' key=passphrase'
                   ',ecryptfs_sig=633937dbcf1fef34'
                   ',passphrase_passwd=password'
                   ',ecryptfs_cipher=aes'
                   ',ecryptfs_key_bytes=16'
                   ',ecryptfs_passthrough=no'
                   ',ecryptfs_enable_filename_crypto=no')
        self._run('mount -t ecryptfs %s %s %s' % (options, edir, mnt))

def check_ping(hostname):

    response = os.system("ping -c 1 %s" % hostname) # linux
    #response = os.system("ping -n 1 %s" % hostname) # Window
    # and then check the response...
    if response == 0:
        print(hostname, 'is up!')
        return True
    else:
        print(hostname, 'is down!')
        for i in range(0, 2):
            response = os.system("ping -c 1 %s" % hostname) # linux
            if response == 0:
                return True
        return False
if __name__ == "__main__":
    main()
