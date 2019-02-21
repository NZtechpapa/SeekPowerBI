#时间 2018/06/21 17:24
#提取职位分类跟具体职位.方便后期根据具体职位进行搜索
import requests # 网络请求
import re
import time
import random
from bs4 import BeautifulSoup
import pandas as pd
url='https://www.lagou.com/'
html = requests.get(url)
html = html.text.encode(html.encoding).decode()
soup= BeautifulSoup(html,'html.parser')
 
dataList=[]
for i in soup.find_all("div",{"class":"menu_sub dn"}):  #这里主要是为了获取到岗位的二级分类.
    for i2 in i.find_all("dl"):
        bigposition=re.search(r'<span>(.*?)</span>',str(i2)).group(1)
        list=re.findall('>(.*?)</a>',str(i2))
        for row in list:
            dataList.append([bigposition,row])
dataList.insert(0,["分类","职位"])  #在list最前面插入column名.
 
 
dataList=pd.DataFrame(dataList)
dataList.to_csv(r"./lagouPositionData.csv",encoding = "utf-8",mode="a+",index=0,header=0)

