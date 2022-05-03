import pygame
import time
import random
import sys
import cv2
import pyttsx3
import mediapipe as mp


# windowsize
WINDOW_W=1000
WINDOW_H=702
WINDOW_SIZE=(WINDOW_W,WINDOW_H)
size_x_cursor=70



pygame.init()
clock = pygame.time.Clock()
pygame.font.init()

engine=pyttsx3.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("ארץ עיר")
bk_image=pygame.image.load("back.jpg")
write_image=pygame.image.load("images.jpg")
cursor_image=pygame.image.load("הורדה.png")
bk_image=pygame.transform.scale(bk_image,(1000,702))
write_image=pygame.transform.scale(write_image,(1000,220))
cursor_image=pygame.transform.scale(cursor_image,(size_x_cursor,40))
cap=cv2.VideoCapture(0)

# clock=pygame.time.clock()
# https://www.yo-yoo.co.il/data/game/solutions/

latters=["א","ב","ג","ד","ה","ו","ז","ח","ט","י","כ","ל","מ","נ","ס","ע","פ","צ","ק","ר","ש","ת"]
Latters=["א","ב","ג","ד","ה","ו","ז","ח","ט","י","כ","ל","מ","נ","ס","ע","פ","צ","ק","ר","ש","ת","ף","ץ","ך","ם"]
myfont=pygame.font.SysFont("fhir",30,70)
# lottery_latter=random.choice(latters)
# latter_font=myfont.render(str(lottery_latter),True,(0,0,0))
current_time=0
latter_font=[]
start=True
mouse_position=(0,0)
ארץ=()
space_touch=0


a=1
while start:
 work,frame=cap.read()
 if a==1:   
   engine.setProperty('rate',0)  
   engine.say("thanks for choosing my game,now the rules ")  
   engine.runAndWait()
   a+=1
 screen.blit(bk_image,(0,0))
#  screen.blit(write_image,(0,500))
 for event in pygame.event.get():
    print (event)
    if event.type==pygame.QUIT:
      start=False
    if event.type==pygame.MOUSEMOTION:
        mouse_position = pygame.mouse.get_pos()
    elif event.type==pygame.KEYDOWN:
      if event.key==pygame.K_SPACE:
        pygame.time.get_ticks()
        lottery_latter=random.choice(latters)
        latters_font =myfont.render(str(lottery_latter),True,(110,220,34))
        latter_font.append(latters_font)
        latters.remove(lottery_latter)
        space_touch+=1
 if space_touch>0:  
    screen.blit(latter_font[0],(922,220))
      
 screen.blit(cursor_image,(mouse_position[0]-size_x_cursor/2,mouse_position[1]-10))
 
 
 pygame.display.flip()
 




pygame.quit
