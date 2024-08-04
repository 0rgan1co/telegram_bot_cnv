from telegram import Update
from telegram.ext import CallbackContext
from constants import EXPLAIN_TECHNIQUE, EXPLAIN_PART_1, EXPLAIN_PART_2, DESIGN_CONVERSATION

async def explain_technique(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text(
        "El objetivo de esta técnica es 'Conectar antes de actuar'. Consta de 2 partes: "
        "1. Auto-conexión\n"
        "2. Conexión durante la conversación\n"
        "Vamos a comenzar con la primera parte: Auto-conexión.\n"
        "1. Clarificar Intenciones:\n"
        "  • ¿Cuál es mi intención en esta conversación?\n"
        "  • Acción: Revisar el decálogo de intenciones para diálogos no violentos.\n"
        "2. Comprensión Profunda de la Perspectiva del Otro:\n"
        "  • ¿Qué preguntas puedo hacer para comprender la perspectiva de la otra persona?\n"
        "  • Ejemplo: ¿Qué escuchaste de lo que dije sobre [tema]?\n"
        "  • Ejemplo: ¿Cuál era tu intención al mencionar [tema]?\n"
        "  • Acción: Mostrar escucha activa y empática.\n"
        "3. Identificar y Transformar Juicios y Culpas:\n"
        "  • ¿Cuáles son mis juicios y culpas hacia mí mismo y hacia la otra persona?\n"
        "  • ¿Cómo puedo traducir estos juicios en necesidades y frases constructivas?\n"
        "  • Acción: Reflexionar sobre necesidades y formular frases respetuosas.\n"
        "4. Pedidos y Ofertas Previos a la Conversación:\n"
        "  • ¿Qué pedidos u ofertas puedo hacer antes de la conversación para preparar el terreno?\n"
        "  • Acción: Identificar acciones o compromisos previos.\n"
        "¿Tienes alguna duda sobre esta primera parte? (sí/no)"
    )
    return EXPLAIN_PART_1

async def explain_part_1(update: Update, context: CallbackContext) -> int:
    if update.message.text.lower() == "sí":
        await update.message.reply_text(
            "Vamos a repasar la primera parte: Auto-conexión.\n"
            "1. Clarificar Intenciones:\n"
            "  • ¿Cuál es mi intención en esta conversación?\n"
            "  • Acción: Revisar el decálogo de intenciones para diálogos no violentos.\n"
            "2. Comprensión Profunda de la Perspectiva del Otro:\n"
            "  • ¿Qué preguntas puedo hacer para comprender la perspectiva de la otra persona?\n"
            "  • Ejemplo: ¿Qué escuchaste de lo que dije sobre [tema]?\n"
            "  • Ejemplo: ¿Cuál era tu intención al mencionar [tema]?\n"
            "  • Acción: Mostrar escucha activa y empática.\n"
            "3. Identificar y Transformar Juicios y Culpas:\n"
            "  • ¿Cuáles son mis juicios y culpas hacia mí mismo y hacia la otra persona?\n"
            "  • ¿Cómo puedo traducir estos juicios en necesidades y frases constructivas?\n"
            "  • Acción: Reflexionar sobre necesidades y formular frases respetuosas.\n"
            "4. Pedidos y Ofertas Previos a la Conversación:\n"
            "  • ¿Qué pedidos u ofertas puedo hacer antes de la conversación para preparar el terreno?\n"
            "  • Acción: Identificar acciones o compromisos previos.\n"
            "¿Tienes alguna duda sobre esta primera parte? (sí/no)"
        )
        return EXPLAIN_PART_1
    else:
        await update.message.reply_text(
            "Perfecto. Ahora vamos a la segunda parte: Conexión durante la conversación.\n"
            "1. Mantener Actitudes de Protagonismo y Curiosidad:\n"
            "  • ¿Cómo me mantendré conectado con las actitudes de protagonismo y curiosidad?\n"
            "  • Acción: Usar recordatorios internos o anclajes.\n"
            "2. Empatizar y Conectar con la Humanidad del Otro:\n"
            "  • ¿Con qué partes de la otra persona puedo empatizar?\n"
            "  • Acción: Mostrar empatía y reconocer emociones y necesidades.\n"
            "3. Descubrimientos sobre Mí, el Otro y la Relación:\n"
            "  • ¿Qué estoy descubriendo de mí, de la otra persona o de nuestra relación?\n"
            "  • Acción: Mantener una mente abierta para el aprendizaje.\n"
            "4. Formular Pedidos y Ofertas durante la Conversación:\n"
            "  • ¿Qué pedidos u ofertas quiero hacer durante la conversación?\n"
            "  • Acción: Formular pedidos claros y específicos basados en las necesidades.\n"
            "¿Tienes alguna duda sobre esta segunda parte? (sí/no)"
        )
        return EXPLAIN_PART_2

async def explain_part_2(update: Update, context: CallbackContext) -> int:
    if update.message.text.lower() == "sí":
        await update.message.reply_text(
            "Vamos a repasar la segunda parte: Conexión durante la conversación.\n"
            "1. Mantener Actitudes de Protagonismo y Curiosidad:\n"
            "  • ¿Cómo me mantendré conectado con las actitudes de protagonismo y curiosidad?\n"
            "  • Acción: Usar recordatorios internos o anclajes.\n"
            "2. Empatizar y Conectar con la Humanidad del Otro:\n"
            "  • ¿Con qué partes de la otra persona puedo empatizar?\n"
            "  • Acción: Mostrar empatía y reconocer emociones y necesidades.\n"
            "3. Descubrimientos sobre Mí, el Otro y la Relación:\n"
            "  • ¿Qué estoy descubriendo de mí, de la otra persona o de nuestra relación?\n"
            "  • Acción: Mantener una mente abierta para el aprendizaje.\n"
            "4. Formular Pedidos y Ofertas durante la Conversación:\n"
            "  • ¿Qué pedidos u ofertas quiero hacer durante la conversación?\n"
            "  • Acción: Formular pedidos claros y específicos basados en las necesidades.\n"
            "¿Tienes alguna duda sobre esta segunda parte? (sí/no)"
        )
        return EXPLAIN_PART_2
    else:
        await update.message.reply_text("¿Te gustaría que te ayude a diseñar alguna conversación? (sí/no)")
        return DESIGN_CONVERSATION