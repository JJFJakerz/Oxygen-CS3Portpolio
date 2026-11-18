class Smartlocker:
    def __init__(self, locker_number, owner, status="available"):
        self.locker_number = locker_number
        self.owner = owner
        self.status = status

    def assign_locker(self, name):
        self.owner = name
        self.status = "unavailable"

    def release_locker():
        self.owner = None
    self.status = "available"

def display_info():
    print(f"Locker Number: {self.locker_number}")
    print(f"Owner: {self.owner}")
    print(f"Status: {self.status}")
