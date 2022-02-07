import win32com.client as win32

outlook = win32.Dispatch("Outlook.Application").GetNamespace('MAPI')

inbox = outlook.GetDefaultFolder(6)

messages = inbox.Items
# messages = messages.Restrict("[SentOn] > '7/2/2022 12:00 AM'")
messages = messages.Restrict(f"[SenderEmailAddress] = '{email_address}'")


for message in messages:
    m = message.Body
    m = m.split("\n")
    print(m)
