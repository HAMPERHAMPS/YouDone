import pytesseract
import time
from PIL import ImageGrab, Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import random
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import atexit
import subprocess
dummy = False
question_count = 1
question_label = None  
correct_answer = None   
quement = 5
syem = False

def exit_handler():
    global asd

    print("Fuck you.")
    
    if syem:
        subprocess.run(['python', 'main.py'])

def on_closing():
    if messagebox.askokcancel("No.", "No."):
        on_closing()

atexit.register(exit_handler)
import threading

def capture_screen_and_extract_text():
    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png")
    text = pytesseract.image_to_string(screenshot)
    return text

import sys
import cv2
import mediapipe as mp
import warnings
sens = False
asd = 0
warnings.filterwarnings("ignore", category=DeprecationWarning)
import time
class HandRaiseCounter:
    def __init__(self):
        self.count = 0
        self.hand_up = False
        self.stage = None
    def detect_hand_raise(self, landmarks):
        
        head_y = landmarks[0].y
        right_hand_y = landmarks[15].y
        left_hand_y = landmarks[16].y
        shouldery = landmarks[11].y
        hipy = landmarks[23].y
        kneey = landmarks[25].y
        elbowr = landmarks[14].y
        elbowl = landmarks[13].y
        ankl = landmarks[27].y
        ankr = landmarks[28].y
        global asd
        global sens
        global quement
        if right_hand_y > elbowr and left_hand_y > elbowl and hipy < kneey and ankl < kneey and ankr < kneey:
            sens = True
            time.sleep(0.5)
        if sens and elbowl < shouldery and elbowr < shouldery:
            sens = False
            asd = asd + 1
            print(f"You have done `{asd}` pushups")
        global pushup_text
        global root
        pushup_text.set(f"Pushups: {asd}/{quement}")
        if asd == quement:
            quement = quement + 1
            asd = 0
            cv2.destroyAllWindows()
            root.destroy()
            
            
            
            
    def draw_coordinates(self, image, landmarks):
        h, w, _ = image.shape
        for idx, landmark in enumerate(landmarks):
            cx, cy = int(landmark.x * w), int(landmark.y * h)
            cv2.putText(image, f'{idx}:({cx},{cy})', (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1, cv2.LINE_AA)

def mainordie():
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    cap = cv2.VideoCapture(0)
    counter = HandRaiseCounter()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = pose.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.pose_landmarks:
            counter.detect_hand_raise(results.pose_landmarks.landmark)
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            counter.draw_coordinates(image, results.pose_landmarks.landmark)

        cv2.imshow('PUSHUP BOIIIIIIIIII', image)
        if quement == asd:
            break
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def fullies():
    global pushup_text
    global root
    global syem
    root = None
    syem = True

    root = tk.Tk()
    root.title("Pushups. Now.")
    root.geometry("400x200")
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)
    script_dir = os.path.dirname(__file__)  
    image_path = os.path.join(script_dir, 'sans.jpg')  
    
    
    image = Image.open(image_path)
    image = image.resize((200, 200))
    img = ImageTk.PhotoImage(image)
    pushup_text = tk.StringVar()
    pushup_text.set(f"Pushups: 0/{quement}")


    question_label = tk.Label(root, textvariable=pushup_text, font=("Helvetica", 24))
    question_label.pack(pady=20)
    ssddd = tk.Label(root, text="MADE BY HAMPER | hamperhamps.space | @hamperhamps", font=("Helvetica", 15), anchor=tk.S) 
    ssddd.pack(pady=20)
    image_label = tk.Label(root, image=img)
    image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.focus_force()
    root.mainloop()
    syem = False
    
    
    

     
import keyboard
def block_alt_tab(e):
    if e.event_type == keyboard.KEY_DOWN:
        if e.name in ['alt', 'tab']:
            return False  # Block the key event
    return True

if __name__ == "__main__":
    while True:
        extracted_text = capture_screen_and_extract_text()
        print(f"Extracted Text: {extracted_text}")
    
        if "game over" in extracted_text.lower() or "you died" in extracted_text.lower() or "spectating" in extracted_text.lower() or "spectate" in extracted_text.lower():
            t1 = threading.Thread(target=mainordie)
            t1.start()
            keyboard.hook(block_alt_tab)
            fullies()
            
            stop_event = threading.Event()

            
    
    
    
    
       
            keyboard.unhook_all()
        
        
        else:
            print("Okay, you're free.")
        
        time.sleep(5)
