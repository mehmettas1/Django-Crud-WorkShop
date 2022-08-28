from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ('fullname','number','mobile', 'email', 'gender','path')
    labels = {
        'fullname':'Full Name',
         'number':'Student Number'
 }
    widgets = {

        'fullname':forms.TextInput(attrs={'class': 'form-control  row mb-3','placeholder':'First Name'}),
        'mobile':forms.TextInput(attrs={'class': 'form-control  row mb-3','placeholder':'Last Name'}),
        'number':forms.NumberInput(attrs={'class': 'form-control  row mb-3','placeholder':'Student Number'}),
        'email':forms.NumberInput(attrs={'class': 'form-control  row mb-3','placeholder':'Student Number'}),
        'gender':forms.TextInput(attrs={'class': 'form-control  row mb-3','placeholder':'Student Number'}),
        'path':forms.TextInput(attrs={'class': 'form-control  row mb-3','placeholder':'Student Number'}),

        }

  def __init__(self, *args, **kwargs):
   super(StudentForm,self).__init__(*args, **kwargs)
   self.fields['path'].empty_label = "Select"
   self.fields['number'].required = False