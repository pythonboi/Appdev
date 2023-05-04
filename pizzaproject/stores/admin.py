from django.contrib import admin
from .models import Pizzeria

# Register your models here.


# This will register the Pizzeria model into the admin.py to abe able to see it in our admin page

admin.site.register(Pizzeria)
