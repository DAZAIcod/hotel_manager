from funks import *

MenuText = '''welcome to HOTEL SYSTEM MANAGER :
options:
1)add a new room to hotel
2)add a new reservation
3)change room status
4)available rooms
5)check the Booking menu
6)show the list of the rooms
7)add a new guest

please select a number : '''

def runn():
    n = input(MenuText)
    while n != '8':
        if n == '1':
            add_room()
            print('1 room added')

        elif n == '2':
            add_reservation()

        elif n == '3':
            change_room_status()
            input('type anything to back:')

        elif n == '4':
            list_of_available_rooms()
            input('type anything to back:')

        elif n == '6':
            list_of_rooms()
            input('type anything to back:')

        elif n == '7':
            add_new_guest()

        else:
            print('select valid character')
            return runn()

        n = int(input(MenuText))





if __name__ == "__main__":
    runn()