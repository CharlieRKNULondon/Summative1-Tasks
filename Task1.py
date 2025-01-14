from random import randint  # Random is for choosing a random number
import tkinter as tk  # Tkinter is for creating the GUI


class EquationGame:
    def __init__(self, root):
        """Initialize the game with a root window and set up the GUI."""
        self.user_score = 0
        self.finished = False

        self.tkinter_root = root
        self.build_gui()

    def build_gui(self):
        """Builds the GUI using tkinter with buttons, labels, and text fields."""
        self.equation_text = tk.Label(self.tkinter_root, text="", font=('Calibri', 14))
        self.equation_text.pack()

        self.user_text_field = tk.Entry(self.tkinter_root, font=('Calibri', 14))
        self.user_text_field.pack()

        self.submit_button = tk.Button(self.tkinter_root, text="Submit", command=self.check_user_answer)
        self.submit_button.pack()

        self.result_text = tk.Label(self.tkinter_root, text="", font=('Arial', 14))
        self.result_text.pack()

        self.score_label = tk.Label(self.tkinter_root, text=f"Score: {self.user_score}", font=('Arial', 14))
        self.score_label.pack()

        self.next_button = tk.Button(self.tkinter_root, text="Next Equation", command=self.next_equation)
        self.next_button.pack()

        self.generate_equation()

    def generate_equation(self):
        """Generate a new multiplication equation with random numbers."""
        self.equation_number_one = randint(0, 999)
        self.equation_number_two = randint(0, 999)
        self.equation_result = self.equation_number_one * self.equation_number_two
        self.equation_text.config(text=f"{self.equation_number_one} × x = {self.equation_result}")

    def check_user_answer(self):
        """Check the user's answer and update the score."""
        print(f"{self.equation_number_one} × x = {self.equation_result}")

        try:
            user_guess = int(self.user_text_field.get())
        except ValueError:
            self.result_text.config(text="Please enter an integer.")
        else:
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


if __name__ == "__main__":
    root = tk.Tk()
    game = EquationGame(root)
    root.mainloop()
