# pylint: disable=bare-except
# pylint: disable=wildcard-import
# pylint: disable=unspecified-encoding
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=global-statement
# pylint: disable=unused-argument
# pylint: disable=missing-timeout
import subprocess
import telebot

TOKEN = "6412450545:AAH0N0coNpBcQdXPzGdGTyPvBGBTs1_IwAI"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['reboot', 'restart'])
def srvreboot(message):
    subprocess.Popen(['reboot'], shell=True)


@bot.message_handler(commands=['shutoff', 'shutup', 'shutdown'])
def shutdown(message):
    subprocess.Popen(['shutdown', 'now'], shell=True)


bot.infinity_polling()
