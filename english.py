# libaries
from imp import load_module
from tracemalloc import stop
from turtle import Screen, window_height, window_width
import pygame
import time
import random
import cv2
import json
import mediapipe as mp
import time


# windowsize
WINDOW_W = 1100
WINDOW_H = 600
WINDOW_SIZE = (WINDOW_W, WINDOW_H)

# strart engines
pygame.init()
clock = pygame.time.Clock()
pygame.font.init()

# load
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("ארץ עיר")
cursor_image = pygame.image.load("הורדה.png")
cursor_image = pygame.transform.scale(cursor_image, (60, 40))
lotteryfont = pygame.font.SysFont('david', 80)
lattersfont = pygame.font.SysFont('david', 24)
writtingfont = pygame.font.SysFont('jacob', 80)
delete_okfont = pygame.font.SysFont('jacob', 25)
objectsfont = pygame.font.SysFont('jacob', 80)
mp_drawing = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_drawing_styles = mp.solutions.drawing_styles

# virables
latters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
keyboardLatters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k","l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
hand_landmarks=None
writtinglatter = ""
pos = None
lottery_latter = None
latter_font = None
step = WINDOW_W//len(keyboardLatters)
latter_pos = -1
running = True
screenword = None
submittedwords = []
cursor_x = 0
cursor_y = 550

score = 0
# fonts
eraser= delete_okfont.render("delete", False, (255, 255, 255))
submit= delete_okfont.render("submit", False, (255, 255, 255))
object1= objectsfont.render("letter", False, (255, 255, 255))
object2= objectsfont.render("country", False, (255, 255, 255))
object3= objectsfont.render("score:", False, (255, 255, 255))
object4= objectsfont.render(str(score), False, (255, 255, 255))

# functions
def cursor_ai_pos(l,cursor_y):
    global keyboardLatters
    if cursor_y < 550 or cursor_y> 572 :
        return ""
    if cursor_y >= 550 and cursor_y <= 572:
        return keyboardLatters[l]
    return ""

def mouse_click_pos_latter(y_mouse_pos, l):
    global keyboardLatters
    
    if y_mouse_pos < 550 or y_mouse_pos > 572 :
        return ""
    # and y_mouse_pos <= 572:
    if y_mouse_pos >= 550 :
        return keyboardLatters[l]
    return ""
with open('untitled.json') as jsonfile:
    jsonData = json.loads(jsonfile.read().encode('utf8'))
            
def a_i(hand_landmarks):
            global writtinglatter  
            global cursor_y
            global cursor_x
            global submittedwords
            global score
            global jsonData
            finger12_y =hand_landmarks.landmark[12].y
            finger16_y = hand_landmarks.landmark[16].y
            finger20_y = hand_landmarks.landmark[20].y
            finger8_y = hand_landmarks.landmark[8].y           
            finger13_y = hand_landmarks.landmark[13].y
            finger9_y = hand_landmarks.landmark[9].y
            finger5_y = hand_landmarks.landmark[5].y
            finger17_y =hand_landmarks.landmark[17].y
           
            finger12_x = hand_landmarks.landmark[12].x
            if finger12_y > 0.75 and finger12_y < 1:
              cursor_x=0
              print(cursor_x)
              cursor_y = 550
            if finger12_y < 0.25 and finger12_y > 0:
              cursor_x = 1050
              cursor_y = 535
            
            if finger12_x < 1 and finger12_x > 0.75 :
               if cursor_y==550 and cursor_x<1050: 
                cursor_x += 42
                print(cursor_x)
                time.sleep(0.2)
               if cursor_y==535 and cursor_x==1050:   
                cursor_x=1050
            if finger12_x < 0.25 and finger12_x > 0 :
              if cursor_y==550 and cursor_x>15:
                cursor_x -= 42
                time.sleep(0.2)
              if cursor_y==535 and cursor_x==1050:
                  cursor_x=15 
                  cursor_y=535       
            if finger16_y >= finger13_y and finger17_y <= finger20_y and finger8_y >= finger5_y and finger12_y >= finger9_y:
                if cursor_y==535 and cursor_x==1050:
                    writtinglatter=""
                    return "",score
                if  cursor_y==550:     
                    l = cursor_x//42
                    return cursor_ai_pos( l ,cursor_y),score                    
                    

                    time.sleep(0.5)
                
                if cursor_y==535 and cursor_x==15:
                    for i in jsonData:
                     if i["char"] == lottery_latter and i["type"] == 1:
                        for word in i["words"]:
                            if word == writtinglatter:
                                writtinglatter=""
                                score +=25
                                return "",score 
                              
            return "",score
                                

# with open('untitled.json') as jsonfile:
#     jsonData = json.loads(jsonfile.read().encode('utf8'))
    # print(jsonData)

# display
while running:
    work, frame = cap.read()
# hands
    screen.fill((0, 0, 0))
    frame = cv2.flip(frame,1)
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks,
                                      mp_hands.HAND_CONNECTIONS,
                                      mp_drawing_styles.get_default_hand_landmarks_style(),
                                      mp_drawing_styles.get_default_hand_connections_style())
            word,score1=a_i(results.multi_hand_landmarks[0])
            writtinglatter += str(word)
            score =score1
            time.sleep(0.1)
            screenword = writtingfont.render(writtinglatter, True, (0, 0, 255))
            object7 = objectsfont.render(str(score), False, (255, 255, 255))
# events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x_mouse = pos[0]
            y_mouse_pos = pos[1]
            l = x_mouse//42
            word = mouse_click_pos_latter(y_mouse_pos, l)
            writtinglatter += word
            if x_mouse > 1040 and x_mouse < 1100 and y_mouse_pos < 550 and y_mouse_pos > 537:
                writtinglatter = ""
            screenword = writtingfont.render(writtinglatter, True, (0, 0, 255))

            if x_mouse >= 0 and x_mouse < 546 and y_mouse_pos < 550 and y_mouse_pos > 537:
                submittedwords.append(writtinglatter)
                for i in jsonData:
                    if i["char"] == lottery_latter and i["type"] == 1:
                        for word in i["words"]:
                            if word == submittedwords[0]:
                                score += 25
                                object7 = objectsfont.render(
                                    str(score), False, (255, 255, 255))
                                submittedwords.pop(0)

                   
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                lottery_latter = str(random.choice(latters))
                # lottery_latter = unicode(lottery_latter,  "Windows-1255")
                letterscreen = lotteryfont.render(
                    lottery_latter, False, (255, 255, 255))
                # llottery=myfont.render(str(lottery_latter),True,(0,0,0))
#blit
    screen.blit(eraser, (1040, 537))
    screen.blit(submit, (1, 537))
    screen.blit(object1, (600, 80))
    screen.blit(object2, (200, 80))
    screen.blit(object3, (0, 0))
    screen.blit(object4, (165, 0))

    pygame.draw.line(screen, (255, 255, 255),
                     (WINDOW_W//2, 80), (WINDOW_W//2, 480), 10)
    pygame.draw.line(screen, (255, 255, 255), (200, 140), (900, 140), 10)
    if lottery_latter != None:
        screen.blit(letterscreen, (600, 200))
    if screenword != None:
        screen.blit(screenword, (200, 200))
    for l in range(len(keyboardLatters)):
        img = lattersfont.render(keyboardLatters[l], True, (5, 200, 100))
        screen.blit(img, (15+l*42, 550))
    screen.blit(cursor_image, (cursor_x, cursor_y))
       
    if cv2.waitKey(1) & 0xff == ord("q"):
        
        break

    pygame.display.flip()


pygame.quit()
