# Generated by Django 3.2.11 on 2022-02-15 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='cr_categ',
            field=models.ManyToManyField(db_column='cr_categ', null=True, related_name='courses', to='course.CourseCategory', verbose_name='Category'),
        ),
    ]
