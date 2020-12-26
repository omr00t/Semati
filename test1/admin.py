from django.contrib import admin

from .models import Personality, Question, Result


admin.site.register(Personality)
admin.site.register(Question)
admin.site.register(Result)
