def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

class Info:
    def __init__(self, social, dob, health, first_name, last_name, address):
        self.__social = social
        self.__dob = dob
        self.__health = health
        self.__first_name = first_name
        self.__last_name = last_name
        self.address = address
    
    @property
    def social(self):
        try:
            return self.__social
        except AttributeError:
            return 0
    
    @property
    def dob(self):
        try:
            return self.__dob
        except AttributeError:
            return 0

    @property
    def health(self):
        try:
            return self.__health
        except AttributeError:
            return 0
    
    @property
    def full_name(self):
        try:
            return f"{self.__first_name} {self.__last_name}"
        except AttributeError:
            return 0
    @property
    def address(self):
        try:
            return self.__address
        except AttributeError:
            return 0
    @address.setter
    def address(self, address):
        if type(address) is str and hasNumbers(address):
            self.__address = address
        else:
            raise TypeError('Address must include house and apartment number as well as street')
    

    
    
kurt = Info('555-55-1234', "1/1/91", 1231231233, "Kurt", "Krafft", "123 Main Street")

# kurt.social = "888-88-8888"
print("social~can't set~", kurt.social)

# kurt.dob = "3/3/93"
print("dob~can't set~", kurt.dob)

# print("This will return nothing", kurt.first_name)
# print("This will return nothing", kurt.last_name)

print("full name", kurt.full_name)

print("address: ", kurt.address)
kurt.address = "123 Party ave"
print("New address: ", kurt.address)





