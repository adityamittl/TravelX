# Generated by Django 3.2 on 2021-07-18 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0016_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_pictures/profile.jpg', upload_to='profile_pictures'),
        ),
    ]