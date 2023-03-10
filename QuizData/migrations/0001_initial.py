# Generated by Django 3.2.11 on 2022-04-01 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Quiz', '0001_initial'),
        ('course', '0007_auto_20220219_1449'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dlevel',
            fields=[
                ('dl_id', models.AutoField(db_column='dl_id', primary_key=True, serialize=False)),
                ('dl_title', models.CharField(max_length=255, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('lg_id', models.AutoField(db_column='qt_id', primary_key=True, serialize=False)),
                ('lg_title', models.CharField(max_length=255, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('qu_id', models.AutoField(db_column='qu_id', primary_key=True, serialize=False)),
                ('reference', models.CharField(blank=True, max_length=500, null=True)),
                ('difficulty', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='dlavel_question3', to='QuizData.dlevel')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='language_question3', to='QuizData.language')),
                ('qtype', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='qtype_question3', to='Quiz.qtype')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='topic_question3', to='course.topic')),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.DO_NOTHING, related_name='ques_user1', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ['qu_id'],
            },
        ),
        migrations.CreateModel(
            name='Ques',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('qd_id', models.AutoField(db_column='qd_id', default=None, primary_key=True, serialize=False)),
                ('question_para', models.TextField(blank=True, default=None, null=True)),
                ('question_text', models.TextField(blank=True, default=None, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True, verbose_name='description')),
                ('solution', models.TextField(blank=True, default=None, null=True, verbose_name='solution')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active Status')),
                ('qid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ques_qdes3', to='QuizData.question')),
                ('ques_lang', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='language_qdes3', to='QuizData.language')),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(default=None, max_length=255, verbose_name='Answer Text')),
                ('is_right', models.BooleanField(default=False)),
                ('language', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='choice_answer3', to='QuizData.language')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='choices', to='QuizData.ques')),
            ],
        ),
    ]
