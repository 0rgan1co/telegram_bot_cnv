from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

TITLE, INTENTION, INTENTION_DETAIL = range(3)

async def start_design_conversation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Iniciando diseño de conversación. Por favor, responde a las siguientes preguntas."
    )
    await update.message.reply_text("¿Cuál es el título que te gustaría darle a esta conversación?")
    return TITLE

async def set_title(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['title'] = update.message.text
    await update.message.reply_text("Título guardado. ¿Cuál es la intención de la conversación?")
    return INTENTION

async def set_intention(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['intention'] = update.message.text
    await update.message.reply_text(
        "Intención guardada. Aquí tienes algunas intenciones comunes para orientarte:\n"
        "1. Comprender y ser comprendida.\n"
        "2. Hacer lo que pueda para incrementar la confianza entre la otra persona y yo.\n"
        "3. Mantener conexión con mi humanidad y la de la otra persona.\n"
        "4. Verme a mí y a la otra persona como seres humanos con necesidades preciosas.\n"
        "5. Mantener una presencia serena y empática.\n"
        "6. Confiar en que yo importo, mis necesidades importan.\n"
        "7. Trabajar hacia una solución que funcione para todo el mundo.\n"
        "8. Permanecer abierta a cambiar de postura a través del diálogo.\n"
        "9. Estar atenta a mis pensamientos, sensaciones corporales, sentimientos.\n"
        "10. Decir la verdad completa con atención y cuidado.\n"
        "Por favor, proporciona más detalles sobre tu intención."
    )
    return INTENTION_DETAIL

async def receive_response(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    response = update.message.text
    context.user_data['response'] = response
    await update.message.reply_text("Respuesta recibida. ¿Tienes más preguntas o deseas terminar?")
    return INTENTION_DETAIL

async def provide_suggestions(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Ofreciendo sugerencias para mejorar tu diseño de conversación.")
    return INTENTION_DETAIL

async def cancel_design(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Diseño de conversación cancelado.")
    return ConversationHandler.END

async def identify_judgments(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Identificando juicios y supuestos en la conversación.")
    return INTENTION_DETAIL