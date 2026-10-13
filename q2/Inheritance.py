class CampusDirector:
    def __init__(self, responsibility):
        self.responsibility = responsibility

    def display_responsibilty(self):
        print("Responsibility:", self.responsibility)

class StudentServicesDepartment(CampusDirector):
    def __init__(self, responsibility, information_dissemation):
        super().__init__(responsibility)
        self.information_dissemation = information_dissemation

    def display_information_dissemation(self):
        print("Information Dissemation:", self.information_dissemation)
        print("Responsibility:", self.responsibility)

class DormManaging(StudentServicesDepartment):
    def __init__(self, responsibility, information_dissemation, dorm_management):
        super().__init__(responsibility, information_dissemation)
        self.dorm_management = dorm_management

    def display_dorm_management(self):
        print("Dorm Management:", self.dorm_management)

print("Campus Director")
parent = CampusDirector("Student Support")
parent.display_responsibilty()

print("Student Services Department")
ssd = StudentServicesDepartment("Student Support", "Providing Information")
dorm = DormManaging("Student Support", "Providing Information", "Managing Dormitories")



ssd.display_information_dissemation()
dorm.display_dorm_management()
