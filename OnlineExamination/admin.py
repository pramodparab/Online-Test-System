from django.contrib import admin
from .models import Student, Question, Exams

admin.site.site_header = "Content Admin"


class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ["question", "exam_name", "marks","option1","option2","option3","option4","solution"]

    class Meta:
        model = Question
      



admin.site.register(Question, QuestionModelAdmin)

admin.site.register(Student)


class ExamModelAdmin(admin.ModelAdmin):
    list_display = ["exam_name", "no_of_ques", "total_marks", "time_duration"]


admin.site.register(Exams, ExamModelAdmin)



