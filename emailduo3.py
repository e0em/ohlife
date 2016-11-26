#!/usr/bin/python2.7
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
DEBUG = 1
INDEX_FILE = '/home/marty/index.txt'
DUO_DB = '/home/marty/emailduo/duo30.txt'
OLD_MAIL_DIR = '/home/marty/env/ohlife/tmp'
OLD_MAIL_SELECTED = random.choice(glob.glob(OLD_MAIL_DIR+"/*.txt"))
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
msg = MIMEText(duo[int(index)-1].strip('\n'))
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
	print msg.as_string
