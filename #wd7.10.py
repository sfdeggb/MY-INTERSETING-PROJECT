#wd7.10
### 根据分页符定位来分割文档

from win32com.client import constants,DispatchEx

wordApp = DispatchEx('Word.Application')
#打开文档
myDoc = wordApp.Documents.Open(r'H:\示例\第6章\8首诗\8首诗_分页符.docx')

docCnt=myDoc.Content#获取文本内容

FindA= docCnt.Find
FindA.ClearFormatting
FindA.MatchWildcards = False

FindA.Text = "^m"#查找分页符
i,j = 0,0
while True:  
    FindA.Execute()#执行查找
    if FindA.Found == True :
        if i>0:
            #doc_new = wordApp.Documents.Add()
            doc_new=wordApp.Documents.Add()
            
            s = docCnt.Start#获取位置
            docRange = myDoc.Range(j, s)#获取区域
            docRange.Copy()
            doc_new.Content.Paste()
            
            j = s + 1#下一个位置
            
            print(str(i))
            doc_new.SaveAs('H:\\示例\\第6章\\8首诗\\1\\'+str(i)+'.docx',16) 
            doc_new.Close()
            
        i = i + 1#看一共能查找到几次
    else:
        break

#进行最后一个文档的处理    
doc_new = wordApp.Documents.Add()
s = myDoc.Content.End
docRange = myDoc.Range(j, s)
docRange.Copy()
doc_new.Content.Paste()
doc_new.SaveAs('H:\\示例\\第6章\\8首诗\\1\\'+str(i)+'.docx',16) 
doc_new.Close()

#关闭源文档和进程
myDoc.Close()
wordApp.Quit()



#定位到第一个分页符将其删除

from win32com.client import constants,DispatchEx

wordApp = DispatchEx('Word.Application')
myDoc = wordApp.Documents.Open(r'H:\示例\第6章\8首诗\1\1.docx')

selection = wordApp.Selection
#设定选择的区域
selection.HomeKey(Unit=constants.wdStory)
selection.EndKey(Unit=constants.wdLine, Extend=constants.wdExtend)

selection.Delete()

myDoc.Save()
myDoc.Close()


####文件改名

import os
from win32com.client import constants,DispatchEx

wordApp = DispatchEx('Word.Application')
path = 'H:\\示例\\第6章\\8首诗\\1\\'#这是一个文件夹的路径
files=os.listdir(path)
print(files)

for file in files:
    myDoc = wordApp.Documents.Open(path+file)
    
    selection = wordApp.Selection
    selection.HomeKey(Unit=constants.wdStory)
    selection.EndKey(Unit=constants.wdLine, Extend=constants.wdExtend)
    
    txt=selection.Text
    
    myDoc.Close()
    
    new_name=path+txt.strip()+".docx"
    os.rename(path+file, new_name)##这里进行重命名
    
wordApp.Quit()
