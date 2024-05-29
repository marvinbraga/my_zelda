import sys

import pygame


class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_size(self) -> tuple:
        return self.width, self.height


class Score:
    def __init__(self, game, color=(255, 255, 255)):
        self.color = color
        self.game = game
        self.score1 = 0
        self.score2 = 0

    def draw(self):
        font = pygame.font.Font(None, 36)
        text_surface = font.render(
            f"Score: {self.score1} - {self.score2}",
            True, self.color
        )
        self.game.screen.blit(text_surface, (self.game.size.width // 2 - text_surface.get_width() / 2, 10))


class Ball(pygame.Rect):
    def __init__(self, game, color=(0, 255, 0)):
        self.game = game
        w, h = self.game.size.get_size()
        self.square = 20
        super().__init__(w / 2, h / 2, self.square, self.square)
        self.color = color
        self.x_speed = 5
        self.y_speed = 5

    def update(self, **kwargs):
        self.x += self.x_speed
        self.y += self.y_speed

        w, h = self.game.size.get_size()
        if self.y < 0 or self.y > h - self.square:
            self.y_speed *= -1
        if self.colliderect(self.game.paddle1) or self.colliderect(self.game.paddle2):
            self.x_speed *= -1


class Paddle(pygame.Rect):
    def __init__(self, x, y, key_up=pygame.K_UP, key_down=pygame.K_DOWN, color=(255, 255, 255)):
        super().__init__(x, y, 10, 100)
        self._key_up = key_up
        self._key_down = key_down
        self.color = color

    def update(self, **kwargs):
        keys = pygame.key.get_pressed()
        if keys[self._key_up]:
            self.y -= 5
        if keys[self._key_down]:
            self.y += 5


class Game:
    def __init__(self):
        pygame.init()
        self.size = Size(800, 600)
        w, h = self.size.get_size()
        self.screen = pygame.display.set_mode((w, h))
        self.clock = pygame.time.Clock()
        self.background_color = (0, 0, 0)

        self.score = Score(game=self)
        self.ball = Ball(game=self)
        self.paddle1 = Paddle(0, h / 2 - 50, pygame.K_w, pygame.K_s)
        self.paddle2 = Paddle(w - 10, h / 2 - 50)

    def check_point(self):
        if self.ball.x < 0:
            self.score.score2 += 1
            self.ball.x = self.paddle2.x - self.ball.square - 1
            self.ball.y = self.paddle2.y
            self.ball.x_speed *= -1
        elif self.ball.x > self.size.width - self.ball.square:
            self.score.score1 += 1
            self.ball.x = self.paddle1.x + self.paddle1.width
            self.ball.y = self.paddle1.y
            self.ball.x_speed *= -1

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.ball.update()
        self.paddle1.update()
        self.paddle2.update()
        self.check_point()

    def draw(self):
        self.screen.fill(self.background_color)
        pygame.draw.rect(self.screen, self.ball.color, self.ball)
        pygame.draw.rect(self.screen, self.paddle1.color, self.paddle1)
        pygame.draw.rect(self.screen, self.paddle2.color, self.paddle2)
        self.score.draw()

    def run(self):
        while True:
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    pong = Game()
    pong.run()
