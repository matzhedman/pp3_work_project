import gspread
import colorama
import os
import datetime
from google.oauth2.service_account import Credentials



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
    print('Hello, welcome to laundry booking!')
    print('Please login to book a time,\nor to see your current bookings.')
    print('Enjoy your day!')

    x = datetime.datetime.now()
    print('____________\n')
    print("Date and time of today:")
    print(x.strftime("%A"))
    print(x.strftime("%x"))
    print('____________\n')

def mainMenu():
    print('MAIN MENU \n')
    print('1) Book a Time')
    print('2) Show my Booking')
    print('3) Log Out\n')   
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
        elif choice == 3:
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
    from colorama import Fore
    print(Fore.RED + '\nYou are logged out!')
    print(Fore.WHITE +'____________\n')    
    start()
    mainMenu()

def monday():
    print('You want to to the laundry on monday')
def tuesday():
    print('You want to to the laundry on tuesday')



start()
mainMenu()


