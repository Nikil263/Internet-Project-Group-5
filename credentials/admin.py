from django.contrib import admin

# Register your models here.
from .models import Profile
from .models import Student
from .models import Course
from .models import File
from .models import Membership
from .models import Payment
from .models import Enrolment
from .models import Assignment
from .models import Review
from .models import WebsiteFeedback


admin.site.register(Profile)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(File)
admin.site.register(Membership)
admin.site.register(Payment)
admin.site.register(Enrolment)
admin.site.register(Assignment)
admin.site.register(Review)
admin.site.register(WebsiteFeedback)