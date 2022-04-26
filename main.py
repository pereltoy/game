from turtle import screensize,circle, window_height
from pickle import TRUE
import pygame
import time
import random
import sys

# windowsize
WINDOW_W=1000
WINDOW_H=702
WINDOW_SIZE=(WINDOW_W,WINDOW_H)
size_x_cursor=70


pygame.init()
clock = pygame.time.Clock()
pygame.font.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("ארץ עיר")
bk_image=pygame.image.load("back.jpg")
write_image=pygame.image.load("images.jpg")
cursor_image=pygame.image.load("הורדה.png")
bk_image=pygame.transform.scale(bk_image,(1000,500))
write_image=pygame.transform.scale(write_image,(1000,220))
cursor_image=pygame.transform.scale(cursor_image,(size_x_cursor,40))


# clock=pygame.time.clock()
# https://www.yo-yoo.co.il/data/game/solutions/

latters=["א","ב","ג","ד","ה","ו","ז","ח","ט","י","כ","ל","מ","נ","ס","ע","פ","צ","ק","ר","ש","ת"]
Latters=["א","ב","ג","ד","ה","ו","ז","ח","ט","י","כ","ל","מ","נ","ס","ע","פ","צ","ק","ר","ש","ת","ף","ץ","ך","ם"]
myfont=pygame.font.SysFont("fhir",30,50)
lottery_latter=random.choice(latters)
# latter_font=myfont.render(str(lottery_latter),True,(0,0,0))
current_time=0
latter_font=[]
start=True



mouse_position=(0,0)
ארץ=()
space_touch=0


while start:
 screen.blit(bk_image,(0,0))
 screen.blit(write_image,(0,500))
 for event in pygame.event.get():
    print (event)
    if event.type==pygame.QUIT:
      start=False
      (805, 146)
      (899, 185)
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
    screen.blit(latter_font[0],(592,410))
      
 screen.blit(cursor_image,(mouse_position[0]-size_x_cursor/2,mouse_position[1]-10))
 
 
 pygame.display.flip()
 
down=42
left=110
position=[158,200,242,284,326,368,410,452]
position2=[922,855,812,702,592,482,372,262,152]
a=158
for i in range(7):
    for t in range(8):
        print(position2[t],position[i])


(922, 200)pygame.quit
922,158
855,158
812,158
702,158
592,158
482,158
372,158
262,158
922,200
855,200
812,200
702,200
592,200
482,200
372,200
262,200
922,242
855,242
812,242
702,242
592,242
482,242
372,242
262,242
922,284
855,284
812,284
702,284
592,284
482,284
372,284
262,284
922,326
855,326
812,326
702,326
592,326
482,326
372,326
262,326
922,368
855,368
812,368
702,368
592,368
482,368
372,368
262,368
922,410
855,410
812,410
702,410
(592,410),(482,410),(372,410),(262,410)
2040