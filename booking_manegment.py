from pricing import PricingManager
from data import DataManager

class  BookingManager:
    # rooms = DataManager.load_rooms()
    # bookings = DataManager.load_bookings()
    # pricing_maneger = PricingManager()
    def __init__(self,rooms,bookings,pricing_maneger):
        self.rooms = rooms
        self.bookings = bookings
        self.pricing_maneger = pricing_maneger 

    def create_booking(customer_name, room_id, booking_date, start_time, players):
        pass

