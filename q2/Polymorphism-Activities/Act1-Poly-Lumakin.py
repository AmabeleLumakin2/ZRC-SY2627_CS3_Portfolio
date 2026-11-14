class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name 
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
       
    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
       
        print(f"Patient Name: {self.__name}")
        self.display_patient_type()
        print(f"Original Bill: {self.__bill_amount}")
        print(f"Final Bill: {self.__bill_amount}")

    def display_patient_type(self):
       print("Patient Type: Regular Patient")


class SeniorPatient(Patient):
    def calculate_bill(self):
        original_bill = super().get_bill_amount()
        final_bill = original_bill * 0.80

        print(f"Patient Name: {self.get_name()}")
        self.display_patient_type()
        print(f"Original Bill: {original_bill}")
        print(f"Final Bill: {final_bill}")

    def display_patient_type(self):
        print("Patient Type: Senior Citizen")
            

class PhilhealthPatient(Patient):
    def calculate_bill(self):
        original_bill = super().get_bill_amount()
        final_bill = original_bill * 0.85
    
        print(f"Patient Name: {self.get_name()}")
        self.display_patient_type()
        print(f"Original Bill: {original_bill}")
        print(f"Final Bill: {final_bill}")

    def display_patient_type(self):
        print("Patient Type: Philhealth Member")


regular_patient = Patient("Juan Dela Cruz", 15000.00)
regular_patient.calculate_bill()
print()

philHealth_patient = PhilhealthPatient("Elsa", 15000.00)
philHealth_patient.calculate_bill()
print()

senior_patient = SeniorPatient("Anna", 15000.00)
senior_patient.calculate_bill()
print()
