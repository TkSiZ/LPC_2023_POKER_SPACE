#Atividade 0010 -

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
# victory text

# lost text





# phase 1 enemy(copas)
image_copas = pygame.image.load("assets/copas.png")
image_copas_rect = image_copas.get_rect()
image_copas_rect.topleft = (scrn_x/2 - (image_copas_rect.width/2), 0)
image_copas_mask = pygame.mask.from_surface(image_copas)


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
triangle_3_left_x = scrn_x / 2 - 450
triangle_3_left_y = scrn_y / 2 + 85
triangle_3_left_rect = triangle_3_mid.get_rect(topleft=(triangle_3_mid_x, triangle_3_mid_y))
triangle_3_left_mask = pygame.mask.from_surface(triangle_3_left)




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
# shot_sound_effect = pygame.mixer.Sound('...')
# bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')

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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                p_1_move_left = False
            if event.key == pygame.K_RIGHT:
                p_1_move_right = False

    # checking the victory condition

    # clear screen

    screen.fill(COLOR_BLACK)

    # ball collision with the lower/upper wall

    # ball collision with the player 1

    # ball collision with the enemy

    # ball movement

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
        screen.blit(image_copas, image_copas_rect);
        pygame.draw.rect(screen, COLOR_WHITE, retangle_1)

    # phase 2 obstacles
    elif phase == 2:

        screen.blit(triangle_3_mid, (triangle_3_mid_x, triangle_3_mid_y))
        screen.blit(triangle_3_left, (triangle_3_left_x, triangle_3_left_y))
        #screen.blit(triangle_right, (triangle_right_x, triangle_right_y))

    # phase 3 obstacles
    #elif phase == 3:

        # pygame.draw.rect(screen, COLOR_WHITE, retangle_3_r)
        # pygame.draw.rect(screen, COLOR_WHITE, retangle_3_l)
        # pygame.draw.rect(screen, COLOR_WHITE, square_3)

    # phase 4 obstacles
    else:
        pygame.draw.rect(screen, COLOR_WHITE, square_4_mid)
        screen.blit(diagonal_bottom_left, (diagonal_bottom_left_x, diagonal_bottom_left_y))
        screen.blit(diagonal_top_right, (diagonal_top_right_x, diagonal_top_right_y))
        screen.blit(diagonal_top_left, (diagonal_top_left_x, diagonal_top_left_y))
        screen.blit(diagonal_bottom_right, (diagonal_bottom_right_x, diagonal_bottom_right_y))

    # update screen
    pygame.display.flip()
    game_clock.tick(speed)

pygame.quit()
