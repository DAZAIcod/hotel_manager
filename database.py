import mysql.connector

CREATE_TABLE_ROOM = '''CREATE TABLE IF NOT EXISTS Room (
                RoomNumber int,
                Status int,
                BedNumber int,
                Met varchar(3),
                Type varchar(20)
                );'''
INSERT_ROOM = 'INSERT INTO Room (RoomNumber, Status, BedNumber, Met, Type) VALUES (%s,%s,%s,%s,%s)'
SELECT_ALL_ROOMS = 'SELECT * FROM Room'
SELECT_ALL_AVAILABLE_ROOMS = 'SELECT * FROM Room WHERE Status = 1'
CHANGE_STATUS_BY_ROOM_NUM = "UPDATE Room SET Status = %s WHERE RoomNumber = %s"


CREATE_TABLE_GUEST = '''CREATE TABLE IF NOT EXISTS Guest(
                GuestID int(10) unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
                FName varchar(30) NOT NULL,
                LName varchar(40) NOT NULL,
                Email varchar(100) NOT NULL,
                phone varchar(12) NOT NULL,
                password varchar(20) NOT NULL
                );'''

INSERT_GUEST = "INSERT INTO Guest (FName,LName,Email,phone, password) VALUES(%s,%s,%s,%s,%s) "
UPDATE_GUEST_ALL = "UPDATE Guest SET FName=%s, LName=%s, Email=%s, phone=%s, password=%s WHERE GuestID = %s"
DELETE_GUEST = "DELETE FROM Guest WHERE GuestID = %s"
CHECK_GUEST = "SELECT * FROM Guest WHERE phone=%s OR Email=%s"
SELECT_GUEST_BY_ID = "SELECT * FROM Guest WHERE GuestID=%s"
LOGIN = "SELECT * FROM Guest WHERE Email = %s and password = %s"
SELECT_ALL_GUEST = "SELECT * FROM Guest"
SEARCH_Guest = "SELECT * FROM Guest WHERE GuestID = %s OR FName LIKE %s OR LName LIKE %s OR Email LIKE %s OR phone LIKE %s"

CREATE_TABLE_Booking = '''CREATE TABLE IF NOT EXISTS Booking(
                BookingID int(10) unsigned NOT NULL AUTO_INCREMENT,
                GuestID int(10) unsigned NOT NULL ,
                RoomNumber int NOT NULL,
                SDate DATE NOT NULL,
                EDate DATE NOT NULL,
                PRIMARY KEY (BookingID),
                FOREIGN KEY (GuestID) REFERENCES Guest(GuestID) 
                ON UPDATE CASCADE ON DELETE RESTRICT,
                FOREIGN KEY (RoomNumber) REFERENCES Room(RoomNumber)
                ON UPDATE CASCADE
                );'''
INSERT_RESERVE = 'INSERT INTO Booking (GuestID, RoomNumber, SDate, EDate) VALUES (%s,%s,%s,%s)'

mydb = mysql.connector.connect(
  host="localhost",
  user="kd",
  password="algorithm",
  database="hoteldb"
)

mycursor = mydb.cursor()
mycursor.execute(CREATE_TABLE_ROOM)
mycursor.execute(CREATE_TABLE_GUEST)
mycursor.execute(CREATE_TABLE_Booking)






