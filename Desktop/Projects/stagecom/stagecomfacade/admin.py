from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Module)

admin.site.register(Content)
# admin.site.register(ItemBase)
admin.site.register(Text)
admin.site.register(File)
admin.site.register(Image)
admin.site.register(Video)