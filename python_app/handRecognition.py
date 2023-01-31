import cv2
from tqdm import tqdm
import time
import mediapipe as mp
import processImage
import configurations
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
    processImage.processHand(img=img)
    # Calculate Frame Rate
    current_time = time.time()
    fps = 1 / (current_time-previous_time)
    previous_time = current_time
    text = str(int(fps))
    # print Frame Rate
    cv2.putText(img=img, text=text, org=(10,70),
     fontFace=configurations.FONT, fontScale=configurations.FONTSCALE, 
     color=(255,0,0), thickness=configurations.THICKNESS)
    #show camera data
    cv2.imshow("Camera", img)
    #wait
    cv2.waitKey(1)
