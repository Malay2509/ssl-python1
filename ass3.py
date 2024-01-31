def check_even_odd(number):
    '''Checks if the given number is even or odd.'''
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
user_input = int(input("Enter a number: "))
result = check_even_odd(user_input)
print(f"The number {user_input} is {result}.")
