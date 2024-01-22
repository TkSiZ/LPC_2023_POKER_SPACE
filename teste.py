import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Colisão entre Rect e Mask")

# Função para carregar uma imagem e criar uma máscara
def load_and_mask(image_path):
    image = pygame.image.load(image_path)
    mask = pygame.mask.from_surface(image)
    return image, mask

# Carrega a imagem e cria a máscara
image, mask = load_and_mask("assets/heart_enemy.png")

# Define a posição inicial do retângulo
rect = pygame.Rect(100, 100, image.get_width(), image.get_height())

# Velocidade de movimento
speed = 2

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimenta o retângulo
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect.x -= speed
    if keys[pygame.K_RIGHT]:
        rect.x += speed
    if keys[pygame.K_UP]:
        rect.y -= speed
    if keys[pygame.K_DOWN]:
        rect.y += speed

    # Verifica colisão entre o retângulo e a máscara
    offset = (rect.x, rect.y)
    if mask.overlap(pygame.mask.from_surface(pygame.Surface(rect.size).convert_alpha()), offset):
        print("Colisão!")

    # Atualiza a tela
    screen.fill((0, 0, 0))  # Preenche o fundo com branco
    screen.blit(image, rect.topleft)  # Desenha a imagem no retângulo

    pygame.display.flip()  # Atualiza a tela
