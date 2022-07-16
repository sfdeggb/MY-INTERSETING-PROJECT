""""文件字数的统计"""

import os
from  collections import Counter

list =list()
puncation = ',。？{}（）：+-...\n'
path = "D:\\大学必读书籍\\CM_圣经\\\Python 黑客与逆向工程师.pdf"#这里是直接读取不了pdf文件的。
with open(path,mode="r") as file_py:
    #num = file_py.seek(1000)
    # print(file_py.name)
    # print(file_py.__str__())
    for line in file_py:#行
        for word in line:
            print(word)
            if word not in puncation:
                list.append()

count = Counter(list)#返回一个字典，每个都是一个键值对。
print(count)