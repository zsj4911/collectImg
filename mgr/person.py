from ast import Pass, Try
from fileinput import filename
from importlib.resources import path
from turtle import title
from django.shortcuts import render
from config import settings

# 导入创建文件夹的功能
from .function import mkdir
import os
from django.http import JsonResponse
import xlrd

def add_person(request):

    # 根据session判断用户是否是登录的管理员用户
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
            'msg': '未登录',
            'redirect': '/mgr/sign.html'}, 
            status=302)

    if request.session['usertype'] != 'mgr' :
        return JsonResponse({
            'ret': 302,
            'msg': '用户非mgr类型',
            'redirect': '/mgr/sign.html'} ,
            status=302)

    myFile = request.FILES.get("file_obj", None)
    if myFile:
        dir = os.path.join(os.path.join(settings.BASE_DIR, 'upload'),'excel')
        destination = open(os.path.join(dir, myFile.name),'wb+')
        for chunk in myFile.chunks():
            destination.write(chunk)
        destination.close()

        print(dir)
        print(myFile.name)
        
        filename = dir + "\\" + myFile.name
        # print(filename)
        workbook = xlrd.open_workbook(filename)
        # 获取第一个sheet表格
        table = workbook.sheets()[0]
        table_list = table.col_values(colx=0, start_rowx=1, end_rowx=None)
        # print(table_list)
        data = {"ret":0,"data":table_list}
        return JsonResponse(data)
    else:
        data = {"ret":"1","msg":"文件上传失败"}
        return JsonResponse(data)


def list_person(request):

    # 根据session判断用户是否是登录的管理员用户
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
            'msg': '未登录',
            'redirect': '/mgr/sign.html'}, 
            status=302)

    if request.session['usertype'] != 'mgr' :
        return JsonResponse({
            'ret': 302,
            'msg': '用户非mgr类型',
            'redirect': '/mgr/sign.html'} ,
            status=302)

    filename = ""
    dir = os.path.join(os.path.join(settings.BASE_DIR, 'upload'),'excel')
    # print(dir)
    filename =  dir + "\\提交名单.xlsx"

    try:
        workbook = xlrd.open_workbook(filename)
        # 获取第一个sheet表格
        table = workbook.sheets()[0]
        table_list = table.col_values(colx=0, start_rowx=1, end_rowx=None)
        data = {"ret":0,"data":table_list}
        return JsonResponse(data)
    except FileNotFoundError:
        data = {"ret":1,"msg":"名单不存在"}
        return JsonResponse(data)


def delete_person(request):

    # 根据session判断用户是否是登录的管理员用户
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
            'msg': '未登录',
            'redirect': '/mgr/sign.html'}, 
            status=302)

    if request.session['usertype'] != 'mgr' :
        return JsonResponse({
            'ret': 302,
            'msg': '用户非mgr类型',
            'redirect': '/mgr/sign.html'} ,
            status=302)

    dir = os.path.join(os.path.join(settings.BASE_DIR, 'upload'),'excel')
    filename =  dir + "\\\\提交名单.xlsx"
    try:
        os.remove(filename)
        data = {"ret":0,"msg":"删除成功"}
        return JsonResponse(data)
    except FileNotFoundError:
        data = {"ret":1,"msg":"删除失败, 文件不存在"}
        return JsonResponse(data)

