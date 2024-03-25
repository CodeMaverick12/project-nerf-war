import pygame
import random
import math
from pygame import mixer


mixer.init()
mixer.music.load("titanium-170190.mp3")
mixer.music.play(-1)
pygame.init()


screen = pygame.display.set_mode((800, 600))

# IMAGES:
pygame.display.set_caption("NERF WAR")
icon = pygame.image.load("space-invaders (1).png")
pygame.display.set_icon(icon)
background = pygame.image.load("ahmed.png")
spaceshipimg = pygame.image.load("spaceship.png")

# FOR ALIEN:
alienimg = []
alienx = []
alieny = []
alienspeedx = []
alienspeedy = []
no_of_aliens = 6

for i in range(no_of_aliens):
    alienimg.append(pygame.image.load("alien.png"))
    alienx.append(random.randint(0, 736))
    alieny.append(random.randint(30, 150))
    alienspeedx.append(1)
    alienspeedy.append(40)

score = 0

# FOR BULLET:
bulletimg = pygame.image.load("bullet.png")
check = False
bulletx = 386
bullety = 450
bullet_speed = 5  # Add bullet speed

# FOR SPACESHIP:
spaceshipx = 386
spaceshipy = 490
changex = 0

def player():
    screen.blit(spaceshipimg, (spaceshipx, spaceshipy))

font = pygame.font.SysFont("Arial", 32, "italic")

# for scoreboard function:
def score_text():
    img = font.render(f"Score = {score}", True, "white")
    screen.blit(img, (10, 10))

# FOR COLLISION FUNCTION:
def collision(bullet_x, bullet_y, object_x, object_y):
    distance = math.sqrt((bullet_x - object_x) ** 2 + (bullet_y - object_y) ** 2)
    return distance < 27


# FOR ENDING FUNCTION:
font_gameover = pygame.font.SysFont("Arial", 64, "italic")

def game_over():
    img_gameover = font_gameover.render("GAME OVER", True, "white")
    screen.blit(img_gameover, (200, 250))

running = True

while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changex = -5
            if event.key == pygame.K_RIGHT:
                changex = 5
            if event.key == pygame.K_SPACE:
                bulletsound=mixer.Sound("shoot02wav-14562.mp3")
                bulletsound.play()

                if not check:
                    check = True
                    bulletx = spaceshipx + 16

        if event.type == pygame.KEYUP:
            changex = 0

    spaceshipx += changex

    if spaceshipx < 0:
        spaceshipx = 0
    elif spaceshipx >= 736:
        spaceshipx = 736

    for i in range(no_of_aliens):
        if alieny[i] > 420:
            for j in range(no_of_aliens):
                alieny[j] = 2000
            game_over()
            break

        alienx[i] += alienspeedx[i]
        if alienx[i] <= 0:
            alienspeedx[i] = 1
            alieny[i] += alienspeedy[i]
        elif alienx[i] >= 736:
            alienspeedx[i] = -1
            alieny[i] += alienspeedy[i]

        # Check for collision
        collision_occurred = collision(bulletx, bullety, alienx[i], alieny[i])
        if collision_occurred:
            explotion = mixer.Sound("explosion-6801.mp3")
            explotion.play()

            bullety = 480
            check = False
            alienx[i] = random.randint(0, 736)
            alieny[i] = random.randint(30, 150)
            score += 1

        screen.blit(alienimg[i], (alienx[i], alieny[i]))

    if bullety <= 0:
        bullety = 490
        check = False

    if check:
        screen.blit(bulletimg, (bulletx, bullety))
        bullety -= bullet_speed

    player()
    score_text()

    pygame.display.update()

pygame.quit()
