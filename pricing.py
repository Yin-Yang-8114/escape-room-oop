from datetime import datetime, timedelta
class PricingManager():
    def calculate_price(room,players,booking_date):
        base_price = room.price_per_person * players
        if booking_date.weekday() in [5, 6]:
            base_price *= 1.15
        if players >= 5 and players <= 6:
            base_price *= 0.90
        elif players >= 7:
            base_price *= 0.85
        return float(round(base_price, 2))

    def calculate_cancellation_fee(booking,current_datetime):
        booking_datetime = datetime.strptime(f"{booking.booking_date} {booking.start_time}", "%Y-%m-%d %H:%M")
        time_difference = booking_datetime - current_datetime
        if time_difference > timedelta(days=1):
            return 0.0  
        elif timedelta(hours=6) < time_difference <= timedelta(days=1):
            return 0.25 * booking.total_price  
        elif time_difference <= timedelta(hours=6):
            return 0.50 * booking.total_price  
        else:
            return 0.0
