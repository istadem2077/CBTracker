import requests

def telegram_sendmessage(bot_chatID, bot_message):

    bot_token = "6059417392:AAHd_ravkjwRjOjTnMBMXTTnywIwxQ94U7w"
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + f"{bot_chatID}" + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
    return response.json()

