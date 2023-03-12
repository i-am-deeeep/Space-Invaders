import pygame
import random
import math
from pygame import mixer

class Bullet:
    def __init__(self,img,bulletX,bulletY,bulletX_mov,bulletY_mov):
        self.img=img
        self.bulletX=bulletX
        self.bulletY=bulletY
        self.bulletX_mov=bulletX_mov
        self.bulletY_mov=bulletY_mov
class Enemy:
    def __init__(self,img,enemyX,enemyY,enemyX_mov,enemyY_mov):
        self.img=img
        self.enemyX=enemyX
        self.enemyY=enemyY
        self.enemyX_mov=enemyX_mov
        self.enemyY_mov=enemyY_mov

        if img==alien1:
            self.enemyY_mov=3.7
        if img==alien2:
            self.enemyY_mov=6
        if img==alien3:
            self.enemyY_mov=1
            self.enemyX_mov=4.6 if random.randint(1,2)==1 else -4.6
        if img==alien4:
            self.enemyY_mov=1.3
            self.enemyX_mov=1.3 if random.randint(1,2)==1 else -1.3
        if img==alien5:
            self.enemyY_mov=8
        if img==alien6:
            self.enemyY_mov=1.3



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
game_start=0


# Player
playerImg=pygame.image.load('spaceship.png')
playerX=370
playerY=480
player_mov=0
def player(im,x,y):
    screen.blit(im,(x,y))
level=starting_level=9
ticks=0
noEnemy=True
noOverheatSpell=False
noOverheatSpell_finish_frame=0

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
bullet_list=[]
overheat=False
overheat_finish_frame=0
gameframe=0
last5secs_list=[0]
last2secs_list=[0]
bulletImg=pygame.image.load('bullet.png')
def bullet(img,x,y):
    screen.blit(img,(x,y))

# Enemy bullet
enemyBulletImg=pygame.image.load('enemy_bullet.png')
enemyBulletX=0
enemyBulletY=2000
enemyBulletY_mov=18
enemyBulletX_mov=18

# Box
boxImg=pygame.image.load('giftbox.png')
boxX=0
boxY=-100
boxY_mov=6
def box(x,y):
    screen.blit(boxImg,(x,y))

# Coin
coinImg=pygame.image.load('coin.png')
coinX=0
coinY=-100
coinY_mov=4
def coin(x,y):
    screen.blit(coinImg,(x,y))

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

# Game start function
def startingPage():
    dy=-30
    reversey=False
    pause=True
    while pause:
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pause=False

        logo=pygame.image.load('logopp3.png')
        screen.blit(logo,(200,50))
        pause_font=pygame.font.Font('IndieFlower-Regular.ttf',40)
        font2=pygame.font.Font('IndieFlower-Regular.ttf',30)
        text0=font2.render("How to play?",True,(255,0,255))
        texthsc=font2.render("Highscore : "+str(high_score_val),True,(255,43,104))
        text1=font2.render("-> Use left and right arrow keys to move",True,(255,255,0))
        text2=font2.render("-> Use space to shoot the aliens to score",True,(255,255,0))
        text4=pause_font.render("Hit space to start the game",True,(20,253,199))
        screen.blit(text0,(150,220))
        screen.blit(texthsc,(580,220))
        screen.blit(text1,(114,260))
        screen.blit(text2,(114,300))
        if reversey==False:
            if dy<30:
                dy+=0.4
            else:
                reversey=True
        else:
            if dy>-30:
                dy-=0.4
            else:
                reversey=False
        screen.blit(text4,(180,500+dy))
        clock.tick(FPS)
        pygame.display.update()


# Score
score_val=0
hisc1=open("exee.txt","r")
highscore=hisc1.read()
hisc1.close()
high_score_val=int(highscore)
highscore_before_start=high_score_val
score_font=pygame.font.Font('IndieFlower-Regular.ttf',32)
def showScore():
    score=score_font.render("Score : "+str(score_val),True,(255,255,255))
    global high_score_val
    if score_val>high_score_val:
        hisc2=open("exee.txt","w")
        high_score_val=score_val 
        hisc2.write(str(score_val))
        hisc2.close()
    high_score=score_font.render("High Score : "+str(high_score_val),True,(255,255,255))
    screen.blit(score,(10,10))
    screen.blit(high_score,(10,50))

# Overheat function
overheat_dy=8
overheat_y1=700
overheat_y2=750
overheat_rev=False
def showOverheat():
    global overheat_dy,overheat_y1,overheat_y2,overheat_rev
    if overheat_rev==False:
        if overheat_dy>0:
            overheat_dy-=0.07
        else:
            overheat_rev=True
    else:
        if overheat_dy<8:
            overheat_dy+=0.07 
    
    overheat_y1-=overheat_dy
    overheat_y2-=overheat_dy
    overheat_font1=pygame.font.Font('IndieFlower-Regular.ttf',50)
    overheat_font2=pygame.font.Font('IndieFlower-Regular.ttf',25)
    text1=overheat_font1.render("OVERHEAT!!",True,(255,0,0))
    text2=overheat_font2.render("slow down firing rate",True,(255,0,0))
    screen.blit(text1,(300,overheat_y1))
    screen.blit(text2,(300,overheat_y2))
def resetOverheatVariables():
    global overheat_dy,overheat_y1,overheat_y2,overheat_rev
    overheat_dy=8
    overheat_y1=700
    overheat_y2=750
    overheat_rev=False

# noOverheatSpell function
noOverheatSpell_dy=8
noOverheatSpell_y1=700
noOverheatSpell_y2=750
noOverheatSpell_rev=False
def showNoOverheatSpell():
    global noOverheatSpell_dy,noOverheatSpell_y1,noOverheatSpell_y2,noOverheatSpell_rev
    if noOverheatSpell_rev==False:
        if noOverheatSpell_dy>0:
            noOverheatSpell_dy-=0.07
        else:
            noOverheatSpell_rev=True
    else:
        if noOverheatSpell_dy<8:
            noOverheatSpell_dy+=0.07 
    
    noOverheatSpell_y1-=noOverheatSpell_dy
    noOverheatSpell_y2-=noOverheatSpell_dy
    noOverheatSpell_font1=pygame.font.Font('IndieFlower-Regular.ttf',50)
    noOverheatSpell_font2=pygame.font.Font('IndieFlower-Regular.ttf',25)
    text1=noOverheatSpell_font1.render("No overheat",True,(255,255,255))
    text2=noOverheatSpell_font2.render("for next 15 seconds",True,(255,255,255))
    screen.blit(text1,(300,noOverheatSpell_y1))
    screen.blit(text2,(300,noOverheatSpell_y2))
def resetNoOverheatSpellVariables():
    global noOverheatSpell_dy,noOverheatSpell_y1,noOverheatSpell_y2,noOverheatSpell_rev
    noOverheatSpell_dy=8
    noOverheatSpell_y1=700
    noOverheatSpell_y2=750
    noOverheatSpell_rev=False
# Game Over function
isGameOver=False
over_font=pygame.font.Font('IndieFlower-Regular.ttf',80)
restart_font=pygame.font.Font('IndieFlower-Regular.ttf',32)
def gameOver():
    d=[[20,False],[253,False],[199,False]]
    frame=0
    mus=0
    ds=0
    dx=0
    pause=True
    while pause:
        frame+=1
        screen.blit(background,(0,0))
        t=tuple(i[0] for i in d)
        if frame>120 and highscore_before_start<score_val:
            if mus==0:
                d[0][0]=255
                d[1][0]=255
                d[2][0]=0
                mixer.Sound('highscore.wav').play()
            mus+=1
            if ds<80:
                ds+=1
            if dx<160:
                dx+=2
            highscore_font=pygame.font.Font('IndieFlower-Regular.ttf',ds)
            for ind,[i,r] in enumerate(d):
                if r==False:
                    if i<255:
                        d[ind][0]+=10
                    else:
                        d[ind][0]-=10
                        d[ind][1]=True
                    if d[ind][0]>255:
                        d[ind][0]=255
                if r==True:
                    if i>0:
                        d[ind][0]-=10
                    else:
                        d[ind][0]+=10
                        d[ind][1]=False
                    if d[ind][0]<0:
                        d[ind][0]=0
            text222=highscore_font.render("NEW HIGHSCORE!!",True,t)
            screen.blit(text222,(290-dx,270))
            
        player(playerImg,playerX,playerY)
        text1=over_font.render("GAME OVER",True,(255,0,0))
        text2=over_font.render("Your score:",True,(20,253,199))
        text22=over_font.render(str(score_val),True,t)
        text3=restart_font.render("Press R to go again!",True,(20,253,199))
        screen.blit(text1,(200,90))
        screen.blit(text2,(160,190))
        screen.blit(text22,(590,190))
        screen.blit(text3,(230,450))
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_r:
                    pause=False
                    restartGame()
        pygame.display.update()

# Restart function
def restartGame():
    mixer.music.load('background-music.wav')
    mixer.music.play(-1)

    global boxY,coinY,last2secs_list,last5secs_list,overheat,highscore_before_start,playerImg,playerX,playerY,player_mov,level,bulletX,bulletY,bulletY_mov,fired,enemyBulletX,enemyBulletY,enemyBulletX_mov,enemyBulletY_mov,score_val,isGameOver,starting_level

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
    highscore_before_start=high_score_val
    isGameOver=False
    overheat=False
    last5secs_list=[]
    last2secs_list=[]
    resetOverheatVariables()
    boxY=-100
    coinY=-100
    resetNoOverheatSpellVariables()

# Pause function
def pauseGame():
    dx=800
    pause=True
    while pause:
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    pause=False

        if dx>-500:
            dx-=2
        else:
            dx=800
        pause_font=pygame.font.Font('IndieFlower-Regular.ttf',40)
        pauseText=pause_font.render("Press P to resume the game",True,(20,253,199))
        screen.blit(pauseText,(0+dx,200))
        showScore()
        clock.tick(FPS)
        pygame.display.update()

clock = pygame.time.Clock()

FPS = 60
######################################## Game loop ####################################################
running=True
while running:

    screen.blit(background,(0,0))

    # Limit framerate
    clock.tick(FPS)


    # Starting page
    if game_start==0:
        game_start=1
        startingPage()
        mixer.Sound('startgame.wav').play()
        mixer.music.play(-1)

    gameframe+=1

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
            
            if event.key==pygame.K_p and isGameOver==False:
                pauseGame()                              
    if pygame.key.get_pressed()[pygame.K_SPACE] and gameframe>25 and (overheat==False or noOverheatSpell==True) and isGameOver==False and ((len(last2secs_list)>0 and gameframe-last2secs_list[-1]>12) or (len(last2secs_list))==0):
        bullet_list.append(Bullet(bulletImg,playerX+24,480,0,15))
        last5secs_list.append(gameframe)
        last2secs_list.append(gameframe)
        mixer.Sound('laser.wav').play()

    # Overheat logic
    for ind,item in enumerate(last5secs_list):
        if gameframe-item>60*5:
            _=last5secs_list.pop(ind)
    for ind,item in enumerate(last2secs_list):
        if gameframe-item>60*2:
            _=last2secs_list.pop(ind)
    if overheat==False and noOverheatSpell==False and len(last5secs_list)>15 and len(last2secs_list)>7:
        overheat=True
        mixer.Sound('overheat.wav').play()
        overheat_finish_frame=gameframe+60*5
    if overheat==True and gameframe>=overheat_finish_frame:
        overheat=False
        resetOverheatVariables()


    for i,enemy_obj in enumerate(enemy_list):

        # alien1 feature
        if enemy_obj.img==alien1:
            if random.randint(1,100)<=2:
                temp=enemy_obj.enemyX_mov
                enemy_obj.enemyX_mov=enemy_obj.enemyY_mov  if random.randint(1,2)==1 else -1*enemy_obj.enemyY_mov
                enemy_obj.enemyY_mov=temp if temp>0 else temp*(-1)
        
        # alien5 feature
        if enemy_obj.img==alien5:
            if enemy_obj.enemyY>390:
                enemy_obj.enemyY_mov=0.4
        
        # alien6 feature
        if enemy_obj.img==alien6:
            if enemy_obj.enemyY<250 and random.randint(1,1000)<=15:
                y=3
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
            for bullet_obj2 in bullet_list:
                del bullet_obj2
            bullet_list.clear()
            playerImg=pygame.image.load('spaceship_dead.png')
            break

        enemy_obj.enemyX+=enemy_obj.enemyX_mov
        enemy_obj.enemyY+=enemy_obj.enemyY_mov
        if enemy_obj.enemyX<0 or enemy_obj.enemyX>736:
            enemy_obj.enemyX= 0 if enemy_obj.enemyX<0 else 736
            enemy_obj.enemyX_mov*=-1
        
        enemy(enemy_obj.img,enemy_obj.enemyX,enemy_obj.enemyY)
        
        if enemy_obj.enemyY>600:
            del enemy_obj
            _=enemy_list.pop(i)
            continue

         
        for ib,bullet_obj in enumerate(bullet_list):
            # Collision of enemy with bullet
            if enemy_obj.img!=enemyBulletImg and isCollision(enemy_obj.enemyX+32,enemy_obj.enemyY+16,bullet_obj.bulletX+8,bullet_obj.bulletY+8,"enemy"): 
                score_val+=1
                del bullet_obj
                __=bullet_list.pop(ib)
                del enemy_obj
                _=enemy_list.pop(i)
                break

            
    for ib,bullet_obj in enumerate(bullet_list):
        bullet_obj.bulletX-=bullet_obj.bulletX_mov
        bullet_obj.bulletY-=bullet_obj.bulletY_mov
        bullet(bullet_obj.img,bullet_obj.bulletX,bullet_obj.bulletY)
        if bullet_obj.bulletX<-16 or bullet_obj.bulletX>800 or bullet_obj.bulletY<-16:
            del bullet_obj
            __=bullet_list.pop(ib)
        


    # player movement
    if isGameOver==False and player_mov!=0:
        playerX+=player_mov*8
        if playerX<0:
            playerX=0
        if playerX>736:
            playerX=736
    player(playerImg,playerX,playerY)

    # Box and coin spawn
    if boxY+coinY==-200 and random.randint(1,1000)<=1:
        if random.randint(1,10)<=2:
            boxX=random.randint(0,768)
            boxY=-32
        else:
            coinX=random.randint(0,768)
            coinY=-32

    # Enemy spawn
    level+=0.0001
    if len(enemy_list)==1:
        noEnemy=True
    if noEnemy:
        ticks+=1
    if (isGameOver==False and ticks>=120) or (len(enemy_list)<8 and isGameOver==False and random.randint(1,1000)<=level):
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
            mixer.Sound('explosion.wav').play()
        if img!=9:
            ticks=0
            noEnemy=False
            enemy_obj=Enemy(img,random.randint(0,736),-64,0,1)
            enemy_list.append(enemy_obj)

    # Box update
    if boxY!=-100:
        boxY+=boxY_mov
        if boxY>600:
            boxY=-100
    box(boxX,boxY)
    
    # Coin update
    if coinY!=-100:
        coinY+=coinY_mov
        if coinY>600:
            coinY=-100
    coin(coinX,coinY)

    # Coin collision
    if isCollision(playerX,playerY,coinX,coinY,"player"):
        score_val+=1
        coinY=-100
        mixer.Sound('coin_collect.wav').play()

    # Box collision
    if isCollision(playerX,playerY,boxX,boxY,"player"):
        boxY=-100
        mixer.Sound('box_collect.mp3').play()
        ra=random.randint(1,1)
        if ra==1 and noOverheatSpell==False:
            noOverheatSpell=True
            noOverheatSpell_finish_frame=gameframe+60*15
    if gameframe>=noOverheatSpell_finish_frame:
        noOverheatSpell=False
        resetNoOverheatSpellVariables()
     

    if isGameOver:
        gameOver()
    else:
        showScore()
    
    if overheat:
        showOverheat()
    
    if noOverheatSpell:
        showNoOverheatSpell()
    
    pygame.display.update()

