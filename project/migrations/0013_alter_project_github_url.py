# Generated by Django 4.0.3 on 2022-03-19 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_project_github_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='github_url',
            field=models.CharField(max_length=256),
        ),
    ]
