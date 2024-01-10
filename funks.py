from database import *
from configparser import ConfigParser
parser = ConfigParser()
parser.read('treebase.ini')
saved_primary_color = parser.get('colors', 'primary_color')
saved_secondary_color = parser.get('colors', 'secondary_color')
saved_highlight_color = parser.get('colors', 'highlight_color')


def how_many_room():
    mycursor.execute(SELECT_ALL_ROOMS)
    count = len(mycursor.fetchall())
    return count


def add_room():
    newnumber = how_many_room()+1
    status = 1
    bednumber = input('how many beds this room has: ')
    area = input('how much is the area of the room: ')
    type = input('please enter the type of the room: ')
    mycursor.execute(INSERT_ROOM, (newnumber, status, bednumber, area, type))
    mydb.commit()


def check_guest_id(id):
    mycursor.execute(SELECT_GUEST_BY_ID, (id,))
    if mycursor.fetchall():
        return True


def add_reservation():
    guest_id = int(input('Enter your id:'))
    if check_guest_id(guest_id):
        room_number = input(f'select the number of the room you want(between 1 to {how_many_room()}):')
        sdate = input('pick your starting day(in type yyyy-mm-dd):')
        edate = input('pick your starting day(in type yyyy-mm-dd):')
        mycursor.execute(INSERT_RESERVE, (guest_id, room_number, sdate, edate))
        mydb.commit()
        print("your reservation is submitted")
    else:
        print('please enter a valid gust id or create a new ne')
        add_reservation()


def search_guest(data):
    mycursor.execute(SEARCH_Guest, (data['id'], data['fname'], data['lname'], data['email'], data['phone']))
    records = mycursor.fetchall()
    return records


def list_of_rooms():
    mycursor.execute(SELECT_ALL_ROOMS)
    all_rooms = mycursor.fetchall()
    print('rooms:')
    print('')
    for room in all_rooms :
        if room[1] == 1:
            status = 'available'
        else:
            status = 'not available'
        print(f'''room number : {room[0]} | status : {status} | bed number : {room[2]} | area : {room[3]} | type : {room[4]}''')


def change_room_status():
    mycursor.execute(SELECT_ALL_ROOMS)
    all_rooms = len(mycursor.fetchall())
    nroom = int(input('please select the number of the room you want: '))
    if nroom > all_rooms:
        print('this room does not exist')
    else:
        status = input('please type 1 for available and 2 for not available: ')
        mycursor.execute(CHANGE_STATUS_BY_ROOM_NUM, (status,nroom))
        mydb.commit()


def list_of_available_rooms():
    mycursor.execute(SELECT_ALL_AVAILABLE_ROOMS)
    all_rooms = mycursor.fetchall()
    print('rooms:')
    print('')
    for room in all_rooms :
        print(f'''room number : {room[0]} | status : available | bed number : {room[2]} | area : {room[3]} | type : {room[4]}''')


def add_new_guest(data):
    mycursor.execute(INSERT_GUEST, (data['fname'], data['lname'], data['email'], data['phone'], data['password']))
    mydb.commit()


def update_guest(data):
    mycursor.execute(UPDATE_GUEST_ALL, (data['fname'], data['lname'], data['email'], data['phone'], data['password'], data['id']))
    mydb.commit()


def delete_guest(id):
    mycursor.execute(DELETE_GUEST, (id,))
    mydb.commit()


def check_email_phone(email,phone):
    mycursor.execute(CHECK_GUEST, (phone, email))
    guest =mycursor.fetchone()
    if guest:
        return True


def login(data):
    mycursor.execute(LOGIN, (data['email'], data['password']))
    user = mycursor.fetchone()
    if user:
        if user[2] == 'master':
            return 'master'
        return True

def all_guest():
    mycursor.execute(SELECT_ALL_GUEST)
    records = mycursor.fetchall()
    return records