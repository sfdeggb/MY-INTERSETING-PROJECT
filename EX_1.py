import xlwings as xw


#app类对象
app = xw.App(visible=False, add_book=False)#打开程序不可见，不添加工作薄
# print(xw.__doc__)
# print("\n\n\n")
print(type(app))
# print(dir(app))
print("app 类的属性和方法如下")
for unit in dir(app):
    leixing = type(eval("app."+unit))#eval()用来执行字符串
    print(leixing)
