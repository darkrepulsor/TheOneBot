from telegram.ext import Updater,CommandHandler
from controllers.bot_controller import handle_quote
import os
from dotenv import load_dotenv
import logging

logger = logging.basicConfig( level = logging.INFO,
                             format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                             filename='MyLogFile.log',
                             filemode='a'
                             )

logger = logging.getLogger(__name__)

load_dotenv()
token = os.getenv("TELEGRAM_TOKEN")

def main():
    updater = Updater(token=token,use_context=True)
    dispatcher = updater.dispatcher

    quote_handler = CommandHandler('quote', handle_quote)
    logger = logging.info('Recebeu o comando e passou para o controller.')
    dispatcher.add_handler(quote_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()