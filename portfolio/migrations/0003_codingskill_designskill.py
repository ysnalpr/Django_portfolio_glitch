# Generated by Django 3.2.6 on 2021-08-23 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_resume_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodingSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('progress', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DesignSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('progress', models.IntegerField(default=0)),
            ],
        ),
    ]
