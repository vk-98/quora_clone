# Generated by Django 3.0.2 on 2020-02-21 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20200221_0748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='question',
        ),
    ]