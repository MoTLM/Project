# Adding data to an excel file from an executable file

import xlsxwriter
import openpyxl
from datetime import date

today = date.today()
yes = set(['yes','y', 'ye', ''])
no = set(['no','n'])

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook("raport"+today.strftime("%B %d"))
worksheet = workbook.add_worksheet()

# Headlines in the sheet
worksheet.write('B1', today.strftime("%B"))
worksheet.write('A2', 'Date')
worksheet.write('B2', 'Describe')
worksheet.write('C2', 'Nr')
worksheet.write('D2', 'Price')
worksheet.write('E2', 'Sum (RON)')

# Start from the first cell.
row = 2
col = 0

# Some data we want to write to the worksheet.
confirm = input("Did you bought anything? (Yes/No)").lower()

if confirm in no:
    print("I am proud of you!")
    worksheet.write(row, col, today.strftime("%B %d, %Y"))
    worksheet.write(row, col +1, "Nothing")
elif confirm in yes:
    for confirm in yes:
        worksheet.write(row, col, today.strftime("%B %d, %Y"))
        item = input("What did you bought?")
        worksheet.write(row, col +1,     item)
        nr = input("How many?")
        worksheet.write(row, col +2,     nr)
        cost = input("Price?")
        worksheet.write(row, col +3,  float(cost))
        row += 1
        confirm = input("Anything else? (Yes/No)").lower()
        if confirm in no:
            break;
else:
    print("We have no time for that!")

# Write a total using a formula.
worksheet.write(3, 4, '=SUM(D3:D1000)')
workbook.close()