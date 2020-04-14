"""
Aneri Shah
Homework 10

Implementing test cases of the student, instructor, major and repository.

"""
import unittest

from HW10_Aneri_Shah import Student, Repository, Instructor


class RepositoryTestCase(unittest.TestCase):
    """ This will check for individual student, instructor, majors and repository if not found test cases"""

    def test_majors(self):
        """ Test case to check for the major instance in Repository class """
        a = Repository('/Users/anerishah/Desktop/SSW810/WEEK 10')
        lis = list()
        for key in a._major:
            lis.append(a._major[key].info())
        result = [['SFEN',['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'],['CS 501', 'CS 513', 'CS 545']],['SYEN', ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']]]
        self.assertEqual(lis, result)

    def test_student(self):
        """ Test case to check for the student instance in Repository class """
        a = Repository('/Users/anerishah/Desktop/SSW810/WEEK 10')
        lis = list()
        for key in a._students:
            lis.append(a._students[key].info())
        result = [
            ['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [],
             3.44],
            ['10115', 'Wyatt, X', 'SFEN', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [],
             3.81],
            ['10172', 'Forbes, I', 'SFEN', ['SSW 555', 'SSW 567'], ['SSW 540', 'SSW 564'],
             ['CS 501', 'CS 513', 'CS 545'], 3.88],
            ['10175', 'Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'],
             ['CS 501', 'CS 513', 'CS 545'], 3.58],
            ['10183', 'Chapman, O', 'SFEN', ['SSW 689'], ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'],
             ['CS 501', 'CS 513', 'CS 545'], 4.0],
            ['11399', 'Cordova, I', 'SYEN', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], [], 3.0],
            ['11461', 'Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800'], ['SYS 612', 'SYS 671'],
             ['SSW 540', 'SSW 565', 'SSW 810'], 3.92],
            ['11658', 'Kelly, P', 'SYEN', [], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810'],
             0.0],
            ['11714', 'Morton, A', 'SYEN', ['SYS 611', 'SYS 645'], ['SYS 612', 'SYS 671', 'SYS 800'],
             ['SSW 540', 'SSW 565', 'SSW 810'], 3.0],
            ['11788', 'Fuller, E', 'SYEN', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], [], 4.0]]
        self.assertEqual(lis, result)

    def test_instructor(self):
        """ Test case to check for the instructor instance in Repository class """
        a = Repository('/Users/anerishah/Desktop/SSW810/WEEK 10')
        lis = list()
        for key in a._instructors:
            for i in a._instructors[key].info_i():
                lis.append(i)
                result = [['98765', 'Einstein, A', 'SFEN', 'SSW 567', 4],
                          ['98765', 'Einstein, A', 'SFEN', 'SSW 540', 3],
                          ['98764', 'Feynman, R', 'SFEN', 'SSW 564', 3],
                          ['98764', 'Feynman, R', 'SFEN', 'SSW 687', 3],
                          ['98764', 'Feynman, R', 'SFEN', 'CS 501', 1],
                          ['98764', 'Feynman, R', 'SFEN', 'CS 545', 1],
                          ['98763', 'Newton, I', 'SFEN', 'SSW 555', 1],
                          ['98763', 'Newton, I', 'SFEN', 'SSW 689', 1],
                          ['98760', 'Darwin, C', 'SYEN', 'SYS 800', 1],
                          ['98760', 'Darwin, C', 'SYEN', 'SYS 750', 1],
                          ['98760', 'Darwin, C', 'SYEN', 'SYS 611', 2],
                          ['98760', 'Darwin, C', 'SYEN', 'SYS 645', 1]]
        self.assertEqual(lis, result)

    def test_repository(self):
        """ Test case to check for the Repository class if the repository is empty or not """
        # NYU is an empty directory
        with self.assertRaises(FileNotFoundError):
            Repository('/Users/anerishah/Desktop/SSW810/WEEK 10/NYU')


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
