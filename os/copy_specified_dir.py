'''program to copy the specific  directories in the destinatioin from source except the text file and files with 0 bytes and send the mail regarding this copying.'''

import smtplib
import os
dest="/home/ubuntu/destination"
dirs=list()
for dpaths,dsubdirs,dfiles in os.walk(dest):
    dirs.append(dsubdirs)
dirs=dirs[0]
fp=open("copyresult.txt","w")
for i in dirs:
    destination="/home/ubuntu/destination/"+i
    source="/home/ubuntu/source/"+i
    for spaths,sdirs,sfiles in os.walk(source):
        for j in sfiles:
           x= os.path.join(spaths,j)
           if not(x.endswith(".txt")):
                if os.path.getsize(x) > 0:
                    os.system("cp "+x+" "+destination)
                    fp.write(x+"\n")
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("testmailbss@gmail.com","vani!@#$")
msg="""\
Subject : msg from copy.py
files are copied"""
server.sendmail("testmailbss@gmail.com","vani@brainstack.in",msg)
server.server.quit()
