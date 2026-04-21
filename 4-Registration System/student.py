class Student :
    def __init__(self, student_id, student_name) :
        self.student_id = student_id 
        self.student_name = student_name
        self.enrolled_courses = []
        
    def enroll_course(self, course_code) :
        if course_code not in self.enrolled_courses :
            self.enrolled_courses.append(course_code)
            return True
        return False
    
    def drop_course(self, course_code) :
        if course_code in self.enrolled_courses :
            self.enrolled_courses.remove(course_code)
            return True
        return False