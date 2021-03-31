import pygame, sys, random


class Ball:
    def __init__(self, ball_speed_x, ball_speed_y):
        self.ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
        self.vx = ball_speed_x
        self.vy = ball_speed_y

    def animate(self, screen_height, screen_width, player, opponent):
        self.ball.x += self.vx
        self.ball.y += self.vy

        if self.ball.top <= 0 or self.ball.bottom >= screen_height:
            self.vy *= -1
        if self.ball.left <= 0 or self.ball.right >= screen_width:
            self.restart()

        if self.ball.colliderect(player.player) or self.ball.colliderect(opponent.opponent):
            self.vx *= -1

    def restart(self):
        self.ball.center = (screen_width / 2, screen_height / 2)
        self.vx *= random.choice((1, -1))
        self.vy *= random.choice((1, -1))


class Player:
    def __init__(self, speed):
        self.player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
        self.speed = speed

    def animate(self, screen_width, screen_height):

        self.player.y += self.speed
        if self.player.top <= 0:
            self.player.top = 0
        if self.player.bottom >= screen_width:
            self.player.top = 0
        if self.player.bottom >= screen_height:
            self.player.bottom = screen_height


class Opponent():

    def __init__(self, speed):
        self.opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)
        self.speed = speed

    def opponent_AI(self, ball, screen_height):

        if self.opponent.centery > ball.ball.centery:
            self.opponent.top -= self.speed
        if self.opponent.centery < ball.ball.centery:
            self.opponent.top += self.speed

        if self.opponent.top <= 0:
            self.opponent.top = 0
        if self.opponent.bottom >= screen_height:
            self.opponent.bottom = screen_height


# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Game rectangles
ball = Ball(7 * random.choice((1, -1)), 7 * random.choice((1, -1)))
player = Player(0)
opponent = Opponent(8)

bg_color = pygame.Color('grey12')
light_gray = (200, 200, 200)

while True:
    # Inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player.speed += 7
            if event.key == pygame.K_UP:
                player.speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player.speed -= 7
            if event.key == pygame.K_UP:
                player.speed += 7

    ball.animate(screen_height, screen_width, player, opponent)
    player.animate(screen_width, screen_height)
    opponent.opponent_AI(ball,screen_height)


    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_gray, player.player)
    pygame.draw.rect(screen, light_gray, opponent.opponent)
    pygame.draw.ellipse(screen, light_gray, ball.ball)
    pygame.draw.aaline(screen, light_gray, (screen_width / 2, 0), (screen_width / 2, screen_height))

    # Updating the window
    pygame.display.flip()
    clock.tick(60)
