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

def start():
    print('Hello, welcome to laundry booking!\n')
    print('Please type in your name to book a time,\nor to see current bookings.\n')
    print('____________\n')
    print(Fore.GREEN + 'Enjoy your day!')
    print(Fore.WHITE + '____________\n')

    print('Enter your name: ')
    name = input()

    def worksheet_name_update(data, worksheet):
        worksheet_to_update = SHEET.worksheet(worksheet)
        worksheet_to_update.append_row(data)

    

def mainMenu():
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

      
#Book a day
def choose_a_day():
    print('Choose a day:\n')
    days = SHEET.worksheet('laundry_days').get_all_values()

    for day in days:
        print(day)
        

    while True:
        try:
            choice = int(input('Type in a number to choose a day: \n'))
        except ValueError:
            print('Not a valid number')
            
        if choice == 1:
            monday()            
            break
        elif choice == 2:
            tuesday()
            break
        elif choice == 3:
            wednesday()
            break
        elif choice == 4:
            thursday()
            break
        elif choice == 5:
            friday()
            break
        elif choice == 6:
            saturday()
            break
        elif choice == 7:
            sunday()
    

        
#Show my bookings menu
def show_my_booking():
    print('Your bookings')

#Log out
def log_out():
    os.system('clear')
    print(Fore.RED + '\nYou are logged out!')
    print(Fore.WHITE + '____________\n')    
    start()
    mainMenu()

#Times
def times():
    print('1) 7.00 AM - 11.00 AM')
    print('2) 11.00 AM - 3.00 PM')
    print('3) 3.00 PM - 7.00 PM')
    print('4) 7.00 PM - 10.00 PM')

#Days
def monday():
    print('\nYou want to do the laundry on Monday')
    print('Please choose a time: ')
    times()

def tuesday():
    print('\nYou want to to the laundry on Tuesday')
    print('Please choose a time: ')
    times()
def wednesday():
    print('\nYou want to to the laundry on Wednesday')
    print('Please choose a time: ')
    times()
def thursday():
    print('\nYou want to to the laundry on Thursday')
    print('Please choose a time: ')
    times()
def friday():
    print('\nYou want to to the laundry on Friday')
    print('Please choose a time: ')
    times()
def saturday():
    print('\nYou want to to the laundry on Saturday')
    print('Please choose a time: ')
    times()
def sunday():
    print('\nYou want to to the laundry on Sunday')
    print('Please choose a time: ')
    times()


def main():
    start_up = start()
    menu = mainMenu()

main()
