#!/usr/bin/env python3
"""
passwordGenerator.py - A simple password generator.

Author: Carlos Valerio (CarlosValerioM)
Date: 2025/03/08
License: MIT
Dependencies: None (built-in functions only)

Description:
This script generates a random password based on user inputs for the number of letters, symbols, and numbers.
It prompts the user to specify how many letters, symbols, and numbers they want in the password,
and then generates a password with the desired characteristics.

Usage:
Run the script and follow the prompts:
    python passwordGenerator.py

Example Output:
    How many letters do you want in your password? 8
    How many symbols do you want in your password? 2
    How many numbers do you want in your password? 3
    Your generated password is: aB3!kL7#
"""
import random

# List of lowercase and uppercase letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# List of numbers from 0 to 9
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List of special symbols
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^',
           '_', '`', '{', '|', '}', '~']

# Prompt the user to specify the quantity of letters, numbers, and symbols for the password
quantityLetters = int(input("How many letters would you like in your password? "))
quantityNumbers = int(input("How many numbers would you like in your password? "))
quantitySymbols = int(input("How many symbols would you like in your password? "))

# Create an empty list to store the components of the new password
newPassword = []

# Add the requested number of random letters to the password list
for i in range(quantityLetters):
    newPassword += random.choice(letters)

# Add the requested number of random numbers to the password list
for i in range(quantityNumbers):
    newPassword += random.choice(numbers)

# Add the requested number of random symbols to the password list
for i in range(quantitySymbols):
    newPassword += random.choice(symbols)

# Shuffle the password list to randomize the order of characters
random.shuffle(newPassword)

# Convert the list of characters back into a single string
newPassword = "".join(newPassword)

# Display the newly generated password
print(f"Your new password is {newPassword}")

