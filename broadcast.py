import telebot
from config import TELEGRAM_API_TOKEN

# Initialize the bot
bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

# List of user IDs or chat IDs to broadcast to
# Add the chat IDs of users/groups to whom you want to send the message
USER_IDS = [123456789, 987654321]  # Replace with actual user/chat IDs

def broadcast_message(message_text):
    """
    Function to broadcast a message to all users in USER_IDS.
    """
    for user_id in USER_IDS:
        try:
            bot.send_message(user_id, message_text)
            print(f"Message sent to {user_id}")
        except Exception as e:
            print(f"Failed to send message to {user_id}: {e}")

if __name__ == "__main__":
    # Message to broadcast
    message_text = "🚀 Special Promotion! Get 20% off on all products this week. Visit our website for more details!"
    
    # Send the broadcast
    broadcast_message(message_text)
