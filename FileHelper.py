import csv
import pandas as pd
import base64
import chardet

def split_file(source_dir, target_dir):
    #计数器
    flag = 0

    #文件名
    name = 1

    #存放数据
    dataList = []

    print("开始")
    with open(source_dir, 'r', encoding='UTF-8')as f_source:
      for line in f_source:
         flag += 1
         dataList.append(line)
         if(flag == 500000):
            print(str(name)+ "file")
            with open(target_dir+"data"+str(name)+".csv", 'w+')as f_target:
               for data in dataList:
                  f_target.write(data)
            name += 1
            flag = 0
            dataList = []

    with open(target_dir+"data"+str(name)+".csv", 'w+')as f_target:
      for data in dataList:
         f_target.write(data)

    print("完成")

def merge_file(source_dir, target_file, file_num):
   with open(target_file, 'w',encoding='utf-8')as t_file:
      flag = 0
      for i in range(1, file_num+1):
         dataList = []
         with open(source_dir+"-0"+str(i)+".csv", 'r',encoding='utf-8')as f_file:
            for line in f_file:
               if(line[0] == "i"):
                  continue
               #dataList.append(str(flag)+',')
               #dataList.append(str(i))
               dataList.append(line[1:])
               flag += 1
         for d  in dataList:
            t_file.write(d)

def get_type_file(source_dir, target_dir):
    flag = 0
    dataList = []

    with open(source_dir, 'r')as f_source:
        for line in f_source:
            index = line.find('(Total Inbound Score')
            if(index != -1):
                dataList.append(line[index:])
                flag += 1
            
        with open(target_dir, 'w+')as t_source:
            for d in dataList:
                t_source.write(d)

def get_sample_file(source, target):
    dataList = []
    flag = 0
    ip_date = {}
    data_csv = open(source, 'r', encoding='UTF-8')
    data = csv.reader(data_csv)
    ip_date = {}
    for row in data:
        if(ip_date.__contains__(row[1])):
            ip_date[row[1]] += 1            
        else:
            ip_date[row[1]] = 1
        if(ip_date[row[1]] <= 10):
            dataList.append(row)
            flag += 1

    with open(target, 'w', encoding='UTF-8', newline='')as f:
        csv_file = csv.writer(f)
        for data in dataList:
            csv_file.writerow(data)
    
    print(source+" has "+str(ip_date.__len__())+" IPs, "+str(flag)+" data")

      
def check_encoding(filename):
    f = open(filename,'rb')
    data = f.read()
    print (chardet.detect(data))
    #print( chardet.detect(data).get("encoding"))

def to_UTF8_file(source, target):
    flag = 0
    dataList = []
    with open(source,'r', encoding='GB2312') as f1:
        for line in f1:
            dataList.append(str(flag)+',')
            dataList.append(line)
           
            flag += 1
            
    with open(target,'w',encoding='utf-8') as f2:
        for data in dataList:
            f2.write(data)

def set_column_name(filename):
    df = pd.read_csv(filename, encoding='UTF-8', header=None, error_bad_lines=False)
    df.columns = ['id','ip','time','domain-name','request','post-data','parameter',
    'url','user-agent','cookie','x-forwaded-for', 
    'domain-country','domain-province','domain-city',
    'ip-country','ip-province', 'ip-city', 'attack-type']
    '''
    df.columns = ['id', 'sub-id','ip','time','domain-name','request','post-data','parameter',
    'url','user-agent','cookie','x-forwaded-for', 
    'domain-country','domain-province','domain-city',
    'ip-country','ip-province', 'ip-city', 'attack-type']
    '''
    
    #length = len(open('data-utf8.csv').readlines())
    df.to_csv(filename, encoding='UTF-8', index=False)

def delete_col(filename, col_name):
    df = pd.read_csv(filename, encoding='UTF-8')
    df = df.drop(columns = [col_name])
    df.to_csv(filename, encoding='UTF-8', index=False)

def fill_null(filename):
    df = pd.read_csv(filename, encoding='UTF-8')
    df = df.fillna('-')
    df.to_csv(filename, encoding='UTF-8', index=False)

if __name__ == "__main__":
   #to_UTF8_file('data-02.csv', 'data-02-decoded-utf8.csv')
   #print('utf8 file generated')
   #get_sample_file("data-04-decoded-utf8.csv", "sample-04.csv")
   #set_column_name('data-04-decoded-utf8.csv')
   #print('column name set')
   #check_encoding("2018-12-01.csv")
   merge_file("data-decoded-utf8", "data.csv", 4)
   #delete_col("data-04-decoded-utf8.csv", "id")
   #fill_null("data-04-decoded-utf8.csv")