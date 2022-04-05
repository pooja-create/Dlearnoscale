# Generated by Django 3.2.11 on 2022-04-05 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0001_initial'),
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
                ('lg_id', models.AutoField(db_column='lg_id', primary_key=True, serialize=False)),
                ('lg_title', models.CharField(max_length=255, verbose_name='Title')),
            ],
        ),
    ]
