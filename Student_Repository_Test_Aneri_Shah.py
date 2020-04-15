"""
Aneri Shah
Homework 11

Implementing test cases of the student, instructor, major and repository.

"""
import unittest

from Student_Repository_Aneri_Shah import Student, Repository, Instructor


class RepositoryTestCase(unittest.TestCase):
    """ This will check for individual student, instructor, majors and repository if not found test cases"""

    def test_majors(self):
        """ Test case to check for the major instance in Repository class """
        a = Repository('/Users/anerishah/Desktop/SSW810/WEEK 10')
        lis = list()
        for key in a._major:
            lis.append(a._major[key].info())
        result = [['SFEN', ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']],
                  ['SYEN', ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']]]
        self.assertEqual(lis, result)

    def test_student(self):
        """ Test case to check for the student instance in Repository class """
        a = Repository('/Users/anerishah/Desktop/SSW810/WEEK 11')
        lis = list()
        for key in a._students:
            lis.append(a._students[key].info())
        result = [['10103',
                   'Jobs, S',
                   'SFEN',
                   ['CS 501', 'SSW 810'],
                   ['SSW 540', 'SSW 555'],
                   [],
                   3.38],
                  ['10115',
                   'Bezos, J',
                   'SFEN',
                   ['SSW 810'],
                   ['SSW 540', 'SSW 555'],
                   ['CS 501', 'CS 546'],
                   2.0],
                  ['10183',
                   'Musk, E',
                   'SFEN',
                   ['SSW 555', 'SSW 810'],
                   ['SSW 540'],
                   ['CS 501', 'CS 546'],
                   4.0],
                  ['11714', 'Gates, B', 'CS', ['CS 546', 'CS 570', 'SSW 810'], [], [], 3.5]]
        self.assertEqual(lis, result)

    def test_instructor(self):
        """ Test case to check for the instructor instance in Repository class """
        a = Repository('/Users/anerishah/Desktop/SSW810/WEEK 11')
        lis = list()
        for key in a._instructors:
            for i in a._instructors[key].info_i():
                lis.append(i)
                result = [['98764', 'Cohen, R', 'SFEN', 'CS 546', 1],
                          ['98763', 'Rowland, J', 'SFEN', 'SSW 810', 4],
                          ['98763', 'Rowland, J', 'SFEN', 'SSW 555', 1],
                          ['98762', 'Hawking, S', 'CS', 'CS 501', 1],
                          ['98762', 'Hawking, S', 'CS', 'CS 546', 1],
                          ['98762', 'Hawking, S', 'CS', 'CS 570', 1]]
        self.assertEqual(lis, result)

    def test_repository(self):
        """ Test case to check for the Repository class if the repository is empty or not """
        # NYU is an empty directory
        with self.assertRaises(FileNotFoundError):
            Repository('/Users/anerishah/Desktop/SSW810/WEEK 11/NYU')

    def test_database(self):
        """ Test case to check if the database file cannot open"""
        with self.assertRaises(IOError):
            Repository('/Users/anerishah/Desktop/SSW810/WEEK 11/810_db_HW11_test')


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
