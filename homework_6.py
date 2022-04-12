class Student:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def display(self):
        return f'{self.name} {self.surname}, grades - {self.grades}'


class Group:

    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_group(self):
        temp = f'Group "{self.name}" students: \n'
        for student in self.students:
            temp += student.display() + "\n"
        return temp


a = Student('John', 'Snow')
b = Student('Tyrion', 'Lannister')
c = Student('Oberyn', 'Martell ')
a.add_grade(3)
a.add_grade(2)
b.add_grade(5)
b.add_grade(5)
c.add_grade(4)
c.add_grade(4)
c.add_grade(3)

g1 = Group('Westeros')
g1.add_student(a)
g1.add_student(b)
g1.add_student(c)
print(g1.display_group())


