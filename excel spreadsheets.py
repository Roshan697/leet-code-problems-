import openpyxl as xl
import os

#print the current working directory
print("current working directory: ", os.getcwd())

#list of all the files in the current working directory
print("files in the current directory: ",os.listdir())

#provide the absolute path to the file 
file_path = os.path.abspath('python excel.xlsx')
print("file path: ",file_path)

wb = xl.load_workbook('test.xlsx')
sheet = wb['Sheet']
cell = sheet['A1']
print(cell.value)