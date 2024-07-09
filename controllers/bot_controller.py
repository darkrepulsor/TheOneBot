from models.quote import Quote
from models.character import Character
from models.books import Books
from views.formatter import format_quote, format_character,format_spf_character,format_books, format_wrong_answer
from telegram import Update
from telegram.ext import ContextTypes,CallbackContext
import logging

logger = logging.getLogger(__name__)

def Menu():
    
    men = f"""Preeeecioooous!!!
          Here are some commands if you need some knowledge or fun:
          \U0001F9D9\u200D\u2642\uFE0F /character - Returns an random character.
          \U0001F9D9\u200D\u2642\uFE0F /quote - Returns an random quote.
          \U0001F9D9\u200D\u2642\uFE0F /book - Returns the name of all three books
          \U0001F9D9\u200D\u2642\uFE0F /spf_character - Returns a specific character need to inform a name """
    return men

async def check_answer(update:Update, context:CallbackContext):
    response = update.message.text
    logger.info(f'Mensagem recebida: {response}')
    if response == 'Mellon':
        logger.info(f'Correct answer received')
        await context.bot.send_message(chat_id=update.effective_chat.id, text=Menu())
    else:
        logger.info(f'Wrong answer received')
        wrong = Quote.get_wrong_answer()
        wrong_answer = format_wrong_answer(wrong)
        await context.bot.send_message(chat_id=update.effective_chat.id,text=wrong_answer)


async def handle_start(update:Update, context:CallbackContext):
    user = update.message.from_user
    logger.info('O bot foi iniciado!!! UHULLL!!')
    message = f"""Fellow {user.username}, I\'m RuleThemAll Bot, you came to the right place if you want knowledge and fun, but first...
    Say friend and enter..."""
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
   

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
       await update.message.reply_text('Fellow, to use this command correctly you need to include the name of the character.')

async def handle_books(update:Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info('Buscando o livro...')
    book = Books.get_books()

    logger.info('Formatando o livro...')
    formatted_books = format_books(book)

    logger.info('Enviando o livro...')
    await context.bot.send_message(chat_id=update.effective_chat.id, text=formatted_books)

    logger.info('Enviou a mensagem!!!!')