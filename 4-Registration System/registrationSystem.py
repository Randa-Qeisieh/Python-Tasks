from student import Student
from course import Course

class RegistrationSystem :
    def __init__(self) :
        self.students = {}
        self.courses = {}
        
    # helper function to get courses for a specific student
    def find_student(self, student_id) :
        return self.students.get(student_id)
    
    def find_course(self, course_code) :
        return self.courses.get(course_code)
    
    def add_student(self, student_id, student_name) :
        if not student_id or not student_name :
            return False, "Error: Student ID and name cannot be empty."
        if student_id in self.students :
            return False, f"Error: Student ID '{student_id}' already exists." 
        self.students[student_id] = Student(student_id, student_name)
        return True, f"✅ Student '{student_name}' (ID: {student_id}) added successfully."
    
    def add_course(self, course_code, course_name, course_capacity) :
        if not course_code or not course_name :
            return False, "Error: Course code and name cannot be empty." 
        if course_code in self.courses :
            return False, f"Error: Course code '{course_code}' already exists." 
        if course_capacity <= 0 :
            return False, "Error: Capacity must be greater than 0."
        self.courses[course_code] = Course(course_code, course_name, course_capacity)
        return True, f"✅ Course '{course_name}' (Code: {course_code}, Capacity: {course_capacity}) added successfully."
    
    def enroll_student(self, student_id, course_code) :
        student = self.find_student(student_id)
        if not student :
            return False, f"Error: Student ID '{student_id}' does not exist."
        course = self.find_course(course_code)
        if not course :
            return False, f"Error: Course code '{course_code}' does not exist."
        if course_code in student.enrolled_courses :
            return False, f"Error: Student '{student_id}' is already enrolled in course '{course_code}'."
        if course.get_enrolled_count() >= course.capacity :
            return False, f"Error: Course '{course_code}' is full ({course.get_enrolled_count()}/{course.capacity})." 
        # enroll the student in both places
        student.enroll_course(course_code)
        course.enroll_student(student_id)
        return True, f"✅ Student '{student_id}' enrolled in course '{course_code}' successfully."
    
    def drop_student(self, student_id, course_code):
        student = self.find_student(student_id)
        if not student:
            return False, f"Error: Student ID '{student_id}' does not exist."
        course = self.find_course(course_code)
        if not course:
            return False, f"Error: Course code '{course_code}' does not exist."
        if course_code not in student.enrolled_courses:
            return False, f"Error: Student '{student_id}' is not enrolled in course '{course_code}'."
        student.drop_course(course_code)
        course.drop_student(student_id)
        return True, f"✅ Student '{student_id}' dropped from course '{course_code}' successfully."
    
    def view_all_students(self) :
        if not self.students :
            return "No students registered yet!"
        result = ["All Students : "]
        for stu_id, stu in self.students.items() :
            courses = ", ".join(stu.enrolled_courses) if stu.enrolled_courses else "None"
            result.append(f"  • {stu.student_name} ( ID : {stu_id} ) | Enrolled {courses}")
        return "\n".join(result)
        
    def view_all_courses(self) :
        if not self.courses :
            return "No courses available yet!"
        result = ["All Courses"]
        for code, course in self.courses.items() :
            enrolled = course.get_enrolled_count()
            result.append(f" • {course.name} ( Code : {code} ) | Capacity : {course.capacity} | Enrolled : {enrolled} ")
        return "\n".join(result)
    
    def view_student_courses(self, student_id) :
        student = self.find_student(student_id)
        if not student :
            return f"Student ID '{student_id}' does not exist."
        if not student.enrolled_courses :
            return f"Student '{student.student_name}' ( ID : {student_id} ) is not enrolled in any courses!"
        result = [f"Courses for '{student.student_name}' ( ID : {student_id} ) :"]
        for code in student.enrolled_courses :
            course = self.find_course(code)
            course_name = course.name if course else "Unknown"
            result.append(f" • {course_name} ( Code : {code} )")
        return "\n".join(result)