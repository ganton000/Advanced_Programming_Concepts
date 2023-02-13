class WeightedGradebook(object):

	def __init__(self):
		self._grades = {}
		self.average_subject_grades = None

	def add_student(self, name):
		self._grades[name] = {}

	def report_grade(self, name, subject, score, weight):
		student_grade = self._grades[name]
		grade_list = student_grade.setdefault(subject, [])
		grade_list.append((score, weight))

	def average_grades_by_subject(self, name):
		student_grade = self._grades[name]
		self.average_subject_grades = {}
		for subject, grades in student_grade.items():
			weighted_scores, total_weight = 0, 0
			for score, weight in grades:
				weighted_scores += score*weight
				total_weight += weight
			self.average_subject_grades[subject] = weighted_scores/total_weight
		return self.average_subject_grades

	def average_grade(self, name):
		if self.average_subject_grades is None:
			self.average_grades_by_subject(name)

		grade_total, num_of_subjects = 0,0
		for grade in self.average_subject_grades.values():
			grade_total += grade
			num_of_subjects += 1
		return (grade_total/num_of_subjects)


if __name__ == "__main__":

	book = WeightedGradebook()
	book.add_student("Isaac")
	book.report_grade("Isaac", "Math", 90, 0.90)
	book.report_grade("Isaac", "Math", 85, 0.10)
	book.report_grade("Isaac", "Gym", 90, 0.20)
	book.report_grade("Isaac", "Gym", 80, 0.20)
	#book.report_grade("Isaac", "Physics", 82)
	#book.report_grade("Isaac", "English", 97)
	print(book.average_grades_by_subject("Isaac"))
	print(book.average_grade("Isaac"))