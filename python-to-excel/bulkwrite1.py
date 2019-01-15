import xlwt
wb=xlwt.Workbook()
ws=wb.add_sheet("Data")
x=[[101,"vani","chennai"],[102,"karthi","Chennai"],[103,"Anand","Madurai"]]
y=["Rollnno","Name","Location where is living"]
heading=xlwt.easyxf('font:bold on;align:wrap on,vert center,horiz center')
for i in range(3):
    ws.write(0,i,y[i],heading)
for i,row in enumerate(x):
    print i,row
    for j,col in enumerate(row):
        print i,j,col
        ws.write(i+1,j,col)
wb.save("demo3.xls")
