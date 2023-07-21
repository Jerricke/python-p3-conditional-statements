#!/usr/bin/env python3


def admin_login(username, password):
    access = "granted" if username.lower() == "admin" and password == '12345' else "denied"
    return f"Access {access}"
    pass

def hows_the_weather(temperature):
    if temperature < 40:
        weather = "It's brisk out there!"
    elif 40 <= temperature <= 65:
        weather = "It's a little chilly out there!"
    elif temperature == 75:
        weather = "It's perfect out there!"
    else:
        weather = "It's too dang hot out there!"
    return weather
    pass

def fizzbuzz(num):
    word = num
    if num%3 == 0 and num%5 == 0:
        word = "FizzBuzz"
    elif num%3 == 0:
        word = "Fizz"
    elif num%5 == 0:
        word = "Buzz"
    else: 
        word = num
    return word
    pass

def calculator(operation, num1, num2):
    operations = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2,
    }
    result = operations.get(operation)
    if result == None:
        print("Invalid operation!")
    return result
    pass

print(calculator("nope", 4, 2))