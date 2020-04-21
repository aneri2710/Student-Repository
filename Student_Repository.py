"""

Aneri Shah
Homework 12

To add web pages into the application that takes data from the database and adds in the HTML pages.

"""

from flask import Flask, render_template
import sqlite3
from typing import Dict, List

app: Flask = Flask(__name__)
""" Adding the database file """
DB_FILE: str = "/Users/anerishah/Desktop/SSW810/WEEK 12/810_db_HW11"


@app.route("/completed")
def completed_table() -> str:
    """ Adding the decorator function which takes the query to execute and printing if any error is found
        Adding the data from the database and rendering the templates from the templates folder.
    """
    try:
        db: sqlite3.Connection = sqlite3.connect(DB_FILE)
        query: str = "SELECT s.Name, s.CWID, g.Course, g.Grade, i.Name AS 'Instructor' " \
                     "FROM grades g JOIN students s ON g.StudentCWID = s.CWID " \
                     "JOIN instructors i ON g.InstructorCWID = i.CWID ORDER BY s.Name"
    except sqlite3.OperationalError as e:
        print(e)

    data: List[Dict[str, str]] = [
        {"name": name, "cwid": cwid, "course": course, "grade": grade, "instructor": instructor}
        for name, cwid, course, grade, instructor in db.execute(query)]
    db.close()

    return render_template("student_summary.html",
                           title="Stevens Repository",
                           table_title="Student, Course, Grade and Instructor",
                           students=data)


if __name__ == '__main__':
    app.run(debug=True)
