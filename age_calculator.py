import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class AgeCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Age Calculator")
        self.root.geometry("600x400")  # Increased from 400x300 to 600x400
        self.root.resizable(False, False)
        
        # Set background color
        self.root.configure(bg="#E6E6FA")  # Light purple background
        
        # Create labels and entries
        title = tk.Label(root, text="Age Calculator", font=("Helvetica", 24, "bold"), 
                        bg="#E6E6FA", fg="#4B0082")  # Dark purple text
        title.pack(pady=20)
        
        # Birth Date Frame
        date_frame = tk.Frame(root, bg="#E6E6FA")
        date_frame.pack(pady=20)
        
        # Style for labels
        label_style = {"font": ("Helvetica", 12), "bg": "#E6E6FA", "fg": "#4B0082"}
        entry_style = {"width": 5, "font": ("Helvetica", 12), "bg": "#F0F8FF"}  # Light blue entries
        
        tk.Label(date_frame, text="Day:", **label_style).grid(row=0, column=0, padx=5)
        self.day_entry = tk.Entry(date_frame, **entry_style)
        self.day_entry.grid(row=0, column=1)
        
        tk.Label(date_frame, text="Month:", **label_style).grid(row=0, column=2, padx=5)
        self.month_entry = tk.Entry(date_frame, **entry_style)
        self.month_entry.grid(row=0, column=3)
        
        tk.Label(date_frame, text="Year:", **label_style).grid(row=0, column=4, padx=5)
        self.year_entry = tk.Entry(date_frame, width=8, font=("Helvetica", 12), bg="#F0F8FF")
        self.year_entry.grid(row=0, column=5)
        
        # Calculate Button with hover effect
        calc_button = tk.Button(root, text="Calculate Age", command=self.calculate_age,
                              font=("Helvetica", 14, "bold"), bg="#9370DB", fg="white",  # Medium purple button
                              activebackground="#7B68EE", activeforeground="white",
                              relief="raised", bd=3)
        calc_button.pack(pady=20)
        
        # Result Label
        self.result_label = tk.Label(root, text="", font=("Helvetica", 14),
                                   bg="#E6E6FA", fg="#4B0082", wraplength=350)
        self.result_label.pack(pady=20)
        
    def calculate_age(self):
        try:
            birth_day = int(self.day_entry.get())
            birth_month = int(self.month_entry.get())
            birth_year = int(self.year_entry.get())
            
            # Get current date
            current_date = datetime.now()
            
            # Calculate age
            age_year = current_date.year - birth_year
            age_month = current_date.month - birth_month
            age_day = current_date.day - birth_day
            
            # Adjust age if birthday hasn't occurred this year
            if age_month < 0 or (age_month == 0 and age_day < 0):
                age_year -= 1
                age_month += 12
            
            # Display result with emoji
            self.result_label.config(
                text=f"🎉 Your age is: {age_year} years, {abs(age_month)} months, and {abs(age_day)} days! 🎈"
            )
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = AgeCalculator(root)
    root.mainloop()