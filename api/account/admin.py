# To display the realted entity in the admin page

from django.contrib import admin
from .models import NewUser

admin.site.register(NewUser)
