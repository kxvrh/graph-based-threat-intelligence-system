#from urllib import request,parse
import urllib
#import urllib.request
#import urllib.parse
import csv
import base64
csvfile = open('/mnt/hgfs/myshare/data/2018-12-03.csv')
csvdata = csv.reader(csvfile)
for row in csvdata:
    if len(row) <= 10:
        continue
    
    url = 'http://localhost' + row[6]
    if row[6] == '-':
        url = 'http://localhost/'
    req = urllib.request.Request(url)
    req.add_header('User-Agent',row[7])
    req.add_header('Accept','html')
    req.add_header('Connection','keep-alive')

    if row[8] != '-':
        req.add_header('Cookie',row[8])
    if row[3] == 'post':
        data = base64.b64decode(row[4])
        try:
       	    f = urllib.request.urlopen(req,data)
            print(f.status)
        except:
            print("wrong")
    if row[3] == 'get':
        try:
            f = urllib.request.urlopen(req)
            print(f.status)
        except:
            print("wrong")
