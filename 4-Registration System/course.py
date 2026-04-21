class Course :
    def __init__(self, course_code, name, capacity) :
        self.course_code = course_code
        self.name = name
        self.capacity = capacity
        self.enrolled_students = []
        
    def enroll_student(self, student_id) :
        if len(self.enrolled_students) < self.capacity and student_id not in self.enrolled_students :
            self.enrolled_students.append(student_id)
            return True
        return False
    
    def drop_student(self, student_id) :
        if student_id in self.enrolled_students :
            self.enrolled_students.remove(student_id)
            return True
        return False
    
    def get_enrolled_count(self) :
        return len(self.enrolled_students)
        