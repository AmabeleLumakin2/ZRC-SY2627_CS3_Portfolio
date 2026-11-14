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
       return(
                f"Patient Name: {self.__name}\n"
                f"Original Bill: {self.__bill_amount}\n"
                f"Final Bill: {self.__bill_amount}\n")

class SeniorPatient(Patient):
    def calculate_bill(self):
        original_bill = super().get_bill_amount()
        final_bill = original_bill * 0.80
        return (
            f"Patient Name: {self.get_name()}\n"
            f"Original Bill: {original_bill}\n"
            f"Final Bill: {final_bill}\n")
            

class PhilhealthPatient(Patient):
    def calculate_bill(self):
        original_bill = super().get_bill_amount()
        final_bill = original_bill * 0.85
        return (
            f"Patient Name: {self.get_name()}\n"
            f"Original Bill: {original_bill}\n"
            f"Final Bill: {final_bill}\n")
                    


regular_patient = Patient("Juan Dela Cruz", 15000.00)
print(regular_patient.calculate_bill())

philHealth_patient = SeniorPatient("Anna", 15000.00)
print(philHealth_patient.calculate_bill())

senior_patient = PhilhealthPatient("Anna", 15000.00)
print(senior_patient.calculate_bill())
