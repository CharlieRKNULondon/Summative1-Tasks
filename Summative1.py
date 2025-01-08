'''Please use Python version 3.9 or above to complete your assignment. Note that
Python 3.9+ cannot be used on Windows 7 and earlier. Please state the Python
version you used to complete this assignment.
Task 1
Write a Python program that completes the following steps:
1. Generates a simple equation with random numbers, such as:
3 × 𝑥 = 12
Assessment Brief: Individual Coursework 2024–25
Cohorts October 2023 and after 2
2. Displays the equation on its own line in the terminal or a GUI of any kind (you
can use Tkinter, Flask, HTML and CSS or any other way to produce ).
3. Check if the user's answer is correct and display an appropriate message.
4. Repeat the process for several equations, keeping track of the user's score.
5. After all equation questions have been answered, output the total score.
6. Once you have completed this task, push the code to GitHub.
Code Quality Expectations
● Follow PEP 8 standards.
● Include appropriate code comments.
● Use docstrings.
● Strive to keep your code simple and readable.
● Structure your code in a modular way.
● Aim to use pure functions where possible.'''
from random import randint #Random is for choosing a random number
import tkinter as tk #Tkinter is for creating the GUI




class Equation_Game():
    def __init__(self, root):
        ''''''
        self.user_score = 0
        self.Finished = False

        self.tinkter_root = root

        self.build_gui()

        
    
    def build_gui(self):
        self.equation_text = tk.Label(self.tinkter_root, text ="", font =('Calbri', 14))
        self.equation_text.pack()

        self.user_text_field = tk.Entry(self.tinkter_root, font=('Calbri', 14))
        self.user_text_field.pack()

        self.submit_button = tk.Button(self.tinkter_root, text="Submit", command=self.check_user_answer)
        self.submit_button.pack()

        self.result_text = tk.Label(self.tinkter_root, text="", font=('Arial', 14))
        self.result_text.pack()

        self.score_label = tk.Label(self.tinkter_root, text=f"Score: {self.user_score}", font=('Arial', 14))
        self.score_label.pack()

        self.next_button = tk.Button(self.tinkter_root, text="Next Equation", command=self.next_equation)
        self.next_button.pack()

        self.generate_equation()

    def generate_equation(self):
        self.equation_number_one = randint(0,999)
        self.equation_number_two = randint(0,999)
        self.equation_result = self.equation_number_one * self.equation_number_two
        self.equation_text.config(text=f"{self.equation_number_one} × x = {self.equation_result}")


    def check_user_answer(self):
        
        print(f"{self.equation_number_one} + * x = +{self.equation_result}")

        try:
            user_guess = int(self.user_text_field.get())
        except ValueError:
            self.result_text.config(text="Please enter an integer.")

        if user_guess != self.equation_number_two:
            self.result_text.config(text="Wrong... :(")
        else:
            self.user_score += 1
            self.result_text.config(text="Correct! :)")
            self.score_label.config(text=f"Score: {self.user_score}")
    def next_equation(self):
        """Prepare the next equation."""
        self.user_text_field.delete(0, tk.END)
        self.generate_equation()
        self.result_text.config(text="")




root = tk.Tk()
game = Equation_Game(root)
root.mainloop()