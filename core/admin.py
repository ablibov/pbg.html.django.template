from django.contrib import admin
from core.models import *
from django.contrib.auth.models import User as def_user
from django.contrib.auth.models import Group

admin.site.unregister(def_user)
admin.site.unregister(Group)

admin.site.register(User,)
# Register your models here.
