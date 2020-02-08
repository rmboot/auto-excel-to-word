# 安装使用
```
git clone https://github.com/rmboot/auto-excel-to-docx
cd auto-excel-to-docx
pip install -r requirements.txt
python auto-excel-to-docx.py
```

# 运行过程
###### 1.pandas读取存储数据的excel表格(data.xlsx)，并将其转换为存储字典(dict)的列表(list)类型。
###### 2.循环读取列表(list)的每项数据(即data.xlsx的每一行)，此时为字典(dict)。
###### 3.docxtpl加载模板文件(temp.docx)并按字典(dict)填充模板的内容。
###### 4.auto-excel-to-docx目录内生成相应的word文件。
