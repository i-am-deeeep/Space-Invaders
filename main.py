import pygame
import random
import math
from pygame import mixer


class Enemy:
    def __init__(self,img,enemyX,enemyY,enemyX_mov,enemyY_mov):
        self.img=img
        self.enemyX=enemyX
        self.enemyY=enemyY
        self.enemyX_mov=enemyX_mov
        self.enemyY_mov=enemyY_mov

        if img==alien1:
            self.enemyY_mov=3
        if img==alien2:
            self.enemyY_mov=5
        if img==alien3:
            self.enemyY_mov=0.5
            self.enemyX_mov=4
        if img==alien4:
            self.enemyY_mov=1
            self.enemyX_mov=1
        if img==alien5:
            self.enemyY_mov=7
        if img==alien6:
            pass



# Initialize the game
pygame.init()

# Create the screen
screen=pygame.display.set_mode((800,600))

# Background
background=pygame.image.load('background.png')

# Background music
mixer.music.load('background-music.wav')
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
level=8

# Enemy
enemy_list=[]
alien1=pygame.image.load('alien1.png')
alien2=pygame.image.load('alien2.png')
alien3=pygame.image.load('alien3.png')
alien4=pygame.image.load('alien4.png')
alien5=pygame.image.load('alien5.png')
alien6=pygame.image.load('alien6.png')
def enemy(img,x,y):
    screen.blit(img,(x,y))

# Bullet
bulletImg=pygame.image.load('bullet.png')
bulletX=0
bulletY=2000
bulletY_mov=18
fired=0
def bullet(x,y):
    screen.blit(bulletImg,(x,y))


# Function to handle all collisions
def isCollision(X1,Y1,X2,Y2,type):
    distance=math.sqrt(math.pow(X1-X2,2)+math.pow(Y1-Y2,2))
    if type=="player":
        return False
        if distance<=45:
            return True
        else:
            return False
    elif type=="enemy":
        if distance<=34:
            return True
        else:
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
            if event.key==pygame.K_SPACE and fired==0:
                fired=1
                bulletY=480-18
                mixer.Sound('laser.wav').play()
    
    if player_mov!=0:
        playerX+=player_mov*5
        if playerX<0:
            playerX=0
        if playerX>736:
            playerX=736
    


    for i,enemy_obj in enumerate(enemy_list):

        # alien1 feature
        if enemy_obj.img==alien1:
            if random.randint(1,100)==1:
                temp=enemy_obj.enemyX_mov
                enemy_obj.enemyX_mov=enemy_obj.enemyY_mov
                enemy_obj.enemyY_mov=temp if temp>0 else temp*(-1)
        
        # alien5 feature
        if enemy_obj.img==alien5:
            if enemy_obj.enemyY>400:
                enemy_obj.enemyY_mov=0.1

        # Game over logic
        if isCollision(playerX+16,playerY+16,enemy_obj.enemyX+16,enemy_obj.enemyY+16,"player"):
            isGameOver=True
            for enemy_obj2 in enemy_list:
                del enemy_obj2
            enemy_list.clear()
            break

        enemy_obj.enemyX+=enemy_obj.enemyX_mov
        enemy_obj.enemyY+=enemy_obj.enemyY_mov
        if enemy_obj.enemyX<0 or enemy_obj.enemyX>736:
            enemy_obj.enemyX= 0 if enemy_obj.enemyX<0 else 736
            enemy_obj.enemyX_mov*=-1
        
        enemy(enemy_obj.img,enemy_obj.enemyX,enemy_obj.enemyY)
        
        if enemy_obj.enemyY>800:
            del enemy_obj
            _=enemy_list.pop(i)
            continue

        # Collision of enemy with bullet
        if isCollision(enemy_obj.enemyX+32,enemy_obj.enemyY+16,bulletX+8,bulletY+8,"enemy"):
            #mixer.Sound('explosion.wav').play()
            fired=0
            bulletY=2000
            score_val+=1
            del enemy_obj
            _=enemy_list.pop(i)
            continue



    # Enemy spawn
    level+=0.0001
    # if level>11:
    #     print("11 hua")
    if isGameOver==False and random.randint(1,1000)<=level:
        r=random.randint(1,6)
        if r==1:
            img=alien1
        if r==2:
            img=alien2
        if r==3:
            img=alien3
        if r==4:
            img=alien4
        if r==5:
            img=alien5
        if r==6:
            img=alien6
        enemy_obj=Enemy(img,random.randint(0,736),-44,0,1)
        enemy_list.append(enemy_obj)



    if fired==0:
        bulletX=playerX+24

    player(playerX,playerY)
    if fired==1:
        bullet(bulletX,bulletY)
        bulletY-=bulletY_mov
        if bulletY<-32:
            fired=0
            bulletY=2000

    if isGameOver:
        gameOver()
    else:
        showScore()
    
    pygame.display.update()