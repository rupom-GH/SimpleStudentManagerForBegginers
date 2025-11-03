class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
class studentManager:
    def __init__(self):
        self.students=[]
    def add_student(self,name,age,grade):
        student=Student(name,age,grade)
        self.students.append(student)
        print("\n {name} added successfully")
    def view_students(self):
        if not self.students:
            print("\n No students found")
        else:
            print("\n student List:")
            for s in self.students:
                print(s)
    def update_student(self,name,new_grade):
        for s in self.students:
            if s.name==name:
                s.grade=new_grade
                print(f"\n {name}`s grade updated successfully)")
                return
        print("\n student not found!")
    def delete_student(self,name):
        for s in self.students:
            if s.name==name:
                self.students.remove(s)
                print("\n {name} deleted successfully!")
                return
        print("\n student not found!")
def main():
    manager = studentManager()

    while True:
        print("\n =====  Student Management Menu  =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice=input("\n Enter your choice:")

        if choice=="1":
            name=input("\n Enter Your Name:")
            age=int(input("\n Enter Your Age:"))
            grade=input("\n Enter Your Grade:")
            manager.add_student(name,age,grade)

        elif choice=="2":
            manager.view_students()
        elif choice=="3":
            name=input("\n Enter Your Name:")
            new_grade=input("\n Enter Your New Grade:")
            manager.update_student(name,new_grade)
        elif choice=="4":
            name=input("\n Enter student name to delete:")
            manager.delete_student(name)
        elif choice=="5":
            print("\n Exiting program...")
            break
        else:
            print("\n Invalid choice! Please try again.")

if __name__=="__main__":
    main()






