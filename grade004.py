class Student:
  def __init__(self, student_id, name, english_score, c_score, python_score):
      self.student_id = student_id
      self.name = name
      self.english_score = english_score
      self.c_score = c_score
      self.python_score = python_score
      self.total_score = self.calculate_total_score()
      self.average_score = self.calculate_average_score()
      self.grade = self.calculate_grade()
      self.rank = None

  def calculate_total_score(self):
      return self.english_score + self.c_score + self.python_score

  def calculate_average_score(self):
      return self.total_score / 3

  def calculate_grade(self):
      average = self.average_score
      if 90 <= average <= 100:
          return 'A+'
      elif 80 <= average < 90:
          return 'A'
      elif 70 <= average < 80:
          return 'B+'
      elif 60 <= average < 70:
          return 'B'
      elif 50 <= average < 60:
          return 'C+'
      elif 40 <= average < 50:
          return 'C'
      else:
          return 'F'


class ScoreManager:
  def __init__(self):
      self.students = []

  def input_student_info(self):
      student_id = input("학번: ")
      name = input("이름: ")
      english_score = int(input("영어 점수: "))
      c_score = int(input("C-언어 점수: "))
      python_score = int(input("파이썬 점수: "))
      student = Student(student_id, name, english_score, c_score, python_score)
      self.students.append(student)

  def calculate_ranks(self):
      sorted_students = sorted(self.students, key=lambda x: x.total_score, reverse=True)
      for i, student in enumerate(sorted_students, start=1):
          student.rank = i

  def display_student_info(self):
      print("=" * 80)
      print("성적관리 프로그램")
      print("=" * 80)
      print(f"{'학번':<10}{'이름':<10}{'영어':<10}{'C-언어':<10}{'파이썬':<10}{'총점':<10}{'평균':<10}{'학점':<10}{'등수':<10}")
      print("=" * 80)
      for student in self.students:
          print(f"{student.student_id:<10}{student.name:<10}{student.english_score:<10}{student.c_score:<10}"
                f"{student.python_score:<10}{student.total_score:<10}{student.average_score:<10.2f}"
                f"{student.grade:<10}{student.rank:<10}")

  def count_students_above_80(self):
      count = sum(1 for student in self.students if student.average_score >= 80)
      return count

  def show_menu(self):
      print("1. 학생 정보 추가")
      print("2. 학생 정보 삭제")
      print("3. 학생 정보 탐색")
      print("4. 전체 학생 정보 출력")
      print("5. 평균 점수가 80점 이상인 학생 수 출력")
      print("6. 프로그램 종료")

  def run(self):
      while True:
          self.show_menu()
          choice = input("메뉴를 선택하세요: ")
          if choice == '1':
              self.input_student_info()
          elif choice == '2':
              # 삭제 기능 추가
              student_id = input("삭제할 학생의 학번을 입력하세요: ")
              self.students = [student for student in self.students if student.student_id != student_id]
              print("학생 정보가 삭제되었습니다.")
          elif choice == '3':
              search_name = input("탐색할 학생의 이름을 입력하세요: ")
              search_id = input("탐색할 학생의 학번을 입력하세요: ")
              found = False
              for student in self.students:
                  if student.name == search_name and student.student_id == search_id:
                      print("===================================================================================")
                      print("탐색 결과:")
                      self.display_student_info()
                      found = True
                      break
              if not found:
                  print("해당하는 학생 정보를 찾을 수 없습니다.")
          elif choice == '4':
              self.display_student_info()
          elif choice == '5':
              count_above_80 = self.count_students_above_80()
              print(f"평균 점수가 80점 이상인 학생 수: {count_above_80}")
          elif choice == '6':
              print("프로그램을 종료합니다.")
              break


if __name__ == "__main__":
  score_manager = ScoreManager()
  score_manager.run()
