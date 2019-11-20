# Generated by Django 2.2.6 on 2019-11-10 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20191111_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseregistration',
            name='subject',
        ),
        migrations.AddField(
            model_name='courseregistration',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='students.Courses'),
            preserve_default=False,
        ),
    ]
