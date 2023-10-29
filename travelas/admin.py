from django.contrib import admin
from travelas.models import Car, Page
from travelas.models import UserProfile
from travelas.models import Car, Page, UserProfile

# Register your models here.

admin.site.register(Car)
admin.site.register(Page)
admin.site.register(UserProfile)
