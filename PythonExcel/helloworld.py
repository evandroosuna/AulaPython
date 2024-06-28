from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

cell = sheet["A1"]
cell
cell.value
cell.value = "coe"
cell.value

workbook.save(filename="hello_world.xlsx")