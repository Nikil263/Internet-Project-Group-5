from django.shortcuts import render
from .models import Profile, Student, Course, File, Membership, Payment, Enrolment, WebsiteFeedback
from django.http import HttpResponse


from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
 


def signup(request):
    if request.method == 'POST':
        firstName = request.POST['name']
        lastName = request.POST['lastname']
        userName = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        userType = request.POST['userType']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return redirect('signup')
            elif User.objects.filter(username=userName).exists():
                messages.info(request, 'username already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=userName, email=email, password=password)
                user.save()

                userProfile = Profile(firstName=firstName, lastName=lastName, userType=userType, userName=user)
                userProfile.save()

                
                return redirect('/login/')
        
        else:
            messages.info(request, "passwords do not match")
            return redirect('signup/')
            
    return render(request, "registrationapp/signup.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # User credentials are valid, log the user in
            login(request, user)
            message = "login successful"
            profile = Profile.objects.get(userName=username)
            print(username)
            print(profile)
            
            print(user)
            
            print(profile)
            allCourses = []
            if profile.userType==1:
                print("student")
                Enr = Enrolment.objects.filter(profile=profile)
                return render(request, 'homepage.html', {'message': message, 'user_type': 1, 'username': username, 'enrol': Enr})
            else:
                try:
                    a = 5
                    allCourses = Course.objects.filter(profile = profile)
                    print(a)
                    print(allCourses)
                except Exception as e:
                    print('%s' % type(e))
                
                                    
                
                
                print("organizer")
                return render(request, 'homepage.html', {'message': message, 'user_type': 2, 'username': username, 'courses': allCourses})
                
        else:
            message = "Invalid username or password"
            return render(request, 'registrationapp/login.html', {'message': message})
    else:
        return render(request, 'registrationapp/login.html')
    
from .forms import CourseSearchForm
def search_courses(request):
    courses = None
    form = CourseSearchForm(request.GET)

    if form.is_valid() and 'search' in request.GET:
        courseName = form.cleaned_data['coursename']

        courses = Course.objects.all()

        if courseName:
            courses = courses.filter(courseName__icontains=courseName)

    #return redirect("/loadHomepage/" + request.user.username + "/ /")
    return render(request, 'course_search_results.html', {'courses': courses, 'form': form, 'username': request.user.username})
from django.shortcuts import redirect
from django.contrib import messages

def leave_review(request, course_id):
   
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        return HttpResponse("Course not found", status=404)

    if request.method == 'POST':
        review = request.POST.get('review')
        rating = request.POST.get('rating')

        # Assuming you have a Review model that stores reviews for courses
        # You can create a new review and associate it with the course and the user
        # Make sure to handle form validation and error handling as needed

        # Example:
        from .models import Review
        new_review = Review(course=course, user=request.user, review=review, rating=rating)
        new_review.save()

        # Render a success page
        return render(request, 'review_submitted.html', {'username':request.user.username})

    return render(request, 'leave_review.html', {'course': course})


def Feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        review = request.POST.get('review')
        rating = request.POST.get('rating')

        print(name)
        print(review)
        print(rating)
        # Assuming you have a Review model that stores reviews for courses
        # You can create a new review and associate it with the course and the user
        # Make sure to handle form validation and error handling as needed

        # Example:
        #print(WebsiteFeedback.objects.all())
        WebsiteFeedback(feedbacker=name, review=review, rating=rating).save()
        

        # Render a success page
        return render(request, 'Feedback.html', {'message': "your feedabck has been submitted"})
    else:
        return render(request, 'Feedback.html', {'message': ""})


    

def logouts(request):
    logout(request)
    return redirect('/')