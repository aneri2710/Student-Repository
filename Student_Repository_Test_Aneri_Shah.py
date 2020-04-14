"""
Aneri Shah
Homework 9

Implementing test cases of the student, instructor, and repository.

"""
import unittest


from HW09_Aneri_Shah import Student, Repository, Instructor


class RepositoryTestCase(unittest.TestCase):
    """ This will check for individual student, instructor and repository if not found test cases"""
    def test_student(self):
        """ Test case to check for the student instance in Repository class """
        a = Repository('/Users/anerishah/Desktop/SSW810/WEEK 9')
        lis = list()
        for key in a._students:
            lis.append(a._students[key].info())
        result = [['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']],
                 ['10115', 'Wyatt, X', 'SFEN', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']],
                 ['10172', 'Forbes, I', 'SFEN', ['SSW 555', 'SSW 567']],
                 ['10175', 'Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687']],
                 ['10183', 'Chapman, O', 'SFEN', ['SSW 689']],
                 ['11399', 'Cordova, I', 'SYEN', ['SSW 540']],
                 ['11461', 'Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800']],
                 ['11658', 'Kelly, P', 'SYEN', ['SSW 540']],
                 ['11714', 'Morton, A', 'SYEN', ['SYS 611', 'SYS 645']],
                 ['11788', 'Fuller, E', 'SYEN', ['SSW 540']]]
        self.assertEqual(lis, result)

    def test_instructor(self):
        """ Test case to check for the instructor instance in Repository class """
        a = Repository('/Users/anerishah/Desktop/SSW810/WEEK 9')
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
            Repository('/Users/anerishah/Desktop/SSW810/WEEK 9/NYU')


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
