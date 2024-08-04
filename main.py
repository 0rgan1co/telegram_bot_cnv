import logging
from telegram.ext import Application, CommandHandler
from handlers import get_conversation_handler, get_start_handler
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configurar el token del bot desde la variable de entorno
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Configurar el registro
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Crear la aplicación del bot
application = Application.builder().token(TOKEN).build()

# Añadir los manejadores de comandos
application.add_handler(get_start_handler())
application.add_handler(get_conversation_handler())

# Iniciar el bot
if __name__ == "__main__":
    application.run_polling()