"""
Aneri Shah
Homework 9

Implementing student, instructor, grades, and repository for entering and processing all the student data,
instructor data and the student's grade """

import os
from collections import defaultdict
from typing import Dict, DefaultDict

from prettytable import PrettyTable

from HW08_Aneri_Shah import file_reader


class Student:
    """ This provides information of the individual student which includes CWID, Name, Major, and the courses taken by them
    This will return individual student information for the repository class."""
    PT_FIELD_NAMES = ['CWID', 'Name', 'Major', 'Courses']

    def __init__(self, cwid: str, name: str, major: str) -> None:
        """ Initializes the cwid, name, major, and courses taken in protected form. """
        self._cwid: str = cwid
        self._name: str = name
        self._major: str = major
        self._courses: Dict[str, str] = dict()

    def add_course_grade(self, course: str, grade: str) -> None:
        """ This is to give the particular course taken by the student the grades earned by them """
        self._courses[course] = grade

    def info(self):
        """return a list of the information about individual student needed for the pretty table"""
        return [self._cwid, self._name, self._major, sorted(self._courses.keys())]


class Instructor:
    """ This provides information of the instructor which includes CWID, Name, Department, and the courses they teach
    This will return the instructor information for the repository class. """
    PT_FIELD_NAMES = ["CWID", "Name", "Dept", "Courses", "Students"]

    def __init__(self, cwid: str, name: str, dept: str) -> None:
        """ This is to initialize the cwid, name, department, and the courses they teach in protected form. """
        self._cwid: str = cwid
        self._name: str = name
        self._dept: str = dept
        self._courses: DefaultDict[str, int] = defaultdict(int)

    def add_course_student(self, course: str) -> None:
        """ Any instructor can teach more than one course.
         So this is to increment the number of courses taught by them"""
        self._courses[course] += 1

    def info_i(self):
        """ return a list of the information about the instructor needed for the pretty table """
        for course, student_num in self._courses.items():
            yield [self._cwid, self._name, self._dept, course, student_num]


class Repository:
    """ This class holds all the information of all the students, all the instructors, and the grades earned by the students.
    This class will create the instance of student, instructor and then print the pretty table according to their field names."""

    def __init__(self, path: str, ptable=False) -> None:
        """store all students, instructors, and print prettytables """
        if not os.path.exists(path):
            raise FileNotFoundError(f'{path} not found')
        self.path: str = path
        self._students: Dict[str, Student] = dict()
        self._instructors: Dict[str, Instructor] = dict()
        try:
            self._read_students(os.path.join(path, "students.txt"))
            self._read_instructors(os.path.join(path, "instructors.txt"))
            self._read_grades(os.path.join(path, "grades.txt"))
        except (FileNotFoundError, ValueError) as e:
            print(e)

        if ptable:
            self.student_pretty_table()
            self.instructor_pretty_table()

    def _read_students(self, path: str) -> None:
        """ read each line from student file and create instance of class student
        and if the file not found or any value error, it raises an exception """
        try:
            for cwid, name, major in file_reader(path, 3, sep='\t', header=False):
                self._students[cwid] = Student(cwid, name, major)

        except (FileNotFoundError, ValueError) as e:
            print(e)

    def _read_instructors(self, path:str):
        """read each line from instructors file and create instance of class instructor
        and if the file not found or any value error, it raises an exception"""
        try:
            for cwid, name, dept in file_reader(path, 3, sep='\t', header=False):
                self._instructors[cwid] = Instructor(cwid, name, dept)

        except (FileNotFoundError, ValueError) as e:
            print(e)

    def _read_grades(self, path: str) -> None:
        """ read the student_cwid, course, grade, instructor_cwid from the grades file
        and checks for the individual student and the individual instructor.
        Raises an exception when unknown student is found"""
        try:
            for student_cwid, course, grade, instructor_cwid in file_reader(path, 4, sep='\t', header=False):
                try:
                    s: Student = self._students[student_cwid]
                    s.add_course_grade(course, grade)
                except KeyError:
                    print(f"Found grade for unknown student {student_cwid}")
                try:
                    inst: Instructor = self._instructors[instructor_cwid]
                    inst.add_course_student(course)
                except KeyError:
                    print(f"Found grade for unknown student {instructor_cwid}")
        except (FileNotFoundError, ValueError) as e:
            print(e)

    def student_pretty_table(self) -> None:
        """print pretty table with student information by calling the global constant."""
        pt = PrettyTable(field_names=Student.PT_FIELD_NAMES)
        for stu in self._students.values():
            pt.add_row(stu.info())

        print("Student Summary")
        print(pt)

    def instructor_pretty_table(self) -> None:
        """print pretty table with instructor information by calling the global constant."""
        pt = PrettyTable(field_names=Instructor.PT_FIELD_NAMES)
        for stu in self._instructors.values():
            for row in stu.info_i():
                pt.add_row(row)

        print("Instructor Summary")
        print(pt)


def main():
    """ define a repository for stevens"""
    stevens: Repository = Repository("/Users/anerishah/Desktop/SSW810/WEEK 9", ptable= True)


if __name__ == '__main__':
    main()
