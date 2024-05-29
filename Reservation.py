import random
from Table import Table

class Reservation:
    used_ids = set()  # Initialize used_ids as a class variable

    def __init__(self, customer_name, date, time, guests):
        self.reservation_id = self.generate_unique_id()  # Automatically generate ID
        self.customer_name = customer_name
        self.date = date
        self.time = time
        self.guests = guests
        self.table_id = None

    @classmethod
    def generate_unique_id(cls):
        available_ids = set(range(1, 31)) - cls.used_ids
        if not available_ids:
            raise Exception("No more available reservation IDs for today.")
        reservation_id = random.choice(list(available_ids))
        cls.used_ids.add(reservation_id)
        return reservation_id

    def check_availability(self, date, time, guests):
    # Only consider tables that are "available" and can accommodate the number of guests
        available_tables = [table for table in Table.tables if table.capacity >= guests and table.status == "available"]
        return available_tables


    def make_reservation(self, name, date, time, guests):
        available_tables = self.check_availability(date, time, guests)
        if available_tables:
            chosen_table = available_tables[0]  # Choose the first available table
            if chosen_table.reserve(date, time):  # Try to reserve the table
                self.table_id = chosen_table
                print(f"Reservation {self.reservation_id} made for {name} with {guests} guests on {date} at {time} at table {self.table_id.table_id}.")
                return True
            else:
                print("Failed to reserve the chosen table. It might just have been taken.")
                return False
        else:
            print("No available tables for the requested time and date.")
            return False

    def update_reservation(self, new_date=None, new_time=None, new_guests=None):
        if new_guests:
            self.guests = new_guests
        if new_date and new_time and self.table_id and not self.table_id.is_available(new_date, new_time):
            print("Requested time is not available. Checking for available tables.")
            available_tables = self.check_availability(new_date, new_time, self.guests)
            if available_tables:
                self.table_id.release(self.date, self.time)  # Release the old table
                self.table_id = available_tables[0]  # Assign a new table
                self.table_id.reserve(new_date, new_time)  # Reserve the new table
                self.date = new_date
                self.time = new_time
                print(f"Reservation updated to table {self.table_id.table_id} on {new_date} at {new_time}.")
            else:
                print("No available tables for the updated requirements.")
        else:
            self.date = new_date if new_date else self.date
            self.time = new_time if new_time else self.time
            print(f"Reservation updated to {self.guests} guests on {self.date} at {self.time}.")

    def cancel_reservation(self):
        if self.table_id:
            self.table_id.release(self.date, self.time)
            print(f"Reservation {self.reservation_id} for {self.customer_name} with {self.guests} on {self.date} at {self.time} canceled.")
            self.table_id = None
            Reservation.used_ids.remove(self.reservation_id)
