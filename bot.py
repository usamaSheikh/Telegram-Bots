import telebot
from telebot import types
from config import TELEGRAM_API_TOKEN
import logging 

# Initialize the bot with the API token
bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

# Set up logging for user messages
logging.basicConfig(filename='user_messages.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to log user messages
def log_message(user_id, username, message):
    logging.info(f"User ID: {user_id}, Username: {username}, Message: {message}")

# Handle the /start command with personalized greeting and main menu
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_first_name = message.from_user.first_name
    bot.reply_to(message, f"Hello, {user_first_name}! Welcome to our service. How can we assist you today?")
    
    # Display menu options using inline buttons
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_products = types.InlineKeyboardButton("View Products", callback_data="view_products")
    btn_support = types.InlineKeyboardButton("Customer Support", callback_data="customer_support")
    btn_faq = types.InlineKeyboardButton("FAQ", callback_data="faq")
    markup.add(btn_products, btn_support, btn_faq)
    
    bot.send_message(message.chat.id, "Please choose an option:", reply_markup=markup)

# Handle button clicks from the inline keyboard
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == "view_products":
        bot.send_message(call.message.chat.id, "Here are our latest products:\n1. Product A\n2. Product B\n3. Product C")
    elif call.data == "customer_support":
        bot.send_message(call.message.chat.id, "Please describe your issue, and one of our representatives will assist you shortly.")
    elif call.data == "faq":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_hours = types.InlineKeyboardButton("Opening Hours", callback_data="hours")
        btn_return = types.InlineKeyboardButton("Return Policy", callback_data="return_policy")
        markup.add(btn_hours, btn_return)
        bot.send_message(call.message.chat.id, "Choose a FAQ option:", reply_markup=markup)
    elif call.data == "hours":
        bot.send_message(call.message.chat.id, "Our opening hours are Mon-Fri, 9 AM to 6 PM.")
    elif call.data == "return_policy":
        bot.send_message(call.message.chat.id, "Our return policy allows returns within 30 days of purchase with a valid receipt.")

# Handle regular text messages and log them
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    log_message(message.from_user.id, message.from_user.username, message.text)
    
    if message.text.lower() in ["hi", "hello"]:
        bot.reply_to(message, "Hi! How can I help you today?")
    elif "price" in message.text.lower():
        bot.reply_to(message, "Our prices start from $100. Would you like to know more about specific products?")
    else:
        bot.reply_to(message, "I'm sorry, I don't understand your question. Type /help for assistance.")

# Handle the /help command with more options
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Here are the available commands:\n/start - Start the bot\n/help - Get help\nYou can also ask about our prices or services!")

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
