import os
import pandas as pd
from docxtpl import DocxTemplate

data = pd.read_excel('data.xlsx')
dict_list = data.to_dict(orient="records")
"""
dict_list = [{'姓名': '张三', '性别': '男', '专业': '网络工程'},
             {'姓名': '李四', '性别': '女', '专业': '法学'},
             {'姓名': '王五', '性别': '男', '专业': '生物工程'}]
"""
for i in dict_list:
    tpl = DocxTemplate('temp.docx')
    tpl.render(i)
    tpl.save(i['姓名']+'.docx')
