# Generated by Django 4.1.1 on 2022-10-02 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djLC_app1', '0004_rename_type_history_type2'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='evaluations2',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='history',
            name='date_end',
            field=models.DateTimeField(),
        ),
    ]
