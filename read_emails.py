import win32com.client as win32

# Initiate outlook session
outlook = win32.Dispatch("Outlook.Application").GetNamespace('MAPI')

# Different folders have default numbers, inbox is 6
inbox = outlook.GetDefaultFolder(6)

# Select all emails
messages = inbox.Items

# Filter these emails according to conditions
# messages = messages.Restrict("[SentOn] > '7/2/2022 12:00 AM'")

email_address = "foo@bar.com"
messages = messages.Restrict(f"[SenderEmailAddress] = '{email_address}'")


# Print the body of each email
for message in messages:
    m = message.Body
    print(m)
