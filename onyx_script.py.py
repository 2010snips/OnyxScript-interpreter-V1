# OnyxScript: A Custom Programming Language Inspired by C#

# Purpose and Philosophy:
# OnyxScript aims to be a versatile language suitable for various domains.
# It combines the best features of C# and Python while maintaining readability and safety.

# Key Features of OnyxScript:
# - Statically Typed: Type safety and early error detection.
# - Modern Syntax: Concise, expressive, and readable.
# - Object-Oriented: Classes, inheritance, and encapsulation.
# - Memory Management: Automatic memory management (garbage collection).
# - Interoperability: Seamless integration with existing Python and C# libraries.

# Real-World Use Cases:
# 1. Web Development: Build web applications using frameworks like Flask or FastAPI.
# 2. Game Development: Create game logic, AI, and scripting for game engines.
# 3. Scientific Computing: Numerical simulations, data analysis, and machine learning.
# 4. Automation: Write scripts for system administration, data processing, and more.
# 5. Embedded Systems: Develop firmware for microcontrollers and IoT devices.

# Sample OnyxScript Code:

# Define a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# Define a function
def calculate_square(num):
    return num * num

def main():
    # Create an instance of Person
    alice = Person("Alice", 30)
    alice.greet()

    # Use the function
    num = 5
    square = calculate_square(num)
    print(f"The square of {num} is {square}")

if __name__ == "__main__":
    main()
