import pandas as pd
import numpy as np
import re

def get_x_npy(csv_dir):
    # 先用pandas读入csv
    csv_file = csv_dir+".csv"
    data = pd.read_csv(csv_file,encoding='UTF-8')
    print(data.shape)
    #x = data.iloc[:, 0:17]
    # 再使用numpy保存为npy
    np.save(csv_dir+"-x.npy", data)
    #x1 = np.load("sample-x-01.npy", allow_pickle=True)

def get_label(csv_dir):
    '''
    SQLI=1, XSS=2, RFI=3, LFI=4, RCE=5, PHPI=6, HTTP=7, SESS=8
    '''
    csv_file = csv_dir+".csv"
    data = pd.read_csv(csv_file,encoding='UTF-8')
    y = data.iloc[:, 17]
    labels = []
    
    for row in y:
        #print(row)
        num = re.findall('\d+', row)
        num = [int(x) for x in num]
        num = num[1:]
        label = (num.index(max(num)))
        #print(num, label)
        labels.append(label)
    
    np.save(csv_dir+"-y.npy", labels)
    

def get_txt(csv_dir):
    data = pd.read_csv(csv_dir+".csv", encoding='UTF-8')
    x = data.iloc[:, 1:]
    print(x.shape)

    x.to_csv(csv_dir+".txt", index=None)

def setCsvDelimiter(filename, target_file, old_byte, new_byte):
    dataList = []
    with open(filename, 'r', encoding='UTF-8')as f:
        for row in f:
            row = row.replace(old_byte, new_byte)
            dataList.append(row)
        
        with open(target_file, 'w', encoding='UTF-8')as f2:
            for d in dataList:
                f2.write(d)
            

def setDelimiter(sname, tname):
    with open(sname,'r+',encoding='utf-8') as f:
        s = [i[:-1].split(' ') for i in f.readlines()]
    with open(tname,'w+',encoding='utf-8') as f:
        for line in s:
            line = line[1:]
            f.write(" ".join(line)+'\n')


def get_data_set(xfile, yfile):
    x = np.load(xfile)
    y = np.load(yfile)
    np.save("sample-x-train.npy", x[:900, :])
    np.save("sample-y-train.npy", y[:900])
    np.save("sample-x-test.npy", x[900:, :])
    np.save("sample-y-test.npy", y[900:])
    #print(x[900:,:].shape, y[900:].shape)


if __name__ == "__main__":
    #get_x_file("sample")
    #delete_col("sample-x.npy", 1)
    #get_label("sample")
    #print(x[0])
    #get_txt("data")
    #setCsvDelimiter("data.csv", "data-x.txt", ",", " ")
    #setDelimiter("data.txt", "train-x.txt")
    #x = np.loadtxt("train-x.txt")
    #np.save("train-x.npy", x)
    get_data_set("sample-x.npy", "sample-y.npy")
