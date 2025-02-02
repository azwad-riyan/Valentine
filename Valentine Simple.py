import tkinter as tk
from tkinter import ttk
import random

def yes_action():
    """Function to be executed when the 'YES' button is clicked."""
    popup = tk.Toplevel(root)
    popup.title("Form2")
    popup.configure(background='white')
    popup.wm_attributes("-topmost", 1)

    message_label = ttk.Label(popup,
                              text="I know you will say yes. Meet me tomorrow at 8\nLispenard street\n\nLove, KinArthur_",
                              font=('Arial', 12),
                              background='white',
                              padding=15)
    message_label.pack(padx=20, pady=20)


def no_action():
    """Function to be executed when the 'NO' button is clicked (currently does nothing)."""
    pass


def move_no_button(event):
    """Function to move the 'NO' button to a random position."""
    no_button = event.widget  # Get the button that triggered the event
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    button_width = no_button.winfo_reqwidth() # Get requested width of button
    button_height = no_button.winfo_reqheight() # Get requested height of button

    # Calculate random positions, ensuring button stays within window bounds
    x = random.randint(0, window_width - button_width - 10) # -10 for a little margin
    y = random.randint(0, window_height - button_height - 10)

    no_button.place(x=x, y=y) # Use place geometry manager to set exact position


root = tk.Tk()
root.title("Valentine?")
root.geometry("300x200")
root.configure(background='white')
root.wm_attributes("-topmost", 1)

# Question Label
question_label = ttk.Label(root, text="Will you be my Valentine?", font=('Arial', 14), background='white')
question_label.pack(pady=20)

# Yes Button
yes_button = ttk.Button(root, text="YES", command=yes_action)
yes_button.pack(side=tk.LEFT, padx=30, pady=20)

# No Button
no_button = ttk.Button(root, text="NO", command=no_action)
# Use place geometry manager initially to easily move it later
no_button.place(x=180, y=120) # Initial position (adjust as needed)

# Bind the <Enter> event (mouse hover) to the move_no_button function
no_button.bind("<Enter>", move_no_button)


root.mainloop()
