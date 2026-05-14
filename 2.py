from collections import namedtuple

Student = namedtuple("Student", ["name", "grade"])

class StudentGroupIterator:
    def __init__(self, students: list[Student]):
        self._students = students
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self) -> Student:
        if self._index < len(self._students):
            res = self._students[self._index]
            self._index += 1
            return res
        raise StopIteration

class StudentGroup:
    def __init__(self, group_name: str):
        self._group_name = group_name
        self._students: list[Student] = []

    def add_student(self, name: str, grade: int) -> None:
        self._students.append(Student(name, grade))

    def __iter__(self):
        return StudentGroupIterator(self._students)

    def top_students(self, n: int = 3):
        sorted_students = sorted(self._students, key=lambda s: s.grade, reverse=True)
        return iter(sorted_students[:n])

def main():
    group = StudentGroup("КІ-21")
    for n, g in [("Олена", 95), ("Іван", 78), ("Марія", 92), ("Петро", 85), ("Анна", 88)]:
        group.add_student(n, g)

    print("\nВсі пари студентів:")
    for s1 in group:
        for s2 in group:
            if s1.name < s2.name:
                print(f"  {s1.name} та {s2.name}")

    print("\nТоп-3 студенти:")
    for student in group.top_students(3):
        print(f"  {student.name}: {student.grade}")

if __name__ == "__main__":
    main()
