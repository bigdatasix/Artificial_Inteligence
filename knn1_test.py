#coding: utf-8
import sys
sys.path.append("E:\ProgramData\Anaconda3")
from  knn import knn1
from numpy import *
input = array([1.1,0.3])
dataSet,labels =knn1.createDataSet()
K = 3
output = knn1.classify(input,dataSet,labels,K)
print(('测试数据为：'),input,("分类结果为："),output)