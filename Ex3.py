#python调用vba
import xlwings as xw

app = xw.App()
wb = app.books.open(r"D:\python\学Python，不加班——轻松实现办公自动化\源代码文件+数据文件\第5章\自动运行宏.自动运行宏.xlsm")
#api属性会将xlwings对象转化为pywin32对象
wb.api.Application.Run('abc')#基于工作薄来调用函数的
wb.save()
#同时的ws = wb.sheets[0]
#rg=ws.range()
#t同时他它的value,addcoment, font, size, blod,
#app一定要记得退出
################### python中直接使用vba函数
# wb.macro(name)##直接books对象调用


################ vba调用python
################自动化excel必须搞清楚文件的结构。
