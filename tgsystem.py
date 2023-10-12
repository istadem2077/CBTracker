import subprocess
import os 
import telebot

TOKEN = "6412450545:AAH0N0coNpBcQdXPzGdGTyPvBGBTs1_IwAI"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['reboot', 'restart'])
def srvreboot(message):
    subprocess.Popen(['reboot'], shell=True)
    
@bot.message_handler(commands=['shutoff', 'shutup', 'shutdown'])
def shutdown(message):
    subprocess.Popen(['shutdown'], shell=True)