from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
        widgets = {
            'first_name': forms.Textarea(
                                attrs={
                                    "placeholder" : 'First Name' ,                                     
                                    "rows": '1',
                                    "type": 'text',
                                    "maxlength" : '80', 
                                    'required': 'true'                                                                                                         
                               }
                            ),
            'last_name': forms.Textarea(
                                attrs={
                                    "placeholder" : 'Last Name' ,                                     
                                    "rows": '1',
                                    "type": 'text',
                                    "maxlength" : '80', 
                                    'required': 'true'                                                                                                         
                               }
                            ),
            'email': forms.Textarea(
                                attrs={
                                    "placeholder" : 'sample@company.com' ,                                     
                                    "rows": '1',
                                    "type": 'text',
                                    "maxlength" : '80', 
                                    'required': 'true'                                                                                                         
                               }
                            ),
        }
class ProfileForm(forms.ModelForm):
    class Meta:
        College_CHOICES = (
        ('Veermata Jijabai Technological Institute','Veermata Jijabai Technological Institute'),
        ('Sardar Patel Institute of Technology','Sardar Patel Institute of Technology'),
        ('KJ Somaiya College of Engineering','KJ Somaiya College of Engineering'),
        ('Dwarkadas J Sanghvi College of Engineering','Dwarkadas J Sanghvi College of Engineering'),
        ('Sardar Patel College of Engineering','Sardar Patel College of Engineering'),
        ('Thadomal Shahani Engineering College','Thadomal Shahani Engineering College'),
        ('Vivekanand Education Societys Institute of Technology','Vivekanand Education Societys Institute of Technology'),
        ('KJ Somaiya Institute of Engineering and Information Technology','KJ Somaiya Institute of Engineering and Information Technology'),
        )
        model = Profile
        fields = ['stu_id', 'mob_num', 'stu_col','course','year']
        widgets = {
            'stu_id': forms.NumberInput(
                attrs={'min':000000000000,'max': 999999999999,'type': 'number'}
                ),
            'mob_num': forms.NumberInput(
                attrs={'min':0000000000,'max': 9999999999,'type': 'number'}
                ),
            'course': forms.TextInput(),
            'year': forms.TextInput(),
            'stu_col' : forms.Select(),
                        
        }