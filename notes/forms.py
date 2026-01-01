from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Notes

user_name = forms.CharField(label='Username', max_length=150, required=True, help_text="Required. 150 characters or fewer.")
password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=True, help_text="Your password must contain at least 8 characters.Letters, digits and @/./+/-/_ only.")

class SignUpForm(UserCreationForm):
    class Meta:
        model = User  # Use built-in User, not Notes
        fields = ['username', 'password1', 'password2']  # Standard fields

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text_field') # specify the fields to include in the form
        
        widgets = {
             'title' : forms.TextInput(attrs={'class': 'form-control my-5'}), # add bootstrap class to title field
            'text_field': forms.Textarea(attrs={'class': 'form-control mb-5'}), # add bootstrap class to text_field
        }
        labels = {
            'text_field': 'Write your toughts here', # custom label for text_field
        }
        
        
    def clean_title(self):
           title = self.cleaned_data['title']
           if 'Django' not in title:
              raise ValidationError("We only accept notes about Django!")
           return title
        
     