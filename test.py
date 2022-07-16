# import os

# path = r"D:\web应用程序开发\课件"

# abspath  = os.path.join(path, "nima")
# print(abspath)
# li = list()
# li=[1,2,3,4,5]
# print(li)

# import zipfile

# # zip_f = zipfile.ZipFile("D:\\归档\\缘定指间.zip")
# # li_names = zip_f.namelist()
# # print(li_names)
# path = "D:\\归档\\缘定指间.zip"
# type = path.split(".")[1]
# print(type)
# import os

# print(os.path.isfile('缘定指间/11111.png'))

# import os, shutil, zipfile

# # zip_f = zipfile.ZipFile("D:\\归档\\缘定指间.zip")#创建一个类的实例
# # li_names = zip_f.namelist()

# # path = zipfile.Path("D:\\归档\\缘定指间.zip")
# # print(str(path))
# # gg = "caonima"
# # gg.join("nian")
# # print(gg)

# keys = ["nima", "wocao"]

# gg = "nima, wocao, kao"

# print(keys[0] in gg)


# import xlwings as xw

# wb = xw.Book()
# sheet = wb.sheets['Sheet1']
# rng = sheet.range('A1:D5')
# print(rng[0,0])
# # wb.close()
# import xlwings as xw

# wb=xw.Book(r"D:\huaxiang.xlsx")
# # wb=#打开excel app及book
# ws=wb.sheets["分析数据"]

# #找出每一列
# ran_le_way = ws.range("J2:J64")
# print(ran_le_way[1,0].value)
import os

for dirpath, dirnames, filenames in os.walk("D:\IR"):
	print(filenames[0])