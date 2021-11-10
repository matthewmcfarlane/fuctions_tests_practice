def return_10():
    return 10

def add(number_1, number_2):
    return number_1 + number_2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1+string_2

def add_string_as_number(str_1, str_2):
    return int(str_1) + int(str_2)

months = {
    1 : "January",
    2 : "February",
    3 : "March",
    4 : "April",
    5 : "May",
    6 : "June",
    7 : "July",
    8 : "August",
    9 : "September",
    10 : "October",
    11 : "November",
    12 : "December",
}

def number_to_full_month_name(number):
        return months[number]

def number_to_short_month_name(number):
        return months[number][:3]


def volume_of_cube(length):
    return length **3

def reverse_string(x):
    return x[::-1]

def fahrenheit_to_celsius(fh):
    return int((fh - 32)*0.556)