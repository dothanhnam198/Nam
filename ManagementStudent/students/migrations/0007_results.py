# Generated by Django 2.2.6 on 2019-11-10 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20191111_0104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_middle', models.FloatField()),
                ('score_final', models.FloatField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Subject')),
            ],
        ),
    ]
