from django import forms
from django.contrib.auth.models import User 
from traveleverywhere.models import User_Profile, Blog, Blog_Image, Question, Answer

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta: 
        model = User 
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm): 
    class Meta: 
        model = User_Profile 
        fields = ('about', 'picture',)

class BlogForm(forms.ModelForm):
    title = forms.URLField(max_length = 50, help_text = "Title of the blog.")
    body = froms.CharField(widget = forms.Textarea, max_length = 10000, help_text = "Contents of the blog.")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required = False)
    location_country = froms.CharField(max_length = 20, help_text = "Country")
    location_city = froms.CharField(max_length = 20, help_text = "City", required = False)
    location_place = froms.CharField(max_length = 50, help_text = "Place", required = False)
    
    class Meta:
        model = Blog
        fields = ('title', 'body', 'location_country', 'location_city', 'location_place', 'publish_data',)
        
class BlogImageForm(forms.ModelForm):
    image = forms.ImageField(label = 'Image')
    
    class Meta:
        model = Blog_Image
        fields ('image',)
        
class QuestionForm(forms.ModelForm):
    title = forms.URLField(max_length = 50, help_text = "Question.")
    body = froms.CharField(widget = froms.Textarea, max_length = 10000, help_text = "Question details.")
    replies = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Question
        fields = ('title', 'body',)
        
class AnswerForm(forms.ModelForm):
    text = froms.CharField(widget = forms.Textarea, max_length = 10000, help_text = "Answer text.")
    
    class Meta:
        model = Answer
        fields = ('text',)