# Generated by Django 4.0.5 on 2022-10-21 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_rename_completedtask_completedtasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='completedtasks',
            name='notes',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]