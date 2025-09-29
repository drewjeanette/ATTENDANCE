import tkinter as tk
from tkinter import messagebox, END

class FeedbackApp:
    """A simple GUI application for collecting customer feedback."""

    def __init__(self, master):
        # 1. Initialize the main window settings
        self.master = master
        self.master.title("Customer Feedback Interface")
        
        # Configure grid for centered layout
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=3)
        self.master.columnconfigure(2, weight=1)
        
        # Set padding for a cleaner look
        main_frame = tk.Frame(master, padx=30, pady=30)
        main_frame.grid(row=0, column=1, sticky="nsew")
        
        for i in range(5):
            main_frame.rowconfigure(i, weight=1)
            
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=3)


        # 2. Header Label
        header_label = tk.Label(
            main_frame, 
            text="Please provide feedback on your experience",
            font=("Arial", 16, "bold"),
            pady=15
        )
        header_label.grid(row=0, column=0, columnspan=2, sticky="ew")

        # --- Name Entry ---
        
        # Label
        tk.Label(main_frame, text="Name:", font=("Arial", 12)).grid(
            row=1, column=0, sticky="w", pady=5, padx=5
        )
        # Entry Box
        self.name_entry = tk.Entry(main_frame, width=50, font=("Arial", 12))
        self.name_entry.grid(row=1, column=1, sticky="ew", pady=5, padx=5)

        # --- Email Entry ---
        
        # Label
        tk.Label(main_frame, text="Email:", font=("Arial", 12)).grid(
            row=2, column=0, sticky="w", pady=5, padx=5
        )
        # Entry Box
        self.email_entry = tk.Entry(main_frame, width=50, font=("Arial", 12))
        self.email_entry.grid(row=2, column=1, sticky="ew", pady=5, padx=5)

        # --- Feedback Text Area ---
        
        # Label
        tk.Label(main_frame, text="Feedback:", font=("Arial", 12)).grid(
            row=3, column=0, sticky="nw", pady=10, padx=5
        )
        # Text Box (larger box for multi-line input)
        self.feedback_text = tk.Text(main_frame, height=10, width=50, font=("Arial", 12), wrap=tk.WORD)
        self.feedback_text.grid(row=3, column=1, sticky="nsew", pady=10, padx=5)

        # --- Submit Button ---
        
        self.submit_button = tk.Button(
            main_frame, 
            text="Submit Feedback", 
            command=self.submit_feedback,
            bg="#4CAF50",  # Green background
            fg="white",    # White text
            font=("Arial", 14, "bold"),
            relief=tk.RAISED,
            bd=3,
            padx=10,
            pady=5
        )
        # Place the button below the inputs, spanning both columns
        self.submit_button.grid(row=4, column=0, columnspan=2, pady=20)

    def submit_feedback(self):
        """
        Handles the submit button click:
        1. Prints the data to the console.
        2. Clears all input fields.
        """
        # 1: Retrieve all entered text
        name = self.name_entry.get()
        email = self.email_entry.get()
        # The Text widget requires '1.0' (line 1, character 0) to 'end'
        feedback = self.feedback_text.get("1.0", END).strip()

        # Print to console (as requested)
        print("\n--- NEW FEEDBACK SUBMISSION ---")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Feedback:")
        print("-------------------------------")
        print(feedback)
        print("-------------------------------\n")

        # 2: Clear all text fields
        self.name_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.feedback_text.delete("1.0", END)
        
        # Provide a visual confirmation to the user (since the console isn't always visible)
        messagebox.showinfo("Success", "Thank you for your feedback! Your submission has been recorded (and printed to the console).")


if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    
    # Initialize and run the application
    app = FeedbackApp(root)
    
    # Start the Tkinter event loop
    root.mainloop()
