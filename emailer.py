import yagmail
def sendmail(to: str, head: str, contents):
    yag = yagmail.SMTP("iskatag2006@gmail.com", oauth2_file="~/credentials.json")
    yag.send(to, head, contents)