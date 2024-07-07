from telegram import Update
from telegram.ext import ApplicationBuilder,CommandHandler
from controllers.bot_controller import handle_quote,handle_character,handle_spf_character, handle_books
import os
from dotenv import load_dotenv
import logging

logger = logging.basicConfig( level = logging.INFO,
                             format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                             filename='MyLogFile.log',
                             filemode='w'
                             )

logger = logging.getLogger(__name__)

httpx_logger = logging.getLogger('httpx')
httpx_logger.setLevel(logging.WARNING)

load_dotenv()
token = os.getenv("TELEGRAM_TOKEN")

def main():
    logger.info('Bot iniciado com sucesso!!!.')
    logger.info('Recebeu o comando e passou para o controller.')
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler('book',handle_books))
    app.add_handler(CommandHandler('quote',handle_quote))
    app.add_handler(CommandHandler('character',handle_character))
    app.add_handler(CommandHandler('spf_character',handle_spf_character))
    app.run_polling()

if __name__ == '__main__':
    main()