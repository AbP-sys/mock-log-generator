import win32com.client as win32

def send_mail(store):
        olApp = win32.Dispatch('Outlook.Application')
        olNS = olApp.GetNameSpace('MAPI')
        mail_item = olApp.CreateItem(0)

        mail_item.Subject = "It's time to scale up your servers"
        mail_item.BodyFormat = 1

        mail_item.Body = "Log Analyser has found consistent increase in your CPU usage\
         Review and scale if needed.\n{}".format(store)
        mail_item.Sender = "prachi.209301334@muj.manipal.edu"
        mail_item.To = "sinhaprachi175@gmail.com"

        mail_item.Display()
        mail_item.Save()
        mail_item.Send()