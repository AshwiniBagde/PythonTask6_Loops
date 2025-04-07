# Example 1: Password Validation

correct_password = 'python123'
attempts = 0

while attempts < 3:
    password = input('Enter your password: ')
    if password == correct_password:
        print('Access Granted!')
        break
    else:
        print('Incorrect Password!')
        attempts += 1
else:
    print('Maximum attempts reached. Access denied.')



# Example 2: Checking for Prime Numbers

def is_prime(number):
    if number <= 1:
        return False
    for i in range (2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

while True:
    user_input = input('Enter a number ("exit" to quit): ')
    if user_input.lower() == "exit":
        break
    if is_prime(int(user_input)):
        print('The number is prime.')
    else:
        print('The number is not prime.')



# Example 3: Counting Vowels in a List of Words

words = ['hello', 'python', 'world', 'apple', 'ashwini', 'arc', 'rose', 'suthiksh', 'myth' ]

def count_vowels(word):
    vowels = 'aeiou'
    return sum(1 for char in word.lower() if char in vowels)

index = 0

while index < len(words):
    word = words[index]
    print(f"The word '{word}' has {count_vowels(word)} vowels.")
    index += 1 



# Example 4: Temperature Alert System

temperature_data = [
{'temperature': 35 , 'status' : '' },
{'temperature': 37 , 'status' : '' },
{'temperature': 39 , 'status' : '' },
{'temperature': 41 , 'status' : '' },
{'temperature': 43 , 'status' : '' },
{'temperature': 45 , 'status' : '' },
{'temperature': 47 , 'status' : '' }
]

index = 0

while index < len(temperature_data):
    data = temperature_data[index]
    if data['temperature'] > 40:
        data['status'] = (f'Warning! Temperature too high: {data["temperature"]}°C')
    else:
        data['status'] = (f'Temperature is fine: {data["temperature"]}°C')
    index += 1


index = 0

while index < len(temperature_data):
    print(temperature_data[index]["status"])
    index += 1

print("System check complete. Shutting down!")



# Example 5: calculate power of a number using while loop

def calculate_power(base, exponent):
    return base ** exponent

# while loop for multiple calculations

while True:
    base = input('Enter base number (or type "stop" to quit): ')
    if base.lower() == "stop":
        break
    exponent = int(input('Enter exponent: '))

    result = (f'{base} ^ {exponent} = {calculate_power(int(base), exponent)}')

    print(result)



# Example 6: Check whether a number is even or odd

number = 1

while number <= 15:
    if number % 2 == 0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')
    number += 1



# Example 7: Check grade based on marks

while True:
    marks = int(input('Enter your marks (type -1 to stop): '))
    if marks == -1:
        print('Exiting the program!')
        break
    if marks >= 90:
        print('Grade A')
    elif marks >= 80:
        print('Grade B')
    elif marks >= 70:
        print('Grade C')
    elif marks >= 60:
        print('Grade D')
    else:
        print('Grade E')



# Example 8: Guess secret number

secret_number = 6

guess = 0

while guess != secret_number:
    guess = int(input('Guess the secret number between 1 to 10 : '))
    if guess < secret_number:
        print('Too low')
    elif guess > secret_number:
        print('Too high')
    else:
        print('You guessed it!!')



# Example 9: Sum of even numbers

num = 1
Total = 0

while num <= 20:
    if num % 2 == 0:
        Total += num
    num += 1

print(f'Sum of even numbers from1 to 20: {Total}')



# Example 10: Multiplication Table

def multiplication_table(number, multiplier):
    return (number * multiplier)

# while loop to generate the table

number = 2
multiplier = 1

while multiplier <= 20:
    print(f'{number} * {multiplier} = {multiplication_table(number , multiplier)}')
    multiplier += 1

