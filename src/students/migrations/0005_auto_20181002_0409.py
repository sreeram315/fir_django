# Generated by Django 2.1.1 on 2018-10-02 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20181002_0327'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='StudentInfo',
        ),
    ]
