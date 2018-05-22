#coding:utf-8
from numpy import *
import operator
##给出训练数据及对应的类别
def createDataSet():
    ##训练数据
    group = array([[1.0,2.0],[1.2,0.1],[0.1,1.4],[0.3,3.5]])
    ##类别
    labels = ['A','A','B','B']
    ##返回
    return group,labels
##通过knn进行分类
def classify(input,dataSet,label,k):
    dataSize = dataSet.shape[0]
    ##计算欧式距离
    diff = tile(input,(dataSize,1)) - dataSet
    sqdiff = diff ** 2
    squareDist = sum(sqdiff,axis = 1)##行向量分别相加，从而获得新的行向量
    dist = squareDist ** 0.5
    ##对距离进行排序
    sortedDistIndex = argsort(dist)##argsort()根据元素的值从大到小对元素进行排序

    classCount = { }
    for i in range(k):
        voteLabe1 = label[sortedDistIndex[i]]
        ##对选取的K个样本所属的类别个数进行统计
        classCount[voteLabe1] = classCount.get(voteLabe1,0) + 1
        ##选取出现的类别次数最多的类别
        maxCount = 0
    for key,value in classCount.items():
        if value > maxCount:
            maxCount = value
            classes = key
    return classes