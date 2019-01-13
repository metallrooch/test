from django.contrib import admin

from .models import Table, User, Reserved

admin.site.register(Table)
admin.site.register(User)
admin.site.register(Reserved)
