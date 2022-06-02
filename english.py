from tracemalloc import stop
from turtle import Screen, window_height, window_width
import pygame
import time
import random
import cv2
import json
import mediapipe as mp


# windowsize
WINDOW_W = 1100
WINDOW_H = 600
WINDOW_SIZE = (WINDOW_W, WINDOW_H)

pygame.init()
clock = pygame.time.Clock()
pygame.font.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("ארץ עיר")
# bk_image=pygame.image.load("back.jpg")
# write_image = pygame.image.load("images.jpg")
cursor_image = pygame.image.load("הורדה.png")
# bk_image=pygame.transform.scale(bk_image,(1200,800))
# write_image = pygame.transform.scale(write_image, (1000, 220))
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
latters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
keyboardLatters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                   "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def mouse_click_pos_latter(y_mouse_pos, l):
    global keyboardLatters
    print(y_mouse_pos)
    if y_mouse_pos < 550 or y_mouse_pos > 572:
        return ""
    if y_mouse_pos > 550 and y_mouse_pos < 572:
        for i in range(len(keyboardLatters)):
            if l == i:
                return keyboardLatters[i]


deleteletter = "delete"
okletter = "submit"
object1 = "letter"
object3 = "country"
score = 0
object5 = "score:"
eraser = delete_okfont.render(deleteletter, False, (255, 255, 255))
submit = delete_okfont.render(okletter, False, (255, 255, 255))
object2 = objectsfont.render(object1, False, (255, 255, 255))
object4 = objectsfont.render(object3, False, (255, 255, 255))
object6 = objectsfont.render(object5, False, (255, 255, 255))
object7 = objectsfont.render(str(score), False, (255, 255, 255))
pos = None
lottery_latter = None
latter_font = None
step = WINDOW_W//len(keyboardLatters)
latter_pos = -1
# Run until the user asks to quit
running = True
writtinglatter = ""
screenword = None
submittedwords = []
finger13_y = 0
finger13_x = 0
cursor_x = 0
cursor_y = 550


with open('untitled.json') as jsonfile:
    jsonData = json.loads(jsonfile.read().encode('utf8'))
    # print(jsonData)


while running:
    work, frame = cap.read()

    screen.fill((0, 0, 0))
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    frame.flags.writeable = True

    # for hand_landmarks in results.multi_hand_landmarks:

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks,
                                      mp_hands.HAND_CONNECTIONS,
                                      mp_drawing_styles.get_default_hand_landmarks_style(),
                                      mp_drawing_styles.get_default_hand_connections_style())
            finger13_y = results.multi_hand_landmarks[0].landmark[13].y
            finger13_x = results.multi_hand_landmarks[0].landmark[13].x

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x_mouse = pos[0]
            print(x_mouse)
            y_mouse_pos = pos[1]
            l = x_mouse//42
            word = mouse_click_pos_latter(y_mouse_pos, l)
            writtinglatter += word
            if x_mouse > 1040 and x_mouse < 1100 and y_mouse_pos < 550 and y_mouse_pos > 537:
                writtinglatter = ""
                submittedwords.pop(0)
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

                   # writtinglatter+= stop
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                lottery_latter = str(random.choice(latters))
                # lottery_latter = unicode(lottery_latter,  "Windows-1255")
                letterscreen = lotteryfont.render(
                    lottery_latter, False, (255, 255, 255))
                # llottery=myfont.render(str(lottery_latter),True,(0,0,0))
    screen.blit(eraser, (1040, 537))
    screen.blit(submit, (1, 537))
    screen.blit(object2, (600, 80))
    screen.blit(object4, (200, 80))
    screen.blit(object6, (0, 0))
    screen.blit(object7, (165, 0))

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
    if finger13_y > 0.85 and finger13_y < 1:
        cursor_x = 0
        cursor_y = 550
    elif finger13_y > 0.15 and finger13_y > 0:
        cursor_x = 1050
        cursor_y = 535

    if finger13_x < 1 and finger13_x > 0.85 and cursor_x > 15:
        cursor_x -= 42
    if finger13_x < 0.15 and finger13_x > 0 and cursor_x < 1050:
        cursor_x += 42

        # if
        # for i in jsonData:
        #     if i["char"] =="a"and i ["type"]==1 :
        #         for word in i["words"]:
        #             if word==submittedwords[0]:
        #                 print ("good job")
    cv2.imshow("my ugly face", cv2.flip(frame, 1))
    if cv2.waitKey(1) & 0xff == ord("q"):
        break

    pygame.display.flip()


pygame.quit()
