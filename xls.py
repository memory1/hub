import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('B:B', len('hello world') + 1)
worksheet.write('B5', 'hello world')
workbook.close()