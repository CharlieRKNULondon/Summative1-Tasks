from random import randint #Random is for choosing a random number
import tkinter as tk #Tkinter is for creating the GUI




class Equation_Game():
    def __init__(self, root):
        
        self.user_score = 0
        self.Finished = False

        self.tinkter_root = root

        self.build_gui()
        #initialising user score, and acceptance states.

        
    
    def build_gui(self):
        """ Builds the GUI using tkinkter for the users, using buttons, labels and text fields.
        """
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

        self.generate_equation() #Calls a function to produce the equation to populate the GUI

    def generate_equation(self):
        """
        Generates a new multiplication equation with two random numbers. Displays the equation with missing factor for user to guess.
        """
        self.equation_number_one = randint(0,999) #Picks a random number between 0 and 999
        self.equation_number_two = randint(0,999)
        self.equation_result = self.equation_number_one * self.equation_number_two #Calculates the result to be displayed to the user.
        self.equation_text.config(text=f"{self.equation_number_one} × x = {self.equation_result}")


    def check_user_answer(self):
        
        print(f"{self.equation_number_one} + * x = +{self.equation_result}")

        try:
            user_guess = int(self.user_text_field.get())
        except ValueError: #Prevents users from entering strings which would result in an error
            self.result_text.config(text="Please enter an integer.")

        if user_guess != self.equation_number_two: #Tests to see if the user guess is equal to the answer
            self.result_text.config(text="Wrong... :(")
        else:
            self.user_score += 1 
            self.result_text.config(text="Correct! :)")
            self.score_label.config(text=f"Score: {self.user_score}")
            #This else section increases the users score, and updates the GUI.
    def next_equation(self):
        """Prepare the next equation."""
        self.user_text_field.delete(0, tk.END) #Clears the text for future user input
        self.generate_equation()
        self.result_text.config(text="")




root = tk.Tk()
game = Equation_Game(root)
root.mainloop()
