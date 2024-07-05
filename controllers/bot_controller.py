from models.quote import Quote
from views.formatter import format_quote
from telegram import Update
from telegram.ext import ContextTypes

async def handle_quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quote = Quote.get_random_quote()
    formatted_quoted = format_quote(quote)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=formatted_quoted)
