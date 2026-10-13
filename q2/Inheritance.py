class CampusDirector:
    def __init__(self):
        self.campus_name = "Main Campus"  

    def manage_campus(self):              
        print("Managing the campus.")


class CurriculumDepartment(CampusDirector):
    def __init__(self):
        super().__init__()
        self.department_name = "Curriculum Department"
        self.program = "Academic Programs"
        self.faculty_count = 25
        self.subject_count = 30             

    def manage_curriculum(self):            
        print("Managing the curriculum.")

    def manage_subjects(self):             
        print("Managing subjects and courses.")


class StudentServicesDepartment(CampusDirector):
    def __init__(self):
        super().__init__()
        self.department_name = "Student Services Department"
        self.student_count = 500             

    def assist_students(self):               
        print("Assisting students.")

    def organize_activities(self):          
        print("Organizing student activities.")



class RegistrarsOffice(CurriculumDepartment):
    def __init__(self):
        super().__init__()
        self.office_name = "Registrar's Office"  

    def manage_records(self):                 
        print("Managing student records.")



class LibraryServicesOffice(CurriculumDepartment):
    pass



class FacultyOffice(CurriculumDepartment):
    pass



class GuidanceOffice(StudentServicesDepartment):
    pass



class DormitoryManagementOffice(StudentServicesDepartment):
    def __init__(self):
        super().__init__()
        self.office_name = "Dormitory Management Office" 

    def manage_dormitory(self):               
        print("Managing dormitory facilities.")



class RecordsManagementOffice(RegistrarsOffice):
    def __init__(self):
        super().__init__()
        self.records_office_name = "Records Management Office"  # 1 Property

    def organize_records(self):               # 1 Method
        print("Organizing and maintaining official records.")



print("CAMPUS DIRECTOR(CD)")
cd = CampusDirector()
print("Campus:", cd.campus_name)
cd.manage_campus()

print("CURRICULUM DEPARTMENT(CID)")
cid = CurriculumDepartment()
print("Department:", cid.department_name)
cid.manage_curriculum()
cid.manage_subjects()

print("STUDENT SERVICES DEPARTMENT(SSD)")
ssd = StudentServicesDepartment()
print("Department:", ssd.department_name)
ssd.assist_students()
ssd.organize_activities()

print("REGISTRAR'S OFFICE")
registrar = RegistrarsOffice()
print("Office:", registrar.office_name)
registrar.manage_records()

print("LIBRARY SERVICES OFFICE")
library = LibraryServicesOffice()
library.manage_curriculum()
print("Library Services Office inherits from CID.")

print("FACULTY OFFICE")
faculty = FacultyOffice()
faculty.manage_subjects()
print("Faculty Office inherits from CID.")

print("GUIDANCE OFFICE")
guidance = GuidanceOffice()
guidance.assist_students()

print("DORMITORY MANAGEMENT OFFICE")
dorm = DormitoryManagementOffice()
print("Office:", dorm.office_name)
dorm.assist_students()
dorm.manage_dormitory()

print("RECORDS MANAGEMENT OFFICE")
records = RecordsManagementOffice()
print("Office:", records.records_office_name)
records.manage_records()
records.organize_records()