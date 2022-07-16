##读取一个文件的时候，读取前8个字节是其文件头。
## 不同的文件有不同的文件头。
## 字面上更改文件扩展名是不会改变文件的本质属性的。
## 只是指明了用哪个扩展打开。

"""os库用来操作操作系统的功能的接口"""
"""os.path模块用来对文件的路径进行操作"""

#### os模块常用的函数
#### os.path模块常用的函数。

import os

# print(os.path)

## 遍历一个文件夹里的所有文件
### listdir()只能遍历一层， 第一层文件和子目录，无法深层遍历

def list_file_in_dir():
	path = "C:\\Users\\HP\\Documents\\Tencent Files\\2128449235\\FileRecv"

	for foldName, subfolders, filenames in os.walk(path):#有三个返回元组
		for filename in filenames:
			print(foldName,filename)
   
## 文件路径的操作
def operate_path():
    path = "C:\\Users\\HP\\Documents\\Tencent Files\\2128449235\\FileRecv\\什么是青年科技教育？.pdf"
    print(os.path.split(path))#m默认用.来分离文件路径和文件名
    print(os.path.dirname(path))#显示文件夹路径
    print(os.path.basename(path))#显示文件名
    print(os.path.splitext(path))#将目录与文件后缀名分开。
    
    
#os.path模块获取文件的属性
## 各种时间, 文件大小，Bytes
## 删除无用的小文件

base_path = "C:\\Users\\HP\\Documents\\Tencent Files\\2128449235\\FileRecv"
def delete_gar_file():
    files = os.listdir(path)
    for file in files:
      type = os.path.splitext(file)[1]
      size = os.path.getsize(file)
      if type == ".txt" and  size<2000:
          os.remove(file)

if __name__ == "__main__":
    # fun1 = operate_path()
	fun2 = delete_gar_file()

    