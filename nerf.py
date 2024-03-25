import pygame
import random
import math
pygame.init()
screen=pygame.display.set_mode((800,600))
#IMAGES:
pygame.display.set_caption("NERF WAR")
icon=pygame.image.load("space-invaders (1).png")
pygame.display.set_icon(icon)
background=pygame.image.load("ahmed.png")
spaceshipimg=pygame.image.load("spaceship.png")
#FOR ALIEN:
alienimg=[]
alienx=[]
alieny=[]
alienspeedx=[]
alienspeedy=[]
no_of_aliens=6
for i in range(no_of_aliens):
  alienimg.append(pygame.image.load("alien.png"))
  alienx.append(random.randint(0,736))
  alieny.append(random.randint(30,150))
  alienspeedx.append(1)
  alienspeedy.append(40)
score=0
#FOR BULLET:
bulletimg=pygame.image.load("bullet.png")
check=False
bulletx=386
bullety=450

#FOR SPACESHIP:
spaceshipx=386
spaceshipy=490
changex=0
def player():
    screen.blit(spaceshipimg,(spaceshipx,spaceshipy))

font=pygame.font.SysFont("Arial",32,"bold")
#for scoreboard function:
def score_text():
    img=font.render(f"Score = {score}",True,"yellow")
    screen.blit(img,(10,10))
#FOR COLLISION FUNCTION:



#FOR ENDING FUNCTION:
font_gameover=pygame.font.SysFont("Arial",64,"bold")
def game_over():
    img_gameover = font_gameover.render("GAME OVER", True, "yellow")
    screen.blit(img_gameover, (200, 250))



running=True
while running:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                changex=-5
            if event.key==pygame.K_RIGHT:
                changex=5
            if event.key==pygame.K_SPACE:
                if check==False:
                 check=True
                 bulletx=spaceshipx+16


        if event.type==pygame.KEYUP:
            changex=0
    spaceshipx+=changex
    # spaceshipx-=changex
    if spaceshipx<0:
        spaceshipx=0
    elif spaceshipx>=736:
        spaceshipx=736
    for i in range(no_of_aliens):
      if alieny[i] > 420:
        for j in range(no_of_aliens):
           alieny[j] = 2000
           game_over()
           break
      alienx[i]+=alienspeedx[i]
      if alienx[i]<=0:
        alienspeedx[i]=1
        alieny[i]+=alienspeedy[i]
      if alienx[i]>=736:
        alienspeedx[i]=-1
        alieny[i]+=alienspeedy[i]
        distance = math.sqrt(math.pow(bulletx - alienx[i], 2) + math.pow(bullety - alieny[i], 2))
        if distance < 27:
          bullety = 480
          check = False
          alienx[i] = random.randint(0, 736)
          alieny[i] = random.randint(30, 150)
          score += 1
        screen.blit(alienimg[i], (alienx[i], alieny[i]))
    if bullety<=0:
        bullety=490
        check=False
    if check:
      screen.blit(bulletimg, (bulletx, bullety))
      bullety-=5


    player()

    score_text()

    pygame.display.update()


