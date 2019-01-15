import xlwt
wb=xlwt.Workbook()
ws=wb.add_sheet("Data")
x=[[101,"vani","chennai"],[102,"karthi","Chennai"],[103,"Anand","Madurai"]]
for i,row in enumerate(x):
    print i,row
    for j,col in enumerate(row):
        print i,j,col
        ws.write(i,j,col)
wb.save("demo2.xls")
