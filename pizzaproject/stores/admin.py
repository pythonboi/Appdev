from django.contrib import admin

# Register your models here.

from .models import Pizzeria

# This will register the Pizzeria model into the admin.py to abe able to see it in our admin page

admin.site.register(Pizzeria)
