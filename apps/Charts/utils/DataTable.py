# this is going to be a set of helper functions to translate from pandas to the
#table structure that google charts wants
#I think it makes the most sense to keep the data in session and manipulate it from there.
#the only reason I might need to make this a class is to have the lable lists global
#all lines come in the format of [[x1,y1],[x2,y2],[xn,yn]]
#when
#So its a little fragile but packageTable will get data into the format that google charts wants, the main requirments is that the data has to have an index that can either be turned into a string or over written by a list of strings and all of the elements need to be of a similar height and shape
#Also when I'm storing session information I need to be storing xAxis lables as a list, lineLables as a lists and the dataTable as a nested list... now can I get pandas to play nicely with this?



import random
import numpy as np
import operator
import sys
import unittest
import requests #library for web request http://docs.python-requests.org/en/master/
import pandas #data structure manipulation http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe

class ViewableChart(object):
    #so when I instantiate a new viewableChart object do I want to be able to pass in values? I think so

    def __init__(self):
        self.LineLables = ["xAxis"]
        self.XAxisLable = []
        self.data = [] #I still don't understand why this works :)
        self.width = 0
        self.height = 0

    def addColumn(self, line, lable):
        self.LineLables.append(lable)
        for x,y in line:
            self.data[x].append(y)

        return self


def getKey(item):
    return item[0]

def makeLine(length): #for now use a line but later add ability to have a call back function to change the shape of the line
    #all lines come in the format of [[x1,y1],[x2,y2],[xn,yn]]
    # function = mx + b
    newLine = []
    for i in range(length):
        newLine.append([i,i * 100])
    return newLine


def makeRandomSet(total_count, variance, selection):
    """this is the help string """
    randomSet = []

    for i in range (0 , int(total_count)):
        randomSet.append([i, random.randint(-1*int(variance),int(variance))+i])
    if (int(total_count) > int(selection)):
        return sorted(random.sample(randomSet, int(selection)), key = getKey)

    return randomSet


def addLine(data, line):
    newData = data
    #add the line to the data... if there is a size mismatch how do i want to handle it? the data holds the xAxis so the line should stitch on to it i think... should it be able to flow past the end? yes hmm also what if my original data had holes and im filling in the blanks with the new line? this is like adding a column in a matrix and they do kinda need to match sizes i may end up doing all of this with pandas dat frames so i'm not going to waste any mroe time on it and just assume that they need to be the same size.

    for x,y in line:
        data[x].append(y)


    return newData

def xAxisToString(dataTable):
    output = []
    for row in dataTable:
        row[0] = str(row[0])
        output.append(row)
    return output

def addLineLables(data, lables):
    output = []
    output.append(lables)
    for row in data:
        output.append(row)
    return output

def package(data, lables, xAxis = 0):
    #this is going to be the last step where we take both sets of lables and slap em on to the data
    if (xAxis == 0):
        data = xAxisToString(data)
    else:
        print(len(data))
        for i in range(len(data)):
            data[i][0] = xAxis[i]

    table = addLineLables(data,lables )

    return table



#for debug
if __name__ == "__main__":
    from pprint import pprint

    # r = makeRandomSet(50,10,5)
    # r2 = makeRandomSet(50,10,5)
    # print(r)
    # addLine(r, r2)

    l1 = makeLine(5)
    l2 = makeLine(5)

    # newtable = addLine(l1, l2)
    # print(newtable)
    # lables = ["xAxis", "Line1", "Line2"]
    # xAxis = ["2000","2001","2002","2003","2004", "2005", "2006"]
    # print("length of xAxis lables is: ", len(xAxis))
    # arrayReponse = package(newtable, lables,xAxis )
    # print(arrayReponse)

    newChart = ViewableChart()
    # newChart.data = l1
    newChart.addColumn(l2, "Line2")
    print(newChart.data)
    print(newChart.LineLables)


    # pprint(myChart.packUp())
