import os
import asyncio
from dotenv import load_dotenv
from telegram.ext import Application
from handlers import get_conversation_handler, get_start_handler

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def set_commands(application):
    bot_commands = [
        ("start", "Iniciar el bot"),
        ("disenar_conversacion", "Diseñar una conversación"),
        ("sugerencias", "Recibir sugerencias"),
        ("identificar_juicios", "Identificar juicios"),
        ("cancelar", "Cancelar el diseño de conversación")
    ]
    await application.bot.set_my_commands(bot_commands)

async def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(get_start_handler())
    application.add_handler(get_conversation_handler())

    await set_commands(application)

    await application.initialize()
    await application.start()
    print("Bot iniciado. Presione Ctrl+C para detener.")

    # Esperar indefinidamente
    while True:
        await asyncio.sleep(1)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot detenido.")