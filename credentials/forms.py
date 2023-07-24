# carapp/forms.py
from django import forms
from credentials.models import Payment
from .models import Assignment, Lecture

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['cardHolder', 'cardNumber', 'cardExpiry', 'cvd']
        labels = {
            'cardHolder': 'Please enter card holder name', 'cardNumber': 'Please enter card number', 'cardExpiry': 'Please enter expiry date mm/yy', 'cvd': 'Please enter cvd number'
        }

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['file']

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['file']

# forms.py


class GradeUpdateForm(forms.Form):
    def __init__(self, enrolled_students, *args, **kwargs):
        super(GradeUpdateForm, self).__init__(*args, **kwargs)
        for student in enrolled_students:
            self.fields[f"grade_{student}"] = forms.CharField(label=student, max_length=100)
class CourseSearchForm(forms.Form):
    coursename = forms.CharField(required=False)



        

