
class Student(object):
    """__init__() functions as the class constructor"""
    def __init__(self, Id=None, Name=None, Theory=None, Practical=None):
        self.Id = Id
        self.Name = Name
        self.Practical = Practical
        self.Theory = Theory
        self.Total = Theory + Practical

StudentList = []

print("****MARKLIST****")
n = int(input("Enter students count: "))

for i in range(n):
    std_id = int(input("Student Id: "))
    std_name = input("Student Name: ")
    std_theory = float(input("Theory Marks: "))
    std_pract = float(input("Practical Marks: "))
    StudentList.append(Student(std_id, std_name, std_theory, std_pract))
    
print("****MARKS****")    
for std in StudentList:
    print ('{} {} {} {} {}'.format(std.Id, std.Name, std.Theory, std.Practical, std.Total))

print ("**Sort By**")
print("1 Theory Marks")
print("2 Practical Marks")
print("3 Total Marks")
print("4 Exit")
option = int(input(": "))

if option == 1:
    StudentList = sorted(StudentList, key=lambda x: x.Theory, reverse = True)
elif option == 2:
    StudentList = sorted(StudentList, key=lambda x: x.Practical, reverse = True)
elif option == 3:
    StudentList = sorted(StudentList, key=lambda x: x.Total, reverse = True)
else:
    sys.exit()
    
print("****SORTED MARKS****")    
for std in StudentList:
    print ('{} {} {} {} {}'.format(std.Id, std.Name, std.Theory, std.Practical, std.Total))


