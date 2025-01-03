class Student:
    def get (self):
        self.rlno=int(input("Enter the Roll Number."))
        self.name=input("Enter Name.")
        self.totalmark=float(input("Enter Total marks."))
    def disp(self):
        print(f"Roll Number:{self.rlno}")
        print(f"Name:{self.name}")
        print(f"Total Marks:{self.totalmark}")
stud1 = Student()
stud1.get()
stud1.disp()
