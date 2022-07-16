#guidang_7.12
#压缩包文件归档

# import os, shutil, zipfile

# zip_f = zipfile.ZipFile("D:\\归档\\缘定指间.zip")#创建一个类的实例
# li_names = zip_f.namelist()


# # for file_name in li_names:
# #     item = "D:\\"+file_name
# #     if (os.path.isfile(file_name)):
# #         type = file_name.split(".")[1]
#         if(type=="pdf"):
#             path = "D:\\文件归档\\juben_pdf"
#             #os.makedirs(path)
#             os.mkdir(path)
#             shutil.copyfile(file_name, path)
#         elif(type=="sb3"):
#             path2 ="D:\\文件归档\\code_sb"
#             os.mkdir(path2)
#             shutil.copyfile(file_name, path2)
#         elif(tyoe=="xml"):
#             path3 = "D:\\文件归档\\xml_sb"
#             os.mkdir(path3)
#             shutil.copyfile(file_name, path3)
#         else:
#             pass
#     else:
#         path4 = "D:\\文件归档"
#         os.mkdir(path4)
#         shutil.copytree(file_name, path4)

# # zip_f.close()


import shutil, os

file_res = r"D:\归档文件\缘定指间.zip"
dis_dir = "D:\归档文件"
#解压
shutil._unpack_zipfile(file_res, dis_dir)
#操作文件夹
path1 = r"D:\归档文件\缘定指间\juben_pdf"
path2 =r"D:\归档文件\\缘定指间\code_sb"
os.mkdir(path1)#建立文件夹
os.mkdir(path2)

#使用os.walk()函数

for dirpath, dirnames, filenames in os.walk(dis_dir):######################################
    # print(dirpath)#每个文件夹的绝对路径，不涉及文件
    # print(dirnames)
    for filename in filenames:
        abs_path_filename = os.path.join(dirpath,filename)###########################
        type = filename.split(".")[1]
        if(type=="pdf"):
            shutil.move(abs_path_filename, path1)#这个才可以把文件复制到目录
        elif(type=="sb3"):
            shutil.move(abs_path_filename, path2)
        elif(type=="xml"):
            path3 = r"D:\归档文件\\缘定指间\xml_sb"
            if(not os.path.exists(path3)):##################
                os.mkdir(path3)
            shutil.move(abs_path_filename, path3)
        elif(type=="c"):
            path4 = r"D:\归档文件\\缘定指间\c_sb"
            if(not os.path.exists(path4)):
                os.mkdir(path4)
            shutil.move(abs_path_filename, path4)
        else:
             pass
     
print("文件归档完成！！！！")

        