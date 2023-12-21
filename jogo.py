import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Configurações
largura_tela = 600
altura_tela = 400
tamanho_celula = 20

# Criação da tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Cobrinha em Python')

# Carregamento das imagens
imagem_cobrinha = pygame.image.load('cobrinha.png')  # Substitua 'cobrinha.png' pelo nome da sua imagem
imagem_comida = pygame.image.load('comida.png')  # Substitua 'comida.png' pelo nome da sua imagem

# Escala das imagens
escala_cobrinha = (2 * tamanho_celula, 2 * tamanho_celula)
escala_comida = (tamanho_celula, tamanho_celula)

# Configurações da cobrinha
cobrinha = [(100, 100), (90, 100), (80, 100)]
direcao = 'DIREITA'
velocidade = 20

# Configurações da comida
comida = (random.randrange(1, (largura_tela // tamanho_celula)) * tamanho_celula,
          random.randrange(1, (altura_tela // tamanho_celula)) * tamanho_celula)

# Carregamento do fundo
imagem_fundo = pygame.image.load('fundo.png')  # Substitua 'fundo.png' pelo nome da sua imagem
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura_tela, altura_tela))

# Função para desenhar a cobrinha
def desenhar_cobrinha():
    for segmento in cobrinha:
        tela.blit(pygame.transform.scale(imagem_cobrinha, escala_cobrinha), (segmento[0], segmento[1]))

# Função para desenhar a comida
def desenhar_comida():
    tela.blit(pygame.transform.scale(imagem_comida, escala_comida), (comida[0], comida[1]))

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and direcao != 'BAIXO':
                direcao = 'CIMA'
            elif evento.key == pygame.K_DOWN and direcao != 'CIMA':
                direcao = 'BAIXO'
            elif evento.key == pygame.K_LEFT and direcao != 'DIREITA':
                direcao = 'ESQUERDA'
            elif evento.key == pygame.K_RIGHT and direcao != 'ESQUERDA':
                direcao = 'DIREITA'

    # Atualização da posição da cobrinha
    if direcao == 'CIMA':
        cobrinha = [(cobrinha[0][0], cobrinha[0][1] - velocidade)] + cobrinha[:-1]
    elif direcao == 'BAIXO':
        cobrinha = [(cobrinha[0][0], cobrinha[0][1] + velocidade)] + cobrinha[:-1]
    elif direcao == 'ESQUERDA':
        cobrinha = [(cobrinha[0][0] - velocidade, cobrinha[0][1])] + cobrinha[:-1]
    elif direcao == 'DIREITA':
        cobrinha = [(cobrinha[0][0] + velocidade, cobrinha[0][1])] + cobrinha[:-1]

    # Verificação de colisão com a parede
    if (
        cobrinha[0][0] < 0 or cobrinha[0][0] >= largura_tela or
        cobrinha[0][1] < 0 or cobrinha[0][1] >= altura_tela
    ):
        pygame.quit()
        sys.exit()

    # Verificação de colisão com a comida
if cobrinha[0] == comida:
    comida = (random.randrange(1, (largura_tela // tamanho_celula)) * tamanho_celula,
              random.randrange(1, (altura_tela // tamanho_celula)) * tamanho_celula)
    cobrinha.append(cobrinha[-1])


    # Verificação de colisão da cobrinha com ela mesma
    if cobrinha[0] in cobrinha[1:]:
        pygame.quit()
        sys.exit()

    # Desenho do fundo
    tela.blit(imagem_fundo, (0, 0))

    # Desenho da cobrinha e da comida
    desenhar_cobrinha()
    desenhar_comida()

    # Atualização da janela
    pygame.display.flip()

    # Controle de frames por segundo
    pygame.time.Clock().tick(10)
