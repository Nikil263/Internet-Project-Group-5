from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
class Profile(models.Model):
    userName = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE, default=None)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    ch = [(0,'-----'), (1,'Student'), (2,'Instructor')]
    userType = models.PositiveIntegerField(choices=ch, default=0)
    def __str__(self):
        return self.firstName

class Student(models.Model):
    studentId = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    member = [(0,'-----'), (1,'Gold'), (2,'Silver'), (3,'Bronze')]

    def __str__(self):
        return self.studentId

class Course(models.Model):
    courseNumber = models.CharField(max_length=50)
    courseName = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


    def __str__(self):
        return self.courseNumber

class File(models.Model):
    courseNumber = models.ForeignKey(Course, on_delete=models.CASCADE)
    fileName = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.fileName

class Membership(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    choices = [('0','-----'), ('1','Gold'), ('2','Silver'), ('3','Bronze')]
    member = models.CharField(max_length=2, choices=choices, default='0')
    def __str__(self):
        return self.member

class Payment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    cardHolder = models.CharField(max_length=200)
    cardNumber = models.CharField(max_length=16)
    cardExpiry = models.CharField(max_length=16)
    cvd = models.CharField(max_length=16)
    
class Enrolment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)
    grade = [(0,'-----'), (1,'W'), (2,'Pass'), (2,'Fail') ]
    marks = models.CharField(max_length=16)
    
    def __str__(self):
        return self.profile.userName.username + " "

def get_assignment_upload_path(instance, filename):
    new_filename = f'assignment_{instance.id}_{filename}'
    return os.path.join('assignments', new_filename)

def get_lecture_upload_path(instance, filename):
    new_filename = f'lecture_{instance.id}_{filename}'
    return os.path.join('lectures', new_filename)

class Assignment(models.Model):
    file = models.FileField(upload_to=get_assignment_upload_path)

    def pre_save(self):
        if self.file:
            self.file.upload_to = get_assignment_upload_path(self, self.file.name)

        super().pre_save()

class Lecture(models.Model):
    file = models.FileField(upload_to=get_lecture_upload_path)

    def pre_save(self):
        if self.file:
            self.file.upload_to = get_lecture_upload_path(self, self.file.name)

        super().pre_save()
class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class WebsiteFeedback(models.Model):
    feedbacker = models.CharField(max_length=20)
    review = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return self.feedbacker
