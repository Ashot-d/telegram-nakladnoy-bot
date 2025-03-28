import os
import telebot
from datetime import datetime

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    sender = f"{message.from_user.first_name} (@{message.from_user.username})"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    caption = f"📄 Расходная накладная\nОтправил: {sender}\nДата: {timestamp}"
    file_id = message.photo[-1].file_id
    bot.send_photo(CHAT_ID, file_id, caption=caption)
    @bot.message_handler(commands=['id'])
def send_chat_id(message):
    bot.send_message(message.chat.id, f"Ваш chat_id: {message.chat.id}")
bot.polling(none_stop=True)
