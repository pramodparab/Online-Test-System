# Generated by Django 2.2.7 on 2020-01-05 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('OnlineExamination', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_no', models.PositiveIntegerField(default=0)),
                ('exam_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineExamination.Exams')),
                ('ques', models.ManyToManyField(to='OnlineExamination.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineExamination.Exams')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineExamination.Student')),
            ],
        ),
    ]
