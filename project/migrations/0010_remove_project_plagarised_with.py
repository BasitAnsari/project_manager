# Generated by Django 4.0.3 on 2022-03-19 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_alter_project_plagarised_with'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='plagarised_with',
        ),
    ]
