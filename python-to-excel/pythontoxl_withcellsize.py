import xlwt
DATA=(("B.Sc Homescienc", 1997),
      ("MCA-Master of Computer Applications",2000),
      ("M.Phil-ComputerScience",2007),
      ("M.E Computer Science and Engineering",2016),
      ("First book - Computer Architecture with MIPs", 2017))
wb=xlwt.Workbook()
ws=wb.add_sheet("MySheet")
for i,row in enumerate(DATA):
    for j,col in enumerate(row):
        ws.write(i, j, col)
    for row in DATA:
        ws.col(0).width=256*len(row[0])
wb.save("mydetails.xls")
