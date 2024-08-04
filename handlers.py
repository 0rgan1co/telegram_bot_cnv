from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, Filters
from conversation_design import design_conversation, receive_response, provide_suggestions, cancel, start

def get_conversation_handler():
    return ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            0: [MessageHandler(Filters.text & ~Filters.command, design_conversation)],
            1: [MessageHandler(Filters.text & ~Filters.command, receive_response)],
            2: [MessageHandler(Filters.text & ~Filters.command, provide_suggestions)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

def get_start_handler():
    return CommandHandler('start', start)