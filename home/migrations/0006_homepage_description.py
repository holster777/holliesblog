# Generated by Django 4.1.2 on 2022-10-13 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_homepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
