from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, ConversationHandler, MessageHandler, filters
from conversation_design import (
    start_design_conversation,
    set_title,
    set_intention,
    receive_response,
    provide_suggestions,
    cancel_design,
    identify_judgments
)

def get_start_handler():
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text('¡Hola! Soy tu bot para preparar conversaciones difíciles.')
    return CommandHandler('start', start)

def get_conversation_handler():
    return ConversationHandler(
        entry_points=[CommandHandler('disenar_conversacion', start_design_conversation)],
        states={
            "TITLE": [MessageHandler(filters.TEXT & ~filters.COMMAND, set_title)],
            "INTENTION": [MessageHandler(filters.TEXT & ~filters.COMMAND, set_intention)],
            "RESPONSE": [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_response)],
            "SUGGESTIONS": [MessageHandler(filters.TEXT & ~filters.COMMAND, provide_suggestions)],
            "JUDGMENTS": [MessageHandler(filters.TEXT & ~filters.COMMAND, identify_judgments)],
        },
        fallbacks=[CommandHandler('cancelar', cancel_design)]
    )