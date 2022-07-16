"""word自动化案列"""
# 自动设置标题

from win32com.client import constants,DispatchEx

wdapp = DispatchEx("Word.Application")
Doc=wdapp.Documents.Open(u"D:\8首诗.docx")
#使用查找个替来完成
FindA= Doc.Content.Find
FindA.ClearFormatting
FindA.MatchByte = False
FindA.Forward = True
FindA.Wrap = constants.WdFindStop
#
Find.Text ="第[0-9]{1,3}首*^13"
#表示可以使用通配符
FindA.MatchWildcards = True 
#进行替换的工作
FindA.Replacement.ClearFormatting
FindA.Replacement.Style = Doc.Styles("标题 1")
FindA.Replacement.ParagraphFormat.Alignment = 1
FindA.Execute(ReplaceWith ="", Format =True, Replace =2)
Doc.SaveAs(u'D:\8首诗2.docx',16)

Doc.Close()
wdapp.Quit()




