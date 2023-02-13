# Refactor of using_classes.py
from collections import namedtuple

Grade = namedtuple("Grade", ("score", "weight"))

class Subject(object):

	def __init__(self):
		self._grades = []

	def report_grade(self, score, weight):
		self._grades.append(Grade(score, weight))

	def average_grade(self):
		total, total_weight = 0, 0
		for grade in self._grades:
			total += grade.score * grade.weight
			total_weight += grade.weight

		return total / total_weight

class Student(object):

	def __init__(self):
		self._subjects = {}

	def subject(self, name):
		if name not in self._subjects:
			self._subjects[name] = Subject()

		return self._subjects[name]

	def average_grade(self):
		total, count = 0, 0
		for subject in self._subjects.values():
			total += subject.average_grade()
			count += 1

		return total / count

class Gradebook(object):

	def __init__(self):
		self._students = {}

	def student(self, name):
		if name not in self._students:
			self._students[name] = Student()
		return self._students[name]

if __name__ == "__main__":

	# grade = Grade(95, 0.42)
	# print(grade)

	grade_book = Gradebook()

	albert = grade_book.student("Albert Einstein")

	math = albert.subject("Math")
	math.report_grade(80, 0.10)
	math.report_grade(80, 0.10)
	math.report_grade(70, 0.80)

	gym = albert.subject("Gym")
	gym.report_grade(100, 0.40)
	gym.report_grade(85, 0.60)

	print(albert.average_grade())
