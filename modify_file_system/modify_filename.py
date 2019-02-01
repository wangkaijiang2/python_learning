#!/usr/bin/python
# -*- coding: UTF-8 -*- 

#Date: 2019/02/01
#Author: aleck
#Desc: 修改指定目录下的所有文件，包括子目录
import os
filepath="E://develop//code//CocosNew//FuGou//assets//CustomMade//wg0012//Prefabs//PopLayer"
#func changefilename
#功能函数
#@para  目录的绝对路径
def changefilename(path):
    #列出目录下的文件夹
    subdir = os.listdir(path)
    #根据自己需求先删掉不想要的文件
    for i in subdir:
        path_remove = os.path.join(path,i)
        if(path_remove.endswith(".meta")):
            os.remove(path_remove)
    #遍历子目录
    for i in subdir:      
        path_second = os.path.join(path,i)
        #如果是文件夹就递归       
        if os.path.isdir(path_second):                    
            changefilename(path_second)
            #如果是文件就修改文件的名字       
        else:
            newname = path_second[:path_second.index('_')+1] + "wg0012" + path_second[path_second.index('.'):]           
            os.rename(path_second,newname) 
def run():
    changefilename(filepath) 
run()
