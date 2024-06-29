import openpyxl as xl

wb = xl.load_workbook('pyhton excel.xlsx')
sheet = wb['Sheet1']
cell = sheet['a1']
print(cell)