# Day-5-Password-Generator
Your Random Password Generator - Difficulty: Easy

# RandomPasswordGenerator

## Author:
Carlos Valerio (CarlosValerioM)

## Date:
2025/03/08

## License:
MIT License

## Dependencies:
None (built-in functions only)

## Description:
`passwordGenerator.py` is a Python script that generates a random password based on the user's desired number of letters, numbers, and symbols. It prompts the user for the following inputs:
1. The number of letters to include in the password.
2. The number of numbers to include in the password.
3. The number of symbols to include in the password.

It then generates a password by randomly selecting characters from predefined lists of uppercase and lowercase letters, numbers, and symbols. The script then shuffles the generated characters to ensure the password is randomized.

## Usage:

1. Clone this repository:

```bash
git clone https://github.com/CarlosValerioM/Day-5-Random-Password-Generator.git
```
Navigate to the project directory:

```bash
cd Day-3-Random-Password-Generator
```
Run the script:
```bash
python passwordGenerator.py
```
The script will prompt you for input, and based on your responses, it will generate a randomized password.

## Example Output:
How many letters would you like in your password? 8

How many numbers would you like in your password? 3

How many symbols would you like in your password? 2

Your new password is Dt1i3DE'&0iIa

## How it works:
The script asks the user for the number of letters, numbers, and symbols to include in the password.

It generates a random selection of letters, numbers, and symbols by randomly choosing from predefined lists.

The characters are shuffled to randomize the order.

The final password is then displayed to the user.

## License:
This project is licensed under the MIT License.
