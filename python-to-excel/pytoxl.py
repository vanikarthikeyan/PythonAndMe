import xlwt
wbv=xlwt.Workbook()
print "The Work book variable is :",wbv
wsv=wbv.add_sheet('demo')
print "The work sheet variable is :",wsv
wsv.write(0,0,101)
wsv.write(0,1,"Vani")
wsv.write(0,2,"Chennai")

wsv.write(1,0,102)
wsv.write(1,1,"karthi")
wsv.write(1,2,"Chennai")
wbv.save("demo.xls")
