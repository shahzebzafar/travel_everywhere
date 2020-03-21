from django import forms
from django.contrib.auth.models import User 
from traveleverywhere.models import User_Profile, Question, Answer, Blog, Blog_Image

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta: 
        model = User 
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm): 
    class Meta: 
        model = User_Profile 
        fields = ('about', 'picture',)

class QuestionForm(forms.ModelForm):
    title = forms.CharField(max_length=50, help_text="Please enter your question.")
    body = forms.CharField(max_length=500, help_text="Please give more informaion for the question.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Question
        fields = ('title','body',)

class AnswerForm(forms.ModelForm):
    text = forms.CharField(max_length=500, help_text="Please enter your answer.")

    class Meta:
        model = Answer
        fields = ('text',)

class BlogForm(forms.ModelForm):
    title = forms.URLField(max_length = 50, help_text = "Title of the blog.")
    body = forms.CharField(widget = forms.Textarea, max_length = 10000, help_text = "Contents of the blog.")
    bodySummary = forms.CharField(widget=forms.HiddenInput(), required = False)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required = False)
    location_country = forms.CharField(max_length = 20, help_text = "Country")
    location_city = forms.CharField(max_length = 20, help_text = "City", required = False)
    location_place = forms.CharField(max_length = 50, help_text = "Place", required = False)

    class Meta:
        model = Blog
        fields = ('title', 'body', 'location_country', 'location_city', 'location_place',)

class BlogImageForm(forms.ModelForm):
    image = forms.ImageField(label = 'Image')

    class Meta:
        model = Blog_Image
        fields = ('image',)
