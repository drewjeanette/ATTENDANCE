import tkinter as tk
from tkinter import ttk

class HelloTranslatorApp:
    """
    A simple Tkinter application structured as a class 
    to demonstrate handling button clicks and updating a label.
    """
    def __init__(self, master):
        # 1. Store the parent window (master)
        self.master = master
        master.title("The 'Hello' Translator")
        
        # 2. Define the main data source: greetings
        self.greetings = {
            "English": "Hello",
            "Français": "Bonjour",
            "Deutsch": "Hallo",
            "Español": "Hola"
        }
        
        # 3. Initialize a Tkinter String variable for the dynamic output label
        # This will hold only the translated greeting (e.g., "Hola").
        self.output_text = tk.StringVar()
        
        # 4. Create the UI components
        self._create_widgets()
        
        # 5. Set initial text for the dynamic label to be empty
        # The static instruction text is now in its own label.
        self.output_text.set("") 

    def _create_widgets(self):
        """Creates and places all widgets in the window."""
        
        # --- A. Static Instruction Label (Stays at the top) ---
        instruction_label = ttk.Label(
            self.master, 
            text="Welcome. Select any language to see the greeting.", # Static text here
            font=('Arial', 12, 'bold'),
            wraplength=350,
            anchor="center"
        )
        instruction_label.pack(pady=(20, 10), padx=10) # Packed first

        # --- B. Button Frame (Packed second) ---
        # A Frame is a container widget used to group and organize other widgets.
        button_frame = ttk.Frame(self.master)
        button_frame.pack(pady=10) 

        # --- C. Create Buttons and place them in the frame using grid ---
        languages = ["English", "Français", "Deutsch", "Español"]
        
        for i, lang in enumerate(languages):
            # Create a lambda function to pass the language name to the handler method.
            button = ttk.Button(
                button_frame, 
                text=lang, 
                command=lambda l=lang: self.translate_greeting(l)
            )
            # Vertical alignment: column 0, row i
            button.grid(row=i, column=0, padx=5, pady=5, sticky="ew")
            
        # Ensure the button frame is centered correctly
        button_frame.grid_columnconfigure(0, weight=1)
        
        # --- D. Dynamic Greeting Display Label (Packed last to show the greeting) ---
        # This label is linked to self.output_text and will be updated on click.
        greeting_display_label = ttk.Label(
            self.master, 
            textvariable=self.output_text, 
            font=('Arial', 18), # Slightly larger font for the greeting
            foreground="blue",
            anchor="center"
        )
        greeting_display_label.pack(pady=20, padx=10)


    def translate_greeting(self, language_key):
        """
        Handles the button click event.
        Looks up the greeting and updates the output label.
        """
        # Retrieve the greeting from the dictionary using the button's text
        greeting = self.greetings.get(language_key, "Error: Language not found")
        
        # Update the StringVar with *only* the greeting, fulfilling the new requirement
        self.output_text.set(greeting)


# --- Application Startup ---
if __name__ == "__main__":
    # Create the root window
    root = tk.Tk()
    # Instantiate the application class, passing the root window as the master
    app = HelloTranslatorApp(root)
    # Start the Tkinter event loop
    root.mainloop()
