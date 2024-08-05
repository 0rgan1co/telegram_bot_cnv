import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler
from handlers import get_conversation_handler, get_start_handler

load_dotenv()  # Cargar las variables de entorno desde el archivo .env

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("No se ha proporcionado un token válido para el bot.")

def main():
    application = Application.builder().token(TOKEN).build()

    # Agregar handlers
    application.add_handler(get_start_handler())
    application.add_handler(get_conversation_handler())

    # Iniciar el bot
    application.run_polling()

if __name__ == '__main__':
    main()