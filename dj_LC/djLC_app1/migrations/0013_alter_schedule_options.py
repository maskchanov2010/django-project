# Generated by Django 4.1.1 on 2022-10-04 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djLC_app1', '0012_remove_history_student_remove_history_teacher_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schedule',
            options={'ordering': ['date_beginning'], 'verbose_name': 'Расписание', 'verbose_name_plural': 'Расписание'},
        ),
    ]
