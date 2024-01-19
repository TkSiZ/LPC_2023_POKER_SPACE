# Atividade 010: Criar o jogo inédito em PyGame
import pygame

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)

player_lifes = 3  # Alterei de 1 para 3, conforme mencionado no GDD
player_shots = 5

scrn_x = 840
scrn_y = 640
size = (scrn_x, scrn_y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Poker_Space")

# Lifes text
player_life = pygame.image.load("assets/player_life.png")
player_life_x = 0
player_life_y = scrn_y - 32

# Shots Text
shots_font = pygame.font.Font('assets/PressStart2P.ttf', 22)
shots_text = shots_font.render('5', True, COLOR_WHITE, COLOR_BLACK)
shots_text_rect = shots_text.get_rect()
shots_text_rect.center = (scrn_x - 22, scrn_y - 22)

# victory text
# Adicione o código para exibir o texto de vitória

# lost text
# Adicione o código para exibir o texto de derrota

# phase 1 obstacles
retangle_1_x = 335
retangle_1_y = 50
retangle_1_pos_x = scrn_x / 2 - (retangle_1_x / 2)
retangle_1_pos_y = scrn_y / 2 - (retangle_1_y / 2)
retangle_1 = pygame.Rect(retangle_1_pos_x, retangle_1_pos_y, retangle_1_x, retangle_1_y)

# phase 2 obstacle

# mid triangle
triangle_3_mid = pygame.image.load("assets/Triangulo_mid.png")
triangle_3_mid_x = scrn_x / 2 - 178
triangle_3_mid_y = scrn_y / 2 - 100

# triangle left
triangle_3_left = pygame.image.load("assets/Triangulo_canto_esquerdo.png")
triangle_3_left_x = 0
triangle_3_left_y = scrn_y / 2 + 70

# triangle right
triangle_3_right = pygame.image.load("assets/Triangulo_canto_direito.png")
triangle_3_right_x = scrn_x - 214
triangle_3_right_y = 30

# phase 3 obstacles

# mid square
square_3_x = 240
square_3_y = 170
square_3_pos_x = scrn_x / 2 - (square_3_x / 2)
square_3_pos_y = scrn_y / 2 - (square_3_y / 2)
square_3 = pygame.Rect(square_3_pos_x, square_3_pos_y, square_3_x, square_3_y)

# right retangle
retangle_3_r_x = 50
retangle_3_r_y = 320
retangle_3_r_pos_x = square_3_pos_x + square_3_x + 150
retangle_3_r_pos_y = scrn_y / 2 - (retangle_3_r_y / 2)
retangle_3_r = pygame.Rect(retangle_3_r_pos_x, retangle_3_r_pos_y, retangle_3_r_x, retangle_3_r_y)

# left retangle
retangle_3_l_x = 50
retangle_3_l_y = 320
retangle_3_l_pos_x = square_3_pos_x - retangle_3_l_x - 150
retangle_3_l_pos_y = scrn_y / 2 - (retangle_3_l_y / 2)
retangle_3_l = pygame.Rect(retangle_3_l_pos_x, retangle_3_l_pos_y, retangle_3_l_x, retangle_3_l_y)

# phase 4 obstacles

# mid square
square_4_x = 140
square_4_y = 160
square_4_pos_x = scrn_x / 2 - (square_4_x / 2)
square_4_pos_y = scrn_y / 2 - (square_4_y / 2 + 10)
square_4_mid = pygame.Rect(square_4_pos_x, square_4_pos_y, square_4_x, square_4_y)

# Diagonals
diagonal_bottom_left = pygame.image.load("assets/Diagonal_1.png")
diagonal_bottom_left_x = 80
diagonal_bottom_left_y = scrn_y - 220

diagonal_top_right = pygame.image.load("assets/Diagonal_1.png")
diagonal_top_right_x = scrn_x - 200
diagonal_top_right_y = 70

diagonal_top_left = pygame.image.load("assets/Diagonal_2.png")
diagonal_top_left_x = diagonal_bottom_left_x
diagonal_top_left_y = diagonal_top_right_y

diagonal_bottom_right = pygame.image.load("assets/Diagonal_2.png")
diagonal_bottom_right_x = diagonal_top_right_x
diagonal_bottom_right_y = diagonal_bottom_left_y

# Sound effects
victory_sound_effect = pygame.mixer.Sound('assets/victory.wav')
lost_sound_effect = pygame.mixer.Sound('assets/defeat.wav')
shot_sound_effect = pygame.mixer.Sound('assets/shot.wav')
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')

# Player 1
p_top_x = scrn_x / 2
p_top_y = scrn_y - 90
p_left_x = (scrn_x / 2) - 40
p_right_x = (scrn_x / 2) + 40
p_sides_y = scrn_y - 35
p_1_colision_x_size = p_right_x - p_left_x
p_1_colision_y_size = p_top_y - p_sides_y
p_1_move_right = False
p_1_move_left = False

# Player 2 (bot)

# game speed
speed = 60

# ball
ball = pygame.image.load("assets/ball.png")
ball_x = 640
ball_y = 360
ball_dx = -5
ball_dy = -5

# shots
shot_1 = 5
shot_2 = 5

# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p_1_move_left = True
            if event.key == pygame.K_RIGHT:
                p_1_move_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                p_1_move_left = False
            if event.key == pygame.K_RIGHT:
                p_1_move_right = False

    # checking the victory condition
    # Adicione a lógica para verificar a condição de vitória e avançar para o próximo nível

    # clear screen
    screen.fill(COLOR_BLACK)

    # ball collision with the lower/upper wall
    if ball_y <= 0 or ball_y >= scrn_y:
        ball_dy *= -1
        bounce_sound_effect.play()  # Adicione o som de colisão com a parede

    # ball collision with the player 1
    if p_left_x < ball_x < p_right_x and p_sides_y < ball_y < p_top_y:
        player_lifes -= 1
        shot_sound_effect.play()  # Adicione o som de colisão com o jogador

    # ball collision with the enemy
    # Adicione as condições de colisão com os obstáculos dos diferentes níveis

    # ball movement
    ball_x += ball_dx
    ball_y += ball_dy

    # player 1 left movement
    if p_1_move_left:
        p_left_x -= 5
        p_top_x -= 5
        p_right_x -= 5

    # player 1 right movement
    if p_1_move_right:
        p_left_x += 5
        p_top_x += 5
        p_right_x += 5

    # player 1 collides with left wall
    if p_left_x <= 0:
        p_left_x = 0
        p_top_x = p_left_x + 40
        p_right_x = p_top_x + 40

    # player 1 collides with right wall
    if p_right_x >= scrn_x:
        p_right_x = scrn_x
        p_top_x = scrn_x - 40
        p_left_x = p_top_x - 40

    # player 2 collides with left wall
    # Adicione a lógica para a colisão do jogador adversário com as paredes

    # player 2 collides with right wall
    # Adicione a lógica para a colisão do jogador adversário com as paredes

    # player 2 "Artificial Intelligence"
    # Adicione o código para a movimentação automática do jogador adversário

    # update shots hud
    shots_text = shots_font.render(str(player_shots), True, COLOR_WHITE, COLOR_BLACK)

    # drawing objects
    pygame.draw.polygon(screen, COLOR_WHITE, [(p_top_x, p_top_y), (p_left_x, p_sides_y), (p_right_x, p_sides_y)])
    screen.blit(shots_text, shots_text_rect)
    screen.blit(player_life, (player_life_x, player_life_y))
    screen.blit(player_life, (player_life_x + 30, player_life_y))
    screen.blit(player_life, (player_life_x + 60, player_life_y))

    # phase 1 obstacle
    pygame.draw.rect(screen, COLOR_WHITE, retangle_1)

    # phase 2 obstacles
    screen.blit(triangle_3_mid, (triangle_3_mid_x, triangle_3_mid_y))
    screen.blit(triangle_3_left, (triangle_3_left_x, triangle_3_left_y))
    screen.blit(triangle_3_right, (triangle_3_right_x, triangle_3_right_y))

    # phase 3 obstacles
    pygame.draw.rect(screen, COLOR_WHITE, retangle_3_r)
    pygame.draw.rect(screen, COLOR_WHITE, retangle_3_l)
    pygame.draw.rect(screen, COLOR_WHITE, square_3)

    # phase 4 obstacles
    pygame.draw.rect(screen, COLOR_WHITE, square_4_mid)
    screen.blit(diagonal_bottom_left, (diagonal_bottom_left_x, diagonal_bottom_left_y))
    screen.blit(diagonal_top_right, (diagonal_top_right_x, diagonal_top_right_y))
    screen.blit(diagonal_top_left, (diagonal_top_left_x, diagonal_top_left_y))
    screen.blit(diagonal_bottom_right, (diagonal_bottom_right_x, diagonal_bottom_right_y))

    # check victory and defeat conditions
    if player_lifes <= 0:
        lost_sound_effect.play()  # Adicione o som de derrota
        # Adicione a lógica para reiniciar o jogo ou encerrar
        game_loop = False

    # Adicione a lógica para verificar a condição de vitória e avançar para o próximo nível

    # update screen
    pygame.display.flip()
    game_clock.tick(speed)

pygame.quit()
