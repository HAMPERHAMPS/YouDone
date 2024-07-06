import pytesseract
import time
from PIL import ImageGrab, Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import random
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

dummy = False
question_count = 1
question_label = None  
correct_answer = None   
quement = 5
def next_question():
    global question_count, correct_answer, quement
    if question_count < quement:
        question_count += 1
        question, correct_answer = generate_question()
        question_label.config(text=question)  
        answer_entry.delete(0, tk.END)
        return question, correct_answer
    else:
        messagebox.showinfo("Finished", "You have completed all questions!")
        question_count = 1
        quement = quement + 1
        root.destroy()

def generate_question():
    num1 = random.randint(-100, 100)
    num2 = random.randint(-100, 100)
    operation = random.choice(['+', '-', '*', '/'])
    
    if operation == '+':
        correct_ans = num1 + num2
    elif operation == '-':
        correct_ans = num1 - num2
    elif operation == '*':
        correct_ans = num1 * num2
    elif operation == '/':
        num2 = random.randint(1, 10)
        num1 = num1 * num2
        correct_ans = num1 // num2
    
    question = f"{num1} {operation} {num2}"
    return question, correct_ans

def check_answer():
    global dummy
    try:
        answer = int(answer_entry.get())
        if answer == correct_answer:
            messagebox.showinfo("Success", "Correct. You're not a dummy!")
            next_question()
        else:
            messagebox.showerror("Error", "Incorrect. You're a dummy.")
            dummy = True
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def capture_screen_and_extract_text():
    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png")
    text = pytesseract.image_to_string(screenshot)
    return text

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Math. Now.")
    root.geometry("400x200")
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)
    script_dir = os.path.dirname(__file__)  
    image_path = os.path.join(script_dir, 'sans.jpg')  
    
    
    image = Image.open(image_path)
    image = image.resize((200, 200))
    img = ImageTk.PhotoImage(image)
    question_label = tk.Label(root, text="", font=("Helvetica", 24)) 
    question_label.pack(pady=20)
    ssddd = tk.Label(root, text="MADE BY HAMPER | hamperhamps.space | @hamperhamps", font=("Helvetica", 15), anchor=tk.S) 
    ssddd.pack(pady=20)
    image_label = tk.Label(root, image=img)
    image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    answer_entry = tk.Entry(root, font=("Helvetica", 24))
    answer_entry.pack(pady=20)
    
    submit_button = tk.Button(root, text="Submit", command=check_answer, font=("Helvetica", 24))
    submit_button.pack(pady=20)
    
    root.protocol("WM_DELETE_WINDOW", lambda: None)  
    
    question, correct_answer = next_question()  
    
    while True:
        extracted_text = capture_screen_and_extract_text()
        print(f"Extracted Text: {extracted_text}")
        
        if "game over" in extracted_text.lower() or "you died" in extracted_text.lower() or "spectating" in extracted_text.lower() or "spectate" in extracted_text.lower():
            question, correct_answer = next_question()
            question_label.config(text=question) 
            root.focus_force()
            root.mainloop()
        else:
            print("Okay, you're free.")
        
        time.sleep(5)
