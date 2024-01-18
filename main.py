import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Configurações do jogo
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Poker Space")

# Cores
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Jogador
jogador_img = pygame.Surface((50, 50))
jogador_img.fill(vermelho)
jogador_rect = jogador_img.get_rect()
jogador_rect.center = (largura // 2, altura - 50)
jogador_velocidade = 5

# Inimigo
inimigo_img = pygame.Surface((50, 50))
inimigo_img.fill(branco)
inimigo_rect = inimigo_img.get_rect()
inimigo_rect.center = (largura // 2, 50)
inimigo_velocidade = 2

# Efeitos sonoros
tiro_sound = pygame.mixer.Sound("tiro.wav")
colisao_sound = pygame.mixer.Sound("colisao.wav")

def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movimentação do jogador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and jogador_rect.left > 0:
            jogador_rect.x -= jogador_velocidade
        if keys[pygame.K_RIGHT] and jogador_rect.right < largura:
            jogador_rect.x += jogador_velocidade

        # Movimentação do inimigo
        if inimigo_rect.x < jogador_rect.x:
            inimigo_rect.x += inimigo_velocidade
        elif inimigo_rect.x > jogador_rect.x:
            inimigo_rect.x -= inimigo_velocidade

        # Verifica colisão entre jogador e inimigo
        if jogador_rect.colliderect(inimigo_rect):
            colisao_sound.play()
            print("Você perdeu! Fim de jogo.")
            pygame.quit()
            sys.exit()

        # Atualizações da tela
        tela.fill((0, 0, 0))
        tela.blit(jogador_img, jogador_rect)
        tela.blit(inimigo_img, inimigo_rect)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
