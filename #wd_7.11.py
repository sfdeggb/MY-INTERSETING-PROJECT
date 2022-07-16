# #wd_7.11

# ### 自动生成公文格式
# from win32com.client import constants, DispatchEx

# wordapp= DispatchEx("Word.Application")
# wordapp.Visible=1#启动是可见
# wordapp.DisplayAlerts=0#

# with open(r'D:\\公文格式自动设置.txt') as f:
#     text=f.read()
    
# worddoc= wordapp.Documents.Add()
# worddoc.Range(0,0).InsertBefore(text)
# CentimetersToPoints=28.35
# #设置页面属性
# worddoc.PageSetup.PageWidth=CentimetersToPoints * 21
# worddoc.PageSetup.PageHeight=CentimetersToPoints * 29.7
# worddoc.PageSetup.TopMargin=CentimetersToPoints * 3.7
# worddoc.PageSetup.BottomMargin=CentimetersToPoints * 3.5
# worddoc.PageSetup.LeftMargin=CentimetersToPoints * 2.8
# worddoc.PageSetup.RightMargin=CentimetersToPoints * 2.6
# worddoc.PageSetup.LinesPage=22
# #设置字体格式和大小
# worddoc.Content.Font.NameFarEast="仿宋_GB2312"
# worddoc.Content.Font.Size=15.75
# #设置段落
# Start=worddoc.Paragraphs(2).Range.Start
# End=worddoc.Paragraphs(worddoc.Paragraphs.Count).Range.End

# myRange=worddoc.Range(Start,End)

# myRange.ParagraphFormat.CharacterUnitFirstLineIndent=2
# worddoc.Paragraphs(1).Range.Font.NameFarEast="方正小标宋简体"
# worddoc.Paragraphs(1).Range.Font.Size=21
# worddoc.Paragraphs(1).Range.Font.Bold=True
# worddoc.Paragraphs(1).Range.ParagraphFormat.Alignment=1

# #使用查找和替换
# FindA=worddoc.Content.Find
# FindA.ClearFormatting
# FindA.MatchWildcards=True
# FindA.Replacement.ClearFormatting
# FindA.Replacement.Font.NameFarEast="黑体"
# FindA.Replacement.Font.Bold=True

# #这里就是规律
# FindText="[一二三四五六七八九十]@、*^13"
# FindA.Execute(FindText,ReplaceWith="",Format=True,Replace=2)

# FindA.Replacement.Font.NameFarEast="楷体_GB2312"
# FindA.Replacement.Font.Bold=True

# FindText="（[一二三四五六七八九十]@）*^13"
# FindA.Execute(FindText,ReplaceWith="",Format=True,Replace=2)
# FindA.Replacement.Font.NameFarEast="仿宋_GB2312"
# FindA.Replacement.Font.Bold=True

# FindA.Execute(FindText="[0-9]@、*^13",ReplaceWith="",Format=True,Replace=2)
# FindA.Execute(FindText="（[0-9]@）*^13",ReplaceWith="",Format=True,Replace=2)

# FindText="[一二三四五六七八九十]@是"

# FindA.Execute(FindText,ReplaceWith="",Format=True,Replace=2)
# ##设置选定区域
# myDoc.Sections(1).Footers(1).PageNumbers.Add(PageNumberAlignment=4)
# myDoc.Sections(1).Footers(1).Range.Select()

# pageNum=wordApp.Selection
# pageNum.MoveLeft(constants.wdCharacter,2)
# pageNum.TypeText("—")
# pageNum.MoveRight(constants.wdCharacter,1)
# pageNum.TypeText("—")
# pageNum.WholeStory()
# pageNum.Font.Name="宋体"
# pageNum.Font.Size=14
# myDoc.Sections(1).Headers(1).Range.ParagraphFormat.Borders(-3).LineStyle=0
# myDoc.SaveAs(r'D:\\公文格式自动设置2.docx')
# myDoc.Close()
# wordApp.Quit()


#### 以压缩包的形式来解析word文档

import os, shutil, zipfile

docxpath=input()
path = docxpath.split('.')[0]

shutil.copyfile(docxpath, path+'yasuo.zip')
temp_f = path+'yasuo.zip'
temp_path="D:\\yaya"
out_path = "D\\wocao"
f=zipfile.ZipFile(temp_f)
for file in f.filelist:
    f.extract(file, temp_path)

f.close()
shutil.copytree(temp_path+'\word\media', out_path)
os.remove(temp_f)
shutil.rmtree(temp_path)

