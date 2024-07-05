from models.quote import Quote
from views.formatter import format_quote

def handle_quote(update, context):
    quote = Quote.get_random_quote()
    formatted_quoted = format_quote(quote)
    context.bot.send_message(chat_id=update.effective_chat.id, text=formatted_quoted)
