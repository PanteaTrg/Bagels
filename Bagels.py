import random


def get_input(max_dig: int):
    max_try = 5
    try_cnt = 1

    while try_cnt <= max_try:
        print(f'Try #{try_cnt}')
        user_input = input('>')
        if len(user_input) != max_dig or not user_input.isdecimal():
            if try_cnt == 1:
                print('دوست عزیز! عدد 3 رقمی وارد کن')
                try_cnt += 1
            elif try_cnt == 2:
                print('برای بار سوم خواهش می کنم عدد وارد کن!')
                try_cnt += 1
            elif try_cnt == 3:
                print('عدد 3 رقمی لطفا!!')
                try_cnt += 1
            elif try_cnt == 4:
                print('ای بابا !')
                try_cnt += 1
            elif try_cnt == 5:
                print('این دیگه آخرین فرصتت بود :(')
                try_cnt += 1
            if try_cnt > max_try:
                print('ازت خواهش کردم عدد 3 رقمی وارد کنی نکردی! دیگه فرصتی نداری !')
                return 0
        else:
            return user_input


print()
print()
print('I am thinking of a 3-digit number. Try to guess what it is :).')
print('Here are some clues:')
print('When I say:       That means:')
print('   Pico           The digit is correct but in the wrong position')
print('   Fermi          The digit is correct and in the right position')
print('   Bagels         No digit is correct')
print()
print('Ok, I have thought up a number.')
print('You have 10 times to guess the correct number. Good luck :)')
print()

secret_number = [int(digit) for digit in str(random.randint(100, 999))]

while True:
    max_guesses = 10
    max_digit = 3

    number_of_guess = 1
    while number_of_guess <= max_guesses:

        print()
        print()
        print(f'Guess #{number_of_guess}: ')
        input_number = get_input(max_digit)
        if input_number == 0:
            break

        else:
            guess_number = [int(char) for char in input_number]
            numbers_intersect = list(set(secret_number) & set(guess_number))
            if guess_number == secret_number:
                print('Congrats!')
                break
            elif not numbers_intersect:
                print('Bagels', end='')
            else:
                for j in range(len(guess_number)):
                    if guess_number[j] == secret_number[j]:
                        print('Fermi ', end='')
                    elif guess_number[j] in secret_number:
                        print('Pico ', end='')
            number_of_guess += 1

        if number_of_guess > max_guesses:
            print()
            print('\nSorry! time is up!. You used all your chances to guess the correct number!')
            print('\nThe secret number is: {}.'.format(int(''.join(map(str, secret_number)))))

    answer = input('\nDo you want to play again?: [Y/N]').lower()
    if answer == 'n':
        print('Thanks for playing! See you Soon :) ')
        break
