import tkinter as tk
from tkinter import ttk
import random

def yes_action():
    """Function to be executed when the 'YES' button is clicked. Show message in same window."""
    # Clear existing widgets from the root window
    question_label.pack_forget()
    yes_button.pack_forget()
    no_button.place_forget() # Use place_forget for widgets placed with 'place'

    # Update the question label to display the Valentine's message
    question_label.config(text="I knew you would say yes. Perfect choice!\nMeet me tomorrow at 8\nVodra Lake\n\nLove, Tokyo_",
                          font=('Arial', 12)) # Removed pady from config
    question_label.pack(pady=20) # pady is correctly used here for pack layout


def no_action():
    """Function to be executed when the 'NO' button is clicked: PUNISHMENT! (Windows pop at once-ish)"""
    new_windows = []
        """You could the value from below"""
    for _ in range(10):
        new_root = tk.Tk()
        new_root.title("Valentine?")
        new_root.geometry("300x200")
        new_root.configure(background='white')
        new_root.wm_attributes("-topmost", 1)

        question_label_new = ttk.Label(new_root, text="Will you be my Valentine?", font=('Arial', 14), background='white')
        question_label_new.pack(pady=20)

        yes_button_new = ttk.Button(new_root, text="YES", command=yes_action) # Using yes_action, it's global
        yes_button_new.pack(side=tk.LEFT, padx=30, pady=20)

        no_button_new = ttk.Button(new_root, text="NO", command=no_action) # Recursive punishment!
        no_button_new.place(x=180, y=120)
        no_button_new.bind("<Enter>", move_no_button)
        no_button_new.bind("<Motion>", move_no_button)
        no_button_new.bind("<Leave>", move_no_button)

        new_windows.append(new_root) # Store the new window instances

    for win in new_windows:
        win.mainloop() # Start mainloop for each window AFTER creating all of them

    root.destroy() # Close the original window after unleashing the chaos


def move_no_button(event):
    """Function to move the 'NO' button to a more random and evasive position."""
    no_button = event.widget
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    button_width = no_button.winfo_reqwidth()
    button_height = no_button.winfo_reqheight()

    if random.random() < 0.7:
        x = random.randint(0, window_width - button_width - 10)
        y = random.randint(0, window_height - button_height - 10)
    else:
        current_x = no_button.winfo_x()
        current_y = no_button.winfo_y()
        x_offset = random.randint(-50, 50)
        y_offset = random.randint(-50, 50)
        x = max(0, min(window_width - button_width - 10, current_x + x_offset))
        y = max(0, min(window_height - button_height - 10, current_y + y_offset))

    no_button.place(x=x, y=y)


root = tk.Tk()
root.title("Valentine?")
root.geometry("300x200")
root.configure(background='white')
root.wm_attributes("-topmost", 1)

# Question Label (defined globally so yes_action can access it)
question_label = ttk.Label(root, text="Will you be my Valentine?", font=('Arial', 14), background='white')
question_label.pack(pady=20)

# Yes Button (defined globally)
yes_button = ttk.Button(root, text="YES", command=yes_action)
yes_button.pack(side=tk.LEFT, padx=30, pady=20)

# No Button (defined globally)
no_button = ttk.Button(root, text="NO", command=no_action) # PUNISHMENT is here now!
no_button.place(x=180, y=120)

# Bind events
no_button.bind("<Enter>", move_no_button)
no_button.bind("<Motion>", move_no_button)
no_button.bind("<Leave>", move_no_button)


root.mainloop()
