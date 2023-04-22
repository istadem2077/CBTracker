import requests

message = ['Baku International School : Full, no seats\n\n', 'Baku Oxford School : Full, no seats\n\n', 'Dunya School : Full, no seats\n\n', 'European Azerbaijan School : Full, no seats\n\n', 'Idrak Lyceum : Full, no seats\n\n', 'Landau School : Full, no seats\n\n', 'Sabis Sun International School : Full, no seats\n\n', 'The State Examination Center : Full, no seats\n\n']
message = "".join(message)
print(message)
def telegram_sendmessage(bot_chatID, bot_message):

    bot_token = "6059417392:AAHd_ravkjwRjOjTnMBMXTTnywIwxQ94U7w"
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + f"{bot_chatID}" + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
    return response.json()

print(telegram_sendmessage(976908358,message))
print(telegram_sendmessage(5670908383, message))
print(telegram_sendmessage(584098198, message))

