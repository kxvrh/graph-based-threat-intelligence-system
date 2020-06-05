import re
import linecache
import pandas as pd
import csv
from urllib import parse
from urllib import request
import base64

def merge(type_file, source_file, target_file):
   flag = 0
   
   data_csv = open(source_file, 'r', encoding='UTF-8')
   data = csv.reader(data_csv)

   i = 3
   prev = 0
   attack = linecache.getline(type_file, i)
   index = attack.find('uri')
   t_uri = re.search('(?<=").*?(?=")', attack[index:])
   t_uri = t_uri.group().replace('\\x', '%')
   t_uri = parse.unquote_plus(t_uri)
   
   for row in data:
      if(flag - prev > 2500):
         break

      r = re.search('([^?]*)', row[6])
      r = r.group().replace('%0A', '\\\\n')
      r = r.replace('%C1%9C', '\\\\')
      s_uri = parse.unquote_plus(r)
      if s_uri == '/':
         s_uri = '/error/noindex.html'
      elif s_uri == '//':
         s_uri = '/error/noindex.html'
      elif s_uri == '-':
         s_uri = '/'
      elif(s_uri[0] == '/' and s_uri[1] == '/'):
         if(s_uri[2] == '/'):
            s_uri = s_uri[2:]
         else:
            s_uri = s_uri[1:]
      
      print(flag)
      #print(s_uri)
      print(i)
      #print(t_uri)
      print('\n')
      for tryIndex in range(-2, 3):  #检查倒序
         attack = linecache.getline(type_file, i + tryIndex)
         index = attack.find('uri')
         t_uri = re.search('(?<=")(.*?)(?=")', attack[index:])
         t_uri = t_uri.group().replace('\\\\x', '%')
         t_uri = parse.unquote(t_uri)
         
         isFind = t_uri == s_uri
         if(isFind):
            content = re.search('[(](.*?)[)]', attack).group()
            if(row[3] == 'post'):
               row[4] = base64.b64decode(row[4])
            content = content[1:len(content)-1]
            content = content.replace(' - ', ',')
            row.append(content)
            
            with open(target_file, 'a', newline='')as t:
               writer = csv.writer(t)
               writer.writerow(row)
            
            i += 1
            prev = flag
            break

      flag += 1
   print(i)

      
         
if __name__ == "__main__":
   type_dir = 'type_0'
   source_dir = '2018-12-0'
   data_dir = 'data-0'
   for i in range(3, 4):
      type_file = type_dir+str(i)+".csv"
      source_file = source_dir+str(i)+".csv"
      data = data_dir+str(i)+".csv"
      merge(type_file, source_file, data)