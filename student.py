def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


class Student:

    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return 0
    
    @first_name.setter
    def first_name(self, name):
        if type(name) is str and hasNumbers(name)== False:
            self.__first_name = name
        else:
            raise TypeError("First Name must be a string and must not contain any numbers")
    
    @property
    def last_name(self):
        try:
            return  self.__last_name
        except AttributeError:
            return 0
    
    @last_name.setter
    def last_name(self, name):
        if type(name) is str and hasNumbers(name) == False:
            self.__last_name = name
        else:
            raise TypeError("Last Name must be a string and must not contain any numbers")
    
    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0
    
    @age.setter
    def age(self, num):
        if type(num) is int and num<100 and num>=1:
            self.__age = num
        else:
            raise ValueError('I am sorry your age must be a number between 1 and 100.')

    @property
    def cohort(self):
        try:
            return self.__cohort
        except AttributeError:
            return 0
    
    @cohort.setter
    def cohort(self, num):
        if type(num) is int:
            self.__cohort = num
        else:
            raise ValueError('I am sorry your cohort class must be a number')
    
    @property
    def full_name(self):
        try:
            self.__full_name = f'{self.__first_name} {self.__last_name}'
            return self.__full_name
        except AttributeError:
            return 0

    def __str__(self):
        return f"{self.full_name} is {self.age} years old and is in cohort {self.cohort}"
    


jack = Student()
jack.first_name = "Jack"
print("first name:", jack.first_name)

jack.last_name = "Jackson"
print("last name: ", jack.last_name)

jack.age = 10
print("age:", jack.age)

jack.cohort = 56
print("cohort", jack.cohort)

print('full name:', jack.full_name)

print("__str__ method: ")
print(jack)