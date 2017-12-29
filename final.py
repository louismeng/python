
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 11:44:10 2017

@author: Administrator
"""
import csv
import numpy as np
import matplotlib.pyplot as plt

def question3():
    name=[]
    price=[]
    qty=[]
    s=0
    print 'Item Name (or CHK for checkout):'
    start = raw_input()
# use loop to ask user whether is done    
    while start!='CHK':
        
        name.append(start)
        ap = float(input('price:'))
        price.append(ap)
        aq = float (input('quantity:'))
        qty.append(aq)
        print 'Item Name (or CHK for checkout):'
        start = raw_input()
    print 'TaX Rate (0.XX): '
    tax = input()
    
    print 'NAMES:' +'      '+'PRICE:'+'      '+'QTY:'+'      '+'TOTALS:'
    for i in name:
        print i 
#change the format
    for j in price:
        print "%.2f" % j
    for k in qty:
        print "%.2f" % k
#zip together to calculate the sum price
    prob = [a*b for a,b in zip(price, qty)]
    for m in prob:
        s=s+m
        print m
    print"----------------------------------------------------------"
    
    print 'SUBTOTAL:'    
    print "%.2f" % s
    print 'TAX RATE:'
    print tax
    print 'TOTAL:' 
    print "%.2f" % (s+s*tax)
          
def question4(test):
#there are two dictionaries to map string into int
    apl = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
    newapl = dict(zip(range(26),"abcdefghijklmnopqrstuvwxyz"))
# define the difference is 3 distance
    key = 3
    

# encipher
    entest = ""
#find stirng in dict and change its position by adding the key
    for c in test.upper():
        if c.isalpha(): entest += newapl[ (apl[c] + key)%26 ]
        else: entest += c

# decipher
    detest = ""
#get the string and offset from encipher, use dict to decipher it by reducing key
    for c in entest.upper():
        if c.isalpha(): detest += newapl[ (apl[c] - key)%26 ]
        else: detest += c

    print test
    print entest
    print detest
    
def question5():
    #get al information
    reader = csv.reader(open('al.csv','r'))
    subjects1=[]
    sub1x=[]
    sub1y=[]
    sub1z=[]
#read from csv and change them into array
    for r in reader:
        subjects1.append(r)
    
    narr=np.array(subjects1)
    
    # 数组减去第一行 头标
    narr=np.delete(narr,0,axis=0)
    #转换成list
    narr=narr.tolist()
    #print narr
#use loop to get the information that we want    
    for i in range (len(narr)):
        if int(narr[i][5])>=100:
        #添加数据 到list
    
            sub1x.append(narr[i][5])
    for i in range (len(sub1x)):
        sub1y.append(narr[i][20])
    for i in range (len(sub1x)):
        sub1z.append(narr[i][10])
    #print len(sub1x), len(sub1y), len(sub1z)
    # x-AB y-OBP z-HR
    
    sub1x = map(int, sub1x)
    
    #sub1y = map(float, sub1y)
    sub1z = map(int, sub1z)
#use loop to scatter plot each plot
    for i in range (len(sub1x)):
        
        plt.scatter(sub1x[i],sub1y[i],c='blue',marker='o', s=sub1z[i])
    
    print '---------------------------'
    #get nl information
    
    reader = csv.reader(open('nl.csv','r'))
    subjects2=[]
    sub2x=[]
    sub2y=[]
    sub2z=[]
    for r in reader:
        subjects2.append(r)
    narr2=np.array(subjects2)
# the same as the last one   
    narr2=np.delete(narr2,0,axis=0)
    narr2=narr2.tolist()
    for i in range (len(narr2)):
        if int(narr2[i][5])>=100:
            sub2x.append(narr2[i][5])
    for i in range (len(sub2x)):
        sub2y.append(narr[i][20])
    for i in range (len(sub2x)):
        sub2z.append(narr[i][10])
    #print sub2x, sub2y,sub2z
    sub2x = map(int, sub2x)
    #sub1y = map(float, sub1y)
    sub2z = map(int, sub2z)
    for i in range (len(sub2x)):
#the same as the last one      
        plt.scatter(sub2x[i],sub2y[i],c='red',marker='o', s=sub2z[i])
    plt.title('Scatter plot')
    plt.ylabel('On Base Percentage')
    plt.xlabel('At Bats')
  
 



        
        
        
        
        
        
        