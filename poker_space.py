#Atividade 0010 -

import random
import pygame

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)

player_lifes = 3
player_shots = 5

scrn_x = 840
scrn_y = 640
size = (scrn_x, scrn_y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Poker_Space")

# Lifes text
player_life = pygame.image.load("assets/player_life.png")
player_life_x = 3
player_life_y = scrn_y - 32

# Shots Text
shots_font = pygame.font.Font('assets/PressStart2P.ttf', 22)
shots_text = shots_font.render('5', True, COLOR_WHITE, COLOR_BLACK)
shots_text_rect = shots_text.get_rect()
shots_text_rect.center = (scrn_x - 22, scrn_y - 22)

# victory text
victory_font = pygame.font.Font('assets/PressStart2P.ttf', 100)
victory_text = victory_font.render('VICTORY', True, COLOR_WHITE, COLOR_BLACK)
victory_text_rect = victory_text.get_rect()
victory_text_rect.center = (scrn_x - 400, scrn_y - 350)

# lost text
defeat_font = pygame.font.Font('assets/PressStart2P.ttf', 100)
defeat_text = defeat_font.render('DEFEAT', True, COLOR_WHITE, COLOR_BLACK)
defeat_text_rect = defeat_text.get_rect()
defeat_text_rect.center = (scrn_x - 400, scrn_y - 350)

# bullets
bullets = []
velocity_bullets_x = []
velocity_bullets_y = []

enemy_bullets = []
enemy_velocity_bullets_x = []
enemy_velocity_bullets_y = []

# Function to draw the shots on the screen
def draw_bullets():
    for bullet in bullets:
        pygame.draw.rect(screen, COLOR_WHITE, bullet)
def draw_bullets_ia():
    for bullet in enemy_bullets :
        pygame.draw.rect(screen, COLOR_WHITE, bullet)

def check_bullet_obstacle_collision(bullet, obstacle):
    return bullet.colliderect(obstacle)

# phase 1 enemy(copas)
image_copas = pygame.image.load("assets/heart_enemy.png")
image_copas_rect = image_copas.get_rect()
image_copas_rect.topleft = (scrn_x/2 - (image_copas_rect.width/2), 0)
image_copas_mask = pygame.mask.from_surface(image_copas)

# phase 2 enemy(paus)
image_paus = pygame.image.load("assets/paus.png")
image_paus_rect = image_paus.get_rect()
image_paus_rect.topleft = (scrn_x/2 - (image_paus_rect.width/2), 0)
image_paus_mask = pygame.mask.from_surface(image_paus)

# phase 3 enemy(espadas)
image_espadas = pygame.image.load("assets/espadas.png")
image_espadas_rect = image_espadas.get_rect()
image_espadas_rect.topleft = (scrn_x/2 - (image_espadas_rect.width/2), 0)
image_espadas_mask = pygame.mask.from_surface(image_espadas)

# phase 4 enemy(ouros)
image_ball = pygame.image.load("assets/heart_enemy.png")
image_ball_rect = image_ball.get_rect()
image_ball_rect.topleft = (scrn_x/2 - (image_ball_rect.width/2), 0)
image_ball_mask = pygame.mask.from_surface(image_ball)

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
triangle_3_rect = triangle_3_mid.get_rect(topleft=(triangle_3_mid_x, triangle_3_mid_y))
triangle_3_mid_mask = pygame.mask.from_surface(triangle_3_mid)

# triangle left
triangle_3_left = pygame.image.load("assets/Triangulo_canto_esquerdo.png")
triangle_3_left_x = 0
triangle_3_left_y = scrn_y / 2 + 70
triangle_3_left_rect = triangle_3_left.get_rect(topleft=(triangle_3_left_x, triangle_3_left_y))
triangle_3_left_mask = pygame.mask.from_surface(triangle_3_left)

# triangle right
triangle_3_right = pygame.image.load("assets/Triangulo_canto_direito.png")
triangle_3_right_x = scrn_x - 214
triangle_3_right_y = 30
triangle_3_right_rect = triangle_3_right.get_rect(topleft=(triangle_3_right_x, triangle_3_right_y))
triangle_3_right_mask = pygame.mask.from_surface(triangle_3_right)


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


# diagonals
diagonal_bottom_left = pygame.image.load("assets/Diagonal_1.png")
diagonal_bottom_left_x = 80
diagonal_bottom_left_y = scrn_y - 220
diagonal_bottom_left_rect = diagonal_bottom_left.get_rect(topleft=(diagonal_bottom_left_x, diagonal_bottom_left_y))

diagonal_top_right = pygame.image.load("assets/Diagonal_1.png")
diagonal_top_right_x = scrn_x - 200
diagonal_top_right_y = 70
diagonal_top_right_rect = diagonal_top_right.get_rect(topleft=(diagonal_top_right_x, diagonal_top_right_y))


diagonal_top_left = pygame.image.load("assets/Diagonal_2.png")
diagonal_top_left_x = diagonal_bottom_left_x
diagonal_top_left_y = diagonal_top_right_y
diagonal_top_left_rect = diagonal_top_left.get_rect(topleft=(diagonal_top_left_x, diagonal_top_left_y))


diagonal_bottom_right = pygame.image.load("assets/Diagonal_2.png")
diagonal_bottom_right_x = diagonal_top_right_x
diagonal_bottom_right_y = diagonal_bottom_left_y
diagonal_bottom_right_rect = diagonal_bottom_right.get_rect(topleft=(diagonal_bottom_right_x, diagonal_bottom_right_y))

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
p_1_colision_y_size = p_sides_y - p_top_y
p_1_move_right = False
p_1_move_left = False
player1_rect = pygame.Rect(p_left_x, p_top_y, p_1_colision_x_size, p_1_colision_y_size)

# game speed
speed = 60
mask_aux = pygame.mask.from_surface(image_ball)

# ball
ball = pygame.image.load("assets/ball.png")
ball_x = 640
ball_y = 360
ball_dx = -5
ball_dy = -5

v_b_x = 6
# game loop
game_loop = True
game_clock = pygame.time.Clock()
phase = 4
retangle_1_movimentation = 5
enemy_bullet_cooldown = 2000  # Enemy shot cooldown
last_enemy_bullet_time = 0
while game_loop:

    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p_1_move_left = True
            if event.key == pygame.K_RIGHT:
                p_1_move_right = True
                # Adds a shot to the list when the spacebar is pressed
            if event.key == pygame.K_SPACE and player_shots >= 0:
                player_shots -= 1
                if player_shots > 0:
                    bullet = pygame.Rect(p_top_x + p_1_colision_x_size // 50 - 4, p_sides_y, 8, 6)
                    bullets.append(bullet)
                    velocity_bullets_y.append(-5)
                    shot_sound_effect.play()
                if p_1_move_right:
                    velocity_bullets_x.append(v_b_x)
                else:
                    velocity_bullets_x.append(-v_b_x)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                p_1_move_left = False
            if event.key == pygame.K_RIGHT:
                p_1_move_right = False

    if player_shots < 0:
        phase = 6



    # detect collision enemy and enemy atack
    if phase == 1:
        i = 0
        for bullet in bullets:
            if bullet.y < 300:
                if velocity_bullets_x[i] < 0:
                    image_copas_rect.x -= 2
                else:
                    image_copas_rect.x += 2
            i += 1

        if current_time - last_enemy_bullet_time > enemy_bullet_cooldown:
            # Adicione uma bala do inimigo
            enemy_bullet = pygame.Rect(image_copas_rect.centerx, image_copas_rect.centery, 8, 6)
            enemy_bullets.append(enemy_bullet)

            # Determine a direção do tiro do inimigo
            if p_left_x > image_copas_rect.left:
                enemy_velocity_bullets_x.append(v_b_x)
            else:
                enemy_velocity_bullets_x.append(-v_b_x)

            # Defina a velocidade vertical
            enemy_velocity_bullets_y.append(5)

            last_enemy_bullet_time = current_time
        # Dentro do loop principal, após a lógica de movimentação das balas do jogador
        bullets_to_remove = []

        p_1_rect = pygame.Rect(p_left_x, p_top_x, p_1_colision_x_size, p_1_colision_y_size)

        for i, (enemy_bullet, enemy_v_bullet_x, enemy_v_bullet_y) in enumerate(
                zip(enemy_bullets, enemy_velocity_bullets_x, enemy_velocity_bullets_y)):
            enemy_bullet.x += enemy_v_bullet_x
            enemy_bullet.y += enemy_v_bullet_y

            if (enemy_bullet.y + enemy_bullet.height) >= scrn_y:
                # Adicione o índice à lista de balas para remover
                bullets_to_remove.append(i)


        # Remova as balas e velocidades correspondentes fora do loop
        for i in reversed(bullets_to_remove):
            enemy_bullets.pop(i)
            enemy_velocity_bullets_y.pop(i)
            enemy_velocity_bullets_x.pop(i)
        ia = 0
        for bullet in enemy_bullets:
            # Verifique as colisões com as laterais e o fundo da tela
            if bullet.x <= 0 or (bullet.x + bullet.width) >= scrn_x:
                enemy_velocity_bullets_x[ia] *= -1
                bounce_sound_effect.play()

            # Corrija as condições de colisão abaixo
            if bullet.colliderect(retangle_1):
                enemy_velocity_bullets_y[ia] *= -1
                enemy_velocity_bullets_x[ia] *= -1
                bounce_sound_effect.play()
            ia += 1

        for bullet in bullets:
            if bullet.colliderect(image_copas_rect):
                bounce_sound_effect.play()
                phase = 2
                player_shots = 5
                bullets.clear()
                enemy_bullets.clear()
                velocity_bullets_y.clear()
                velocity_bullets_x.clear()
                pygame.time.delay(200)


    if phase == 2:
        i = 0
        for bullet in bullets:
            if bullet.y < 300:
                if velocity_bullets_x[i] < 0:
                    image_paus_rect.x -= 2
                else:
                    image_paus_rect.x += 2
            i += 1

        if current_time - last_enemy_bullet_time > enemy_bullet_cooldown:
            # Adicione uma bala do inimigo
            enemy_bullet = pygame.Rect(image_copas_rect.centerx, image_copas_rect.centery, 8, 6)
            enemy_bullets.append(enemy_bullet)

            # Determine a direção do tiro do inimigo
            if p_left_x > image_copas_rect.left:
                enemy_velocity_bullets_x.append(v_b_x)
            else:
                enemy_velocity_bullets_x.append(-v_b_x)

            # Defina a velocidade vertical
            enemy_velocity_bullets_y.append(5)

            last_enemy_bullet_time = current_time
        # Dentro do loop principal, após a lógica de movimentação das balas do jogador
        bullets_to_remove = []

        p_1_rect = pygame.Rect(p_left_x, p_top_x, p_1_colision_x_size, p_1_colision_y_size)

        for i, (enemy_bullet, enemy_v_bullet_x, enemy_v_bullet_y) in enumerate(
                zip(enemy_bullets, enemy_velocity_bullets_x, enemy_velocity_bullets_y)):
            enemy_bullet.x += enemy_v_bullet_x
            enemy_bullet.y += enemy_v_bullet_y

            if (enemy_bullet.y + enemy_bullet.height) >= scrn_y:
                # Adicione o índice à lista de balas para remover
                bullets_to_remove.append(i)


        # Remova as balas e velocidades correspondentes fora do loop
        for i in reversed(bullets_to_remove):
            enemy_bullets.pop(i)
            enemy_velocity_bullets_y.pop(i)
            enemy_velocity_bullets_x.pop(i)
        ia = 0
        for bullet in enemy_bullets:
            # Verifique as colisões com as laterais e o fundo da tela
            if bullet.x <= 0 or (bullet.x + bullet.width) >= scrn_x:
                enemy_velocity_bullets_x[ia] *= -1
                bounce_sound_effect.play()


        for bullet in bullets:
            if bullet.colliderect(image_paus_rect):
                phase = 3
                player_shots = 5
                bullets.clear()
                enemy_bullets.clear()
                velocity_bullets_y.clear()
                velocity_bullets_x.clear()
                pygame.time.delay(200)

    if phase == 3:
        i = 0
        for bullet in bullets:
            if bullet.y < 300:
                if velocity_bullets_x[i] < 0:
                    image_espadas_rect.x -= 2
                else:
                    image_espadas_rect.x += 2
            i += 1
        if current_time - last_enemy_bullet_time > enemy_bullet_cooldown:
            # Adicione uma bala do inimigo
            enemy_bullet = pygame.Rect(image_copas_rect.centerx, image_copas_rect.centery, 8, 6)
            enemy_bullets.append(enemy_bullet)

            # Determine a direção do tiro do inimigo
            if p_left_x > image_copas_rect.left:
                enemy_velocity_bullets_x.append(v_b_x)
            else:
                enemy_velocity_bullets_x.append(-v_b_x)

            # Defina a velocidade vertical
            enemy_velocity_bullets_y.append(5)

            last_enemy_bullet_time = current_time
        # Dentro do loop principal, após a lógica de movimentação das balas do jogador
        bullets_to_remove = []

        p_1_rect = pygame.Rect(p_left_x, p_top_x, p_1_colision_x_size, p_1_colision_y_size)

        for i, (enemy_bullet, enemy_v_bullet_x, enemy_v_bullet_y) in enumerate(
                zip(enemy_bullets, enemy_velocity_bullets_x, enemy_velocity_bullets_y)):
            enemy_bullet.x += enemy_v_bullet_x
            enemy_bullet.y += enemy_v_bullet_y

            if (enemy_bullet.y + enemy_bullet.height) >= scrn_y:
                # Adicione o índice à lista de balas para remover
                bullets_to_remove.append(i)


        # Remova as balas e velocidades correspondentes fora do loop
        for i in reversed(bullets_to_remove):
            enemy_bullets.pop(i)
            enemy_velocity_bullets_y.pop(i)
            enemy_velocity_bullets_x.pop(i)
        ia = 0
        for bullet in enemy_bullets:
            # Verifique as colisões com as laterais e o fundo da tela
            if bullet.x <= 0 or (bullet.x + bullet.width) >= scrn_x:
                enemy_velocity_bullets_x[ia] *= -1
                bounce_sound_effect.play()

        for bullet in bullets:
            if bullet.colliderect(image_espadas_rect):
                phase = 4
                player_shots = 5
                bullets.clear()
                enemy_bullets.clear()
                velocity_bullets_y.clear()
                velocity_bullets_x.clear()
                pygame.time.delay(200)
    if phase == 4:
        i = 0
        for bullet in bullets:
            if bullet.y < 300:
                if velocity_bullets_x[i] < 0:
                    image_ball_rect.x -= 2
                else:
                    image_ball_rect.x += 2
            i += 1
        if current_time - last_enemy_bullet_time > enemy_bullet_cooldown:
            # Adicione uma bala do inimigo
            enemy_bullet = pygame.Rect(image_copas_rect.centerx, image_copas_rect.centery, 8, 6)
            enemy_bullets.append(enemy_bullet)

            # Determine a direção do tiro do inimigo
            if p_left_x > image_copas_rect.left:
                enemy_velocity_bullets_x.append(v_b_x)
            else:
                enemy_velocity_bullets_x.append(-v_b_x)

            # Defina a velocidade vertical
            enemy_velocity_bullets_y.append(5)

            last_enemy_bullet_time = current_time
        # Dentro do loop principal, após a lógica de movimentação das balas do jogador
        bullets_to_remove = []

        p_1_rect = pygame.Rect(p_left_x, p_top_x, p_1_colision_x_size, p_1_colision_y_size)

        for i, (enemy_bullet, enemy_v_bullet_x, enemy_v_bullet_y) in enumerate(
                zip(enemy_bullets, enemy_velocity_bullets_x, enemy_velocity_bullets_y)):
            enemy_bullet.x += enemy_v_bullet_x
            enemy_bullet.y += enemy_v_bullet_y

            if (enemy_bullet.y + enemy_bullet.height) >= scrn_y:
                # Adicione o índice à lista de balas para remover
                bullets_to_remove.append(i)


        # Remova as balas e velocidades correspondentes fora do loop
        for i in reversed(bullets_to_remove):
            enemy_bullets.pop(i)
            enemy_velocity_bullets_y.pop(i)
            enemy_velocity_bullets_x.pop(i)
        ia = 0
        for bullet in enemy_bullets:
            # Verifique as colisões com as laterais e o fundo da tela
            if bullet.x <= 0 or (bullet.x + bullet.width) >= scrn_x:
                enemy_velocity_bullets_x[ia] *= -1
                bounce_sound_effect.play()

        for bullet in bullets:
            if bullet.colliderect(image_ball_rect):
                bullets.clear()
                enemy_bullets.clear()
                velocity_bullets_y.clear()
                velocity_bullets_x.clear()
                phase = 5
                victory_sound_effect.play()
                print("win")

    # checking the victory condition

    # clear screen

    screen.fill(COLOR_BLACK)
    # ball collision with the wall left and right
    i=0
    for bullet in bullets:
        if (bullet.x + bullet.width) >= 840 and velocity_bullets_x[i]>0:
            velocity_bullets_x[i] *= -1
            bounce_sound_effect.play()
        if bullet.x <= 0 and velocity_bullets_x[i]<0:
            velocity_bullets_x[i] *= -1
            bounce_sound_effect.play()
        i+=1
    # ball collision with the rectangle (phase 1)
    if phase == 1:
        retangle_1_pos_x += retangle_1_movimentation
        if retangle_1_pos_x < 0 or retangle_1_pos_x + retangle_1_x > scrn_x:
            retangle_1_movimentation *= -1
        retangle_1 = pygame.Rect(retangle_1_pos_x, retangle_1_pos_y, retangle_1_x, retangle_1_y)
        pygame.draw.rect(screen, COLOR_WHITE, retangle_1)
        i = 0
        for ball in bullets:
            if ball.colliderect(retangle_1):
                velocity_bullets_y[i] *= -1
                bounce_sound_effect.play()
                velocity_bullets_x[i] = random.choice([v_b_x, -v_b_x])
            i += 1


    # ball collision with the triangles (phase 2)
    elif phase == 2:
        i = 0
        for bullet, v_bullet_x, v_bullet_y in zip(bullets, velocity_bullets_x, velocity_bullets_y):
            if triangle_3_left_rect.colliderect(bullet):
                bullet.x = triangle_3_left_rect.x + triangle_3_left_rect.width + 1
                velocity_bullets_x[i] = v_b_x
                bounce_sound_effect.play()

            if triangle_3_right_rect.colliderect(bullet):
                bullet.x = triangle_3_right_rect.x - bullet.width - 1
                velocity_bullets_x[i] = -v_b_x
                bounce_sound_effect.play()

            if triangle_3_rect.colliderect(bullet):
                bullet.y = triangle_3_rect.y + triangle_3_rect.height + 1
                velocity_bullets_y[i] *= -1
                bounce_sound_effect.play()

            i += 1

    elif phase == 3:
            i = 0
            for bullet in bullets:
                if bullet.colliderect(retangle_3_l):
                    if bullet.x > retangle_3_l.x:
                        bullet.x = retangle_3_l.x + retangle_3_l.width + 1
                        velocity_bullets_x[i] = v_b_x
                        bounce_sound_effect.play()
                    else:
                        bullet.x = retangle_3_l.x - bullet.width - 1
                        velocity_bullets_x[i] = -v_b_x
                        bounce_sound_effect.play()

                    if velocity_bullets_y[i] < 0 and bullet.y > (retangle_3_l.y + (retangle_3_l.height/2)):
                        velocity_bullets_y[i] = v_b_x
                        bounce_sound_effect.play()
                    if velocity_bullets_y[i] > 0 and bullet.y < (retangle_3_l.y + (retangle_3_l.height/2)):
                        velocity_bullets_y[i] = -v_b_x
                        bounce_sound_effect.play()
                i+=1

            i = 0
            for bullet in bullets:
                if bullet.colliderect(retangle_3_r):
                    if bullet.x > retangle_3_r.x:
                        bullet.x = retangle_3_r.x + retangle_3_r.width + 1
                        velocity_bullets_x[i] = v_b_x
                        bounce_sound_effect.play()
                    else:
                        bullet.x = retangle_3_r.x - bullet.width - 1
                        velocity_bullets_x[i] = -v_b_x
                        bounce_sound_effect.play()

                    if velocity_bullets_y[i] < 0 and bullet.y > (retangle_3_r.y + (retangle_3_r.height / 2)):
                        velocity_bullets_y[i] = v_b_x
                        bounce_sound_effect.play()
                i += 1

            i = 0
            for bullet in bullets:
                if bullet.colliderect(square_3):
                    if bullet.x > square_3.x:
                        bullet.x = square_3.x + square_3.width + 1
                        velocity_bullets_x[i] = 3
                        bounce_sound_effect.play()
                    else:
                        bullet.x = square_3.x - bullet.width - 1
                        velocity_bullets_x[i] = -v_b_x
                        bounce_sound_effect.play()

                    if velocity_bullets_y[i] < 0 and bullet.y > (square_3.y + (square_3.height / 2)):
                        velocity_bullets_y[i] = v_b_x
                        bounce_sound_effect.play()
                    if velocity_bullets_y[i] > 0 and bullet.y < (square_3.y + (square_3.height / 2)):
                        velocity_bullets_y[i] = -v_b_x
                        bounce_sound_effect.play()
                i += 1
    elif phase == 4:
        i = 0
        for bullet in bullets:
            if bullet.colliderect(diagonal_bottom_left_rect):
                if bullet.x > diagonal_bottom_left_rect.x:
                    bullet.x = diagonal_bottom_left_rect.x + diagonal_bottom_left_rect.width + 1
                    velocity_bullets_x[i] = 3
                    bounce_sound_effect.play()
                else:
                    bullet.x = diagonal_bottom_left_rect.x - bullet.width - 1
                    velocity_bullets_x[i] = -v_b_x
                    bounce_sound_effect.play()

                if velocity_bullets_y[i] < 0 and bullet.y > (diagonal_bottom_left.y + (diagonal_bottom_left.height / 2)):
                    velocity_bullets_y[i] = v_b_x
                    bounce_sound_effect.play()
                if velocity_bullets_y[i] > 0 and bullet.y < (diagonal_bottom_left.y + (diagonal_bottom_left.height / 2)):
                    velocity_bullets_y[i] = -v_b_x
                    bounce_sound_effect.play()
            i += 1
        i = 0
        for bullet in bullets:
            if bullet.colliderect(diagonal_top_left_rect):
                if bullet.x > diagonal_top_left_rect.x:
                    bullet.x = diagonal_top_left_rect.x + diagonal_top_left_rect.width + 1
                    velocity_bullets_x[i] = 3
                    bounce_sound_effect.play()
                else:
                    bullet.x = diagonal_top_left_rect.x - bullet.width - 1
                    velocity_bullets_x[i] = -v_b_x
                    bounce_sound_effect.play()

                if velocity_bullets_y[i] < 0 and bullet.y > (
                        diagonal_top_left_rect.y + (diagonal_top_left_rect.height / 2)):
                    velocity_bullets_y[i] = v_b_x
                    bounce_sound_effect.play()
                if velocity_bullets_y[i] > 0 and bullet.y < (
                        diagonal_top_left_rect.y + (diagonal_top_left_rect.height / 2)):
                    velocity_bullets_y[i] = -v_b_x
                    bounce_sound_effect.play()
            i += 1

        i = 0
        for bullet in bullets:
            if bullet.colliderect(diagonal_bottom_right_rect):
                if bullet.x > diagonal_bottom_right_rect.x:
                    bullet.x = diagonal_bottom_right_rect.x + diagonal_bottom_right_rect.width + 1
                    velocity_bullets_x[i] = 3
                    bounce_sound_effect.play()
                else:
                    bullet.x = diagonal_bottom_right_rect.x - bullet.width - 1
                    velocity_bullets_x[i] = -v_b_x
                    bounce_sound_effect.play()

                if velocity_bullets_y[i] < 0 and bullet.y > (
                        diagonal_bottom_right_rect.y + (diagonal_bottom_right_rect.height / 2)):
                    velocity_bullets_y[i] = v_b_x
                    bounce_sound_effect.play()
                if velocity_bullets_y[i] > 0 and bullet.y < (
                        diagonal_bottom_right_rect.y + (diagonal_bottom_right_rect.height / 2)):
                    velocity_bullets_y[i] = -v_b_x
                    bounce_sound_effect.play()
            i += 1

        i = 0
        for bullet in bullets:
            if bullet.colliderect(diagonal_top_right_rect):
                if bullet.x > diagonal_top_right_rect.x:
                    bullet.x = diagonal_top_right_rect.x + diagonal_top_right_rect.width + 1
                    velocity_bullets_x[i] = 3
                    bounce_sound_effect.play()
                else:
                    bullet.x = diagonal_top_right_rect.x - bullet.width - 1
                    velocity_bullets_x[i] = -v_b_x
                    bounce_sound_effect.play()

                if velocity_bullets_y[i] < 0 and bullet.y > (
                        diagonal_top_right_rect.y + (diagonal_top_right_rect.height / 2)):
                    velocity_bullets_y[i] = v_b_x
                    bounce_sound_effect.play()
                if velocity_bullets_y[i] > 0 and bullet.y < (
                        diagonal_top_right.y + (diagonal_top_right.height / 2)):
                    velocity_bullets_y[i] = -v_b_x
                    bounce_sound_effect.play()
            i += 1


    # ball collision with the lower wall player 1
    i = 0
    for bullet, v_bullet_y in zip(bullets, velocity_bullets_y):
        if (bullet.y + bullet.height) >= 640:
            velocity_bullets_y[i] *= -1
            bounce_sound_effect.play()
        if (bullet.y + bullet.height) <= 0:
            velocity_bullets_y[i] *= -1
            bounce_sound_effect.play()
        i+=1
    # ball collision with the player 1


    # ball movement
    for bullet, v_bullet_y, v_bullet_x in zip(bullets, velocity_bullets_y, velocity_bullets_x):
        bullet.y += v_bullet_y
        bullet.x += v_bullet_x
        # Removes shots that leave the screen
        if bullet.y < 0:
            bullets.remove(bullet)
            velocity_bullets_y.remove(v_bullet_y)
            velocity_bullets_x.remove(v_bullet_x)
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
    # ia

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

    # player 2 collides with right wall

    # player 2 "Artificial Intelligence"

    # update shots hud
    shots_text = shots_font.render(str(player_shots), True, COLOR_WHITE, COLOR_BLACK)

    # drawing objects

    # phase 1 obstacle
    if phase == 1:
        screen.blit(image_copas, image_copas_rect)
        pygame.draw.rect(screen, COLOR_WHITE, retangle_1)
        pygame.draw.polygon(screen, COLOR_WHITE, [(p_top_x, p_top_y), (p_left_x, p_sides_y), (p_right_x, p_sides_y)])
        screen.blit(shots_text, shots_text_rect)
        screen.blit(player_life, (player_life_x, player_life_y))
        screen.blit(player_life, (player_life_x + 30, player_life_y))
        screen.blit(player_life, (player_life_x + 60, player_life_y))

    # phase 2 obstacles
    elif phase == 2:
        screen.blit(image_paus, image_paus_rect)
        screen.blit(triangle_3_mid, (triangle_3_mid_x, triangle_3_mid_y))
        screen.blit(triangle_3_left, (triangle_3_left_x, triangle_3_left_y))
        screen.blit(triangle_3_right, (triangle_3_right_x, triangle_3_right_y))
        pygame.draw.polygon(screen, COLOR_WHITE, [(p_top_x, p_top_y), (p_left_x, p_sides_y), (p_right_x, p_sides_y)])
        screen.blit(shots_text, shots_text_rect)
        screen.blit(player_life, (player_life_x, player_life_y))
        screen.blit(player_life, (player_life_x + 30, player_life_y))
        screen.blit(player_life, (player_life_x + 60, player_life_y))

    # phase 3 obstacles
    elif phase == 3:
        screen.blit(image_espadas, image_espadas_rect)
        pygame.draw.rect(screen, COLOR_WHITE, retangle_3_r)
        pygame.draw.rect(screen, COLOR_WHITE, retangle_3_l)
        pygame.draw.rect(screen, COLOR_WHITE, square_3)
        pygame.draw.polygon(screen, COLOR_WHITE, [(p_top_x, p_top_y), (p_left_x, p_sides_y), (p_right_x, p_sides_y)])
        screen.blit(shots_text, shots_text_rect)
        screen.blit(player_life, (player_life_x, player_life_y))
        screen.blit(player_life, (player_life_x + 30, player_life_y))
        screen.blit(player_life, (player_life_x + 60, player_life_y))

    # phase 4 obstacles
    elif phase == 4:
        screen.blit(image_ball, image_ball_rect)
        pygame.draw.rect(screen, COLOR_WHITE, square_4_mid)
        screen.blit(diagonal_bottom_left, (diagonal_bottom_left_x, diagonal_bottom_left_y))
        screen.blit(diagonal_top_right, (diagonal_top_right_x, diagonal_top_right_y))
        screen.blit(diagonal_top_left, (diagonal_top_left_x, diagonal_top_left_y))
        screen.blit(diagonal_bottom_right, (diagonal_bottom_right_x, diagonal_bottom_right_y))
        pygame.draw.polygon(screen, COLOR_WHITE, [(p_top_x, p_top_y), (p_left_x, p_sides_y), (p_right_x, p_sides_y)])
        screen.blit(shots_text, shots_text_rect)
        screen.blit(player_life, (player_life_x, player_life_y))
        screen.blit(player_life, (player_life_x + 30, player_life_y))
        screen.blit(player_life, (player_life_x + 60, player_life_y))

    elif phase == 5:
        screen.blit(victory_text, victory_text_rect)

    elif phase == 6:
        lost_sound_effect.play()
        screen.blit(defeat_text, defeat_text_rect)


    draw_bullets()
    draw_bullets_ia()
    # update screen
    pygame.display.flip()
    game_clock.tick(speed)

pygame.quit()
