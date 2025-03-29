import tkinter

def add(numbers):
    result = 0
    for number in numbers:
        result += number
    return result
    
def subtract(numbers):
    result = 0
    for number in numbers:
        result -= number
    return result

def multiply(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result *= number
    return result

def divide(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result /= number
    return result

def module(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result %= number
    return result

#si me voy a otro archivo te vienes conmigo o te puedes quedar editando este? oka


def resolve(operation, numbers):
    match operation:
        case "sumar":
            return add(numbers)
        case "restar":
            return subtract(numbers)
        case "multiplicar":
            return multiply(numbers)
        case "dividir":
            return divide(numbers)
        case "modulo":
            return module(numbers)

def string_to_array(string):
    chars = string.split(" ")
    return chars

def chars_to_numbers(char_array):
    numbers = [int(char) for char in char_array]
    return numbers #donde
