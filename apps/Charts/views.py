from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.http import JsonResponse
import json
from .utils import DataTable as DT


def index(request):

     return render(request, "Charts/index.html")


def pageLoad(request):
    lables = ['Year', 'Sales', 'Expenses', 'Revenue', 'lable4']
    xAxis = ["2000","2001","2002","2003","2004", "2005", "2006"]
    data = [
            [0,  1000,      400,      600,       100],
            [1,  1170,      460,      710,       200],
            [2,  660,       1400,     -740,      300],
            [3,  1030,      540,      490,       900],
            [4,  None, None,     None,      500],
            [5,  500, 400,     300,      600],
            [6,  200, 750,     -300,      900],
    ]
    anotherColumn = DT.makeLine(len(data))
    data = DT.addLine(data,anotherColumn )
    DefualtData =DT.package(data,lables, xAxis)

    return JsonResponse({"DefualtData" : DefualtData })
