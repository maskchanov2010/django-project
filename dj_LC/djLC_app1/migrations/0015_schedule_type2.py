# Generated by Django 4.1.1 on 2022-10-05 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djLC_app1', '0014_remove_schedule_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='type2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='djLC_app1.category', verbose_name='Категория'),
        ),
    ]