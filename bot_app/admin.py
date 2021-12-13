from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(TweetLookUpWord)
admin.site.register(TweetLookUpBadWord)
admin.site.register(OutBoundDirectMessage)
admin.site.register(TweetLookUpCoordinates)
