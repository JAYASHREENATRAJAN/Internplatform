# Generated by Django 4.2.13 on 2024-05-25 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intern_platform', '0010_internship_apply_before_internship_date_posted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internship',
            name='apply_before',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='internship',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='internship',
            name='internship_area',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='internship',
            name='internship_country',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='internship',
            name='internship_state',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='internship',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='internship',
            name='stipend',
            field=models.CharField(max_length=255),
        ),
    ]
