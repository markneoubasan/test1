from django.contrib import admin
from .models import Instructor, Post, Course, User, Enrollment, Admin

admin.site.register(Instructor)
admin.site.register(Admin)
admin.site.register(Post)
admin.site.register(Course)
admin.site.register(User)
admin.site.register(Enrollment)