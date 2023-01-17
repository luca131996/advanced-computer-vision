import pandas as pd
import numpy as np
import cv2
from tqdm import tqdm
import time
import mediapipe as mp

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    cv2.imshow("Camera", img)
    cv2.waitKey(1)