## word文档拆分
from win32com.client import constants, DispatchEx

wordapp = DispatchEx("Word.Application")
myDoc=wordapp.Documents.Open("D:\\8首诗.docx")

FindA=myDoc.Content.Find
FindA.MatchByte=False
FindA.Forward = True
FindA.warp=constants.wdFindStop
FindA.Text="第[0-9]{1,3}首*^13"
FindA.MatchWildcards=True

FindA.Excute(ReplaceWith='^m^&',Replace=2)
myDoc.SaveAs("D:\\8首诗.docx", 16)

myDoc.Close()
wordapp.Quit()