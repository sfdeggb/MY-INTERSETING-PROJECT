#成绩分发
from win32.client import constants, Dispatchs
import pandas as pd

df=pd.DataFrame(pd.read_excel("io"))#度去excel
df=df[['姓名','课程编号','课程名称','成绩']]
names=df['姓名'].drop_duplicates().values.tolist()
### 上面都是pandas的操作哦

wordApp=DispatchEx('word.Applacation')
#有几个就要·见几个word文档
for name in names:
    myDoc=wordApp.Documents.Open("")#多次打开
    df1=df[df['姓名']==name]
    
    rows=len(df1)
    
    df2=df1[['课程编号','课程姓名','成绩']]
    
    bm=myDoc.Bookmarks('姓名')
    bm.Range.Text=name
    
    bmRange=myDoc.Bookmarks('成绩表').Range#书签
    
    table=myDoc.addTables()#添加表格
    table.Borders.#设置边界粗细2
    #表格单元格赋值
    #循环填写数据
    #保存
    #关闭文档
    #退出应用程序
    
    