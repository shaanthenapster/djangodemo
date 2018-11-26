# Generated by Django 2.1.3 on 2018-11-26 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyWork',
            fields=[
                ('emp_work_id', models.IntegerField(auto_created=True, max_length=1000, primary_key=True, serialize=False, unique=True)),
                ('work_description', models.CharField(max_length=100)),
                ('work_remarks', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.IntegerField(auto_created=True, max_length=1000, primary_key=True, serialize=False, unique=True)),
                ('emp_name', models.CharField(max_length=30)),
                ('doj', models.DateField(verbose_name='date of joinig')),
                ('emp_desig', models.CharField(max_length=20)),
                ('emp_uname', models.CharField(max_length=15)),
                ('emp_salary', models.FloatField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='dailywork',
            name='emp_refs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Employee'),
        ),
    ]
