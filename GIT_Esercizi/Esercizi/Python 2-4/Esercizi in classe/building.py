from CorsoITS import room

class Building:
    def __init__(self, name: str, address: str, floors: str, room:str):
        self.name = name
        self.address = address
        self.floors = floors
        self.room = room
    def add_room(self):
        pass
    def set_name(self):
        return self.name
    
    def set_address(self):
        return self.address
    
    def set_floors(self):
        return self.floors
    
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def get_floors(self):
        return self.floors
    
    def __str__(self) -> str:
        pass