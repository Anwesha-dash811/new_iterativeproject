def course_creation():
    print("MY COURSES")
    n1=int(input("Enter the number of courses to enter: "))
    for i in range(n1):
        uv=input("Upload the video name: ")
        ud=input("Upload the course details: ")
    print("COURSE DETAILS" +uv+":" +ud)
def create_quiz():
    print("CREATE QUIZ")
    t=input("Enter the title of quiz: ")
    n2=int(input("Enter the number of questions: "))
    tim=int(input("Enter the time-limit in minutes: "))
    for j in range(n2):
        qt=input("Enter question text: ")
        no=int(input("Enter the number of options: "))
        for k in range(no):
            np=input("Enter the options")
    print("QUESTION PAPER: " +qt+np)
course_creation()
create_quiz()


