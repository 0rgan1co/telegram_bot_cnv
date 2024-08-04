Feature: Diseñar una conversación difícil

  Scenario: El usuario quiere diseñar una conversación
    Given el bot ha preguntado si el usuario quiere diseñar alguna conversación
    When el usuario responde "sí"
    Then el bot guía al usuario a través de una serie de preguntas para diseñar la conversación

  Scenario: El usuario no quiere diseñar una conversación
    Given el bot ha preguntado si el usuario quiere diseñar alguna conversación
    When el usuario responde "no"
    Then el bot finaliza la interacción y ofrece ayuda en otro momento si es necesario