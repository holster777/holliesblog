# Generated by Django 4.1.2 on 2022-10-13 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_homepage_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='description',
            new_name='call_to_action',
        ),
    ]
