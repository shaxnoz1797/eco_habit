from django.contrib import admin
from .models import User, Habit



# 1. User modelini ro'yxatdan o'tkazamiz
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')



# 2. Habit modelini ro'yxatdan o'tkazamiz
@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'is_done')
    list_filter = ('is_done', 'user')