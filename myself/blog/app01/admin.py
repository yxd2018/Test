from django.contrib import admin
from app01.models import *

# Register your models here.

class Home1Admin(admin.ModelAdmin):
    list_display = ('title', 'time', 'author')

class Aboutus1Admin(admin.ModelAdmin):
    list_display = ('time', 'author')

class Aboutus2Admin(admin.ModelAdmin):
    list_display = ('time', 'author')

class Scenic1Admin(admin.ModelAdmin):
    list_display = ('title', 'author', 'time')

class Scenic2Admin(admin.ModelAdmin):
    list_display = ('title', 'author', 'time')

class Scenic3Admin(admin.ModelAdmin):
    list_display = ('title', 'author', 'time')

class IndustriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'time')

admin.site.register(Home1, Home1Admin)
admin.site.register(Aboutus1, Aboutus1Admin)
admin.site.register(Aboutus2, Aboutus2Admin)
admin.site.register(Scenic1, Scenic1Admin)
admin.site.register(Scenic2, Scenic2Admin)
admin.site.register(Scenic3, Scenic3Admin)
admin.site.register(Industries, IndustriesAdmin)