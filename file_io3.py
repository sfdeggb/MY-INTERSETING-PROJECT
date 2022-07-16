### python 标准库之shutil 可以处理文件，文件夹，压缩包。

import shutil
import os
import glob
import hashlib

# print(shutil)
# print(dir(shutil))
#复制文件
#移动文件
#删除文件
#压缩与解压缩


##### 整理文件

# def sort_fie():
    
# 	#创建目的文件夹
# 	deal_path = "C:\\Users\HP\\Documents"
# 	obj_path = "C:\\Users\\HP\\Documents"

# 	# os.mkdir(obj_path+r"\word2文档")
# 	# os.mkdir(obj_path+r"\excel2文档")
# 	# os.mkdir(obj_path+r"\tupian2")

# 	path1 = obj_path+r"\word文档"
# 	path2 = obj_path+r"\excel文档"
# 	path3 =obj_path+r"\tupian"

# 	##解压压缩包
# 	##进入文件夹进行查找
# 	docfiles = glob.glob(deal_path+r"\*.docx")
# 	print(docfiles)
# 	for file in docfiles:
# 		shutil.move(file, path1)
		
# 	excelfiles=glob.glob(deal_path+r"\*.xlsx")
# 	for file in excelfiles:
# 		shutil.move(file, path2)

# 	pngfiles=glob.glob(deal_path+r"\*.png")
# 	for file in pngfiles:
# 		shutil.move(file, path3)
  
# ### 文件查找； glob moudle 和 fnmatch moudle
# ### 重复文件的查找 MD5码，文件的ID
# ### 清理文件迷宫
# path = r"C:\Users\HP\Pictures"

# def file_tree(path, depth):
#     if depth==0:
#         print("文件夹："+ path)
#     for file in os.listdir(path):
#         print('|	'* depth + '+--'+file)## 通过这个来打印出所有的文件,指定相应的格式
#         dirctory = path+'/'+file
#         if os.path.isdir(dirctory):
#             file_tree(dirctory, depth+1)

# file_tree(path, 0)


path = r"C:\Users\HP\Pictures"
## 修改文件名称
for flodname, subfolds, filenames in os.walk(path):
    for filename in filenames:
        abspath = os.path.join(flodname, filename)
        new_name = abspath.replace("\\", "-").replace(':', "-").replace('--', '-')
        new_name = path+new_name
        os.rename(abspath, os.path.join(flodname,new_name))
## 删除空文件夹
for file in os.listdir(path):
    directory = path+'\\'+file
    if os.path.isdir(directory):
        shutil.rmtree(directory)      
## 删除重复文件
list = list()
for file in os.listdir(path):
    fileName=path+"\\"+file
    if os.path.isdir(fileName):
        shutil.rmtree(fileName)
    else:
        m = hashlib.md5()
        with open(filename,'rb') as mfile:
            m.update(mfile.read())#将值放入m种
            md5_value = m.hexdigest()#16进制进行计算
            if md5_value in list:
                os.unlink(fileName)#删除文件
            else:
                list.append(md5_value)



