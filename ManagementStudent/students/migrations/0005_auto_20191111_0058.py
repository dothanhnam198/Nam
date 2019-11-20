# Generated by Django 2.2.6 on 2019-11-10 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20191107_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='subject',
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('course_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('period', models.CharField(max_length=20)),
                ('day', models.CharField(max_length=20)),
                ('room', models.CharField(max_length=20)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='CourseRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_opened', models.DateField()),
                ('date_closed', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Subject')),
            ],
        ),
    ]
