import urllib
import urllib2
import csv
import base64
import time
csvfile = open('/mnt/hgfs/myshare/code/2018-12-03.csv')
csvdata = csv.reader(csvfile)
i = 0
file = open('index.txt', 'w')
for row in csvdata:
    print(i)
    if(i == 300000):
        break
    if len(row) <= 10:
        continue
    
    url = 'http://localhost' + row[6]
    if row[6] == '-':
        url = 'http://localhost/'
    req = urllib2.Request(url)
    req.add_header('User-Agent',row[7])
    req.add_header('Accept','html')
    req.add_header('Connection','keep-alive')

    if row[8] != '-':
        req.add_header('Cookie',row[8])
    if row[3] == 'post':
        data = base64.b64decode(row[4])
        try:
            f = urllib2.urlopen(req,data)
        except urllib2.HTTPError as e:
            #print(e.code)
            file.write(str(i)+"\n")

    if row[3] == 'get':
        try:
            f = urllib2.urlopen(req)
        except urllib2.HTTPError as e:
            file.write(str(i)+"\n")
            #print(e.code)

    i = i + 1
    #time.sleep(0.05)

f.close()
  
    