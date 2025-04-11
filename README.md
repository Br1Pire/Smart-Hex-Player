
# Documentación de la Estrategia del Jugador Inteligente (`SmartPlayer`)

## Descripción General

El jugador `SmartPlayer` implementa una estrategia inteligente para el juego de Hex utilizando el algoritmo **Minimax con poda Alpha-Beta**, complementado por una **evaluación heurística dinámica** que varía según la etapa del juego (inicio, medio y final). Su objetivo es seleccionar el mejor movimiento posible a partir de una evaluación profunda del estado del tablero, teniendo en cuenta tanto su posición como la del oponente.

---

## Algoritmo de Selección de Movimiento

El método principal `play(board)` itera sobre todos los movimientos posibles en el tablero actual y simula cada uno utilizando el algoritmo Minimax con una profundidad limitada. Para cada simulación, se evalúa el tablero utilizando una heurística adaptativa. Finalmente, selecciona el movimiento con la mejor puntuación.

Si varios movimientos obtienen la misma mejor puntuación, elige uno aleatoriamente entre ellos.

---

## Minimax con Poda Alpha-Beta

El método `minimax` explora recursivamente los movimientos posibles alternando entre jugador maximizador (el propio jugador) y minimizador (el oponente). La profundidad del árbol está limitada a 3 niveles para mantener la eficiencia.

La poda alpha-beta se emplea para eliminar ramas del árbol de decisiones que no influirán en la elección final, reduciendo significativamente el tiempo de cómputo.

---

## Evaluación del Tablero

La función `evaluate_board` determina cuál de las tres estrategias heurísticas aplicar en función del progreso de la partida. Esta decisión se basa en:

- El número total de turnos jugados (`turns_amount`)
- El tamaño del tablero (`n`)
- Una estimación del 60% del total de casillas para identificar el medio juego

### Etapas del Juego

#### 1. Juego Temprano (`evaluate_early_game`)
En las primeras etapas, la estrategia se basa en una **matriz de pesos** centrada en el medio del tablero. Las celdas más cercanas al centro tienen mayor peso, promoviendo el control del área central.

Adicionalmente, se penaliza ligeramente la cercanía a fichas enemigas al aumentar el peso de las celdas vacías adyacentes a estas.

#### 2. Medio Juego (`evaluate_mid_game`)
En esta etapa se combina la evaluación temprana con una estimación del número de nodos necesarios para conectar los lados opuestos del tablero:

- **`own_nodes_to_connect`**: estima los nodos que el jugador necesita para ganar.
- **`opp_nodes_to_connect`**: estima los nodos que el oponente necesita para ganar.

La evaluación da más importancia a las conexiones propias y penaliza la cercanía de las conexiones del oponente.

#### 3. Final del Juego (`evaluate_end_game`)
En la etapa final, el jugador ignora la matriz de pesos y se enfoca exclusivamente en la conectividad. Se calcula la diferencia ponderada entre los nodos requeridos por ambos jugadores para cerrar su conexión:

- A menor cantidad de nodos requeridos, mayor la puntuación para el jugador.

---

## Estimación de Nodos para Conectar (`estimate_remaining_nodes_to_connect`)

Este método emplea una versión simplificada del algoritmo **A\*** para estimar cuántas celdas vacías (nodos) necesita un jugador para conectar sus dos bordes asignados.

- Se inicializa una cola de prioridad (heap) con los bordes de entrada.
- Se expande hacia los bordes de salida considerando menor costo a las fichas propias, y mayor costo (1) a celdas vacías.
- Se devuelve el costo mínimo para alcanzar el borde opuesto.

---

## Matriz de Pesos Inicial (`generate_weight_matrix`)

Genera una matriz centrada en el tablero, donde las celdas cercanas al centro tienen mayor valor. Esta matriz se utiliza en el juego temprano para fomentar el posicionamiento estratégico central.

---

## Consideraciones Finales

- El jugador usa una profundidad fija de 3 en el algoritmo Minimax.
- La estrategia se adapta a cada etapa del juego para lograr un balance entre posicionamiento, conectividad y control del tablero.
- La implementación busca eficiencia sin sacrificar calidad en las decisiones.

---
