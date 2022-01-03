from django.contrib import admin
from .models import WFMTTaskModel,Category
# Register your models here.

admin.site.register(Category)
admin.site.register(WFMTTaskModel)