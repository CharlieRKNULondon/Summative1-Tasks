# Equation Game

## Project Overview

The Equation Game is a simple game, which uses tkinkter as a GUI, enabling users to practice their division skills to identify the value of x, which is missing from the equation. Each time the user presses next equation, a new random number will be generated.

![image](https://github.com/user-attachments/assets/9eca4eb8-3f99-421c-badb-738032e2b290)

## User Documentation

### Game Objective

This Equation Game is designed to engage users in solving math problems in an interactive way. The goal of this game is to challenge the user to solve multiplication equations by determining the missing integer.

Skills users can improve through repeatedly solving equations:

**-** Mental Math Skills: practice quick calculations without using a calculator.

**-** Problem Solving Abilities: strengthen logical thinking by analyzing equations.

**-** Focus and Accuracy: encourages attention to detail by solving problems.

### Prerequisites

 **-** Any version of Python 3.8 or later installed on your computer.
 
 **-** Tkinkter (Python Library)
 
 **-** Random (Python Library)

### How to Get an IDE

#### What is an IDE?
An Integrated Development Environment (IDE) is a software application that provides tools to write, debug, and run code. Examples include PyCharm, Visual Studio Code, or IDLE (included with Python).

#### Steps to Install an IDE:

#### PyCharm:

Visit https://www.jetbrains.com/pycharm/ and download the Community Edition (free).

Follow the installation instructions for your operating system.

#### Visual Studio Code:

Visit https://code.visualstudio.com/ and download VS Code.

Install the Python extension from the Extensions Marketplace.

 ### How to Play

 1. Download the Python File and run the game in any IDE of your choice
 2. Read the equation carefully. Solve for x the missing number.
 3. Enter your answer (must be an integer) in the text box.
 4. Press **Submit** to check your answer. The game will provide feedback, either, "Correct!" or "Wrong...".
 5. If you are correct your score will be incremented by 1.
 6. If you would like to skip an equation or move to another, press the **Next Equation** button.

### Troubleshooting ###

**- The program is unresponsive**: check you have Python and Tkinkter installed within user OS. If needed restart the program.
**- Non-Numeric error:** double-Check your input, you can only enter integers.

#### Example Gameplay

What the game looks like in action:

 ![image](https://github.com/user-attachments/assets/27e4ae8d-3687-427d-ada4-5b76689cff68)

![image](https://github.com/user-attachments/assets/ed755033-6c04-4f43-8dcf-b3eb6ae86174)


## Techical Documentation

### How to Get Python and Check the Version

Download and install Python:

Visit the official Python website: https://www.python.org/.

Download the latest version compatible with your operating system (Windows, macOS, or Linux).

Follow the installation instructions for your operating system. 

After installing:

Open a terminal or command prompt.

Type the following command and press Enter: ```python --version```

The installed Python version will be displayed. Ensure it is 3.8 or later.


### Code Structure

 1. ```EquationGame``` **Class**
This utilises the features of Object Orientated Programming (OOP). The class manages the core functionality of the game and allows variables to be shared between methods whilst remaining local.
 2. **Methods**
    **-** ```__init__(self, root)``` Initialises the game state, variables such as score and GUI setup.
    
    **-** ```build_gui(self)``` Constructs the GUI using tkinkter labels, text fields and buttons.
    
    **-** ```generate_equation(self)``` Generates a new equation with two random integers between 0 and 999.
    
    **-** ```check_user_answer(self):``` Validates user input and checks it against the correct answer. It also updates the score and feedback based on if the user is correct.
    
    **-** ```next_equation(self)``` Clears the text field, and prepares a new equation for the using.

### Key Variables

**-** ```self.user_score```: tracks the user's current score.

**-** ```self.equation_number_one``` : the first random integer in the equation.

**-** ```self.equation_number_two``` : the second random integer in the equation, this is used to check against user input to validate if it is correct.

**-** ```self.equation_result```: the result of multiplying the two integers.


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
    self.result_text.config(text="Wrong... :(")
```

3. **Resetting the GUI for the Next Equation**:
```self.user_text_field.delete(0, tk.END)
self.generate_equation()
self.result_text.config(text="")
```
