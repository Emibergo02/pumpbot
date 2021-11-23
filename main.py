from pyrogram import Client
from pyrogram.handlers import MessageHandler

def dump(client, message):
    if message.text is not None:
        if "kucoin.com" in message.text:
            print(message.text[message.text.find("kucoin.com/")+11:])

app = Client("WeArePoor",14161945,"f0e1e792f0bc2ab1de43e39226eddf8d")

app.add_handler(MessageHandler(dump))

app.run()