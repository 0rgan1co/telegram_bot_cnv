Feature: Explicar la técnica de diseño de conversaciones

  Scenario: Explicar la técnica de diseño de conversaciones
    Given un usuario inicia el bot
    When el usuario envía el comando "/explicar_tecnica"
    Then el bot explica que el objetivo de la técnica es "Conectar antes de actuar" y consta de 2 partes: "Auto-conexión" y "Conexión durante la conversación"
    And el bot pregunta si el usuario tiene alguna duda sobre la primera parte

  Scenario: El usuario tiene dudas sobre la primera parte de la técnica
    Given el bot ha explicado la primera parte de la técnica
    When el usuario responde "sí" a la pregunta de si tiene dudas
    Then el bot vuelve a explicar la primera parte de la técnica

  Scenario: El usuario no tiene dudas sobre la primera parte de la técnica
    Given el bot ha explicado la primera parte de la técnica
    When el usuario responde "no" a la pregunta de si tiene dudas
    Then el bot explica la segunda parte de la técnica y pregunta si el usuario tiene alguna duda sobre esta parte

    