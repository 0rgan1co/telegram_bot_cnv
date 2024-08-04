import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pytest_bdd import scenarios, given, when, then
from telegram import Update, Bot
from telegram.ext import CallbackContext
from BotDialogosCNV.explain_technique import explain_technique, explain_part_1, explain_part_2
from BotDialogosCNV.conversation_design import design_conversation, receive_response, provide_suggestions

# Escenarios
scenarios('features/explain_technique.feature')
scenarios('features/conversation_design.feature')

# Given
@given('un usuario inicia el bot')
def start_bot():
    pass

@given('el bot ha explicado la primera parte de la técnica')
def explained_first_part():
    pass

@given('el bot ha preguntado si el usuario quiere diseñar alguna conversación')
def asked_design_conversation():
    pass

# When
@when('el usuario envía el comando "/explicar_tecnica"')
def send_explain_command():
    update = Update(update_id=1, message=MockMessage("/explicar_tecnica"))
    context = CallbackContext(bot=MockBot())
    explain_technique(update, context)

@when('el usuario responde "sí" a la pregunta de si tiene dudas')
def user_responds_yes():
    update = Update(update_id=1, message=MockMessage("sí"))
    context = CallbackContext(bot=MockBot())
    explain_part_1(update, context)

@when('el usuario responde "no" a la pregunta de si tiene dudas')
def user_responds_no():
    update = Update(update_id=1, message=MockMessage("no"))
    context = CallbackContext(bot=MockBot())
    explain_part_2(update, context)

@when('el usuario responde "sí"')
def user_wants_design():
    update = Update(update_id=1, message=MockMessage("sí"))
    context = CallbackContext(bot=MockBot())
    design_conversation(update, context)

@when('el usuario responde "no"')
def user_does_not_want_design():
    update = Update(update_id=1, message=MockMessage("no"))
    context = CallbackContext(bot=MockBot())
    design_conversation(update, context)

# Then
@then('el bot explica que el objetivo de la técnica es "Conectar antes de actuar" y consta de 2 partes: "Auto-conexión" y "Conexión durante la conversación"')
def check_explain_technique():
    # Aquí iría la lógica para verificar que el bot envió el mensaje correcto.
    pass

@then('el bot pregunta si el usuario tiene alguna duda sobre la primera parte')
def check_ask_first_part_doubts():
    # Aquí iría la lógica para verificar que el bot envió el mensaje correcto.
    pass

@then('el bot vuelve a explicar la primera parte de la técnica')
def check_reexplain_first_part():
    # Aquí iría la lógica para verificar que el bot envió el mensaje correcto.
    pass

@then('el bot explica la segunda parte de la técnica y pregunta si el usuario tiene alguna duda sobre esta parte')
def check_explain_second_part():
    # Aquí iría la lógica para verificar que el bot envió el mensaje correcto.
    pass

@then('el bot guía al usuario a través de una serie de preguntas para diseñar la conversación')
def check_design_conversation():
    # Aquí iría la lógica para verificar que el bot envió el mensaje correcto.
    pass

@then('el bot finaliza la interacción y ofrece ayuda en otro momento si es necesario')
def check_end_interaction():
    # Aquí iría la lógica para verificar que el bot envió el mensaje correcto.
    pass

# Clases Mock para simular los objetos Update y Bot
class MockMessage:
    def __init__(self, text):
        self.text = text

    async def reply_text(self, text):
        print(text)  # O almacenar el mensaje para verificarlo en las pruebas

class MockBot(Bot):
    def __init__(self):
        pass