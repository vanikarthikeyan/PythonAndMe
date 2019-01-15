import xlrd 
wb=xlrd.open_workbook("demo2.xls")
ns=wb.nsheets
snames=wb.sheet_names()
print "Total number of sheets :",ns
print "Sheet names :",snames
ws=wb.sheet_by_index(1)
nr=ws.nrows
nc=ws.ncols
print "Total number of rows contain data:",nr
print "Total number of columns contain data:",nc
for i in range(nr):
    for j in range(nc):
        x=ws.cell(i,j).value
        print x

