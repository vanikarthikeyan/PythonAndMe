import xlwt
wbv=xlwt.Workbook()
print "The Work book variable is :",wbv
wsv=wbv.add_sheet('demo')
print "The work sheet variable is :",wsv
x=[[101,"vani","chennai"],[102,"karthi","Chennai"]]
i=0
while i<2:
    j=0
    while j<3:
        wsv.write(i,j,x[i][j])
        j=j+1
    i=i+1

wbv.save("demo1.xls")
