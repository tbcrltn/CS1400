from dataclasses import dataclass, field


@dataclass(order = True)
class Student:
    id: int
    name: str
    major: str
    courses: list[str] = field(default_factory = list)

    def enroll(self, course: str):
        self.courses.append(course)
    
    def total_courses(self):
        return len(self.courses)
    

def main():
    student1 = Student(100, "Toby", "CS")
    student2 = Student(101, "Alex", "DS")
    student3 = Student(102, "Chase", "LA")
    student1.enroll("CS1400")
    student1.enroll("CS2800")
    student1.enroll("CS2000")
    student2.enroll("DS2000")
    student2.enroll("DS2730")
    student3.enroll("LA1005")
    student3.enroll("LA1500")
    student3.enroll("LA2230")
    print(student1.total_courses())
    print(student2.total_courses())
    print(student3.total_courses())
    print(student1 < student2) #both statements should print True
    print(student2 < student3) 


if __name__ == "__main__":
    main()