"""

Plan for how the calculator should work:
    1. User types their first number, hits the -> button
    2. User types their second number
    2. (ALTERNATE) User chooses the % option, and the number is converted
    3. User chooses the operation that they wish to apply (+, -, x, /)
    4. The first and second number are then added, subtracted, etc. and that value is stored
    5. The user either resets the calculator, or will input another number and the process will continue

Example:
    1. 1234   (1st Number)
    2. 5678   (2nd Number)
    3. +      (Chooses Operator)
    4. 6912   (Result is Shown & Stored)
    5. 6910   (2nd Number)
    6. -      (Chooses Operator)
    7. 2      (Answer is Shown)
    8. c      (User Clears and Resets the Calculator)

"""


from tkinter import *

root = Tk()
root.configure(background='tan')
root.geometry('160x130')

###############################

equation = StringVar()  # The equation that is shown in the entry
equation.set('')

equation_string = ''  # The equation that is manipulated in the program

result = 0  # The end result of the calculation

first_number = 0
second_number = 0

current_number = "first"

entry = Entry(textvariable=equation, width=25, bg='dark grey')
# Creates the entry for the equation

button_0 = Button(text='0', width=3, bg='black', fg='light grey', command=lambda: add_to_equation('0', False, None))
button_1 = Button(text='1', width=3, bg='black', fg='light grey', command=lambda: add_to_equation('1', False, None))
button_2 = Button(text='2', width=3, bg='black', fg='light grey', command=lambda: add_to_equation('2', False, None))
button_3 = Button(text='3', width=3, bg='black', fg='light grey', command=lambda: add_to_equation('3', False, None))
button_4 = Button(text='4', width=3, bg='black', fg='light grey', command=lambda: add_to_equation('4', False, None))
button_5 = Button(text='5', width=3, bg='black', fg='light grey', command=lambda: add_to_equation('5', False, None))
button_6 = Button(text='6', width=3, bg='black', fg='light grey', command=lambda: add_to_equation('6', False, None))
button_7 = Button(text='7', width=3, bg='black', fg='light grey', command=lambda: add_to_equation('7', False, None))
button_8 = Button(text='8', width=3, bg='black', fg='light grey', command=lambda: add_to_equation('8', False, None))
button_9 = Button(text='9', width=3, bg='black', fg='light grey', command=lambda: add_to_equation('9', False, None))
button_dec = Button(text='.', width=3, bg='black', fg='light grey', command=lambda: add_to_equation('.', False, None))
# Creates the number-related buttons

button_add = Button(text='+', width=3, bg='black', fg='light grey', command=lambda: add_to_equation(' + ', True, 1))
button_sub = Button(text='-', width=3, bg='black', fg='light grey', command=lambda: add_to_equation(' - ', True, 2))
button_mult = Button(text='x', width=3, bg='black', fg='light grey', command=lambda: add_to_equation(' x ', True, 3))
button_div = Button(text='/', width=3, bg='black', fg='light grey', command=lambda: add_to_equation(' / ', True, 4))
button_per = Button(text='%', width=3, bg='black', fg='light grey', command=lambda: add_to_equation(' % ', True, 5))
button_neg = Button(text='+/-', width=3, bg='black', fg='light grey', command=lambda: add_to_equation(' -', True, 6))
# Creates the operator buttons

button_clr = Button(text='c', width=3, bg='black', fg='light grey', command=lambda: clear_equation(True))
button_eql = Button(text='=', width=3, bg='black', fg='light grey', command=lambda: clear_equation(False))
# Creates the clear and equals buttons

button_nextNum = Button(text='->', width=3, bg='black', fg='light grey', command=lambda: add_to_equation('', True, 7))
# This button lets the user switch to the next number that they wish to change

###############################

# Organizes all the elements with .grid()
entry.grid(row=0, column=0, columnspan=5)

button_0.grid(row=4, column=0)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_dec.grid(row=4, column=2)

button_add.grid(row=3, column=3)
button_sub.grid(row=3, column=4)
button_mult.grid(row=2, column=3)
button_div.grid(row=2, column=4)
button_per.grid(row=1, column=3)
button_neg.grid(row=1, column=4)

button_clr.grid(row=4, column=1)
button_eql.grid(row=4, column=4)

button_nextNum.grid(row=4, column=3)

###############################


def clear_equation(clear):
    global equation_string
    global first_number
    global second_number
    global result
    global current_number

    if clear:
        equation.set('')
        equation_string = ''
        result = 0
        first_number = 0
        second_number = 0
        current_number = 'first'
        # reset the equations

    elif not clear:  # Once I changed how the calculator worked, I realized that I don't really need an equals button
        equation.set('')
        equation_string = ''
        result = 0
        first_number = 0
        second_number = 0
        current_number = 'first'


def add_to_equation(value, operator, operator_choice):
    global equation_string
    global result
    global first_number
    global second_number
    global current_number

    temp = equation.get()
    new_equation = temp + value
    equation.set(new_equation)
    entry.configure(textvariable=equation)

    if not operator:
        if current_number == "first":
            result += int(value)
            temp_string = str(first_number) + value
            first_number = int(temp_string)
            equation_string += str(first_number)

        elif current_number == "second":
            result += int(value)
            temp_string_2 = str(second_number) + value
            second_number += int(temp_string_2)
            equation_string += str(second_number)

    elif operator:
        if operator_choice == 1:  # Addition
            result = first_number + second_number
            equation.set(result)
        if operator_choice == 2:  # Subtraction
            result = first_number - second_number
            equation.set(result)
        if operator_choice == 3:  # Multiplication
            result = first_number * second_number
            equation.set(result)
        if operator_choice == 4:  # Division
            result = first_number / second_number
            equation.set(result)
        if operator_choice == 5:  # Percentage (This does not work)
            pass
        if operator_choice == 6:  # Negative/Positive (This does not work very well)
            pass
            # result = first_number * -1
            # equation.set(result)
        if operator_choice == 7:
            current_number = "second"
            equation.set('')


###############################

root.mainloop()
