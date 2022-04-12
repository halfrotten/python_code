#AverageGrade takes in student then returns weighted grade
#weighted grades are 20% for discussions,40% for quizzes, 40% for assignements

def AverageGrade(student_in):
    while True:
        try:#get input and make sure its a integer
            disc_grade=eval(input('please enter discusion grade ')) 
            break
        except:
            pass
    while True:
        try:#get input and make sure its a integer
            quiz_grade=eval(input('please enter quiz grade '))
            break
        except:
            pass
    while True:
        try:#get input and make sure its a integer
            assign_grade=eval(input('please enter programming assignment grade '))
            break
        except:
            pass


    return ((disc_grade*.20)+(quiz_grade*.40)+(assign_grade*.40)) #returning weighted grade



if  __name__== '__main__':
    top_grade=0
    top_student=None
    students=['Jim','Bob','Andy','Kim']#list of students needing scores to be logged
    check=[]#store students logged
    for i in range(len(students)): 
        
        while True:
            student_in=input('Please enter your name ')
            if student_in in students: #check to see student in system list
                if student_in in check:#check to see if students scores already logged
                    print('student information already entered ')
                else:
                    check.append(student_in) # add student to logged list
                    break
            else:
                print('not correct student information')
        
        student_in_grade=AverageGrade(student_in)#calling function returning weighted grade
        check.append(student_in_grade)#adding score to list next to student
        if student_in_grade>top_grade: #checking to see if top grade against last entered grade
            top_grade=student_in_grade #store top grade and student
            top_student=student_in
    print("\nthe top student is",top_student, "and their grade is",str(top_grade))#print grade
    #print('\n','the list of total students and their grades',check)
    #print list of users and grades
          
    
    
        
        
        
 
