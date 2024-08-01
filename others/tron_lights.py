import sys

import pygame
from loguru import logger

# Inicializar Pygame
pygame.init()

# Definir cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TRON_BLUE = (0, 170, 255)
TRON_RED = (255, 0, 0)
LIGHT_WALL_COLOR = (255, 255, 0)
GRID_COLOR = (20, 20, 20)  # Cor sutil para a grade

# Definir tamanho da arena
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MAX_LIGHT_WALL_LENGTH = 400
CELL_SIZE = 10  # Aumentado para tornar a grade mais visível
SPEED = 2  # Aumentado para manter a jogabilidade fluida
GRID_SIZE = 10  # Tamanho das células da grade


class LightWallSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, owner, color=LIGHT_WALL_COLOR):
        super().__init__()
        self.color = color
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.alpha = 255
        self.decrement = self.alpha / MAX_LIGHT_WALL_LENGTH
        self.owner = owner
        self.update_image()

    def update(self):
        self.alpha -= self.decrement
        if self.alpha <= 0:
            self.kill()
        else:
            self.update_image()

    def update_image(self):
        color = self.color + (int(self.alpha),)
        self.image.fill(color)


class LightCycleSprite(pygame.sprite.Sprite):
    def __init__(self, name, x, y, color, walls_group):
        super().__init__()
        self.name = name
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.color = color
        self.direction = 'right'
        self.walls_group = walls_group
        self.speed = SPEED

    def __str__(self):
        return self.name

    def update(self):
        self.move()
        self.create_light_wall()

    def move(self):
        if self.direction == 'right':
            self.rect.x += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed

        # Verificar colisão com as bordas da tela
        if not (0 <= self.rect.x < SCREEN_WIDTH and 0 <= self.rect.y < SCREEN_HEIGHT):
            self.kill()

    def create_light_wall(self):
        wall = LightWallSprite(self.rect.x, self.rect.y, self)
        self.walls_group.add(wall)

    def set_direction(self, direction):
        self.direction = direction


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tron Game")
        self.clock = pygame.time.Clock()
        self.reset_game()

    def reset_game(self):
        self.walls_group = pygame.sprite.Group()
        self.players_group = pygame.sprite.Group()
        self.arena_walls = []
        self.player1 = LightCycleSprite(name="Flint", x=100, y=200, color=TRON_BLUE, walls_group=self.walls_group)
        self.player2 = LightCycleSprite(name="Sark", x=500, y=200, color=TRON_RED, walls_group=self.walls_group)
        self.players_group.add(self.player1, self.player2)
        self.running = True
        self.player1_direction = 'right'
        self.player2_direction = 'left'
        self.game_over_message = None

    def run(self):
        while True:
            self.game_loop()
            if not self.show_game_over_screen():
                break
        pygame.quit()
        sys.exit()

    def game_loop(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player1_direction = 'up'
        elif keys[pygame.K_s]:
            self.player1_direction = 'down'
        elif keys[pygame.K_a]:
            self.player1_direction = 'left'
        elif keys[pygame.K_d]:
            self.player1_direction = 'right'

        if keys[pygame.K_UP]:
            self.player2_direction = 'up'
        elif keys[pygame.K_DOWN]:
            self.player2_direction = 'down'
        elif keys[pygame.K_LEFT]:
            self.player2_direction = 'left'
        elif keys[pygame.K_RIGHT]:
            self.player2_direction = 'right'

        self.player1.set_direction(self.player1_direction)
        self.player2.set_direction(self.player2_direction)

    def update(self):
        self.players_group.update()
        self.walls_group.update()

        # Verificar colisão entre os jogadores
        if pygame.sprite.collide_rect(self.player1, self.player2):
            logger.warning("Colisão entre os jogadores!")
            self.player1.kill()
            self.player2.kill()
            self.game_over("Empate!")

        # Verificar colisão com as paredes da arena
        for wall in self.arena_walls:
            if self.player1.rect.colliderect(wall):
                logger.warning(f"O player {self.player1} colidiu com a arena.")
                self.player1.kill()
                self.game_over(f"Player {self.player2} venceu!")
            if self.player2.rect.colliderect(wall):
                logger.warning(f"O player {self.player2} colidiu com a arena.")
                self.player2.kill()
                self.game_over(f"Player {self.player1} venceu!")

        # Verificar colisão com as paredes de luz do oponente
        for wall in self.walls_group:
            if wall.owner != self.player1 and self.player1.rect.colliderect(wall.rect):
                logger.warning(f"O player {self.player1} colidiu com a parede de luz do oponente.")
                self.player1.kill()
                self.game_over(f"Player {self.player2} venceu!")
            if wall.owner != self.player2 and self.player2.rect.colliderect(wall.rect):
                logger.warning(f"O player {self.player2} colidiu com a parede de luz do oponente.")
                self.player2.kill()
                self.game_over(f"Player {self.player1} venceu!")

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_grid()
        self.draw_arena()
        self.walls_group.draw(self.screen)
        self.players_group.draw(self.screen)
        pygame.display.flip()

    def draw_grid(self):
        for x in range(0, SCREEN_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

    def draw_arena(self):
        pygame.draw.rect(self.screen, WHITE, (0, 0, SCREEN_WIDTH, 20))
        pygame.draw.rect(self.screen, WHITE, (0, SCREEN_HEIGHT - 20, SCREEN_WIDTH, 20))
        pygame.draw.rect(self.screen, WHITE, (0, 0, 20, SCREEN_HEIGHT))
        pygame.draw.rect(self.screen, WHITE, (SCREEN_WIDTH - 20, 0, 20, SCREEN_HEIGHT))

        # Adicionar colisão à arena
        self.arena_walls = [
            pygame.Rect(0, 0, SCREEN_WIDTH, 20),
            pygame.Rect(0, SCREEN_HEIGHT - 20, SCREEN_WIDTH, 20),
            pygame.Rect(0, 0, 20, SCREEN_HEIGHT),
            pygame.Rect(SCREEN_WIDTH - 20, 0, 20, SCREEN_HEIGHT)
        ]

    def game_over(self, message):
        self.running = False
        self.game_over_message = message

    def show_game_over_screen(self):
        self.screen.fill(BLACK)
        font = pygame.font.Font(None, 36)

        # Exibir mensagem de fim de jogo
        text = font.render(self.game_over_message, True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50))
        self.screen.blit(text, text_rect)

        # Exibir instruções para reiniciar ou sair
        restart_text = font.render("Pressione R para reiniciar ou Q para sair", True, WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))
        self.screen.blit(restart_text, restart_rect)

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset_game()
                        return True
                    elif event.key == pygame.K_q:
                        return False
            self.clock.tick(60)

        return False

    def restart_game(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset_game()
                        return True
                    elif event.key == pygame.K_q:
                        return False
        return False


if __name__ == "__main__":
    Game().run()
