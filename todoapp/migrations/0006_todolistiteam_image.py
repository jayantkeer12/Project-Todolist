# Generated by Django 4.0.6 on 2022-07-27 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_remove_uploadimage_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistiteam',
            name='image',
            field=models.ImageField(default='', upload_to='myimage/'),
        ),
    ]
