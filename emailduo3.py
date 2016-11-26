#!/usr/bin/python2.7
# -*- coding: utf8 -*-
# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText
# Create a text/plain message
# Import Random
import random
# Import the old mail file
import glob
from datetime import date
import os.path
import time
import datetime
#今天日期 (2006-11-18)
today = datetime.date.today()
DEBUG = 0
INDEX_FILE = '/home/marty/index.txt'
DUO_DB = '/home/marty/emailduo/duo30.txt'
OLD_MAIL_DIR = '/home/marty/env/ohlife/tmp'
OLD_MAIL_SELECTED = random.choice(glob.glob(OLD_MAIL_DIR+"/*.txt"))
OLD_DAY = OLD_MAIL_SELECTED.split("/")[6].split("_",1)[0].split("-")
#設定要相減的日期
other_day = datetime.date(int(OLD_DAY[0]),int(OLD_DAY[1]),int(OLD_DAY[2]))
result = today - other_day
if DEBUG == 1: print(OLD_MAIL_SELECTED)
if not os.path.isfile(INDEX_FILE):
    with open(INDEX_FILE, 'w') as the_file:
        the_file.write('0\n')
fi = open(INDEX_FILE,'r+')
index = fi.readline()
#print("Index:"+index)
fi.seek(0)
fi.write(str(int(index)+1))
fi.close()

f = open(DUO_DB,'r')
duo = f.readlines()
old_mail = open(OLD_MAIL_SELECTED,'r')
#msg.as_string = msg.as_string + str(old_mail.readlines())
sum_txt = ''
for old_mail_txt in old_mail.readlines():
    sum_txt = sum_txt + str(old_mail_txt)
minetext = "Just reply to this email with your entry.\n" \
    + "這是你在" + str(result.days) +"天前寫的：\n" \
    + duo[int(index)-1] \
    + str(other_day)+"\n"+sum_txt
#msg = MIMEText(minetext,'plain','utf-8')
msg = MIMEText(minetext)
old_mail.close()
f.close()

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Today! '+ str(date.today()) + ' The contents of DUO 3.0 ' + 'No.' + index.strip("\n")
#msg['Subject'] = 'The contents of DUO 3.0 '
#print (msg['Subject'])
msg['From'] = '"Oh Life Logger" <marty.cmd@sg.browan.com>'
msg['To'] = "marty@browan.com"
# Send the message via our own SMTP server, but don't include the
# envelope header.
if DEBUG == 0 :
	s = smtplib.SMTP('localhost')
	s.sendmail(msg['From'], msg['To'], msg.as_string())
	s.quit()
else:
	print msg
