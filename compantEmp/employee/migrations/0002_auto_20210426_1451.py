# Generated by Django 3.1.7 on 2021-04-26 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='skill',
        ),
        migrations.AddField(
            model_name='employee',
            name='skill',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='skills',
            name='skill',
        ),
        migrations.AddField(
            model_name='skills',
            name='skill',
            field=models.ManyToManyField(to='employee.employee'),
        ),
    ]
