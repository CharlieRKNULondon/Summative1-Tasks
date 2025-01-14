"""Players generally sit in a circle. 
The player designated to go first says the number "one", and the players then count upwards in turn. 
However, any number divisible by three is replaced by the word fizz and any number divisible by five is replaced by the word buzz. 
Numbers divisible by both three and five (i.e. divisible by fifteen) become fizz buzz. 
A player who hesitates or makes a mistake is eliminated.
For example, a typical round of fizz buzz would start as follows:
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, Fizz Buzz, 31, 32, Fizz, 34, Buzz, Fizz, ..."""

#FizzBuzz_Range = int(input("Please enter your final number for entry in the fizz buzz list"))

def FizzBuzz_Solver(FizzBuzz_Range):
    """A simple function which works out the Fizz Buzz problem within a given range of numbers"""
    FizzBuzz_list = []
    for number in range(1, (FizzBuzz_Range+1)): # For loop to iterate through list.
        if number % 3 == 0 and number % 5 == 0: #Determining if number is divisible by 3 and 5
            FizzBuzz_list.append("Fizz Buzz")
        elif number % 3 == 0: #Determining if divisible 3
            FizzBuzz_list.append("Fizz")
        elif number % 5 == 0:
            FizzBuzz_list.append("Buzz")
        else: #if not divisible, adds the number to the list
            FizzBuzz_list.append(number)
    
    return FizzBuzz_list

