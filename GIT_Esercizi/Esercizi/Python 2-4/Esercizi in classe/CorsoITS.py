from building import Building
class room:
    def __init__(self, name, floor, num_seats):
        self.name= name
        self.floor= floor
        self.num_seats= num_seats
        pass
    def set_name(self):
        return self.name
    def set_floor(self):
        return self.floor
    def set_numseats(self):
        return self.num_seats
    def get_name(self):
        return self.name
    def get_floor(self):
        return self.floor
    def get_num_seats(self):
        return self.num_seats
    def __str__(self) -> str:
        return room