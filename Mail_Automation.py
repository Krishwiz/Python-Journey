import win32com.client

import datetime

 

""" Send mail via Outlook."""

obj = win32com.client.Dispatch("Outlook.Application")

 

newMail = obj.CreateItem(olMailItem)

newMail.Subject = 'Test'

newMail.Body = "This is a automated mail using python"

newMail.To = "212803481@ge.com"


newMail.Send()

    