import sys

import pygame

# Configurações iniciais do jogo
WIDTH, HEIGHT = 640, 480
BALL_SIZE = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
FPS = 60

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Inicializa o jogo
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Cria a bola e os paddles
ball = pygame.Rect(WIDTH / 2, HEIGHT / 2, BALL_SIZE, BALL_SIZE)
paddle1 = pygame.Rect(0, HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - PADDLE_WIDTH, HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Variáveis de jogo
ball_x_speed = 5
ball_y_speed = 5

# scores
score1, score2 = 0, 0

while True:
    # Trata os eventos do usuário
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move os paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.y -= 5
    if keys[pygame.K_s]:
        paddle1.y += 5
    if keys[pygame.K_UP]:
        paddle2.y -= 5
    if keys[pygame.K_DOWN]:
        paddle2.y += 5

    # Move a bola
    ball.x += ball_x_speed
    ball.y += ball_y_speed

    # Verifica se a bola atingiu uma parede ou um paddle
    if ball.y < 0 or ball.y > HEIGHT - BALL_SIZE:
        ball_y_speed = -ball_y_speed
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_x_speed = -ball_x_speed

    if ball.x < 0:  # Se a bola sair pela lateral esquerda
        score2 += 1
        ball.x = paddle2.x - PADDLE_WIDTH - 10
        ball.y = paddle2.y
        ball_x_speed = ball_x_speed
    elif ball.x > WIDTH - BALL_SIZE:  # Se a bola sair pela lateral direita
        score1 += 1
        ball.x = paddle1.x + PADDLE_WIDTH + 1
        ball.y = paddle1.y
        ball_x_speed = ball_x_speed

    # Desenha o jogo
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, ball)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)

    font = pygame.font.Font(None, 36)
    text_surface = font.render(
        f"Score: {score1} - {score2}"
        f" | 1: {paddle1.x}, {paddle1.y} | 2: {paddle2.x}, {paddle2.y} | "
        f"ball: {ball.x}, {ball.y} "
        "".strip(),
        True, WHITE
    )
    screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() / 2, 10))

    # Atualiza a tela
    pygame.display.flip()
    clock.tick(FPS)
