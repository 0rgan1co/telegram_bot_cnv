from telegram import Update
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, filters, CallbackContext

from conversation_design import design_conversation, receive_response, provide_suggestions, cancel_design
from explain_technique import explain_technique

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('¡Hola! Soy tu bot para preparar conversaciones difíciles.')

def get_start_handler():
    return CommandHandler('start', start)

def get_conversation_handler():
    return ConversationHandler(
        entry_points=[CommandHandler('design_conversation', design_conversation)],
        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_response)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, provide_suggestions)]
        },
        fallbacks=[CommandHandler('cancel', cancel_design)]
    )