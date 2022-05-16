import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands=mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5) 
cap=cv2.VideoCapture(0)
while True:
    
    work,frame=cap.read()
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))