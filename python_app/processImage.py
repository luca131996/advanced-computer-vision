import cv2
import mediapipe as mp
import configurations
mpDraw = mp.solutions.drawing_utils
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False)

def processHand(img):
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for id, lm in enumerate(hand_landmarks.landmark):
                height, width, channel = img.shape
                cx, cy = int(lm.x*width), int(lm.y*height)
                if id == configurations.THUMB_ID:
                    cv2.circle(img, (cx, cy), radius=configurations.RADIUS, color=(204, 0, 102), 
                    thickness=configurations.THICKNESS)
            mpDraw.draw_landmarks(img, hand_landmarks, mpHands.HAND_CONNECTIONS)