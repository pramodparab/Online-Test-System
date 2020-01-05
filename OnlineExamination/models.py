from django.db import models
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



def upload_image(instance, filename):
    return "%s/%s" % (instance.user, filename)


class Student(models.Model):
    user = models.CharField(primary_key=True, max_length=20, unique=True)
    name = models.CharField(max_length=20)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$',
                                 message="Phone number must be entered in the define format")
    phone = models.CharField(validators=[phone_regex], max_length=12)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to=upload_image, null=True, blank=True, height_field='height_field', width_field='width_field')
    height_field = models.IntegerField(default=0, null=True)
    width_field = models.IntegerField(default=0, null=True)
    stream = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.user)


class Exams(models.Model):
    id = models.AutoField(primary_key = True, unique = True)
    exam_name = models.CharField(max_length=50)
    no_of_ques = models.CharField(max_length=20)
    total_marks = models.CharField(max_length=20)
    time_duration = models.DurationField(default='00:00:00')

    def __str__(self):
        return str(self.exam_name)

class Subject(models.Model):
    subject_name = models.CharField(max_length=25)
    exam_name = models.ForeignKey(Exams,on_delete=models.CASCADE,default=0)

    def __str__(self):
        return str(self.subject_name)

class Chapter(models.Model):
    chapter_name = models.CharField(max_length=30)
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE,default=0)

    def __str__(self):
        return str(self.chapter_name)

class Topic(models.Model):
    topic_name = models.CharField(max_length=50)
    chapter_name=models.ForeignKey(Chapter,on_delete=models.CASCADE,default=0)

    def __str__(self):  
        return str(self.topic_name)    

    

class Question(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    exam_name = models.ForeignKey(Exams, on_delete=models.CASCADE)
    subject_name = models.ForeignKey(Subject,on_delete=models.CASCADE,default=0)
    chapter_name = models.ForeignKey(Chapter,on_delete = models.CASCADE,default=0)
    topic_name = models.ForeignKey(Topic,on_delete = models.CASCADE,default=0)
    marks = models.PositiveIntegerField(default=0)
    question = RichTextUploadingField()
    option1 = RichTextUploadingField(max_length=100)
    option2 = RichTextUploadingField(max_length=100)
    option3 = RichTextUploadingField(max_length=100)
    option4 = RichTextUploadingField(max_length=100)
    choose = (('A', 'option1'), ('B', 'option2'), ('C', 'option3'), ('D', 'option4'))
    answer = models.CharField(max_length=1, choices=choose)
    solution = RichTextUploadingField()

    def __str__(self):
        return str(self.question)

