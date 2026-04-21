from registrationSystem import RegistrationSystem

def main() :
    system = RegistrationSystem()
    print("Student Course Registration System Started!\n")
    
    while True :
        print("="*50)
        print("STUDENT COURSE REGISTRATION MENU")
        print("="*50)
        print("1. Add a new student")
        print("2. Add a new course")
        print("3. Enroll a student in a course")
        print("4. Drop a student from a course")
        print("5. View all students")
        print("6. View all courses")
        print("7. View courses for a specific student")
        print("8. Exit")
        print("=" * 55)
        
        choice = input("Enter your choice [1-8] : ").strip()
        
        match choice :
            case '1' :
                stu_id = input("Enter Student ID : ").strip()
                name = input("Enter Student Name : ").strip()
                success, msg = system.add_student(stu_id, name)
                print(msg)
            
            case '2' :
                code = input("Enter Course Code : ").strip()
                name = input("Enter Course Name : ").strip()
                try : 
                    capacity = int(input("Enter Course Capacity : "))
                    success, msg = system.add_course(code, name, capacity)
                    print(msg)
                except ValueError :
                    print("Capacity must be a valid integer!")
                    
            case '3' :
                stu_id = input("Enter Student ID : ").strip()
                code = input("Enter Course Code : ").strip()
                success, msg = system.enroll_student(stu_id, code)
                print(msg)
                
            case '4' :
                stu_id = input("Enter Student ID : ").strip()
                code = input("Enter Course Code : ").strip()
                success, msg = system.drop_student(stu_id, code)
                print(msg)
            case '5' : 
                print(system.view_all_students())
                
            case '6' :
                print(system.view_all_courses())
                
            case '7' : 
                stu_id = input("Enter Student ID : ").strip()
                print(system.view_student_courses(stu_id))
            
            case '8' :
                print("👋 Goodbye!~")
                return
            
            case _ :
                print("❌ Invalid choice! Please enter a number between 1 and 8!")
                
main()