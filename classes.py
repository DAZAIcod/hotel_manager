class Hotel():

    def __init__(self, name:str):

        self.hotel_name = name
        self.rooms = []
        self.bookings = []

    def add_room(self):
        num = len(self.rooms)+1
        room_number = 1
        while int(room_number) < num:
            room_number = input(f"what is the number of this room?(recommend:{num}) ")
        room_type = 0
        while room_type not in ('1','2','3') :
            room_type = input('enter the type of room(1.1 bed,2.2 bed ,3.sweet): ')
        room = Room(number=room_number, status='not reserved', met='70', type= room_type)
        self.rooms.append(room)

    def remove_room(self, room):

        self.rooms.remove(room)

    def make_booking(self, room, guest, start_date, end_date):

        self.bookings.append(Booking(id, guest, room, start_date, end_date))


class Room():

    def __init__(self, number: str, status: str, met: str, type: str):
        self.number = number
        self.type = type
        self.status = status
        self.met = met

    def update_status(self, status: str):
        self.status = status


class Booking():

    def __init__(self,booking_id =booking_id, guest = guest, room = room, start_date =start_date, end_date= end_date ):
        self.booking_id = booking_id
        self.guest = guest
        self.room = room
        self.start_date = start_date
        self.end_date = end_date

    def check_status(self):
        None


sadr = Hotel('sadr')

