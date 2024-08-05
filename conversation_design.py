from telegram import Update
from telegram.ext import CallbackContext

async def design_conversation(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text("Iniciando diseño de conversación. Por favor, responde a las siguientes preguntas.")
    context.user_data['responses'] = []
    return 1

async def receive_response(update: Update, context: CallbackContext) -> int:
    user_response = update.message.text
    context.user_data['responses'].append(user_response)
    await update.message.reply_text("Respuesta recibida. ¿Tienes más preguntas o deseas terminar?")
    return 2

async def provide_suggestions(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text("Aquí hay algunas sugerencias para tu conversación.")
    return -1

async def cancel_design(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text("Diseño de conversación cancelado.")
    return -1