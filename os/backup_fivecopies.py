import datetime
import os,glob
filename=str(datetime.datetime.today())
fname=datetime.datetime.today().strftime("%Y%m%d")
bupfile="/home/ubuntu/deveops/string5.zip"
os.system("cp -arpv " +bupfile+" /home/ubuntu/deveops/backup/"+fname)
filesearch="/home/ubuntu/deveops/backup/2018*"
list1=[]
for i in glob.glob(filesearch):
    list1.append(i)
list1.sort()
count=0
for i in list1:
    count=count+1
if count>5:
    os.remove(list1[0])
os.system("ls -l "+filesearch)
