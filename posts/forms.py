from django import forms
from .models import posts

class Post_Form(forms.ModelForm):

    class Meta:
        model = posts
        fields = ('title','body')