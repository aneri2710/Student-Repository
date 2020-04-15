"""
Aneri Shah
Homework 11

Implementing student, instructor, grades, major and repository for entering and processing all the student data,
instructor data and the student's grade along with the major of that student
Connecting to the database and running query to print the student grade summary table
"""

import os
from collections import defaultdict
from typing import Dict, DefaultDict

from prettytable import PrettyTable

from HW08_Aneri_Shah import file_reader
import sqlite3


class Major:
    """ This is a Major class for adding the majors based on required and elective courses in the majors.txt. """
    PT_FIELD_NAMES = ["Major", "Required", "Electives"]

    def __init__(self, major: str) -> None:
        """ Initializes the major, required and elective courses taken in protected form. """
        self._major = major
        self._required = set()
        self._elective = set()

    def add_course_re(self, flag, course: str) -> None:
        """ Checks if the course is required or elective from the majors.txt file """
        if flag.lower() == 'r':
            self._required.add(course)
        elif flag.lower() == 'e':
            self._elective.add(course)
        else:
            raise ValueError(f"Unknown Flag: {flag}")

    def remaining(self, courses):
        """ Checks for the grades in the list of grades.
        Returns the remaining number of courses which can be remaining or elective """
        completed_courses = set()
        remaining_required = self._required.copy()
        remaining_elective = self._elective.copy()

        for course, grade in courses.items():
            if grade in ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']:
                completed_courses.add(course)
                if course in self._elective:
                    remaining_elective = []

            if course in self._required and grade in ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']:
                remaining_required.remove(course)

        return completed_courses, remaining_required, remaining_elective

    def info(self):
        """return a list of the information about the courses needed for the pretty table"""
        return [self._major, sorted(self._required), sorted(self._elective)]


class Student:
    """ This provides information of the individual student which includes CWID, Name, Major, the courses which are completed, remaining and elective and their gpa.
    This will return individual student information for the repository class."""
    PT_FIELD_NAMES = ['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Required', 'Remaining Electives', 'GPA']

    def __init__(self, cwid: str, name: str, major: str) -> None:
        """ Initializes the cwid, name, major, and courses taken in protected form along with the completed courses, remaining courses and elective courses """
        self._cwid: str = cwid
        self._name: str = name
        self._major: str = major
        self._courses: Dict[str, str] = dict()

        self._completed_courses = None
        self._remaining_required = None
        self._remaining_electives = None

    def add_course_grade(self, course: str, grade: str) -> None:
        """ This is to give the particular course taken by the student the grades earned by them """
        self._courses[course] = grade

    def gpa(self):
        """calculate the GPA and return to student class"""
        grades: Dict[str, float] = {"A": 4.00, "A-": 3.75, "B+": 3.25, "B": 3.00, "B-": 2.75, "C+": 2.25, "C": 2.00,
                                    "C-": 0.00, "D+": 0.00, "D": 0.00, "D-": 0.00, "F": 0.00}
        try:
            total: float = sum([grades[grade] for grade in self._courses.values()]) / len(self._courses.values())
            return round(total, 2)
        except ZeroDivisionError as e:
            print(e)

    def course_re(self, inst_major):
        """ This will see for the courses in the major class by calling the remaining courses of the major class. """
        self._completed_courses, self._remaining_required, self._remaining_electives = inst_major.remaining(
            self._courses)

    def info(self):
        """return a list of the information about individual student needed for the pretty table"""
        return [self._cwid, self._name, self._major, sorted(self._completed_courses), sorted(self._remaining_required),
                sorted(self._remaining_electives), self.gpa()]


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
    """ This class holds all the information of all the students, all the instructors, the grades earned by the students, and the major courses taken by the students.
    This class will create the instance of student, instructor and then print the pretty table according to their field names."""

    def __init__(self, path: str, ptable=False) -> None:
        """store all students, instructors, majors and print prettytables """
        if not os.path.exists(path):
            raise FileNotFoundError(f'{path} not found')
        self.path: str = path
        self._students: Dict[str, Student] = dict()
        self._instructors: Dict[str, Instructor] = dict()
        self._major: Dict[str, Major] = dict()
        try:
            self._read_major(os.path.join(path, "majors.txt"))
            self._read_students(os.path.join(path, "students.txt"))
            self._read_instructors(os.path.join(path, "instructors.txt"))
            self._read_grades(os.path.join(path, "grades.txt"))
            self._read_re()

        except (FileNotFoundError, ValueError) as e:
            print(e)

        if ptable:
            self.major_pretty_table()
            self.student_pretty_table()
            self.instructor_pretty_table()

    def _read_major(self, path: str) -> None:
        """ read each line from majors file and create instance of class major
        and if the file not found or any value error, it raises an exception """
        try:
            for major, req, course in file_reader(path, 3, sep='\t', header=True):
                if major not in self._major:
                    self._major[major] = Major(major)

                self._major[major].add_course_re(req, course)

        except (FileNotFoundError, ValueError) as e:
            print(e)

    def _read_students(self, path: str) -> None:
        """ read each line from student file and create instance of class student
        and if the file not found or any value error, it raises an exception """
        try:
            for cwid, name, major in file_reader(path, 3, sep='\t', header=True):
                if cwid not in self._students:
                    self._students[cwid] = Student(cwid, name, major)
                else:
                    print(f" Duplicate student {cwid}")
        except (FileNotFoundError, ValueError) as e:
            print(e)

    def _read_instructors(self, path: str):
        """read each line from instructors file and create instance of class instructor
        and if the file not found or any value error, it raises an exception"""
        try:
            for cwid, name, dept in file_reader(path, 3, sep='\t', header=True):
                if cwid not in self._instructors:
                    self._instructors[cwid] = Instructor(cwid, name, dept)
                else:
                    print(f" Duplicate instructor {cwid}")

        except (FileNotFoundError, ValueError) as e:
            print(e)

    def _read_grades(self, path: str) -> None:
        """ read the student_cwid, course, grade, instructor_cwid from the grades file
        and checks for the individual student and the individual instructor.
        Raises an exception when unknown student is found"""
        try:
            for student_cwid, course, grade, instructor_cwid in file_reader(path, 4, sep='\t', header=True):
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

    def _read_re(self):
        """ checking for the cwid in the major which is not in the repository """
        for cwid in self._students:
            student_info = self._students[cwid]
            student_major = student_info._major

            try:
                student_info.course_re(self._major[student_major])
            except:
                print(f" Student with CWID {cwid}  has a major {student_major} not in repository")

    def major_pretty_table(self) -> None:
        """print pretty table with major information by calling the global constant."""
        pt = PrettyTable(field_names=Major.PT_FIELD_NAMES)
        for mj in self._major.values():
            pt.add_row(mj.info())

        print("Major Summary")
        print(pt)

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


def database_connection():
    print("Student Grade Summary")
    try:
        db:sqlite3.Connection = sqlite3.connect('/Users/anerishah/Desktop/SSW810/WEEK 11/810_db_HW11')
    except sqlite3.OperationalError as e:
        print(e)
    else:
        pt:PrettyTable = PrettyTable(field_names=['Name', ' CWID', 'Course', 'Grade', 'Instructor'])
        try:
            query = """
                     select s.Name, s.CWID, g.Course, g.Grade, i.Name
                                      from students s join grades g on s.CWID = g.StudentCWID join instructors i on g.InstructorCWID = i.CWID
                                                           order by s.Name, g.Grade
                     """
            for row in db.execute(query):
                pt.add_row(row)
            print(pt)

        except sqlite3.OperationalError as e:
            print(e)


def main():
    """ define a repository for stevens"""
    stevens: Repository = Repository("/Users/anerishah/Desktop/SSW810/WEEK 11", ptable=True)
    database_connection()


if __name__ == '__main__':
    main()
