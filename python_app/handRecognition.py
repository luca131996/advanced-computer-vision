import cv2
from tqdm import tqdm
import time
import mediapipe as mp
#configurations
FONT = cv2.FONT_HERSHEY_PLAIN
THICKNESS = 3
FONTSCALE = 3
RADIUS = 20
THUMB_ID = 4

#OpenCV object
cap = cv2.VideoCapture(0)
#Hand object from Mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False)
mpDraw = mp.solutions.drawing_utils

previous_time = 0
current_time = 0

# Execution Loop
while True:
    #read camera data
    success, img = cap.read()
    #convert to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for id, lm in enumerate(hand_landmarks.landmark):
                height, width, channel = img.shape
                cx, cy = int(lm.x*width), int(lm.y*height)
                if id == THUMB_ID:
                    cv2.circle(img, (cx, cy), radius=RADIUS, color=(204, 0, 102), thickness=THICKNESS)
            mpDraw.draw_landmarks(img, hand_landmarks, mpHands.HAND_CONNECTIONS)
    
    # Calculate Frame Rate
    current_time = time.time()
    fps = 1 / (current_time-previous_time)
    previous_time = current_time
    text = str(int(fps))
    # print Frame Rate
    cv2.putText(img=img, text=text, org=(10,70),
     fontFace=FONT, fontScale=FONTSCALE, color=(255,0,0), thickness=THICKNESS)
    #show camera data
    cv2.imshow("Camera", img)
    #wait
    cv2.waitKey(1)
