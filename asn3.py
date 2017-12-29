#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:22:59 2017
My name is Fantuo Meng
My student number is 250919681
@author: louis
"""
import scipy.stats
import matplotlib.pylab as plt
import numpy as np
import csv
import scipy.io
# load data from csv
def loaddata(filename):
    
    reader = csv.reader(open(filename , 'r'))
    subjects = []
	
    for r in reader:
        subjects.append(r)
   	
    return subjects




# change data from list into array 
def dat2arr(datalist):
    
    
    
    newarray=np.array(datalist)
    aarray= np.delete(newarray,0,1)
    
    return aarray
    
    
 
# save file as matlab
def save_array(arr, fname):
    
    
    mydict = {}
    mydict['vampire_array']=arr
    
    scipy.io.savemat(fname ,mydict)
    
#manage every element of arr and sort them by the last number. 
#finally calculate the mean min max element of each column
def column_stats(arr, col):
    
    nlist=[]
    vlist=[]
    list=arr.tolist()
    for i in range (len(list)):
        if (list[i][6]=='0'):
            nlist.append(list[i])
        else:
            vlist.append(list[i])
    
    varray=np.array(vlist)
    narray=np.array(nlist)
    
    
    
    
    va=np.array(varray).astype(np.float)
    vmean = np.mean(va, axis=0)[col]
    vmax= va.max(axis=0)[col]
    vmin= va.min(axis=0)[col]
    
   
    
    na=np.array(narray).astype(np.float)
    nmean = np.mean(na, axis=0)[col]
    nmax= na.max(axis=0)[col]
    nmin= na.min(axis=0)[col]
 
    
    
    listv=[]
    listv.append(vmean.tolist())
    listv.append(vmin.tolist())
    listv.append(vmax.tolist())
    
    listn=[]
    listn.append(nmean.tolist())
    listn.append(nmin.tolist())
    listn.append(nmax.tolist())
    
    result=[]
    result.append(listv)
    result.append(listn)
    
    return result
# make a histogram and compare each column
def his_compare(arr,col):
    b=np.array(arr).astype(np.float)
    plt.hist(b[:,col])
    plt.show()
# compare two columns of arr and return the pearsonr number    
def corr_columns(arr,col1,col2):
    b=np.array(arr).astype(np.float)
    return (scipy.stats.pearsonr(b[col1],b[col2]))
 # scatter two columns of arr   
def scatter_columns(arr, col1, col2):
    plt.scatter(arr[:,col1], arr[:,col2])
    plt.show()
# input a row and figure out whether it is a vampire
def is_vampire1(row):
    #q=0.5
    #ww=0.5
    #ss = 0.5
    
    if row[2]>1.12:
        q=0.999
    elif 0.52<row[2]<1.12:
        q=0.9
    elif 0.2<row[2]<0.52:
        q=0.7    
    elif -0.44<row[2]<0.2:
        q=0.5    
    #elif row[2]<-0.44:
    else:
        q=0.4
    
    if row[3]< -0.1:
        ww=0.999
    elif -0.1<row[3]< 0.4:
        ww=0.9
    elif 0.4<row[3]< 0.8:
        ww=0.7
    elif 0.8<row[3]< 1.0:
        ww=0.5
    else:
    #elif row[3]>1:
        ww=0.4

    if row[4]<-0.2:
        ss=0.999
    elif -0.2<row[4]<0.55:
        ss=0.9        
    elif 0.55<row[4]<0.9:
        ss=0.7
    elif 0.9<row[4]<1:
        ss=0.5
    #elif row[4]>1:
    else:
        ss=0.4
    
    return q*ww*ss
# store all the data to measure my function
def log_likelihood(arr, is_vampire1):
    b=np.array(arr).astype(np.float)
    likelihood = 0;
    for row in b:
        result = is_vampire1(row)
        if row[6]>0.5:
            likelihood += np.log(result)
            
        else:
            likelihood += np.log(1-result)
    return likelihood

 