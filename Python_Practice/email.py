#!/usr/bin/python

import smtplib
import email.utils

content = "example stuff here"

mail = smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()
mail.starttls()

mail.login('sezan@monogramorthopedics.com','Itsmytlx06')
mail.sendmail('sezan@monogramorthopedics.com','sezansaimon@gmail.com',content)
mail.close()
