import tkinter as tk
from tkinter import ttk
import random

def yes_action(current_root): # Modified to accept the current window as argument
    """Function to be executed when the 'YES' button is clicked. Show message in same window."""
    # Clear existing widgets from the current window
    question_label = current_root.question_label # Access question_label via window
    yes_button = current_root.yes_button       # Access yes_button via window
    no_button = current_root.no_button         # Access no_button via window

    question_label.pack_forget()
    yes_button.pack_forget()
    no_button.place_forget()

    # Update the question label to display the Valentine's message in the current window
    question_label.config(text="I knew you would say yes. Perfect choice!\nMeet me tomorrow at 8\nLispenard street\n\nLove, KinArthur_",
                          font=('Arial', 12))
    question_label.pack(pady=20)


def no_action():
    """Function to be executed when the 'NO' button is clicked: PUNISHMENT! (Windows pop at once-ish)"""
    new_windows = []
    for _ in range(100):
        new_root = tk.Tk()
        new_root.title("Valentine?")
        new_root.geometry("300x200")
        new_root.configure(background='white')
        new_root.wm_attributes("-topmost", 1)

        # Store widgets as attributes of the new window so yes_action can find them
        new_root.question_label = ttk.Label(new_root, text="Will you be my Valentine?", font=('Arial', 14), background='white')
        new_root.question_label.pack(pady=20)

        new_root.yes_button = ttk.Button(new_root, text="YES", command=lambda r=new_root: yes_action(r)) # Pass new_root
        new_root.yes_button.pack(side=tk.LEFT, padx=30, pady=20)

        new_root.no_button = ttk.Button(new_root, text="NO", command=no_action) # Recursive punishment!
        new_root.no_button.place(x=180, y=120)
        new_root.no_button.bind("<Enter>", move_no_button)
        new_root.no_button.bind("<Motion>", move_no_button)
        new_root.no_button.bind("<Leave>", move_no_button)

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

# Store widgets as attributes of the root window for easy access in yes_action
root.question_label = ttk.Label(root, text="Will you be my Valentine?", font=('Arial', 14), background='white')
root.question_label.pack(pady=20)

root.yes_button = ttk.Button(root, text="YES", command=lambda r=root: yes_action(r)) # Pass root to yes_action
root.yes_button.pack(side=tk.LEFT, padx=30, pady=20)

root.no_button = ttk.Button(root, text="NO", command=no_action) # PUNISHMENT is here now!
root.no_button.place(x=180, y=120)

# Bind events
root.no_button.bind("<Enter>", move_no_button)
root.no_button.bind("<Motion>", move_no_button)
root.no_button.bind("<Leave>", move_no_button)


root.mainloop()