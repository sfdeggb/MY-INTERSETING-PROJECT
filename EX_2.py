import xlwings as xw

app = xw.App(visible=False, add_book=False)
# print("excel应用程序！", app)

att_mth_list = dir(app)
# print("app属性对象的属性和方法", sep=" ")
# print(att_mth_list)

books = app.books #collection合集
# print(type(books))
# print(dir(books))

#book类还是book对象
book = books.add() #自己添加自己
# print(dir(book))
# print(book.sheets)
sheets = book.sheets
# print(dir(sheets))
sheet = sheets.add(name="niubi")
# print(dir(sheet))

#### 工作表对象 sheet 操作的基本单位
### 获取单元格对象或者是单元格区域
sheet = sheets[0]
ran  = sheet['a1']#可以用字母(不区别大小写)，数字（类似于从横坐标）
# print(ran)
# print(type(ran))
ran2 = sheet.range("a1:b2")
# print(ran2)]
# print(sheet.cells)
#### 魔术方法
book.close()
app.quit()


"""python调用VBA"""
