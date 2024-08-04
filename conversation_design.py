from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

# Define stages of the conversation
ASK_RESPONSE, PROVIDE_SUGGESTIONS = range(2)

def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Vamos a diseñar una conversación difícil. Primero, ¿cuál es tu intención en esta conversación?"
    )
    return ASK_RESPONSE

def design_conversation(update: Update, context: CallbackContext) -> int:
    user_response = update.message.text
    context.user_data['response'] = user_response
    update.message.reply_text(
        "Gracias por compartir. ¿Te gustaría recibir sugerencias para mejorar la conversación?"
    )
    return PROVIDE_SUGGESTIONS

def receive_response(update: Update, context: CallbackContext) -> int:
    user_response = update.message.text
    context.user_data['response'] = user_response
    update.message.reply_text(
        "Gracias por compartir. ¿Te gustaría recibir sugerencias para mejorar la conversación?"
    )
    return PROVIDE_SUGGESTIONS

def provide_suggestions(update: Update, context: CallbackContext) -> int:
    if update.message.text.lower() in ['sí', 'si', 'yes']:
        update.message.reply_text("Aquí tienes algunas sugerencias para mejorar tu conversación...")
    else:
        update.message.reply_text("Entendido. ¡Buena suerte con tu conversación!")

    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Operación cancelada.')
    return ConversationHandler.END