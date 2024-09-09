"""This is a program to calculate the monthly payment on a loan"""
import json
import os
import sys

def prompt(string1):
    """Format the display for each prompt"""
    print(f'>>>{string1}')

def invalid_number(number_str):
    """Validate each entry and return error if invalid"""
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def messages(message):
    """Get messages from JSON"""
    return MESSAGES[message]

def clear():
    """Clear terminal after each calculation"""
    os.system('clear')

with open('loan_calculator.json', 'r') as file:
    MESSAGES = json.load(file)

def another_calculation():
    """Ask the user if they want to perform another calculation"""
    prompt(messages('another_calculation'))
    answer = input()
    answer_clean = answer[0].lower()
    match answer_clean:
        case "y":
            clear()
        case "n":
            clear()
            sys.exit(0)
        case _:
            prompt(messages('another_calc_error'))
            another_calculation()

prompt(messages('welcome'))

clear()

while True:
#prompt user for loan amount
    while True:
        prompt(messages('amount_prompt'))
        amount = input()

        if not invalid_number(amount) and float(amount) > 0:
            break

        prompt(messages('invalid_amount'))

    while True:
        prompt(messages('apr_prompt'))
        annual_rate = input()

        if not invalid_number(annual_rate) and float(annual_rate) >= 0:
            break
        prompt(messages('invalid_apr'))

    while True:
        prompt(messages('duration_prompt'))
        duration_months = input()

        if not invalid_number(duration_months) and float(duration_months) > 0:
            break
        prompt(messages('invalid_duration'))


    monthly_rate = float(annual_rate)/12/100

    if float(monthly_rate) == 0:
        monthly_payment = float(amount) / (float(duration_months))
    else:
        monthly_payment = float(amount) * (float(monthly_rate) / (1 - (1 + float(monthly_rate)) **
                                                                  (-float(duration_months))))

    rounded_payment = round(float(monthly_payment), 2)
    prompt(messages('result').format(rounded_payment=rounded_payment))

    another_calculation()

    clear()
