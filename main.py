import pygame
import random
import math
from pygame import mixer

# Initialize the game
pygame.init()

# Create the screen
screen=pygame.display.set_mode((800,600))

# Background
background=pygame.image.load('background.png')

# Background music
mixer.music.load('background_music.wav')
mixer.music.play(-1)

# Title and icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Player
playerImg=pygame.image.load('spaceship.png')
playerX=370
playerY=480
player_mov=0
def player(x,y):
    screen.blit(playerImg,(x,y))

# Enemy
enemyX=[]
enemyY=[]
enemyX_mov=[]
enemyY_mov=[]
num_of_enemies=6
for i in range(num_of_enemies):
    enemyX.append(random.randint(0,736))
    enemyY.append(-44)
    enemyX_mov.append(4)
    enemyY_mov.append(10)
enemyImg=pygame.image.load('enemy.png')
def enemy(x,y):
    screen.blit(enemyImg,(x,y))

# Bullet
bulletImg=pygame.image.load('bullet.png')
bulletX=0
bulletY=480-18
bulletY_mov=10
fired=0
def bullet(x,y):
    screen.blit(bulletImg,(x,y))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
    if distance<32:
        return True
    return False

# Score
score_val=0
score_font=pygame.font.Font('freesansbold.ttf',32)
def showScore():
    score=score_font.render("Score : "+str(score_val),True,(255,255,255))
    screen.blit(score,(10,10))

# Game Over
isGameOver=False
over_font=pygame.font.Font('freesansbold.ttf',64)
def gameOver():
    text1=over_font.render("GAME OVER :/",True,(255,255,255))
    text2=over_font.render("Your score: "+str(score_val),True,(255,255,255))
    screen.blit(text1,(200,250))
    screen.blit(text2,(200,320))

# Game loop
running=True
while running:
    # RGB
    screen.fill((0,0,0))

    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                player_mov=-1
            if event.key==pygame.K_RIGHT:
                player_mov=1
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT and player_mov==-1:
                player_mov=0
            if event.key==pygame.K_RIGHT and player_mov==1:
                player_mov=0

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                fired=1
                bulletY=480-18
                mixer.Sound('laser.wav').play()
    
    if player_mov!=0:
        playerX+=player_mov*4
        if playerX<0:
            playerX=0
        if playerX>736:
            playerX=736
    
    for i in range(num_of_enemies):

        # Game over logic
        if enemyY[i]>=435 and abs(enemyX[i]-playerX)<5:
            isGameOver=True
            for j in range(num_of_enemies):
                enemyY[j]=800

        enemyX[i]+=enemyX_mov[i]
        if enemyX[i]<0:
            enemyX[i]=0
            enemyX_mov[i]*=-1
            enemyY[i]+=enemyY_mov[i]
        if enemyX[i]>736:
            enemyX[i]=736
            enemyX_mov[i]*=-1
            enemyY[i]+=enemyY_mov[i]
        # Collision
        collision=isCollision(enemyX[i]+16,enemyY[i]+16,bulletX+8,bulletY+8)
        if collision:
            mixer.Sound('explosion.wav').play()
            fired=0
            bulletY=2000
            score_val+=1
            enemyX[i]=random.randint(0,736)
            enemyY[i]=-44
        enemy(enemyX[i],enemyY[i])


    if fired==0:
        bulletX=playerX+16



    player(playerX,playerY)
    if fired==1:
        bullet(bulletX,bulletY)
        bulletY-=10
        if bulletY<-32:
            fired=0
            bulletY=2000

    if isGameOver:
        gameOver()
    showScore()
    pygame.display.update()