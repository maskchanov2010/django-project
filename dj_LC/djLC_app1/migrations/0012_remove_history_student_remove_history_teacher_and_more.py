# Generated by Django 4.1.1 on 2022-10-04 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djLC_app1', '0011_alter_history_evaluations1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='student',
        ),
        migrations.RemoveField(
            model_name='history',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='student',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='teacher',
        ),
        migrations.AddField(
            model_name='history',
            name='student',
            field=models.ManyToManyField(to='djLC_app1.student', verbose_name='Ученик'),
        ),
        migrations.AddField(
            model_name='history',
            name='teacher',
            field=models.ManyToManyField(to='djLC_app1.teacher', verbose_name='Учитель'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='student',
            field=models.ManyToManyField(to='djLC_app1.student', verbose_name='Ученик'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='teacher',
            field=models.ManyToManyField(to='djLC_app1.teacher', verbose_name='Учитель'),
        ),
    ]
