# isinstance() 함수 활용
"""class Student:
    def study(self):
        print("공부를 합니다")


class Teacher:
    def teach(self):
        print("학생을 가르칩니다")


classroom = [Student(), Student(), Teacher(), Student(), Student()]


for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()"""


# __str()__ 함수
"""class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average())


students = [
    Student("황준하", 100, 100, 100, 100),
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98)
]

print("이름 ", "총점", "평균", sep="\t")

for student in students:

    print(str(student))"""


# 크기 비교 함수
"""class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self, student):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(student),
            self.get_average(student))

    def __eq__(self, value):
        return self.get_sum() == value.get_sum()

    def __ne__(self, value):
        return self.get_sum() != value.get_sum()

    def __gt__(self, value):
        return self.get_sum() > value.get_sum()

    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()

    def __lt__(self, value):
        return self.get_sum() < value.get_sum()

    def __le__(self, value):
        return self.get_sum() <= value.get_sum()


students = [
    Student("황준하", 100, 100, 100, 100),
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98)
]

student_a = Student("황준하", 100, 100, 100, 100)
student_b = Student("윤인성", 87, 98, 88, 95)

print("student_a == student_b:", student_a == student_b)
print("student_a != student_b:", student_a != student_b)
print("student_a > student_b:", student_a > student_b)
print("student_a >= student_b:", student_a >= student_b)
print("student_a < student_b:", student_a < student_b)
print("student_a <= student_b:", student_a <= student_b)"""


# 클래스 변수
"""class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count += 1
        print("{}번째 학생이 생성되었습니다.".format(Student.count))


students = [
    Student("황준하", 100, 100, 100, 100),
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98)
]

print()
print("현재 생성된 학생 수는 {}명입니다.".format(Student.count))"""


# 클래스 함수
class Student:

    count = 0
    students = []


    @classmethod
    def print(cls):
        print("------학생 목록------")
        print("이름 \t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("------- ------- -------")

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average())


Student("황준하", 100, 100, 100, 100)
Student("윤인성", 87, 98, 88, 95)
Student("연하진", 92, 98, 96, 98)
Student("구지연", 76, 96, 94, 90)
Student("나선주", 98, 92, 96, 92)
Student("윤아린", 95, 98, 98, 98)

Student.print()