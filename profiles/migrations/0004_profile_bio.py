# Generated by Django 4.0.5 on 2022-06-30 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default=1, max_length=140),
            preserve_default=False,
        ),
    ]
