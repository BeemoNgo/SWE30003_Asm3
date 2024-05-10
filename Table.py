class Table:
    tables = []

    def __init__(self, table_id, capacity):
        self.table_id = table_id
        self.capacity = capacity
        self.reservations = {}  # Stores reservations by date and time
        self.status = "free"  # Possible states: free, reserved, occupied, ordered
        Table.tables.append(self)

    @classmethod
    def initialise_tables(cls):
        for i in range(1, 21):  # Creates 20 tables
            cls.tables.append(Table(table_id=i, capacity=4))  # Assuming each table has a capacity of 4

    def __str__(self):
        return f"Table {self.table_id} with capacity {self.capacity}, Status: {self.status}"

    def reserve(self, date, time):
        if self.is_available(date, time):
            self.reservations[(date, time)] = True
            self.status = "reserved"
            print(f"Reservation successful: {self}")
            return True
        print(f"Reservation failed: {self}")
        return False

    def release(self, date, time):
        if (date, time) in self.reservations:
            self.reservations.pop((date, time), None)
            self.check_status()  # Check if should change status back to free
            print(f"Release successful: {self}")

    def is_available(self, date, time):
        return (date, time) not in self.reservations and self.status in ["free", "occupied"]

    def is_reserved(self, date, time):
        return (date, time) in self.reservations and self.status == "reserved"

    def is_occupied(self):
        return self.status == "occupied"

    def set_occupy_table(self):
        if self.status in ["free", "reserved"]:
            self.status = "occupied"
            print(f"Table occupied: {self}")

    def order_placed(self):
        if self.status == "occupied":
            self.status = "ordered"
            print(f"Order placed: {self}")

    def order_paid(self):
        if self.status == "ordered":
            self.status = "free"
            print(f"Order paid, table now free: {self}")

    def check_status(self):
        if not self.reservations:
            self.status = "free"
            print(f"Status check - table now free: {self}")

    def get_table_info(self):
        return f"Table ID: {self.table_id}, Capacity: {self.capacity}, Current Status: {self.status}"


# # Example usage to initialise tables
# Table.initialise_tables()
# table10 = Table.tables[10]  # Accessing table 10 which is indexed as 9
# print(table10)  # Initially free
# table10.reserve("2023-10-01", "19:00")
# print(table10)  # Should be reserved
# table10.set_occupy_table()
# print(table10.get_table_info())  # Now occupied
# table10.order_placed()
# print(table10.get_table_info())  # Status after order placed
# table10.order_paid()
# print(table10)  # Should return to free after payment
