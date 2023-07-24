from django.shortcuts import render
from .models import Profile, Student, Course, File, Membership, Payment, Enrolment
from .forms import PaymentForm, AssignmentForm, LectureForm, GradeUpdateForm
import os

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404

def setting(request, userType):
    return render(request, 'settings.html', {'user_type': userType})

def course_creation(request):
    if request.method == 'POST':
        courseNumber = request.POST['courseNumber']
        courseName = request.POST['courseName']
        profile = get_object_or_404(Profile, userName=request.user)
        
        course = Course.objects.create(courseNumber=courseNumber, courseName=courseName, profile=profile)
        
        course.save()
        message = "course has been saved"
        userName = request.user.username
        return redirect("/loadHomepage/" + userName + "/ /")

    else:
        return render(request, 'course_creation.html', {'message': 'hi', 'user_type': 2})

    
def loadHomepage(request, username, message):
    # print(User.username)
    profile = Profile.objects.get(userName = username)
    # print(user)
    print(profile)
    allCourses = []
    #message = ""
    
    if profile.userType==1:
        print("student")
        Enr = Enrolment.objects.filter(profile=profile)
        return render(request, 'homepage.html', {'message': message, 'user_type': 1, 'enrol': Enr, 'username': username})
    else:
        try:
            a = 5
            allCourses = Course.objects.filter(profile = profile)
            print(a)
            #allCourses = Course.objects.all()
            print(allCourses)
        except Exception as e:
            print('%s' % type(e))
        print("organizer")
        return render(request, 'homepage.html', {'message': message, 'user_type': 2, 'username': username, 'courses': allCourses})


def member(request):
    message = ""
    events = []
    username = ""
    
    return render(request, 'membership/member.html', {'message': message, 'user_type': 1, 'events': events, 'username': username})

def payment(request):
    if request.method == 'POST':
        cardHolder = request.POST.get('cardHolder')
        cardNumber = request.POST.get('cardNumber')
        cardExpiry = request.POST.get('cardExpiry')
        cvd = request.POST.get('cvd')

        print(cardHolder)
        print(cardNumber)
        print(cardExpiry)
        print(cvd)

        userName = request.user.username
        return redirect("/loadHomepage/" + userName + "/membership successful/")
    else:
        message = ""
        events = []
        username = request.user.username
        print(username)
        profile = Profile.objects.get(userName=username)
        print(profile)
        membership = request.POST.get('membership')
        print(membership)
        member = Membership(profile=profile, member=membership)
        member.save()
        form = PaymentForm(request.POST)
        return render(request, 'membership/payment.html', {'message': message, 'form': form, 'user_type': 1, 'events': events, 'username': username})

def loadPaymentForm(request):
    form = PaymentForm
    return render(request, 'membership/payment.html', {'message': "", 'form': form, 'user_type': 1, 'username': request.user.username})

def payment(request):
    if request.method == 'POST':
        cardHolder = request.POST.get('cardHolder')
        cardNumber = request.POST.get('cardNumber')
        cardExpiry = request.POST.get('cardExpiry')
        cvd = request.POST.get('cvd')

        print(cardHolder)
        print(cardNumber)
        print(cardExpiry)
        print(cvd)

        userName = request.user.username
        return redirect("/loadHomepage/" + userName + "/membership successful/")

def courseDetails(request, courseId):
    print("course id " , courseId)
    return render(request, 'course/course_details.html', {'courseId': courseId, 'user_type': 1, 'username': request.user.username})

def lectures(request, courseId):
    print("course id lectures" , courseId)
    print(request.user.username)
    return render(request, 'course/lectures.html', {'courseId': courseId, 'user_type': 1, 'username': request.user.username})

def assignments(request, courseId):
    print("course id assignments" , courseId)
    print(request.user.username)
    return render(request, 'course/assignments.html', {'courseId': courseId, 'user_type': 1, 'username': request.user.username})

def upload_assignment(request, courseId):
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            filename = request.FILES['file'].name
            upload_dir = os.path.join('assignments', str(courseId))
            upload_path = os.path.join(upload_dir, filename)
            assignment.file.field.upload_to = ''
            assignment.file.name = upload_path
            assignment.save()
            
            
            return render(request, 'course/assignments.html', {'courseId': courseId, 'user_type': 1, 'username': request.user.username})
    else:
        form = AssignmentForm()
    return render(request, 'course/assignments.html', {'form': form, 'courseId': courseId})

def upload_lecture(request, courseId):
    # print("course id upload asssignment" , courseId)
    if request.method == 'POST':
        print("saving lecture")
        form = LectureForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            filename = request.FILES['file'].name
            upload_dir = os.path.join('lectures', str(courseId))
            upload_path = os.path.join(upload_dir, filename)
            assignment.file.field.upload_to = ''
            assignment.file.name = upload_path
            assignment.save()
            return render(request, 'course/lectures.html', {'courseId': courseId, 'user_type': 1, 'username': request.user.username})
    else:
        form = LectureForm()
    return render(request, 'course/lectures.html', {'form': form, 'courseId': courseId})


def enrolment(request, username):
    if request.method == 'POST':
        profile = Profile.objects.get(userName=username)
        course = Course.objects.all()
        c = request.POST.get('course')
        co = Course.objects.filter(courseNumber=c)
        try:
            e = Enrolment.objects.get(profile=profile)
            e.course.add(co)

        except:
            e = Enrolment(profile=profile, marks='0')

            e.save()
            e.course.set(co)
        return redirect("/loadHomepage/" + username + "/enrolment successful/")

    else:
        course = Course.objects.all()
        return render(request, 'enrol.html', {'course': course, 'username': username})


def cd(request, username, courseid):
    course = Course.objects.get(pk=courseid)
    print("sdfd")
    directory = 'C:\\Users\\Intel\\PycharmProjects\\internet\\media\\assignments'
    directory = os.path.join(directory, str(courseid))
    file_list = []
    print(f"Directory: {directory}")
    try:
        for root, dirs, files in os.walk(directory):
            print(f'Root: {root}')
            print(f'Directories: {dirs}')
            print(f'Files: {files}')
            for file in files:
                file_path = os.path.join(root, file)
                file_list.append(file_path)

    except Exception as e:
        print(f"Error occurred during os.walk(): {str(e)}")

    directory = 'C:\\Users\\Intel\\PycharmProjects\\internet\\media\\lectures'
    directory = os.path.join(directory, str(courseid))
    file_list1 = []
    print(f"Directory: {directory}")
    try:
        for root, dirs, files in os.walk(directory):
            print(f'Root: {root}')
            print(f'Directories: {dirs}')
            print(f'Files: {files}')
            for file in files:
                file_path = os.path.join(root, file)
                file_list1.append(file_path)

    except Exception as e:
        print(f"Error occurred during os.walk(): {str(e)}")

    for file_path in file_list:
        print(file_path)
    print(file_list)

    return render(request, 'cd.html',
                  {'course': courseid, 'username': username, 'files': file_list, 'files1': file_list1})

def assign_grades_for_course(course_number, grades_dict):
    try:
        course = Course.objects.get(pk=course_number)
        print("cc", " ", course)
        enrollments = Enrolment.objects.filter(course=course)

        for enrollment in enrollments:
            username = enrollment.profile.userName.username
            print("u = ", username)
            if username in grades_dict:
                print("true")
                grade = grades_dict[username]
                print("grade = " , grade)
                enrollment.marks = grade
                print("enrol marks ", enrollment.marks)
                enrollment.save()  # Save the changes to the database
                print("enrol saved")
    except Course.DoesNotExist:
        pass

def grade_update_view(request):
    if request.method == "POST":
        course_id = request.POST.get('courseId')
        course = Course.objects.get(pk=course_id)
        enrolled_students = [enrollment.profile.userName.username for enrollment in Enrolment.objects.filter(course=course)]

        form = GradeUpdateForm(enrolled_students, request.POST)
        if form.is_valid():
            print("form is valid")

            grades_dict = {student: form.cleaned_data[f"grade_{student}"] for student in enrolled_students}
            print("gdictionary")
            print(grades_dict)
            print("course id ", course_id)

            assign_grades_for_course(course_id, grades_dict)

    else:
        course_id = request.POST.get('courseId')
        course = Course.objects.get(pk=course_id)
        enrolled_students = [enrollment.profile.userName.username for enrollment in Enrolment.objects.filter(course=course)]
        students_dictionary = {enrollment.profile.userName.username: enrollment.marks for enrollment in Enrolment.objects.filter(course=course)}
        form = GradeUpdateForm(enrolled_students, initial=students_dictionary)
    return redirect("/loadHomepage/" + request.user.username + "/ /")

def create_grades_dict_for_course(request, courseId):

    try:
        course = Course.objects.get(pk=courseId)
        print("course = ", course)
        enrollments = Enrolment.objects.filter(course=course)

        grades_dict = {enrollment.profile.userName.username: enrollment.marks for enrollment in enrollments}
        enrolledStudents = list(grades_dict.keys())
        print(grades_dict)

        return render(request, 'grading/student_list.html',  {'courseId': courseId, 'studentsDictionary': grades_dict, 'enrolledStudents': enrolledStudents, 'username': request.user.username})
    except Course.DoesNotExist:
        return None

