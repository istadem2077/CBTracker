# pylint: disable=bare-except
# pylint: disable=wildcard-import
# pylint: disable=unspecified-encoding
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=global-statement
# pylint: disable=missing-timeout
import requests
import json

def notify(bot_chatID, bot_message:str):

    bot_token = "6059417392:AAHd_ravkjwRjOjTnMBMXTTnywIwxQ94U7w"
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + f"{bot_chatID}" + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
    return response.json()


def cberror(bot_message:str, bot_chatID = 5670908383):

    bot_token = "6412450545:AAH0N0coNpBcQdXPzGdGTyPvBGBTs1_IwAI"
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + f"{bot_chatID}" + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
    return response.json()

def logs(file:str, bot_chatID = 5670908383):

    bot_token = "6412450545:AAH0N0coNpBcQdXPzGdGTyPvBGBTs1_IwAI"
    return json.loads(requests.post(f"https://api.telegram.org/bot{bot_token}/sendDocument", files={'document' : open(file, 'rb')}, data={'chat_id' : bot_chatID}).content.decode('utf-8'))
