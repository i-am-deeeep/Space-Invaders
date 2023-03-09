import pygame,time
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
            self.enemyY_mov=3.5
        if img==alien2:
            self.enemyY_mov=5.4
        if img==alien3:
            self.enemyY_mov=0.9
            self.enemyX_mov=4.3
        if img==alien4:
            self.enemyY_mov=1.2
            self.enemyX_mov=1.2
        if img==alien5:
            self.enemyY_mov=7.5
        if img==alien6:
            self.enemyY_mov=1.1



# Initialize the game
pygame.init()

# Create the screen
screen=pygame.display.set_mode((800,600))

# Background
background=pygame.image.load('background.png')

# Title and icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)


# Background music
mixer.music.load('background-music.wav')
mixer.music.play(-1)


# Player
playerImg=pygame.image.load('spaceship.png')
playerX=370
playerY=480
player_mov=0
def player(im,x,y):
    screen.blit(im,(x,y))
level=starting_level=9

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
bulletY_mov=28
fired=0
def bullet(x,y):
    screen.blit(bulletImg,(x,y))

# Enemy bullet
enemyBulletImg=pygame.image.load('enemy_bullet.png')
enemyBulletX=0
enemyBulletY=2000
enemyBulletY_mov=18
enemyBulletX_mov=18


# Function to handle all collisions
def isCollision(X1,Y1,X2,Y2,type):
    distance=math.sqrt(math.pow(X1-X2,2)+math.pow(Y1-Y2,2))
    #return False
    if type=="player":
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
score_font=pygame.font.Font('IndieFlower-Regular.ttf',32)
def showScore():
    score=score_font.render("Score : "+str(score_val),True,(255,255,255))
    screen.blit(score,(10,10))

# Game Over
isGameOver=False
over_font=pygame.font.Font('IndieFlower-Regular.ttf',80)
restart_font=pygame.font.Font('IndieFlower-Regular.ttf',32)
def gameOver():
    text1=over_font.render("GAME OVER",True,(255,0,0))
    text2=over_font.render("Your score: "+str(score_val),True,(20,253,199))
    text3=restart_font.render("Press R to restart the game",True,(20,253,199))
    screen.blit(text1,(210,170))
    screen.blit(text2,(210,275))
    screen.blit(text3,(210,390))

# Restart function
def restartGame():
    mixer.music.load('background-music.wav')
    mixer.music.play(-1)

    global playerImg,playerX,playerY,player_mov,level,bulletX,bulletY,bulletY_mov,fired,enemyBulletX,enemyBulletY,enemyBulletX_mov,enemyBulletY_mov,score_val,isGameOver,starting_level

    playerImg=pygame.image.load('spaceship.png')
    playerX=370
    playerY=480
    player_mov=0
    level=starting_level=8

    bulletX=0
    bulletY=2000
    bulletY_mov=18
    fired=0

    enemyBulletX=0
    enemyBulletY=2000
    enemyBulletY_mov=18
    enemyBulletX_mov=18

    score_val=0
    isGameOver=False



clock = pygame.time.Clock()

FPS = 60
######################################## Game loop ####################################################
running=True
while running:
    # RGB
    screen.fill((0,0,0))

    screen.blit(background,(0,0))

    # Limit framerate
    clock.tick(FPS)


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
            if event.key==pygame.K_SPACE and fired==0 and isGameOver==False:
                fired=1
                bulletY=480-18
                mixer.Sound('laser.wav').play()
            
            if event.key==pygame.K_r and isGameOver:
                restartGame()


    if isGameOver==False and player_mov!=0:
        playerX+=player_mov*6
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
        
        # alien6 feature
        if enemy_obj.img==alien6:
            if enemy_obj.enemyY<200 and random.randint(1,100)==1:
                y=2.4
                x=y*(enemy_obj.enemyX-playerX)/(enemy_obj.enemyY-playerY)
                enemy_list.append(Enemy(enemyBulletImg,enemy_obj.enemyX+24,enemy_obj.enemyY+48,x,y)) 

        # Game over logic
        if (enemy_obj.img!=enemyBulletImg and isCollision(playerX+16,playerY+16,enemy_obj.enemyX+16,enemy_obj.enemyY+16,"player")) or (enemy_obj.img==enemyBulletImg and isCollision(playerX+32,playerY+32,enemy_obj.enemyX+8,enemy_obj.enemyY+8,"enemy")):
            isGameOver=True
            mixer.music.stop()
            mixer.Sound('crash.wav').play()
            pygame.time.wait(1500)
            mixer.Sound('game-over.wav').play()
            for enemy_obj2 in enemy_list:
                del enemy_obj2
            enemy_list.clear()
            playerImg=pygame.image.load('spaceship_dead.png')
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
        if enemy_obj.img!=enemyBulletImg and isCollision(enemy_obj.enemyX+32,enemy_obj.enemyY+16,bulletX+8,bulletY+8,"enemy"):
            #mixer.Sound('explosion.wav').play()
            fired=0
            bulletY=2000
            score_val+=1
            del enemy_obj
            _=enemy_list.pop(i)
            continue


    # Enemy spawn
    level+=0.0001
    if (len(enemy_list)<8 and isGameOver==False and random.randint(1,1000)<=level):
        r=random.randint(1,6)
        img=9
        if r==1 and level>starting_level+0.6:
            img=alien1
        if r==2:
            img=alien2
        if r==3:
            img=alien3
        if r==4:
            img=alien4
        if r==5 and level>starting_level+0.3:
            img=alien5
        if r==6 and level>starting_level+1:
            img=alien6
        if img!=9:
            enemy_obj=Enemy(img,random.randint(0,736),-64,0,1)
            enemy_list.append(enemy_obj)



    if fired==0:
        bulletX=playerX+24

    player(playerImg,playerX,playerY)
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