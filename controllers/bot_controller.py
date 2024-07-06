from models.quote import Quote
from models.character import Character
from views.formatter import format_quote, format_character
from telegram import Update
from telegram.ext import ContextTypes
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
    logger.info('Preparando para formatara o personagem...')
    character = Character.get_random_character()
    logger.info('Recebeu o personagem...')
    formatted_character = format_character(character)
    logger.info('Formatou o personagem...')
    await context.bot.send_message(chat_id=update.effective_chat.id, text=formatted_character)
    logger.info('Enviou a mensagem!!!')
    