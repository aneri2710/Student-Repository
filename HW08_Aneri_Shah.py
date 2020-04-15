"""
Aneri Shah
Homework 8

Implementing different functions to implement different python modules such as datetime, prettytable, os

"""

from datetime import datetime, timedelta
import os
from typing import Tuple, Iterator, Dict
from prettytable import PrettyTable


def date_arithmetic()-> Tuple[datetime, datetime, int]:
    """ Implementing datetime module for returning of dates after some specific period of time """
    three_days_after_02272000: datetime = datetime(2020, 2, 27) + timedelta(days=3)

    three_days_after_02272017: datetime = datetime(2019, 2, 27) + timedelta(days=3)

    date3 = datetime(2019, 2, 1)
    date4 = datetime(2019, 9, 30)
    days_passed_01012017_10312017: int = date4 - date3

    return three_days_after_02272000, three_days_after_02272017, days_passed_01012017_10312017.days


def file_reader(path, fields, sep='|', header=False) -> Iterator[Tuple[str]]:
    """ Implementing a file reader function which allows to read a file and returns the number of fields which are
    separated by a separator """
    try:
        filePath = open(path, "r")
    except FileNotFoundError:
        print("File not found")
    else:
        with filePath:
            if filePath != "":
                if header is True:
                    next(filePath)
                for offset, line in enumerate(filePath):
                    result = line.strip().split(sep)
                    if len(result) == fields:
                        yield tuple(line.strip().split(sep))
                    else:
                        raise ValueError(f" {filePath} has {len(result)} on line {offset + 1} but expected {fields} ")


class FileAnalyzer:
    """ Class FileAnalyzer is a class which implements different functions to get the number of lines, characters,
    functions and classes in a directory with .py file """
    def __init__(self, directory: str) -> None:
        """ Initializing the directory and file summary of the class """
        self.directory: str = directory # NOT mandatory!
        self.files_summary: Dict[str, Dict[str, int]] = dict()

        self.analyze_files() # summerize the python files data

    def analyze_files(self) -> None:
        """ This will search the file ending with .py and counts the number of  lines, characters, unctions and
        classes and adding it in files.summary"""
        for files in os.listdir(self.directory):
            if files.endswith('.py'):
                classno, lines, funcno, charno = 0, 0, 0, 0
                try:
                    f = open(os.path.join(self.directory,files),'r')
                except FileNotFoundError:
                    raise FileNotFoundError
                else:
                    for lineno in f.readlines():
                        lines += 1
                        if lineno.strip().startswith('def '):
                            funcno += 1
                        if lineno.strip().startswith('class '):
                            classno += 1
                        charno += len(lineno)
                    self.files_summary[files] = {"class": classno, "function": funcno, "line": lines, "char": charno}
                    f.close()

    def pretty_print(self) -> None:
        """ This will print the pretty table of the field names  """
        pretty_table = PrettyTable()
        pretty_table.field_names = ["File Name", "Classes", "Functions", "Lines", "Characters"]

        for values in self.files_summary.items():
            pretty_table.add_row([values, values["class"], values["function"],
                                  values["line"], values["char"]])

        return pretty_table