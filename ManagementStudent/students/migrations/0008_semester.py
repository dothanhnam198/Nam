# Generated by Django 2.2.6 on 2019-11-10 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_results'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('semester_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
