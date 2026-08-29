from django import forms
from .models import Course, Review

# Course form
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'price']

# Review form
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']
        widgets = {
            'rating': forms.HiddenInput(),
        }