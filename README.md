# Telegram Bot for Broadcasting Messages and Customer Interaction

## Project Overview
This project demonstrates how to build a Telegram bot to broadcast messages, promotions, and handle basic customer service commands. The bot is built using Python and the `pyTelegramBotAPI` library.

### Features:
- Handles common commands like `/start` and `/help`.
- Broadcasts messages to a list of users or groups.
- Can be extended to handle more complex customer service features.

### Requirements:
- Python 3.x
- `pyTelegramBotAPI`

### Create a Telegram Bot
First, you need to create a Telegram bot using BotFather.
- Open Telegram and search for BotFather.
- Type /start and follow the instructions to create a new bot.
- Once the bot is created, BotFather will give you an API token. You’ll need this token to interact with the Telegram API.

### How to Run:
1. Install Required Dependencies: You’ll need the pyTelegramBotAPI library to interact with Telegram’s API. Install it using:
- pip install pyTelegramBotAPI

2. Run the Main Bot: Start the bot by running:
- python bot.py
- The bot will start listening for user messages and respond to commands like /start and /help.

3. Broadcast a Message: You can send broadcast messages by running:
- python broadcast.py
- This will send the predefined message to all user IDs listed in the USER_IDS array.

### Example Output:
- Screenshot 1: User interaction with the bot.
- Screenshot 2: Broadcast message sent to a user.
- Screenshot 3: Console output confirming the broadcast.

