from django.contrib import admin
from django.urls import path
from . import views
from . import v_controller

urlpatterns = [
    path('', views.login_view),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),

    path('setting/<int:userType>/', v_controller.setting, name='setting'),

     path('member/', v_controller.member, name='member'),

    path('payment/', v_controller.payment, name='payment'),
    path('loadPaymentForm/', v_controller.loadPaymentForm, name='loadPaymentForm'),
   
     path('course_creation/', v_controller.course_creation, name='course_creation'),

  path('loadHomepage/<str:username>/<str:message>/', v_controller.loadHomepage, name='loadHomepage'),

  path('logout/', views.logouts, name='logout'),

   path('courseDetails/<int:courseId>/', v_controller.courseDetails, name='courseDetails'),

    path('lectures/<int:courseId>/', v_controller.lectures, name='lectures'),

     path('assignments/<int:courseId>/', v_controller.assignments, name='assignments'),

    path('course_grading/<int:courseId>/', v_controller.create_grades_dict_for_course, name='course_grading'),
path('assign_grades_for_course/', v_controller.grade_update_view, name='assign_grades_for_course'),

     path('search/', views.search_courses, name='search'),

     path('upload_assignment/<int:courseId>/', v_controller.upload_assignment, name='upload_assignment'),

    path('upload_lecture/<int:courseId>/', v_controller.upload_lecture, name='upload_lecture'),

    path('enrolment/<str:username>/', v_controller.enrolment, name='enrolment'),
    path('coursedisplay/<str:username>/<int:courseid>', v_controller.cd, name='cd'),

    path('course_review/<int:course_id>/leave_review/', views.leave_review, name='course_review'),
    
    path('feedback/', views.Feedback, name='feedback'),
    






  
     


    


]
