import pygame
from pygame.locals import *
from pygame import mixer
import random
import time
left=2
right=1
size=width,height=(650,650)
road_width=int(width/1.4)
roadmark_width=int(width/65)
left_lane=width/2-road_width/4
right_lane=width/2+road_width/4
speed=1
k=speed
p=0
pygame.init()
running=True
screen=pygame.display.set_mode(size)
pygame.display.set_caption("SAI's car game")
screen.fill((120,255,0))
pygame.draw.rect(screen,(50,50,50),(width/2-road_width/2,0,road_width,height))
pygame.draw.rect(screen,(255,255,255),(width/2-roadmark_width/2,0,roadmark_width,height))
pygame.draw.rect(screen,(255,255,255),(width/2-road_width/2+roadmark_width*2,0,roadmark_width,height))
pygame.draw.rect(screen,(255,255,255),(width/2+road_width/2-roadmark_width*3,0,roadmark_width,height))
pygame.display.update()
UserCar=pygame.image.load("Usercar1.png.png")
UserCar_location=UserCar.get_rect()
UserCar_location.center=left_lane,height*0.8
OtherCar=pygame.image.load("OtherCar1.png.png")
OtherCar_location=OtherCar.get_rect()
OtherCar_location.center=right_lane,height*0.2
count=0
score=0
crash=mixer.Sound("Crash.wav")
font=pygame.font.Font("freesansbold.ttf",32)
textX=width/2-roadmark_width/2-50
textY=0
def show_score(x,y,level_score):
    if(speed>k):
        level_score=1+p
    else:
        pass
    score_value = font.render("Score: " + str(score), True, (253,238,0))
    level_value = font.render("Level: "+str(level_score),True,(253,238,0))
    screen.blit(score_value, (x,y))
    screen.blit(level_value, (width/2-roadmark_width/2-50,33))
    pygame.display.update()
over_font=pygame.font.Font('freesansbold.ttf',32)
mixer.music.load("Background Music.wav")
mixer.music.play(-1)
while running:
    count+=1
    if count==5000:
        speed+=0.25
        count=0
        p+=1
    OtherCar_location[1]+=speed
    if OtherCar_location[1]>height:
        if random.randint(0,1)==0:
            OtherCar_location.center=left_lane,-200
            score+=1
        else:
            OtherCar_location.center=right_lane,-200
            score+=1
    if UserCar_location[0]==OtherCar_location[0] and OtherCar_location[1]>UserCar_location[1]-250:
        mixer.music.stop()
        crash.play()
        time.sleep(1)
        break
    for event in pygame.event.get():
        if event.type==QUIT:
            running = False
        if event.type==KEYDOWN:
            if event.key in [K_a,K_LEFT]:
                if(left<=1):
                    UserCar_location=UserCar_location.move([-int(road_width/2),0])
                    left+=1
                    right-=1
                else:
                    pass
            if event.key in [K_d,K_RIGHT]:
                if(right<=1):
                    UserCar_location=UserCar_location.move([int(road_width/2),0])
                    right+=1
                    left-=1
                else:
                    pass
    pygame.draw.rect(screen, (50, 50, 50), (width / 2 - road_width / 2, 0, road_width, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 - roadmark_width / 2, 0, roadmark_width, height))
    pygame.draw.rect(screen, (255, 255, 255),
                     (width / 2 - road_width / 2 + roadmark_width * 2, 0, roadmark_width, height))
    pygame.draw.rect(screen, (255, 255, 255),
                     (width / 2 + road_width / 2 - roadmark_width * 3, 0, roadmark_width, height))
    screen.blit(UserCar,UserCar_location)
    screen.blit(OtherCar, OtherCar_location)
    show_score(textX, textY,1)
    pygame.display.update()
mixer.music.stop()
crash.play()
over_value = font.render("GAME OVER..." , True, (253,238,0))
screen.blit(over_value,(width/2-roadmark_width/2-100,width/2-roadmark_width/2-50))
pygame.display.update()
time.sleep(1)
pygame.quit()