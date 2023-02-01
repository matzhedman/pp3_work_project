import gspread
import colorama
import os
import datetime
from google.oauth2.service_account import Credentials
from colorama import Fore

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('pp3_work_project')


"""
To run the program: python3 run.py
"""


def start():
    """
    First view, asks you to type in your name.
    Name should be logged and be added to the summary in the end - not working yet.
    """
    print('\nHello, welcome to laundry booking!\n')
    print('Please type in your name to book a time,\nor to see current bookings.\n')
    print('____________\n')
    print(Fore.GREEN + 'Enjoy your day!')
    print(Fore.WHITE + '____________\n')
    print('Enter your name: ')
    name = input()

    """
    Function not working yet
    """
    # def worksheet_name_update(data, worksheet):
    #     worksheet_to_update = SHEET.worksheet(worksheet)
    #     worksheet_to_update.append_row(data)


def mainMenu():
    """
    Menu. 
    Shows the day and date of today.
    Gives three choices to navigate further.
    """
    os.system('clear')
    x = datetime.datetime.now()
    print('____________\n')
    print("Date and time of today:")
    print(x.strftime("%A"))
    print(x.strftime("%x"))
    print('____________\n')

    print('MAIN MENU \n')
    print('1) Book a Time')
    print('2) Show all current Bookings')
    print('00) Back to Start\n')
    while True:
        try:
            choice = int(input('Type in number to choose an option: \n'))
        except ValueError:
            print("Not a valid number")

        if choice == 1:
            choose_a_day()
            break
        elif choice == 2:
            show_my_booking()
            break
        elif choice == 00:
            log_out()
        else:
            print('Not a valid number, please choose 1), 2) or 00).')


# Choose a day
def choose_a_day():
    os.system('clear')
    print('Choose a day:\n')
    days = SHEET.worksheet('laundry_days').get_all_values()

    for day in days:
        print(day)
    while True:
        try:
            choice = int(input('\nType in a number to choose a day: \n'))
        except ValueError:
            print('Not a valid number')

        if choice == 1:
            print('You chose Monday.')
        elif choice == 2:
            print('You chose Tuesday.')
        elif choice == 3:
            print('You chose Wednesday.')
        elif choice == 4:
            print('You chose Thursday.')
        elif choice == 5:
            print('You chose Friday.')
        elif choice == 6:
            print('You chose Saturday.')
        elif choice == 7:
            print('You chose Sunday.')
        times()


# Show my bookings menu
def show_my_booking():
    """
    Function not working yet. Bookings should be added to spreadsheet, 
    when going in to this menu it should get all bookings, if any, from the spreadsheet
    and show it here. 
    No bookings? -> a message that says "No current booking"
    """
    print('Your bookings')

# Log out


def log_out():
    os.system('clear')
    print(Fore.RED + '\nYou are logged out!')
    print(Fore.WHITE + '____________\n')
    main()

# Times


def times():
    os.system('clear')
    print('\nPlease choose a time: \n')

    print('1) 7.00 AM - 11.00 AM')
    print('2) 11.00 AM - 3.00 PM')
    print('3) 3.00 PM - 7.00 PM')
    print('4) 7.00 PM - 10.00 PM')
    while True:
        try:
            choice = int(input('Type in number to choose an option: \n'))
        except ValueError:
            print("Not a valid number")
        if choice == 1:
            print('placeholder1')

        summary()


def summary():
    os.system('clear')
    print('This is the day "day should appear here"\n')
    print('Would you like to confirm, and go back to Start?')
    answer = input("(yes / no)\n")
    if answer == 'yes':
        os.system('clear')
        main()
    elif answer == 'no':
        os.system('clear')
        choose_a_day()


def main():
    """
    Run all program functions
    """
    start_up = start()
    menu = mainMenu()
    laundry_times = times()
    summary_end = summary()


main()
