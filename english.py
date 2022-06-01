
from tracemalloc import stop
from turtle import Screen, window_height, window_width
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
objectsfont=pygame.font.SysFont('jacob',80)
# ,"c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
latters=["a","b"]
keyboardLatters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def mouse_click_pos_latter (y_mouse_pos,l):
    global keyboardLatters
    print(y_mouse_pos)
    if y_mouse_pos<550 or y_mouse_pos>572:
        return ""
    if y_mouse_pos>550 and y_mouse_pos<572:
        for i in range (len(keyboardLatters)):
            if l==i:
                return keyboardLatters[i]

deleteletter="delete"
okletter="submit"
object1="letter"
object3="country"
score=0
object5="score:"
eraser = delete_okfont.render(deleteletter, False, (255, 255, 255))
submit=delete_okfont.render(okletter, False, (255, 255, 255))
object2=objectsfont.render(object1,False, (255, 255, 255))
object4=objectsfont.render(object3,False, (255, 255, 255))
object6=objectsfont.render(object5,False, (255, 255, 255))
object7=objectsfont.render(str(score),False, (255, 255, 255))
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


with open('untitled.json') as jsonfile:
    jsonData = json.loads(jsonfile.read().encode('utf8'))
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
            l=x_mouse//42            
            word = mouse_click_pos_latter(y_mouse_pos,l)
            writtinglatter+=word
            if x_mouse>1040 and x_mouse<1100 and y_mouse_pos<550 and y_mouse_pos>537:
              
                writtinglatter=""          
            screenword=writtingfont.render(writtinglatter,True,(5,200,100))
            if x_mouse>=0 and x_mouse<546 and y_mouse_pos<550 and y_mouse_pos>537:
                submittedwords.append(writtinglatter)
                for i in jsonData:
                  if i["char"] ==lottery_latter and i ["type"]==1 :
                    for word in i["words"]:
                      if word==submittedwords[0]:
                        score+=25
                        object7=objectsfont.render(str(score),False, (255, 255, 255))
                        submittedwords.pop(0)

                        print ("good job")
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
    screen.blit(object2,(600,80))
    screen.blit(object4,(200,80))
    screen.blit(object6,(0,0))
    screen.blit(object7,(165,0))
    # if len(submittedwords)>0:
        # for i in database['']:
            # print(i)
    pygame.draw.line(screen,(255, 255, 255),(WINDOW_W//2,80),(WINDOW_W//2,480),10)
    pygame.draw.line(screen,(255, 255, 255),(200,140),(900,140),10)
    if lottery_latter!=None:
       screen.blit(text_surface,(WINDOW_W//2,100))
    if screenword!=None:
        screen.blit(screenword,(WINDOW_W//2,WINDOW_H//2))
    for l in range(len(keyboardLatters)):
        img=lattersfont.render(keyboardLatters[l],True,(5,200,100))
        screen.blit(img,(15+l*42,550))
        # for i in jsonData:
        #     if i["char"] =="a"and i ["type"]==1 :
        #         for word in i["words"]:
        #             if word==submittedwords[0]:
        #                 print ("good job")
    # Flip the display
    pygame.display.flip()
    
# Done! Time to quit.
pygame.quit()
