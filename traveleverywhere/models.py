from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.URLField(max_length = 50)
    body = models.CharField(max_length = 500)
    replies = models.IntegerField(default = 0)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Question, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Questions'

    def __str__(self): 
        return self.title

class Answer(models.Model):
    text = models.CharField(max_length = 500)
    question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name = 'question')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user', null=True)

    def __str__(self): 
        return self.text

class Blog(models.Model):
    title = models.URLField(max_length = 50)
    body = models.CharField(max_length = 10000)
    likes = models.IntegerField(default = 0)
    publish_date = models.DateField(auto_now_add = True)
    location_country = models.CharField(max_length = 20)
    location_city = models.CharField(max_length = 20, blank = True)
    location_place = models.CharField(max_length = 50, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Blogs'
    
    def __str__(self):
        return self.title
        
class Blog_Image(models.Model):
    image = models.ImageField(upload_to = 'blog_images', blank = True)
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.image
                
class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    about = models.CharField(max_length = 500, blank=True)
    
    def __str__(self):
        return self.user.username

class Airline(models.Model):
    name = models.CharField(max_length=20)
    link = models.URLField(max_length=30)
    rating = models.IntegerField(default=0)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Agency(models.Model):
    name = models.CharField(max_length=20)
    link = models.URLField(max_length=30)
    rating = models.IntegerField(default=0)
    user = models.ManyToManyField(User)

    class Meta:
        verbose_name_plural = 'Agencies'

    def __str__(self):
        return self.name

class BookingWebsite(models.Model):
    name = models.CharField(max_length=20)
    link = models.URLField(max_length=30)
    rating = models.IntegerField(default=0)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name