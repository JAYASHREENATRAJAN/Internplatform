# Generated by Django 4.2.3 on 2024-05-14 06:02

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intern_platform', '0003_employer_student_remove_customuser_user_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_employer',
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('intern', 'Intern'), ('employer', 'Employer')], default='intern', max_length=20),
        ),
        migrations.AddField(
            model_name='internprofile',
            name='college',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='internprofile',
            name='experience',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='internprofile',
            name='university',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
        migrations.DeleteModel(
            name='Employer',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
