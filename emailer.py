import yagmail
def sendmail(to: str, head: str, contents: str):
    yag = yagmail.SMTP("iskatag2006@gmail.com", oauth2_file="~/credentials.json")
    yag.send("itagizade@yahoo.com", head, contents)