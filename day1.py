

import csv


class Student:
    def __init__(self, name , age, grade):

        self.name = name
        self.age = age
        self.grade = grade



class StudentManager:
    def __init__(self):
        self.students = []

    def load_csv(self, filename="students.csv"):
        """Load all students from a CSV file."""

        try:
            with open(filename, "r", encoding="utf-8") as file:

                reader = csv.DictReader(file)
                for row in reader:

                    self.students.append(Student(row["name"],int(row["age"]),
                            int(row["grade"])))
        except FileNotFoundError:
            print(f"error , {filename} do not exist")
            return False

        except (KeyError, ValueError):
            print("error , Wrong format for csv file ")
            return False
        #print(self.st)
        return True  

    def average (self):
    
            if self.students :
                total = 0
                for student in self.students:
                    total += student.grade
                return total/len(self.students)
           
            else:
                print("error , we have error on students.avg(No students available)")

    def best (self):
        if self.students :
            wow = self.students[0]
            for student in self.students:
                if student.grade > wow.grade:
                    wow = student
            return wow
        
        else:
            print("error , we have error on students.best")
         
if __name__ == "__main__":
    group = StudentManager()

    if group.load_csv():
        average = group.average()
        best = group.best()

        print(average)
        print(best.name)
        print(best.grade)

    else:
        print("error , we have error on main")