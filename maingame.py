
from tracemalloc import stop
from turtle import window_height, window_width
import pygame
import time
import random
import cv2
import json



# windowsize
WINDOW_W=1100
WINDOW_H=600
WINDOW_SIZE=(WINDOW_W,WINDOW_H)

pygame.init()
clock = pygame.time.Clock()
pygame.font.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("ארץ עיר")
# bk_image=pygame.image.load("back.jpg")
write_image=pygame.image.load("images.jpg")
cursor_image=pygame.image.load("הורדה.png")
# bk_image=pygame.transform.scale(bk_image,(1200,800))
write_image=pygame.transform.scale(write_image,(1000,220))
cursor_image=pygame.transform.scale(cursor_image,(70,40))
lotteryfont = pygame.font.SysFont('david', 80)
lattersfont=pygame.font.SysFont('david', 24)
writtingfont=pygame.font.SysFont('david', 30)
delete_okfont=pygame.font.SysFont('jacob',25)
latters=["א","ב","ג","ד","ה","ו","ז","ח","ט","י","כ","ל","מ","נ","ס","ע","פ","צ","ק","ר","ש","ת"]
keyboardLatters=["א","ב","ג","ד","ה","ו","ז","ח","ט","י","כ","ל","מ","נ","ס","ע","פ","צ","ק","ר","ש","ת","ף","ץ","ך","ם"]


def mouse_click_pos_latter (y_mouse_pos,l):
    global keyboardLatters
    print(y_mouse_pos)
    if y_mouse_pos<550 or y_mouse_pos>572:
        return ""
    if y_mouse_pos>550 and y_mouse_pos<572:
        for i in range (len(keyboardLatters)):
            if l==i:
                return keyboardLatters[len(keyboardLatters)-l-1]

deleteletter="delete"
okletter="submit"
eraser = delete_okfont.render(deleteletter, False, (255, 255, 255))
submit=delete_okfont.render(okletter, False, (255, 255, 255))
pos=None
lottery_latter=None
latter_font=None
step=WINDOW_W//len(keyboardLatters)
latter_pos=-1
# Run until the user asks to quit
running = True
writtinglatter=""
screenword=None
submittedwords=[]
with open('database.json','r',encoding='utf-8') as jsonfile:
    a=jsonfile.read()
    jsonData = json.loads(a)
    print(jsonData)
    
while running:
    # Fill the background with white
    screen.fill((0, 0, 0))
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x_mouse=pos[0]
            y_mouse_pos=pos[1]
            l=(x_mouse-15)//42            
            word = mouse_click_pos_latter(y_mouse_pos,l)
            writtinglatter=word+writtinglatter
            if x_mouse>1040 and x_mouse<1100 and y_mouse_pos<550 and y_mouse_pos>537:
              
                writtinglatter=""          
            screenword=writtingfont.render(writtinglatter,True,(5,200,100))
            if x_mouse>=0 and x_mouse<546 and y_mouse_pos<550 and y_mouse_pos>537:
                submittedwords.append(writtinglatter)
           # writtinglatter+= stop
        if event.type == pygame.QUIT:
            running = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                lottery_latter=str(random.choice(latters))
                # lottery_latter = unicode(lottery_latter,  "Windows-1255")
                text_surface = lotteryfont.render(lottery_latter, False, (255, 255, 255))
                # llottery=myfont.render(str(lottery_latter),True,(0,0,0))
    screen.blit(eraser,(1040,537))
    screen.blit(submit,(1,537))
    if len(submittedwords)>0:
        for i in database['']:
            print(i)
 
    if lottery_latter!=None:
       screen.blit(text_surface,(WINDOW_W//2,100))
    if screenword!=None:
        screen.blit(screenword,(WINDOW_W//2,WINDOW_H//2))
    for l in range(len(keyboardLatters)):
        img=lattersfont.render(keyboardLatters[len(keyboardLatters)-l-1],True,(5,200,100))
        screen.blit(img,(15+l*42,550))

    # Flip the display
    pygame.display.flip()
    
# Done! Time to quit.
pygame.quit()
