from django.contrib import admin

from tracks.models import Question, Track, Answers

admin.site.register(Question)
admin.site.register(Track)
admin.site.register(Answers)
