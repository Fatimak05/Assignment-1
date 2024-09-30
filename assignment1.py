from enum import Enum

#Enum for room status
class RoomStatus (Enum):
    Available = "Available"
    Occupied = "Occupied"
    Reserved = "Reserved"

class Customer:
    """Class to represent a customer"""
    #initializes customer attributes
    def __init__(self,firstName, lastName,email,phoneNumber,id):
        self.__firstName= firstName
        self.__lastName = lastName
        self.__email = email
        self.__phoneNumber = phoneNumber
        self.__id = id

    # Setter and Getter methods
    def set_firstName(self,firstName):
        self.__firstName= firstName

    def get_firstName(self):
        return self.__firstName

    def set_lastName(self, lastName):
        self.__lastname = lastName

    def get_lastName(self):
        return self.__lastName

    def set_email(self,email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_phoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber

    def get_phoneNumber(self):
        return self.__phoneNumber

    def set_id(self,id):
        self.__id = id

    def get_id(self):
        return self.__id

class ReservationDetails:
    """Class to represent reservation details"""
    #Initializes reservation details attributes
    def __init__(self, reservationNumber, checkInDate, checkOutDate, customerName, roomNumber):
        self.__reservationNumber = reservationNumber
        self.__checkInDate= checkInDate
        self.__checkOutDate = checkOutDate
        self.__customerName = customerName
        self.__roomNumber = roomNumber

    #Setter and Getter methods
    def set_reservationNumber(self,reservationNumber):
        self.__reservationNumber = reservationNumber

    def get_reservationNumber(self):
        return self.__reservationNumber

    def set_checkInDate(self, checkInDate):
        self.__checkInDate = checkInDate

    def get_checkInDate(self):
        return self.__checkInDate

    def set_checkOutDate(self,checkOutDate):
        self.__checkOutDate = checkOutDate

    def get_checkOutDate(self):
        return self.__checkOutDate

    def set_customerName(self, customerName):
        self.__customerName = customerName

    def get_customerName(self):
        return self.__customerName

    def set_roomNumber(self,roomNumber):
        self.__roomNumber = roomNumber

    def get_roomNumber(self):
        return self.__roomNumber

class Room:
    """Class to represent room information"""
    #initializes room attributes
    def __init__(self, numberOfRooms, roomType, roomStatus, costPerNight, numberOfNights):
        self.__numberOfRooms =numberOfRooms
        self.__roomType = roomType
        self.__roomStatus = roomStatus
        self.__costPerNight = costPerNight
        self.__numberOfNights = numberOfNights

    #Setter and Getter methods
    def set_numberOfRooms(self, numberOfRooms):
        self.__numberOfRooms = numberOfRooms

    def get_numberOfRooms(self):
        return self.__numberOfRooms

    def set_roomType(self, roomType):
        self.__roomType = roomType

    def get_roomType(self):
        return self.__roomType

    def set_roomStatus(self, roomStatus):
        self.__roomStatus = roomStatus

    def get_roomStatus(self):
        return self.__roomStatus

    def set_costPerNight(self, costPerNight):
        self.__costPerNight = costPerNight

    def get_costPerNight(self):
        return self.__costPerNight

    def set_numberOfNights(self, numberOfNights):
        self.__numberOfNights = numberOfNights

    def get_numberOfNights(self):
        return self.__numberOfNights


class Payment:
    """Class to represent payment details"""

    #Initializes payment attributes
    def __init__(self, paymentMethod, roomSubtotal, taxAndFees, totalCharges, paymentStatus):
        self.__paymentMethod = paymentMethod
        self.__roomSubtotal = roomSubtotal
        self.__taxAndFees = taxAndFees
        self.__totalCharges = totalCharges
        self.__paymentStatus = paymentStatus

    #Setter and Getter methods
    def set_paymentMethod(self, paymentMethod):
        self.__paymentMethod = paymentMethod

    def get_paymentMethod(self):
        return self.__paymentMethod

    def set_roomSubtotal(self,  roomSubtotal):
        self.__roomSubtotal = roomSubtotal

    def get_roomSubtotal(self):
        return self.__roomSubtotal

    def set_taxAndFees(self, taxAndFees):
        self.__taxAndFees = taxAndFees

    def get_taxAndFees(self):
        return self.__taxAndFees

    def set_totalCharges(self, totalCharges):
        self.__totalCharges = totalCharges

    def get_totalCharges(self):
        return self.__totalCharges

    def set_paymentStatus(self, paymentStatus):
        self.__paymentStatus = paymentStatus

    def get_paymentStatus(self):
        return self.__paymentStatus

    #method to calculate total charges
    def calculateTotalCharges(self):
        pass

    #method to process the payment
    def processPayment(self):
        pass

    #method to update payment status
    def updatePaymentStatus(self):
        pass

#creating objects
customer = Customer("Fatima", "Alamoodi", "Fatima.Alamoodi@email.com", "0501234567", "AE123456")
reservation = ReservationDetails("RD123", "28-09-2024", "30-09-2024", "Fatima", 111)
room = Room(1, "Double",RoomStatus.Available , 500.00, 2)
payment= Payment("Credit Card", 500.00, 100.00, 600.00, "Completed")

#Displaying customer information
print("Customer Name:",customer.get_firstName(), customer.get_lastName())
print("Customer Email:",customer.get_email())
print("Customer Phone Number:",customer.get_phoneNumber())
print("Customer ID:",customer.get_id())

#Displaying reservation details
print("Reservation Details:")
print("Reservation Number:",reservation.get_reservationNumber())
print("Check-In Date:",reservation.get_checkInDate())
print("Check-Out Date:", reservation.get_checkOutDate())
print("Customer Name:",reservation.get_customerName())
print("Room Number:",reservation.get_roomNumber())

#Displaying room details
print("Room Details:")
print("Number of Rooms:",room.get_numberOfRooms())
print("Room Type:",room.get_roomType())
print("Room Status:",room.get_roomStatus().value)
print("Cost Per Night:",room.get_costPerNight())
print("Number Of Nights:",room.get_numberOfNights())

#Displaying payment details
print("Payment Details:")
print("Payment Method:",payment.get_paymentMethod())
print("Room Subtotal:", payment.get_roomSubtotal())
print("Tax and Fees:",payment.get_taxAndFees())
print("Total Charges:",payment.get_totalCharges())
print("Payment Status:", payment.get_paymentStatus())