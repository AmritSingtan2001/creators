import site
from django.contrib import admin
from .models import Creators, Subject,Chapter, SubChapter

class CreatorsAdmin(admin.ModelAdmin):
    model: Creators
    list_display = ['id', 'fullname', 'email', 'password', 'address', 'type' ]

admin.site.register(Creators, CreatorsAdmin)

class SubAdmin(admin.ModelAdmin):
    model: Subject
    list_display = ['id', 'title', 'writer', 'price' ]
admin.site.register(Subject, SubAdmin)

class ChapterAdmin(admin.ModelAdmin):
    model: Chapter
    list_display = ['id', 'subject', 'chaptername', 'pagenumber', 'writername']
admin.site.register(Chapter, ChapterAdmin)

class SubChapterAdmin(admin.ModelAdmin):
    model: SubChapter
    list_display = ['id', 'chapter', 'subchaptername', 'writername', 'pagenumber']
admin.site.register(SubChapter, SubChapterAdmin)
