from django.contrib import admin
from .models import Notice
from .models import Student
from .models import Category
from .models import Subscription
from .models import SNlink

admin.site.register(Notice)
admin.site.register(Student)
admin.site.register(Category)
admin.site.register(Subscription)
admin.site.register(SNlink)


