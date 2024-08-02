from django.contrib import admin
from api.admins import *
from api.models import *

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Note, NoteAdmin)