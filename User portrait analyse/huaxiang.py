### 处理excel文档
##思路：excel办公自动化
### 涉及exel文档的几个库：
# xlwings：xlwings是一个python库，支持从Excel中调用Python，也支持通过Python去操作Excel，甚至可以调用VBA脚本。
# Xlsxwriter库：精华在于写入元素到excel库中

import xlwings as xw

wb=xw.Book(r"C:\Users\HP\Desktop\问卷调查所有数据.xlsx")
# wb=#打开excel app及book
ws=wb.sheets["分析数据"]

#找出每一列
ran_le_way = ws.range("J2:J64")
ran_sl_pro = ws.range("K2:K64")
ran_plan = ws.range("L2:L64")
ran_live_pro = ws.range("M2:M64")

#处理,遍历处理，然后写入
# content1 = ran_le_way.value
# content2 = ran_sl_pro.value
# content3 = ran_plan.value
# content4 = ran_live_pro.value
con_list = [ran_le_way.value, ran_sl_pro.value, ran_plan.value, ran_live_pro.value]
keys1=["导师", "实验室", "自学", "学校", "考研"]
keys2=["老师", "同学", "大佬", "放弃", "无"]
keys3=["证书", "考研", "课程", "实习"]
keys4=[ "学习", "迷茫", "交流", "人际" , "自律", "自制"]

key_list = [keys1, keys2,keys3, keys4]#多重列表
count = 0
#定位区域行列值, 按照区域对象自身作为参照
row=0
col=0
for con in con_list:
	for content in con:#编历每一列的内容
		keys = key_list[count]
		#判断关键词是否出现
		if(keys[0]=="导师"):
			col=0
			#3个判断的顺序不能乱
			if(keys[4] in content):
				ran_le_way[row, col].value="C"
			if(keys[2] in content or keys[3] in content):
				ran_le_way[row, col].value="B"
			if(keys[0] in content or keys[1] in content):
				ran_le_way[row, col].value="A"
		
		if(keys[0]=="老师"):
			col=0
			#3个判断的顺序不能乱
			if(keys[4] in content or keys[3] in content):
				ran_sl_pro[row, col].value="C"
			if(keys[2] in content or keys[1] in content):
				ran_sl_pro[row, col].value="B"
			if(keys[0] in content ):
				ran_sl_pro[row, col].value="A"

		if(keys[0]=="证书"):
			col=0
			#3个判断的顺序不能乱
			if(keys[3] in content):
				ran_plan[row, col].value="A"
			if(keys[0] in content or keys[2] in content):
				ran_plan[row, col].value="B"
			if(keys[1] in content ):
				ran_plan[row, col].value="C"
      
		if(keys[0]=="学习"):
			col=0
			#3个判断的顺序不能乱
			if(keys[0] in content):
				ran_live_pro[row, col].value="A"
			if(keys[1] in content ):
				ran_live_pro[row, col].value="B"
			if(keys[2] in content or keys[2] in content):
				ran_live_pro[row, col].value="C"
			if(keys[4] in content or keys[5] in content):
				ran_live_pro[row, col].value="D"
		row= row+1
	count=count+1
	row=0
#关闭工作薄.
wb.save(path="D:\\画像数据_finnal.xlsx")
wb.close()
#关闭应用程序

