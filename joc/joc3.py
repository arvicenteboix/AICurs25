import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
PADDLE_WIDTH = WIDTH * 0.2
PADDLE_HEIGHT = 10
BALL_SPEED = 5
PADDLE_SPEED = 2
FPS = 60
ANGLE = 45

win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Ball:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT - PADDLE_HEIGHT - BALL_RADIUS
        self.speed = BALL_SPEED
        self.angle = math.radians(-ANGLE)

    def move(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

    def draw(self):
        pygame.draw.circle(win, (255, 255, 255), (int(self.x), int(self.y)), BALL_RADIUS)

class Paddle:
    def __init__(self):
        self.x = WIDTH / 2 - PADDLE_WIDTH / 2
        self.y = HEIGHT - PADDLE_HEIGHT
        self.speed = PADDLE_SPEED

    def move(self, key):
        if key[pygame.K_LEFT] and self.x - self.speed > 0:
            self.x -= self.speed
        if key[pygame.K_RIGHT] and self.x + self.speed < WIDTH - PADDLE_WIDTH:
            self.x += self.speed

    def draw(self):
        pygame.draw.rect(win, (255, 255, 255), pygame.Rect(self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT))

def main():
    run = True
    ball = Ball()
    paddle = Paddle()
    space_pressed = False

    while run:
        clock.tick(FPS)
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                space_pressed = True

        if space_pressed:
            ball.move()
            if ball.y - BALL_RADIUS < 0 or (ball.y + BALL_RADIUS > paddle.y and paddle.x < ball.x < paddle.x + PADDLE_WIDTH):
                ball.angle = -ball.angle
            elif ball.x - BALL_RADIUS < 0 or ball.x + BALL_RADIUS > WIDTH:
                ball.angle = math.pi - ball.angle

        paddle.move(key)

        win.fill((0, 0, 0))
        ball.draw()
        paddle.draw()
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

