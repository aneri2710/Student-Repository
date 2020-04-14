"""
Aneri Shah
Homework 8

Implementing test cases of the functions

"""

import unittest
import datetime
from HW08_Aneri_Shah import date_arithmetic, file_reader, FileAnalyzer


class TestFile(unittest.TestCase):
    """ To check for different functions describing different modules """

    def test_date_arithmetic(self):
        """ Test cases for date arithmetic """
        self.assertTupleEqual(date_arithmetic(),
                              (datetime.datetime(2020, 3, 1, 0, 0), datetime.datetime(2019, 3, 2, 0, 0), 241))
        self.assertNotEqual(date_arithmetic(),
                            (datetime.datetime(2019, 9, 30, 0, 0), datetime.datetime(2019, 2, 1, 0, 0), 21))
        self.assertNotEqual(date_arithmetic(), '')

    def test_file_reading_gen(self):
        """ Test cases for file reading with header and seperated by | """
        self.assertEqual(
            [a for a in file_reader("/Users/anerishah/Desktop/SSW810/WEEK 9/file.txt", 3, "|", True)],
            [["123", "Jin He", "Computer Science"], ["234", "Nanda Koka", "Software Engineering"],
             ["345", "Benji Cai", "Software Engineering"]])
        self.assertEqual(
            [a for a in file_reader("/Users/anerishah/Desktop/SSW810/WEEK 9/file.txt", 3, "|", False)],
            [['CWID', 'Name', 'Major'],
             ['123', 'Jin He', 'Computer Science'],
             ['234', 'Nanda Koka', 'Software Engineering'],
             ['345', 'Benji Cai', 'Software Engineering']])
        self.assertNotEqual(
            [a for a in file_reader("/Users/anerishah/Desktop/SSW810/WEEK 8/file.txt", 3, "|", False)],
            [['123', 'Jin He', 'Computer Science'],
             ['234', 'Nanda Koka', 'Software Engineering'],
             ['345', 'Benji Cai', 'Software Engineering']])

    def test_file_analyzer(self):
        """Test cases for file analyser"""
        file_analyzer = FileAnalyzer("/Users/anerishah/Desktop/SSW810/WEEK 9")
        self.assertEqual({'HW08_Aneri_Shah.py': {'char': 3685, 'class': 1, 'function': 5, 'line': 88},
 'HW08_Test_Aneri_Shah.py': {'char': 2594,
                             'class': 1,
                             'function': 3,
                             'line': 60},
 'HW09_Aneri_Shah.py': {'char': 6122, 'class': 3, 'function': 13, 'line': 146},
 'HW09_Test_Aneri_Shah.py': {'char': 2572,
                             'class': 1,
                             'function': 3,
                             'line': 59}},
                         file_analyzer.files_summary)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
