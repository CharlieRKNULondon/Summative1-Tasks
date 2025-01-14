# Equation Game

![image](https://github.com/user-attachments/assets/9eca4eb8-3f99-421c-badb-738032e2b290)

## Project Overview

The Equation Game is a simple game, which uses tkinkter as a GUI, enabling users to practice their division skills to identify the value of x, which is missing tfrom the equation. Each time the user presses next equation, a new random number will be generated.

## User Documentation

### Prerequisites

 **-** All version of Python 3.8 and later installed on your computer
 **-** Tkinkter (Python Library)
 **-** Random (Python Library)

 ### How to Play

 1. Download the Python File and run the game in any IDE of your choice
 2. Read the equation carefully. Solve for x the missing number.
 3. Enter your answer (must be an integer) in the text box.
 4. Press **Submit** to check your answer. The game will provide feedback, either, "Correct!" or "Wrong...".
 5. If you are correct your score will be incremented by 1.
 6. If you would like to skip an equation or move to another, press the **Next Equation** button.

#### Example Gameplay

What the game looks like in action:

 ![image](https://github.com/user-attachments/assets/27e4ae8d-3687-427d-ada4-5b76689cff68)

![image](https://github.com/user-attachments/assets/ed755033-6c04-4f43-8dcf-b3eb6ae86174)


## Techical Documentation

### Code Structure

 1. ```EquationGame``` **Class**
This utilises the features of Object Orientated Programming (OOP). The class manages the core functionality of the game and allows variables to be shared between methods whilst remaining local.
 2. **Methods**
    **-** ```__init__(self, root)```: Initialises the game state, variables such as score and GUI setup.
    **-** ```build_gui(self)```: Constructs the GUI using tkinkter labels, text fields and buttons.
    **-** ```generate_equation(self)```: Generates a new equation with two random integers between 0 and 999.
    **-** ```check_user_answer(self):```: Validates user input and checks it against the correct answer. It also updates the score and feedback based on if the user is correct.
    **-** ```next_equation(self)```: Clears the text field, and prepares a new equation for the using.

### Code Examples

1. **Equation Generation**
```self.equation_number_one = randint(0, 999)
self.equation_number_two = randint(0, 999)
self.equation_result = self.equation_number_one * self.equation_number_two
self.equation_text.config(text=f"{self.equation_number_one} × x = {self.equation_result}")
```
2. **Answer Validation**
```try:
    user_guess = int(self.user_text_field.get())
except ValueError:
    self.result_text.config(text="Please enter an integer.")
    return

if user_guess == self.equation_number_two:
    self.user_score += 1
    self.result_text.config(text="Correct! :)")
else:
    self.result_text.config(text="Wrong... :(")```
3. **Resetting the GUI for the Next Equation**:
```self.user_text_field.delete(0, tk.END)
self.generate_equation()
self.result_text.config(text="")
```
