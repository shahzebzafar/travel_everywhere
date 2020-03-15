from django.contrib import admin
from traveleverywhere.models import Question, Answer, Blog, Blog_Image, User_Profile, Airline, Agency, BookingWebsite

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Blog)
admin.site.register(Blog_Image)
admin.site.register(User_Profile)
admin.site.register(Airline)
admin.site.register(Agency)
admin.site.register(BookingWebsite)