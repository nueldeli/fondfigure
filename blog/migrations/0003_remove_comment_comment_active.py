# Generated by Django 3.1 on 2021-04-09 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210406_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_active',
        ),
    ]
