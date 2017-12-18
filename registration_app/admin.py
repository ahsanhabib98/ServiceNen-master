# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Division, District, Area, Profile

admin.site.register(Division)
admin.site.register(District)
admin.site.register(Area)
admin.site.register(Profile)

# Register your models here.
