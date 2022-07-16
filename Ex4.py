#Ex4
#### xlxsw文档的读取可以通过读取xml文档来进行操作

### openpyxl,用来读写。xlxs文档(只能操作这一种文档类型)

# import openpyxl as xl
# from openpyxl.styles import colors
# from openpyxl.styles import Font
# import openpyxl.styles
# import openpyxl.workbook

# # xl.Workbook()
# # openpyxl.workbook.

# wb=xl.load_workbook(u"C:\\Users\HP\Documents\excel文档\咖啡师认证表指引20210922v1.xlsx")#read_only
# print(dir(wb))
# # wb.sheetnames
# ws2 = wb.create_sheet()
# wb.remove_sheet(worksheet)
# wb.save(filename)
# wb.close()

# ws = wb.get_sheet_by_name(name)
# ws.max_row
# ws.max_column
# ws.sheet_properties.tabColor = colors.BLUE
# ws.merge_cells()

# cell = ws.cell(row, column)#row and column 都是以1开始
# cell.value
# # cell.font = Font(name= , bold=,
# #                  size=
# #                  )

# cell.alignment = Alignment()



##### XlsxWriter .xlsx的生成库(只适合从零开始制作xlxs文档)，不能够读取excel文档
# import xlsxwriter as xlwriter

# wb  = xlwriter.Workbook("C:\\Users\HP\Documents\excel文档\图表.xlsx")
# font = wb.add_format()
# font.border_index = 3


# ws = wb.add_worksheet()
# ## ws.()一共有大概两百多个，常用的记录
# ws.write(0, 0, "nima", font)
# ws.write_row(row, col, data)
# ws._write_formula(row, col, formula)
# ws.merge_range(data)

#### pandas 读取excel文档
import pandas as pd 



