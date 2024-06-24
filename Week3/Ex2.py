class Person:
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob

class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.__grade = grade
    
    def describe(self):
        print(f"Student - Name: {self._name} - YOB: {self._yob} - Grade: {self.__grade}")

class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.__subject = subject
    
    def describe(self):
        print(f"Teacher - Name: {self._name} - YOB: {self._yob} - Subject: {self.__subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        print(f"Doctor - Name: {self._name} - YOB: {self._yob} - Specialist: {self.__specialist}")

class Ward:
    def __init__(self, name):
        self.__name = name
        self.__peopleList = []
    def add_person(self, person):
        self.__peopleList.append(person)

    def count_doctor(self):
        count = 0
        for person in self.__peopleList:
            if isinstance(person, Doctor):
                count+=1
        return count
    def sort_age(self):
        self.__peopleList = sorted(self.__peopleList, key = lambda person: person._yob, reverse=True)

    def compute_average(self):
        count = 0
        res = 0
        for person in self.__peopleList:
            if isinstance(person, Teacher):
                count+=1
                res+= person._yob
        return res/count

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for person in self.__peopleList:
            person.describe()
            
            
        


w1 = Ward("hanni")
doctor1 = Doctor("dasddasd",111,"eewew")
doctor2 = Doctor("dasddasd",113231,"eewew")
doctor3 = Doctor("dasdddsdasd",113231,"eewew")
w1.add_person(doctor1)
print(w1.count_doctor())
w1 = Ward("han")
w1.add_person(doctor2)
w1.add_person(doctor3)
print(w1.count_doctor())
