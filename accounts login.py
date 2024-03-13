import csv
import tkinter as tk 
import pygetwindow as gw
import pyautogui
import gc
from tkinter import ttk

def action(img):
    text_location = pyautogui.locateOnScreen(img, grayscale=True, confidence=0.8)

    if text_location is not None:        
        x, y = pyautogui.center(text_location)
        
        pyautogui.moveTo(x, y)
        pyautogui.click() 
        pyautogui.sleep(0.5)
        return False

def wait_for_text_and_click():    
    try:
        action("./riot games.png")

    except pyautogui.ImageNotFoundException:
        pass

    gc.collect()

def create_typing_function(login, password):
    def type_and_send():
        pyautogui.press('tab')
        pyautogui.write(login)
        pyautogui.press('tab')
        pyautogui.write(password)
        # pyautogui.press('enter')
    return type_and_send

def create_login_button(username, password):
    def login():
        riot_client = gw.getWindowsWithTitle("Riot Client")[0]
        if riot_client:
            riot_client.activate()
            
            wait_for_text_and_click()

            typing_function = create_typing_function(username, password)
            typing_function()

    return login

def main():
    csv_file_path = "./users.csv"
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        num_labels = len(rows)

        window = tk.Tk()
        window.title('Accounts Auto Logger')

        for i, row in enumerate(rows):
            if len(row) >= 2:
                username, password, account = row[0], row[1], row[2]
                label = ttk.Label(window, text=f"{account}")
                label.grid(row=i, column=0, padx=10, pady=10)

                login_button = ttk.Button(window, text="Log In", command=create_login_button(username, password))
                login_button.grid(row=i, column=1, padx=10, pady=10)


    window.mainloop()

if __name__ == "__main__":
    main()
