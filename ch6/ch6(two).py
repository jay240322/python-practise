#  Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user

subject1 = int(input("enter the marks: "))
subject2 = int(input("enter the marks: "))
subject3 = int(input("enter the marks: "))

total_marks = ((subject1+subject2+subject3)*100)/300

if(total_marks>=40 and subject1>=33 and subject2>=33 and subject3>=33):
    print("you'r are passed !  \n\t congratulation",total_marks)
else:
    print("you'r are failed ! ", total_marks,"\ntry gain next year")