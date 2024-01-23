#Atividade 0010 -

import random
import pygame

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)

player_lifes = 1
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

# bullets
bullets = []
velocity_bullets_x = []
velocity_bullets_y = []
deteccao_anterior = []

# victory text

# lost text

# Function to draw the shots on the screen
def draw_bullets():
    for bullet in bullets:
        pygame.draw.rect(screen, COLOR_WHITE, bullet)

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
image_ball = pygame.image.load("assets/copas.png")
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
# victory_sound_effect = pygame.mixer.Sound('...')
# lost_sound_effect = pygame.mixer.Sound('...')
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
mask_aux = pygame.mask.from_surface(image_ball)
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
phase = 2
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
                # Adds a shot to the list when the spacebar is pressed
            if event.key == pygame.K_SPACE and player_shots > 0:
                player_shots -= 1
                bullet = pygame.Rect(p_top_x + p_1_colision_x_size // 50 - 4, p_sides_y, 8, 6)
                bullets.append(bullet)
                velocity_bullets_y.append(-5)
                velocity_bullets_x.append(0)
                deteccao_anterior.append(False)
                shot_sound_effect.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                p_1_move_left = False
            if event.key == pygame.K_RIGHT:
                p_1_move_right = False

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
        i=0
        for bullet in bullets:
            if bullet.colliderect(retangle_1):
                velocity_bullets_y[i]*=-1
                bounce_sound_effect.play()
                velocity_bullets_x[i] = random.choice([3, -3])
                pygame.time.delay(50)

            i+=1
    # ball collision with the triangles (phase 2)
    elif phase == 2:
        i = 0
        # middle triangle
        for bullet in bullets:
            if bullet.colliderect(triangle_3_rect) and (not deteccao_anterior[i]):

                deteccao_anterior[i] = True
                velocity_bullets_y[i] *= -1
                bounce_sound_effect.play()
                if velocity_bullets_x[i] == 0:
                    velocity_bullets_x[i] = random.choice([3, -3])
                else:
                    velocity_bullets_x[i]*=random.choice([1, -1])
            elif (not bullet.colliderect(triangle_3_rect)) and deteccao_anterior[i]:
                deteccao_anterior[i] = False
            i += 1
        # left triangle
        i = 0
        for bullet in bullets:
            if bullet.colliderect(triangle_3_left_rect) and (not deteccao_anterior[i]):

                deteccao_anterior[i] = True
                velocity_bullets_y[i] *= -1
                bounce_sound_effect.play()
                if velocity_bullets_x[i] == 0:
                    velocity_bullets_x[i] = random.choice([3, -3])
                else:
                    velocity_bullets_x[i] *= random.choice([1, -1])
            elif (not bullet.colliderect(triangle_3_left_rect)) and deteccao_anterior[i]:
                deteccao_anterior[i] = False
            i += 1
        # right triangle
        i=0
        for bullet in bullets:
            if bullet.colliderect(triangle_3_right_rect) and (not deteccao_anterior[i]):

                deteccao_anterior[i] = True
                velocity_bullets_y[i] *= -1
                bounce_sound_effect.play()
                if velocity_bullets_x[i] == 0:
                    velocity_bullets_x[i] = random.choice([3, -3])
                else:
                    velocity_bullets_x[i] *= random.choice([1, -1])
            elif (not bullet.colliderect(triangle_3_right_rect)) and deteccao_anterior[i]:

                deteccao_anterior[i] = False
            i += 1
    
    elif phase == 3:
        i = 0
        for bullet in bullets:
            if bullet.colliderect(triangle_3_rect) and (not deteccao_anterior[i]):

                deteccao_anterior[i] = True
                velocity_bullets_y[i] *= -1
                bounce_sound_effect.play()
                if velocity_bullets_x[i] == 0:
                    velocity_bullets_x[i] = random.choice([3, -3])
                else:
                    velocity_bullets_x[i] *= random.choice([1, -1])
            elif (not bullet.colliderect(triangle_3_rect)) and deteccao_anterior[i]:
                deteccao_anterior[i] = False
            i += 1
    # ball collision with the lower/upper wall phase 1
    # ball collision with the lower wall player 1
    i = 0
    for bullet, v_bullet_y in zip(bullets, velocity_bullets_y):
        if (bullet.y + bullet.height) >= 640:
            velocity_bullets_y[i] *= -1
            #velocity_bullets_x[i] = random.choice([2, -2])
        if (bullet.y + bullet.height) <= 0:
            velocity_bullets_y[i] *= -1
            #velocity_bullets_x[i] = random.choice([2, -2])
        i+=1
    # ball collision with the player 1

    # ball collision with the enemy

    # ball movement
    for bullet, v_bullet_y, v_bullet_x in zip(bullets, velocity_bullets_y, velocity_bullets_x):
        bullet.y += v_bullet_y
        bullet.x += v_bullet_x
        # Removes shots that leave the screen
        #if bullet.y < 0:
            #bullets.remove(bullet)
            #velocity_bullets_y.remove(v_bullet_y)
            #velocity_bullets_x.remove(v_bullet_x)
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

    # player 2 collides with right wall

    # player 2 "Artificial Intelligence"

    # update shots hud
    shots_text = shots_font.render(str(player_shots), True, COLOR_WHITE, COLOR_BLACK)

    # drawing objects
    pygame.draw.polygon(screen, COLOR_WHITE, [(p_top_x, p_top_y), (p_left_x, p_sides_y), (p_right_x, p_sides_y)])
    screen.blit(shots_text, shots_text_rect)
    screen.blit(player_life, (player_life_x, player_life_y))
    screen.blit(player_life, (player_life_x + 30, player_life_y))
    screen.blit(player_life, (player_life_x + 60, player_life_y))
    # phase 1 obstacle
    if phase == 1:
        screen.blit(image_copas, image_copas_rect)
        pygame.draw.rect(screen, COLOR_WHITE, retangle_1)

    # phase 2 obstacles
    elif phase == 2:
        screen.blit(image_paus, image_paus_rect)
        screen.blit(triangle_3_mid, (triangle_3_mid_x, triangle_3_mid_y))
        screen.blit(triangle_3_left, (triangle_3_left_x, triangle_3_left_y))
        screen.blit(triangle_3_right, (triangle_3_right_x, triangle_3_right_y))

    # phase 3 obstacles
    elif phase == 3:
        screen.blit(image_espadas, image_espadas_rect)

        pygame.draw.rect(screen, COLOR_WHITE, retangle_3_r)
        pygame.draw.rect(screen, COLOR_WHITE, retangle_3_l)
        pygame.draw.rect(screen, COLOR_WHITE, square_3)

    # phase 4 obstacles
    else:
        screen.blit(image_ball, image_ball_rect)
        pygame.draw.rect(screen, COLOR_WHITE, square_4_mid)
        screen.blit(diagonal_bottom_left, (diagonal_bottom_left_x, diagonal_bottom_left_y))
        screen.blit(diagonal_top_right, (diagonal_top_right_x, diagonal_top_right_y))
        screen.blit(diagonal_top_left, (diagonal_top_left_x, diagonal_top_left_y))
        screen.blit(diagonal_bottom_right, (diagonal_bottom_right_x, diagonal_bottom_right_y))
    draw_bullets()
    # update screen
    pygame.display.flip()
    game_clock.tick(speed)

pygame.quit()
