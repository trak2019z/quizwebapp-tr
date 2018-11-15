from django.contrib import admin
from classroom.models import Answer, Question, Student, StudentAnswer, Subject, User


class UserAdmin(admin.ModelAdmin):
    pass


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')


class StudentAdmin(admin.ModelAdmin):
    pass


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'text')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'is_correct')


admin.site.register(User, UserAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
