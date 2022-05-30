from turtle import window_height, window_width
import pygame
import time
import random
import cv2



# windowsize
WINDOW_W=1100
WINDOW_H=600
WINDOW_SIZE=(WINDOW_W,WINDOW_H)

pygame.init()
clock = pygame.time.Clock()
pygame.font.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("ארץ עיר")
bk_image=pygame.image.load("back.jpg")
write_image=pygame.image.load("images.jpg")
cursor_image=pygame.image.load("הורדה.png")
bk_image=pygame.transform.scale(bk_image,(1200,800))
write_image=pygame.transform.scale(write_image,(1000,220))
cursor_image=pygame.transform.scale(cursor_image,(70,40))
lotteryfont = pygame.font.SysFont('david', 80)
lattersfont=pygame.font.SysFont('david', 24)
latters=["א","ב","ג","ד","ה","ו","ז","ח","ט","י","כ","ל","מ","נ","ס","ע","פ","צ","ק","ר","ש","ת"]
keyboardLatters=["א","ב","ג","ד","ה","ו","ז","ח","ט","י","כ","ל","מ","נ","ס","ע","פ","צ","ק","ר","ש","ת","ף","ץ","ך","ם"]


def mouse_click_pos_latter (pos,l):
    global keyboardLatters
    if pos<550 or pos>572:
        return None
    else:
        for i in range (len(keyboardLatters)):
            if l==i:
                return keyboardLatters[i]


pos=None
lottery_latter=None
latter_font=None
step=WINDOW_W//len(keyboardLatters)
latter_pos=-1
# Run until the user asks to quit
running = True
while running:
    # Fill the background with white
    screen.fill((0, 0, 0))
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x_mouse=pos[0]
            pos=pos[1]
            l=x_mouse-15//42
            mouse_click_pos_latter(pos,l)
        if event.type == pygame.QUIT:
            running = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                lottery_latter=str(random.choice(latters))
                # lottery_latter = unicode(lottery_latter,  "Windows-1255")
                text_surface = lotteryfont.render(lottery_latter, False, (255, 255, 255))
                # llottery=myfont.render(str(lottery_latter),True,(0,0,0))
    print(mouse_click_pos_latter)
    if lottery_latter!=None:
       screen.blit(text_surface,(WINDOW_W//2,100))

    
    for l in range(len(keyboardLatters)):
        img=lattersfont.render(keyboardLatters[len(keyboardLatters)-l-1],True,(5,200,100))
        screen.blit(img,(15+l*42,550))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
