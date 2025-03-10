import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Set your bot token
TOKEN = '7810273343:AAFBv9fdN2vhIdinRwkgQesCtciPBYqiVdk'  # Replace with your actual bot token

# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_name = update.message.from_user.first_name
    greeting = f"Hello, {user_name}! I'm your Telegram bot. How can I help you?"
    await update.message.reply_text(greeting)

# Function to handle text messages
async def human_like_response(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text.lower()  # Get the message and convert to lowercase for case-insensitive matching

    # Responding to specific phrases
    if "how are you" in user_message:
        responses = [
            "I'm doing great, thanks for asking! How about you?",
            "I'm fine, thank you! What about you?",
            "All good here, how are you?"
        ]
        await update.message.reply_text(random.choice(responses))
    elif "hello" in user_message or "hi" in user_message:
        greetings = [
            "Hello there! 😊",
            "Hi! How's it going?",
            "Hey! What's up?"
        ]
        await update.message.reply_text(random.choice(greetings))
    elif "bye" in user_message or "goodbye" in user_message:
        farewell_responses = [
            "Goodbye! Take care! 👋",
            "See you later! 😊",
            "Bye-bye! Have a great day!"
        ]
        await update.message.reply_text(random.choice(farewell_responses))
    elif "how old are you" in user_message:
        await update.message.reply_text("I don't age, but I am always learning! 😄")
    elif "what is your name" in user_message:
        await update.message.reply_text("I'm your friendly bot. You can call me Bot! 🤖")
    else:
        # Default response for other messages
        responses = [
            "Hmm, interesting. Tell me more!",
            "I'm not sure about that, but let's talk about something else!",
            "Oh, that's cool. What else do you want to talk about?"
        ]
        await update.message.reply_text(random.choice(responses))

# Main function
def main() -> None:
    # Create the application
    application = ApplicationBuilder().token(TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, human_like_response))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()







