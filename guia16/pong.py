import py5
import random

# Variables de posición y dimensiones de las paletas, velocidad y tamaño de la pelota
paddle1_y = paddle2_y = 0
paddle_width = paddle_height = 0
paddle_speed = ball_size = 0
ball_x = ball_y = ball_dx = ball_dy = 0
player1_score = player2_score = 0
game_over = False
winner = ""        
keys = set()

# Lista para almacenar los power-ups y efectos activos
power_ups = []
active_effects = []
power_up_size = 20
power_up_effect_duration = 15 * 60  # Duración del efecto en frames (15 segundos)
power_up_spawn_duration = 5 * 60    # Duración de aparición de un power-up (5 segundos)

default_color = (255, 255, 255)
paddle_color = ball_color = default_color

def setup():
    # Configuración inicial del juego
    py5.size(800, 400)
    global paddle_width, paddle_height, paddle_speed, ball_size
    global ball_x, ball_y, ball_dx, ball_dy
    global paddle1_y, paddle2_y, player1_score, player2_score
    paddle_width = 20
    paddle_height = 100
    paddle_speed = 7
    ball_size = 20
    reset_game()  # Reinicia el juego

def reset_game():
    # Reinicia todas las variables y estados del juego
    global ball_x, ball_y, ball_dx, ball_dy, paddle1_y, paddle2_y
    global player1_score, player2_score, power_ups, active_effects, game_over, winner
    ball_x = py5.width / 2
    ball_y = py5.height / 2
    ball_dx = 5
    ball_dy = 3
    paddle1_y = py5.height / 2 - paddle_height / 2
    paddle2_y = py5.height / 2 - paddle_height / 2
    player1_score = 0
    player2_score = 0
    power_ups = []
    active_effects = []
    game_over = False
    winner = ""

def draw():
    # Función principal de dibujo que se ejecuta en cada frame
    global ball_x, ball_y, ball_dx, ball_dy, paddle1_y, paddle2_y
    global player1_score, player2_score, paddle_color, ball_color, game_over

    py5.background(0)
    
    if game_over:
        display_winner()  # Muestra el ganador si el juego terminó
        return

    # Dibuja las paletas y la pelota
    py5.fill(*paddle_color)
    py5.rect(30, paddle1_y, paddle_width, paddle_height)
    py5.rect(py5.width - 30 - paddle_width, paddle2_y, paddle_width, paddle_height)
    
    py5.fill(*ball_color)
    py5.ellipse(ball_x, ball_y, ball_size, ball_size)
    
    # Muestra el marcador
    py5.fill(255)
    py5.text_size(32)
    py5.text_align(py5.CENTER)
    py5.text(f"{player1_score} - {player2_score}", py5.width / 2, 40)
    
    # Instrucciones para los jugadores
    py5.text_size(16)
    py5.text_align(py5.LEFT)
    py5.text("Jugador 1: W (Arriba), S (Abajo)", 10, 30)
    py5.text_align(py5.RIGHT)
    py5.text("Jugador 2: O (Arriba), L (Abajo)", py5.width - 10, 30)
    
    # Movimiento de la pelota
    ball_x += ball_dx
    ball_y += ball_dy
    
    # Incrementa la velocidad de la pelota cada minuto
    if py5.frame_count % (60 * 60) == 0:
        ball_dx *= 1.1
        ball_dy *= 1.1
    
    # Rebote de la pelota en los bordes superior e inferior
    if ball_y <= ball_size / 2 or ball_y >= py5.height - ball_size / 2:
        ball_dy *= -1
    
    # Rebote en las paletas
    if ball_x - ball_size / 2 <= 30 + paddle_width:
        if paddle1_y < ball_y < paddle1_y + paddle_height:
            ball_dx *= -1
            ball_x = 30 + paddle_width + ball_size / 2
    
    if ball_x + ball_size / 2 >= py5.width - 30 - paddle_width:
        if paddle2_y < ball_y < paddle2_y + paddle_height:
            ball_dx *= -1
            ball_x = py5.width - 30 - paddle_width - ball_size / 2
    
    # Puntuación si la pelota sale de los bordes laterales
    if ball_x < 0:
        player2_score += 1
        reset_ball()  
        deactivate_all_effects() 
        if player2_score >= 15:
            end_game("Jugador 2")  

    if ball_x > py5.width:
        player1_score += 1
        reset_ball()
        deactivate_all_effects()
        if player1_score >= 15:
            end_game("Jugador 1")

    # Movimiento de las paletas
    if 'w' in keys and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if 's' in keys and paddle1_y < py5.height - paddle_height:
        paddle1_y += paddle_speed
    if 'o' in keys and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if 'l' in keys and paddle2_y < py5.height - paddle_height:
        paddle2_y += paddle_speed

    # Manejo de power-ups
    for power_up in power_ups[:]:
        x, y, effect, spawn_time = power_up
        if py5.frame_count - spawn_time > power_up_spawn_duration:
            power_ups.remove(power_up)
        else:
            draw_power_up(x, y, effect)
            # Verifica si la pelota toca el power-up
            if (x - power_up_size / 2 < ball_x < x + power_up_size * 1.5 and
                    y - power_up_size / 2 < ball_y < y + power_up_size * 1.5):
                apply_power_up(effect)  
                power_ups.remove(power_up)

    # Efectos activos
    for effect in active_effects[:]:
        effect_name, start_time = effect
        if py5.frame_count - start_time > power_up_effect_duration:
            deactivate_effect(effect_name)  # Desactiva el efecto si ya ha expirado
            active_effects.remove(effect)

    # Genera un nuevo power-up cada 5 segundos
    if py5.frame_count % 300 == 0:
        spawn_power_up()

def key_pressed():
    # Agrega la tecla presionada al conjunto de teclas activas
    global keys
    keys.add(py5.key)
    if py5.key == 'r' and game_over: 
        reset_game()

def key_released():
    # Elimina la tecla soltada del conjunto de teclas activas
    global keys
    keys.discard(py5.key)

def reset_ball():
    # Reinicia la posición y dirección de la pelota
    global ball_x, ball_y, ball_dx, ball_dy
    ball_x = py5.width / 2
    ball_y = py5.height / 2
    ball_dx *= -1
    ball_dy = py5.random(-3, 3)

def spawn_power_up():
    # Genera un power-up en una posición aleatoria
    x = random.randint(100, py5.width - 100)
    y = random.randint(50, py5.height - 50)
    effect = random.choice(["speed_up", "paddle_increase", "slow_down", "paddle_decrease"])
    power_ups.append([x, y, effect, py5.frame_count])

def draw_power_up(x, y, effect):
    # Dibuja el power-up con un color dependiendo del efecto
    if effect == "speed_up":
        py5.fill(0, 255, 0)
    elif effect == "paddle_increase":
        py5.fill(0, 0, 255)
    elif effect == "slow_down":
        py5.fill(255, 255, 0)
    elif effect == "paddle_decrease":
        py5.fill(255, 0, 0)
    py5.rect(x, y, power_up_size, power_up_size)

def apply_power_up(effect):
    # Aplica el efecto del power-up
    global ball_dx, ball_dy, paddle_height, paddle_color, ball_color
    if effect == "speed_up":
        ball_dx *= 1.5
        ball_dy *= 1.5
        paddle_color = ball_color = (0, 255, 0)
    elif effect == "slow_down":
        ball_dx *= 0.5
        ball_dy *= 0.5
        paddle_color = ball_color = (255, 255, 0)
    elif effect == "paddle_increase":
        paddle_height += 50
        paddle_color = ball_color = (0, 0, 255)
    elif effect == "paddle_decrease":
        paddle_height -= 50
        paddle_color = ball_color = (255, 0, 0)
    active_effects.append([effect, py5.frame_count])

def deactivate_effect(effect):
    # Desactiva el efecto del power-up y restaura valores originales
    global ball_dx, ball_dy, paddle_height, paddle_color, ball_color
    if effect == "speed_up" or effect == "slow_down":
        ball_dx = 5
        ball_dy = 3
    elif effect == "paddle_increase" or effect == "paddle_decrease":
        paddle_height = 100
    paddle_color = ball_color = default_color

def deactivate_all_effects():
    # Desactiva todos los efectos activos
    global active_effects
    for effect in active_effects:
        deactivate_effect(effect[0])
    active_effects.clear()

def display_winner():
    # Muestra el ganador en la pantalla
    py5.fill(255)
    py5.text_size(64)
    py5.text_align(py5.CENTER)
    py5.text(f"{winner} ha ganado!", py5.width / 2, py5.height / 2)

def end_game(winning_player):
    # Finaliza el juego y muestra el ganador
    global game_over, winner
    game_over = True
    winner = winning_player
