import telebot
from config import TELEGRAM_API_TOKEN

# Initialize the bot with the API token
bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

# Handle the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to our Telegram bot! How can we assist you today?")

# Handle the /help command
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Here are the available commands:\n/start - Start the bot\n/help - Get help")

# Handle regular messages
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "You said: " + message.text)

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
