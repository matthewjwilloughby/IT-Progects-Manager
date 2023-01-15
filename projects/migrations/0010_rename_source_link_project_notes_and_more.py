# Generated by Django 4.0.5 on 2022-10-21 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_rename_demo_link_project_priority_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='source_link',
            new_name='notes',
        ),
        migrations.RemoveField(
            model_name='project',
            name='featured_image',
        ),
        migrations.RemoveField(
            model_name='project',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='project',
            name='vote_ratio',
        ),
        migrations.RemoveField(
            model_name='project',
            name='vote_total',
        ),
    ]