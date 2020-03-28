from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length = 50)
    body = models.CharField(max_length = 500)
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
    title = models.CharField(max_length = 50)
    body = models.CharField(max_length = 10000)
    bodySummary = models.CharField(max_length = 200)
    publish_date = models.DateField(auto_now_add = True)
    location_country = models.CharField(max_length = 20)
    location_city = models.CharField(max_length = 20, blank = True)
    location_place = models.CharField(max_length = 50, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    slug = models.SlugField(max_length = 50, unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Blogs'
    
    def __str__(self):
        return self.title

def get_image_filename(instance, filename):
    title = instance.blog.title
    slug = slugify(title)
    return "blog_images/%s-%s" % (slug, filename) 
        

class Blog_Image(models.Model):
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE, default = None)
    image = models.ImageField(upload_to = get_image_filename, verbose_name = "Image")

class BlogLike(models.Model):
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
                
class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    about = models.CharField(max_length = 500, blank=True)
    
    def __str__(self):
        return self.user.username

class Airline(models.Model):
    name = models.CharField(max_length=20)
    link = models.URLField(max_length=30)

    def __str__(self):
        return self.name

class AirlineLike(models.Model):
    airline = models.ForeignKey(Airline, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)

class AirlineDislike(models.Model):
    airline = models.ForeignKey(Airline, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)

class Agency(models.Model):
    name = models.CharField(max_length=20)
    link = models.URLField(max_length=30)

    class Meta:
        verbose_name_plural = 'Agencies'

    def __str__(self):
        return self.name
    
class AgencyLike(models.Model):
    agency = models.ForeignKey(Agency, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)

class AgencyDislike(models.Model):
    agency = models.ForeignKey(Agency, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)

class BookingWebsite(models.Model):
    name = models.CharField(max_length=20)
    link = models.URLField(max_length=30)

    def __str__(self):
        return self.name

class WebsiteLike(models.Model):
    website = models.ForeignKey(BookingWebsite, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)

class WebsiteDislike(models.Model):
    website = models.ForeignKey(BookingWebsite, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)