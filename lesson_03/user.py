class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printName(self):
        print(f"{self.firstname}")

    def printLastname(self):
        print(f"{self.lastname}")

    def printFI(self):
        print(f"{self.firstname} {self.lastname}")
