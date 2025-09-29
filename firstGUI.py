import tkinter as tk
import tkinter.messagebox as msg

# --- 1. Define the main action/function ---
def handle_click():
    """This function is called when the button is clicked."""
    
    # Get the text currently in the entry box
    user_input = entry_text.get()
    
    if user_input:
        # A. Update the output label
        output_message = f"Last input: '{user_input}'"
        output_label.config(text=output_message)
        
        # B. Show a pop-up message box
        msg.showinfo(
            "Input Confirmation", 
            f"Thank you for typing: {user_input}"
        )
    else:
        # If the input box is empty, show an error message box
        msg.showerror("Input Error", "Please enter some text before clicking the button!")


# --- 2. Set up the main window ---
# Create the root window (the main application window)
root = tk.Tk()
root.title("Tkinter App with Message Box")
root.geometry("400x200") # Set initial window size (Width x Height)

# --- 3. Create the widgets (using standard tk widgets) ---

# A. Text Input (Entry Widget)
entry_text = tk.StringVar()  # Variable to hold the text input
input_entry = tk.Entry(
    root, 
    textvariable=entry_text, 
    width=30,
    bg="white" # Standard tk widgets often benefit from explicit styling
)
entry_text.set("Type something here...") 

# B. Output Display (Label Widget)
output_label = tk.Label(
    root, 
    text="Click the button to process your input!",
    fg="blue", # Foreground (text) color
    font=('Arial', 10)
)

# C. Button Widget
action_button = tk.Button(
    root, 
    text="Show Pop-up & Output", 
    command=handle_click,
    padx=10, # Internal padding
    pady=5  # Internal padding
)

# --- 4. Arrange the widgets (using the 'pack' layout manager) ---

input_entry.pack(pady=10)
action_button.pack(pady=5)
output_label.pack(pady=10)

# --- 5. Run the application main loop ---
root.mainloop()