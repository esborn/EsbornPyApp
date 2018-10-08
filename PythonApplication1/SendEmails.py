

def __Emailer(text, subject, recipients, auto=True):
    import win32com.client as win32   
    try:
        outlook = win32.GetActiveObject('Outlook.Application')
    except:
        outlook = win32.Dispatch('Outlook.Application')
    
    mail = outlook.CreateItem(0)

    if hasattr(recipients, 'strip'):
        recipients = [recipients]

    for recipient in recipients:
        mail.Recipients.Add(recipient)

    mail.Subject = subject
    mail.HtmlBody = text

    if auto:
        mail.send
    else:
        mail.Display(True)



emailbody ="""<p style="font-family:Gill Sans MT;font-size:14;">Hi Team,<br>
Your Team Site has been migrated to this link:<br>
Please note the old site access had been restricted and no changes can be made, review the migrated site and if there any issue please send an email to onenet@savethechildren.org 
<br>
Regards, <br><br>

<b>Esborn Mugu</b> | SharePoint Applications Support Analyst | <br>
<b><font color="red">Save the Children</font></b> | Matundu Close, Off School Lane, Westlands |PO Box 27679 - 00506, Nairobi |<br>
Tel: +254 20 4246000 | Email: Esborn.Mugu@savethechildren.org | http://www.savethechildren.net |<br>
Skype: Esborn.Mugu </p>"""


subject='Team Site migration'
recipients='esborn.mugu@savethechildren.org,Gitonga, Moses'


__Emailer(emailbody.format(subtype='html'),subject,recipients.split(','))

