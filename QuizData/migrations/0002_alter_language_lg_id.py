# Generated by Django 3.2.11 on 2022-04-05 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizData', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='lg_id',
            field=models.AutoField(db_column='lg_id', primary_key=True, serialize=False),
        ),
    ]
