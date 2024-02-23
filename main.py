import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Initializes the booking_list dictionary to save bookings.
booking_list = {}


# Log the TelegramBot for errors.
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# The start function facilitates the creation of a user ID and introduces the user to the bot.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    welcome_text = """Hey! Welcome to CS' tuition booking bot!\n
To book, type in the date and time in DD-MM hh:mm after your /book.\n
E.g. /book 25-05 16:30"""

    booking_list[context._user_id]=[]

    await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_text)


# A function that records the user's requested tuition timing.
async def book(update: Update, context: ContextTypes.DEFAULT_TYPE):

    booking_list[context._user_id].append(' '.join(context.args))

    await context.bot.send_message(chat_id=update.effective_chat.id, text='Thanks for making a booking with us!')


# A function to allow the user to view their bookings.
async def view(update: Update, context: ContextTypes.DEFAULT_TYPE):

    output_string = "Your bookings are:\n\n" + "\n".join(booking_list[context._user_id])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=output_string)


# Starts the TelegramBot and its various functions.
if __name__ == '__main__':
    application = ApplicationBuilder().token('7133972347:AAF5wlaYgyvn_NhQQ5csxbhOZx6CzHTmzEE').build()
    
    start_handler = CommandHandler('start', start)
    book_handler = CommandHandler('book', book)
    view_handler = CommandHandler('view', view)


    application.add_handler(start_handler)
    application.add_handler(book_handler)
    application.add_handler(view_handler)
    
    application.run_polling()
