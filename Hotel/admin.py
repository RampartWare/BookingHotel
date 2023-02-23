from django.contrib import admin
from Hotel.models import User,Hotel,Phone_Number

# Register your models here.
admin.site.register(User),
admin.site.register(Hotel),
admin.site.register(Phone_Number)
