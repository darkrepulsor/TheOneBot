from models.quote import Quote
from models.character import Character
from models.books import Books
from views.formatter import format_quote, format_character,format_spf_character,format_books
from telegram import Update
from telegram.ext import ContextTypes,CallbackContext
import logging

logger = logging.getLogger(__name__)

async def handle_quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info('Preparando para formatar a fala aleatória...')    
    quote = Quote.get_random_quote()
   
    logger.info('Recebeu a fala...')    
    formatted_quoted = format_quote(quote)
   
    logger.info('Formatou a fala...')    
    await context.bot.send_message(chat_id=update.effective_chat.id, text=formatted_quoted)
   
    logger.info('Enviou a mensagem!!!')    

async def handle_character(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info('Buscando o personagem...')
    character = Character.get_random_character()
    
    logger.info('Formatando o personagem...')
    formatted_character = format_character(character)
    
    logger.info('Enviando o personagem...')
    await context.bot.send_message(chat_id=update.effective_chat.id, text=formatted_character)
    
    logger.info('Enviou a mensagem!!!')
    
async def handle_spf_character(update: Update, context: CallbackContext):
    if context.args:
        argumento = ' '.join(context.args)
        logger.info(f'Recebido comando /spf_character com argumento: {argumento}')
    
        logger.info('Preparando para formatar o personagem...')
        character = Character.get_specifc_character(argumento)

        logger.info('Recebeu o personagem...')
        formatted_character = format_spf_character(character)

        logger.info('Formatou o personagem...')
        await context.bot.send_message(chat_id=update.effective_chat.id, text=formatted_character)

        logger.info('Enviou a mensagem!!!')
    else:
        update.message.reply_text('Fellow, to use this command correctly you need to include the name of the character.')

async def handle_books(update:Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info('Buscando o livro...')
    book = Books.get_books()

    logger.info('Formatando o livro...')
    formatted_books = format_books(book)

    logger.info('Enviando o livro...')
    await context.bot.send_message(chat_id=update.effective_chat.id, text=formatted_books)

    logger.info('Enviou a mensagem!!!!')