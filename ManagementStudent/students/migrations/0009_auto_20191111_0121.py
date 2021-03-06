# Generated by Django 2.2.6 on 2019-11-10 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseregistration',
            name='semester',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='students.Semester'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='results',
            name='semester',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='students.Semester'),
            preserve_default=False,
        ),
    ]
