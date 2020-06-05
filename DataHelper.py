import csv
import re
import numpy as np

def count_IP_num(filename):
    data_csv = open(filename, 'r', encoding='UTF-8')
    data = csv.reader(data_csv)
    ip_date = {}
    for row in data:
        if(ip_date.__contains__(row[1])):
            ip_date[row[1]] += 1
        else:
            ip_date[row[1]] = 1
    
    count = 0
    for (k,v) in  ip_date.items(): 
        count += 1
        print (k, v) 
    print(count)

def AHP():
    matrix = np.array([[1, 3, 5, 1, 5, 5],
              [1/3, 1, 3, 1/2, 3, 5],
              [1/5, 1/3, 1, 1/3, 2, 3],
              [1, 2, 3, 1, 5, 5],
              [1/5, 1/3, 1/2, 1/5, 1, 1],
              [1/5, 1/5, 1/3, 1/5, 1, 1]])
    #print(matrix.shape)
    eigenvalue,featurevector = np.linalg.eig(matrix)
    print(featurevector)
    max_eigen = max(float(x) for x in eigenvalue)
    #print(max_eigen)
    CI = (max_eigen - 6)/(6 - 1)
    RI = 1.24
    CR = CI/RI
    if(CR < 0.1):
        print("一致性通过")
    else:
        print("一致性不通过")
    print(CR)
    W = ReImpo(matrix)
    print(W)

def ReImpo(F):
    n=np.shape(F)[0]
    W=np.zeros([1,n])
    for i in range(n):
        t=1
        for j in range(n):
            t=F[i,j]*t
        W[0,i]=t**(1/n)
    W=W/sum(W[0,:])  # 归一化 W=[0.874,2.467,0.464]
    return W.T


if __name__ == "__main__":
    #count_IP_num("data-04-decoded-utf8.csv")
    AHP()

    